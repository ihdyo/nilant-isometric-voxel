"""Voxel Fauna · the Blender engine (bpy). Builds an animal's editable project from its model script and renders it.

  build(grid, look, rig)        the voxel meshes (one object per part, one material per palette key), the stage
                                (ground, light rig, sky), and one scene per composition (ILL/INF x 1x1, 9x16, 16x9), all
                                linking the same Animal, Stage and Lights collections, each with its own framed camera
  render(scene, profile, ...)   the two passes (animal over transparency, shadow on the ground) laid over the exact
                                background hex -> a flat PNG (see vf_standards: "Background and shadow")
  save(path)                    the .blend, with a README text block

Every number comes from vf_standards.py. Called by vf_job.py (`python _system/studio/scripts/vf.py ...`).
"""
import json
import math
import os
import sys
import time

import bpy
import bmesh
import numpy as np
from mathutils import Matrix, Vector

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import vf_standards as ST  # noqa: E402
import vf_color as VC  # noqa: E402
from vf_voxel import apply as _apply  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PALETTE = VC.PALETTE
REPORT = []

CORNERS = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1))
CUBE = ((0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6), (0, 4, 7, 3), (1, 2, 6, 5))


def log(line):
    REPORT.append(line)
    print("VF:", line, flush=True)


# ---- colour ---------------------------------------------------------------------------------------------------------
hex_of = VC.hex_of          # a Tailwind token or "#RRGGBB" (owner 2026-11-16: tokens are no longer required)
srgb = VC.srgb


def _lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def background_hex(look):
    """The colour every open pixel gets: a vivid pastel of the animal's background (vf_standards.BACKGROUND_RULE)."""
    R = ST.BACKGROUND_RULE
    return VC.pastel(look["background"], R["max_chroma"], R["lightness"])


def rgba(token, a=1.0):
    return tuple(_lin(c) for c in srgb(token)) + (a,)


def _set(node, name, value):
    s = node.inputs.get(name)
    if s is not None:
        s.default_value = value


def _nodes(idblock):
    try:
        idblock.use_nodes = True          # deprecated in Blender 5 (always on); harmless where it still exists
    except Exception:
        pass
    return idblock.node_tree


# ---- scene ----------------------------------------------------------------------------------------------------------
def clear():
    for coll in (bpy.data.objects, bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.cameras,
                 bpy.data.worlds, bpy.data.images, bpy.data.texts):
        for item in list(coll):
            coll.remove(item)
    for c in list(bpy.data.collections):
        bpy.data.collections.remove(c)
    first = bpy.data.scenes[0]
    for s in list(bpy.data.scenes)[1:]:
        bpy.data.scenes.remove(s)
    first.name = "ILL 1x1"
    REPORT[:] = []
    return first


def plastic(key, token, finish=None):
    P = ST.MATERIALS[finish or ST.GEOMETRIES[ST.GEOMETRY]["material"]]
    m = bpy.data.materials.new(f"VF · {key} · {token}")
    nt = _nodes(m)
    b = next((n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"), None) or nt.nodes.new("ShaderNodeBsdfPrincipled")
    _set(b, "Base Color", rgba(VC.tone(token, **ST.ANIMAL_TONE)))    # calmed (owner 2026-11-17, standards v2.3)
    _set(b, "Roughness", P["roughness"])
    _set(b, "Specular IOR Level", P["specular"])
    _set(b, "Coat Weight", P["coat"])
    _set(b, "Coat Roughness", P["coat_roughness"])
    _set(b, "Subsurface Weight", P["subsurface"])
    _set(b, "Subsurface Scale", P["subsurface_scale"])
    _set(b, "Subsurface Radius", P["subsurface_radius"])
    m.diffuse_color = rgba(token)
    return m


def ground_material():
    m = bpy.data.materials.new("VF · ground (shadow pass)")
    nt = _nodes(m)
    nt.nodes.clear()
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    d = nt.nodes.new("ShaderNodeBsdfDiffuse")
    g = ST.SHADOW["ground_grey"]
    d.inputs["Color"].default_value = (g, g, g, 1.0)
    nt.links.new(d.outputs[0], out.inputs["Surface"])
    m.diffuse_color = (g, g, g, 1.0)
    return m


def _collection(name, scene):
    c = bpy.data.collections.new(name)
    scene.collection.children.link(c)
    return c


DIRS = ((0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0))      # the normal of each CUBE face


def ground_offset(grid):
    """Voxels to lift the posed animal by so its lowest point stands on z = 0."""
    return -grid.posed_bounds()[0][2]


def animal_meshes(grid, palette, coll, geometry=None):
    """One object per part, one material per palette key. "block": every visible voxel its own bevelled cube.
    "merged": a part's outer faces share vertices, so its flat planes carry no seams; faces against another part are
    kept, so parts meet with a visible seam. "mob": merged faces with sharp edges (no bevel, flat shading), matte,
    flat solid colours. Each object's origin is its part's hinge (vf_voxel joint pivot) and its transform is the
    part's pose, so the sections can be turned again in the .blend; plates are squashed in the mesh."""
    geometry = geometry or ST.GEOMETRY
    G = ST.GEOMETRIES[geometry]
    s = ST.VOXEL
    keys = sorted(palette)
    mats = {k: plastic(k, palette[k], G["material"]) for k in keys}
    missing = [c for c in grid.colors() if c not in palette]
    if missing:
        raise KeyError(f"model uses colour keys not in animal.json look.palette: {missing}")
    lift = ground_offset(grid)
    objs, culled = [], 0
    for part, voxels in sorted(grid.parts().items()):
        used = sorted({c for _, c in voxels})
        index = {c: i for i, c in enumerate(used)}
        mine = {k for k, _ in voxels}
        j = grid.joints.get(part)
        origin = j["pivot"] if j else (0.0, 0.0, 0.0)
        bm = bmesh.new()
        cache = {}

        def local(p):
            q = grid.scaled(part, p)
            return ((q[0] - origin[0]) * s, (q[1] - origin[1]) * s, (q[2] - origin[2]) * s)

        def vert(p):
            v = cache.get(p)
            if v is None:
                v = cache[p] = bm.verts.new(local(p))
            return v

        for (x, y, z), color in voxels:
            if ST.CULL_HIDDEN and not grid.visible((x, y, z), part):
                culled += 1
                continue
            if geometry == "block":
                vs = [bm.verts.new(local((x + dx, y + dy, z + dz))) for dx, dy, dz in CORNERS]
                for f in CUBE:
                    face = bm.faces.new([vs[i] for i in f])
                    face.material_index = index[color]
            else:
                for f, (dx, dy, dz) in zip(CUBE, DIRS):
                    if (x + dx, y + dy, z + dz) in mine:
                        continue
                    pts = [vert((x + CORNERS[i][0], y + CORNERS[i][1], z + CORNERS[i][2])) for i in f]
                    try:
                        face = bm.faces.new(pts)
                    except ValueError:      # the same face twice cannot happen on a voxel surface; skip if it does
                        continue
                    face.material_index = index[color]
        me = bpy.data.meshes.new(f"VF · {part}")
        bm.to_mesh(me)
        bm.free()
        for c in used:
            me.materials.append(mats[c])
        for p in me.polygons:
            p.use_smooth = G["bevel"]           # sharp boxes shade flat; bevelled ones smooth across the bevel
        o = bpy.data.objects.new(f"VF · {part}", me)
        m = grid.matrix(part)                       # rest -> posed, voxel units; the origin sits on the hinge
        p0 = _apply(m, origin)
        o.matrix_world = Matrix(((m[0][0], m[0][1], m[0][2], p0[0] * s),
                                 (m[1][0], m[1][1], m[1][2], p0[1] * s),
                                 (m[2][0], m[2][1], m[2][2], (p0[2] + lift) * s),
                                 (0.0, 0.0, 0.0, 1.0)))
        coll.objects.link(o)
        if G["bevel"]:
            b = o.modifiers.new("VF bevel", "BEVEL")
            b.width = ST.BEVEL["width"]
            b.segments = ST.BEVEL["segments"]
            b.profile = ST.BEVEL["profile"]
            b.limit_method = G["limit"]
            b.angle_limit = math.radians(ST.BEVEL_ANGLE)
            b.use_clamp_overlap = True
            try:
                b.harden_normals = True
            except Exception:
                pass
        # the stacking bias: this part's stacking level on every vertex, the modifier last (vf_standards.STACK_LEVELS)
        at = me.attributes.new(DEPTH_ATTR, "FLOAT", "POINT")
        at.data.foreach_set("value", [float(stack_level(grid, part))] * len(me.vertices))
        add_depth_bias(o)
        objs.append(o)
    turned = sum(1 for jj in grid.joints.values() if any(abs(a) > 0.01 for a in jj["rotate"]))
    log(f"model: {len(objs)} parts ({geometry}), {len(grid.v)} voxels, {culled} hidden voxels not built, "
        f"{len(mats)} materials, {turned} turned sections, lifted {lift:+.2f} voxels to the ground")
    return objs


def stage(scene, rig_name):
    """Ground, light rig and sky (vf_standards: light rig)."""
    st = _collection("Stage", scene)
    size = ST.SHADOW["ground_size"]
    me = bpy.data.meshes.new("VF · ground")
    h = size / 2
    me.from_pydata([(-h, -h, 0), (h, -h, 0), (h, h, 0), (-h, h, 0)], [], [(0, 1, 2, 3)])
    me.materials.append(ground_material())
    ground = bpy.data.objects.new("VF · ground", me)
    st.objects.link(ground)

    lc = _collection("Lights", scene)
    rig = ST.RIGS[rig_name]
    for role in ("key", "rim"):
        L = rig[role]
        d = bpy.data.lights.new(f"VF · {role}", "SUN")
        d.energy = L["energy"]
        d.angle = ST.SUN_MIN_ANGLE
        d.color = rgba(L["token"])[:3]
        d.use_shadow = L.get("shadow", True)
        o = bpy.data.objects.new(f"VF · {role} sun", d)
        rx, ry, rz = L["rotation"]
        o.rotation_euler = (math.radians(rx), math.radians(ry), math.radians(rz + ST.RIG_TURN))
        lc.objects.link(o)

    w = bpy.data.worlds.new("VF · sky")
    nt = _nodes(w)
    bg = next((n for n in nt.nodes if n.type == "BACKGROUND"), None)
    if bg is None:
        nt.nodes.clear()
        out = nt.nodes.new("ShaderNodeOutputWorld")
        bg = nt.nodes.new("ShaderNodeBackground")
        nt.links.new(bg.outputs[0], out.inputs["Surface"])
    bg.inputs["Color"].default_value = rgba(ST.SKY["token"])
    bg.inputs["Strength"].default_value = ST.SKY["strength"]
    log(f"stage: rig '{rig_name}', sky {ST.SKY['token']} x{ST.SKY['strength']}")
    return ground, w


# ---- camera and framing ---------------------------------------------------------------------------------------------
def view_axes():
    a, e = math.radians(ST.CAMERA["azimuth"]), math.radians(ST.CAMERA["elevation"])
    back = Vector((math.sin(a) * math.cos(e), -math.cos(a) * math.cos(e), math.sin(e)))   # Nilant pose_of convention
    q = (-back).to_track_quat("-Z", "Y")
    R = q.to_matrix()
    return q, R.col[0].copy(), R.col[1].copy(), back


def corners_of(grid):
    """Every visible voxel corner of the posed, grounded animal, in metres (what the camera frames)."""
    s = ST.VOXEL
    lift = ground_offset(grid)
    return [Vector((p[0] * s, p[1] * s, (p[2] + lift) * s)) for p in grid.posed_points()]


def frame(kind, ratio, pts, width, height):
    """Ortho scale and camera location that put the animal's projected box in its zone (vf_standards.FRAMING)."""
    q, right, up, back = view_axes()
    us = [p.dot(right) for p in pts]
    vs = [p.dot(up) for p in pts]
    ds = [p.dot(back) for p in pts]
    bw, bh = max(us) - min(us), max(vs) - min(vs)
    bu, bv = (max(us) + min(us)) / 2, (max(vs) + min(vs)) / 2
    spec = ST.FRAMING[kind][ratio]
    x0, y0, x1, y1 = spec["zone"]
    fill = spec["fill"]
    A = width / height
    need_w = bw / (fill * (x1 - x0))
    need_h = bh / (fill * (y1 - y0))
    if width >= height:
        scale = max(need_w, need_h * A)
        vw, vh = scale, scale / A
    else:
        scale = max(need_h, need_w / A)
        vw, vh = scale * A, scale
    du = ((x0 + x1) / 2 - 0.5) * vw
    dv = (0.5 - (y0 + y1) / 2) * vh
    depth = (max(ds) + min(ds)) / 2 + ST.CAMERA["distance"]
    loc = right * (bu - du) + up * (bv - dv) + back * depth
    box = dict(u=(min(us), max(us)), v=(min(vs), max(vs)))
    return dict(rotation=q, location=loc, ortho_scale=scale, view=(vw, vh), box=box, box_size=(bw, bh))


def camera(scene, name, fr):
    c = bpy.data.cameras.new(name)
    c.type = "ORTHO"
    c.ortho_scale = fr["ortho_scale"]
    c.sensor_fit = "AUTO"
    c.clip_start, c.clip_end = ST.CAMERA["clip_start"], ST.CAMERA["clip_end"]
    c.dof.use_dof = ST.CAMERA["dof"]
    o = bpy.data.objects.new(name, c)
    o.location = fr["location"]
    o.rotation_mode = "QUATERNION"
    o.rotation_quaternion = fr["rotation"]
    scene.collection.objects.link(o)
    scene.camera = o
    return o


# ---- render settings ------------------------------------------------------------------------------------------------
def apply_profile(scene, profile, ratio):
    P = ST.PROFILES[profile]
    B = ST.RENDER_BASE
    w, h = ST.SIZES[ratio]
    r = scene.render
    r.engine = B["engine"]
    r.resolution_x, r.resolution_y = round(w * P["scale"]), round(h * P["scale"])
    r.resolution_percentage = 100
    r.use_motion_blur = B["motion_blur"]
    r.film_transparent = True
    ee = scene.eevee
    for k, v in list(B["eevee"].items()) + list(P["eevee"].items()):
        try:
            setattr(ee, k, v)
        except Exception as e:
            log(f"profile {profile}: could not set eevee.{k} ({e})")
    try:
        ee.ray_tracing_options.resolution_scale = P["rt_resolution"]
        ee.ray_tracing_options.use_denoise = P["rt_denoise"]
    except Exception as e:
        log(f"profile {profile}: ray tracing options ({e})")
    vs = scene.view_settings
    vs.view_transform = ST.COLOR["view"]
    vs.look = ST.COLOR["look"]
    vs.exposure = ST.COLOR["exposure"]
    im = r.image_settings
    im.file_format = "PNG"
    im.color_mode = "RGBA"
    im.color_depth = "16"
    try:
        scene.compositing_node_group = None     # no bloom (vf_standards.RENDER_BASE)
    except Exception:
        pass
    scene.render.use_compositing = False


def build(grid, look, rig_name=None, geometry=None):
    """The whole editable project in memory. Returns {scene name: frame info}. `rig_name` and `geometry` override the
    locked standards only for comparison stills (vf.py selftest --compare), never for an animal."""
    rig_name = rig_name or ST.RIG
    first = clear()
    ac = _collection("Animal", first)
    objs = animal_meshes(grid, look["palette"], ac, geometry)
    ground, world = stage(first, rig_name)
    pts = corners_of(grid)
    frames = {}
    for kind in ST.KINDS:
        for ratio in ST.RATIOS:
            name = f"{kind} {ratio}"
            sc = bpy.data.scenes.get(name)
            if sc is None:
                sc = bpy.data.scenes.new(name)
                for cname in ("Animal", "Stage", "Lights"):
                    sc.collection.children.link(bpy.data.collections[cname])
            sc.world = world
            apply_profile(sc, "ULTRA", ratio)
            w, h = ST.SIZES[ratio]
            fr = frame(kind, ratio, pts, w, h)
            camera(sc, f"CAM · {name}", fr)
            sc["vf_background"] = background_hex(look)
            sc["vf_profile"] = "ULTRA"
            frames[name] = dict(ortho_scale=fr["ortho_scale"], view=fr["view"], box_size=fr["box_size"])
    bpy.context.window_manager  # noqa: B018 (keeps the context alive in background runs)
    log(f"build: {len(frames)} composition scenes, ground and {len(objs)} animal objects")
    return frames


# ---- passes and the composite ---------------------------------------------------------------------------------------
def _animal_objects():
    return list(bpy.data.collections["Animal"].all_objects)


# ---- the stacking depth bias (vf_standards.STACK_LEVELS) ------------------------------------------------------------------
DEPTH_ATTR, BIAS_ATTR, DEPTH_MOD = "vf_depth", "vf_bias", "VF depth"


def stack_level(grid, part):
    """How far (voxels) the part is nudged towards the camera in a loop's animal pass (vf_standards.STACK_LEVELS): a limb
    (a leg, shin, foot or flipper, or anything hanging from one) not at all, the body (every part without a joint) a
    hair, every other jointed section well over the body."""
    p, n = part, 0
    while p in grid.joints and n < 16:
        if p.split("_")[0] in ST.STACK_LIMBS:
            return ST.STACK_LEVELS["limb"]
        p = grid.joints[p].get("parent")
        n += 1
    return ST.STACK_LEVELS["body"] if part not in grid.joints else ST.STACK_LEVELS["section"]


def _depth_group():
    ng = bpy.data.node_groups.get("VF · depth bias")
    if ng:
        return ng
    ng = bpy.data.node_groups.new("VF · depth bias", "GeometryNodeTree")
    ng.interface.new_socket(name="Geometry", in_out="INPUT", socket_type="NodeSocketGeometry")
    ng.interface.new_socket(name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry")
    N, L = ng.nodes, ng.links
    gi, go = N.new("NodeGroupInput"), N.new("NodeGroupOutput")
    na = N.new("GeometryNodeInputNamedAttribute")
    na.data_type = "FLOAT_VECTOR"
    na.inputs["Name"].default_value = BIAS_ATTR
    sp = N.new("GeometryNodeSetPosition")
    L.new(gi.outputs["Geometry"], sp.inputs["Geometry"])
    L.new(na.outputs["Attribute"], sp.inputs["Offset"])
    L.new(sp.outputs["Geometry"], go.inputs["Geometry"])
    return ng


def add_depth_bias(o):
    """The last modifier of an animal mesh: every vertex moves towards the camera by its stacking level (the vf_depth point
    attribute, in voxels). The offset is written per vertex (vf_bias) in the object's own axes, so call it
    again whenever the object's rotation changes (the rig does, after the join). Off until depth_bias(True)."""
    me = o.data
    back = view_axes()[3]
    local = o.matrix_world.to_3x3().inverted() @ (back * ST.VOXEL)      # one voxel towards the camera
    n = len(me.vertices)
    depth = [0.0] * n
    me.attributes[DEPTH_ATTR].data.foreach_get("value", depth)
    if BIAS_ATTR in me.attributes:
        me.attributes.remove(me.attributes[BIAS_ATTR])
    vec = me.attributes.new(BIAS_ATTR, "FLOAT_VECTOR", "POINT")
    # by stacking level (legs 0, body 0.05, head and the rest 2.05 voxels): an ear moves with its head, so its shadow
    # stays put and a far ear never jumps in front of the head; the legs never move, so they keep their whole length
    vec.data.foreach_set("vector", [c * d for d in depth for c in local])
    m = o.modifiers.get(DEPTH_MOD)
    if m:
        o.modifiers.remove(m)
    m = o.modifiers.new(DEPTH_MOD, "NODES")
    m.node_group = _depth_group()
    m.show_viewport = m.show_render = False
    return m


def depth_bias(on):
    """Turn the stacking bias on (the animal pass) or off (the shadow pass, the saved file)."""
    for o in _animal_objects():
        m = o.modifiers.get(DEPTH_MOD)
        if m:
            m.show_render = m.show_viewport = on


def _ground():
    return bpy.data.objects["VF · ground"]


def _load(path):
    im = bpy.data.images.load(path, check_existing=False)
    im.colorspace_settings.name = "Non-Color"
    im.alpha_mode = "STRAIGHT"
    w, h = im.size
    a = np.empty(w * h * 4, dtype=np.float32)
    im.pixels.foreach_get(a)
    bpy.data.images.remove(im)
    return a.reshape(h, w, 4)


def _to_lin(x):
    return np.where(x <= 0.04045, x / 12.92, ((x + 0.055) / 1.055) ** 2.4)


def _to_srgb(x):
    x = np.clip(x, 0.0, 1.0)
    return np.where(x <= 0.0031308, x * 12.92, 1.055 * np.power(x, 1 / 2.4) - 0.055)


def _blur(a, r):
    """Box blur of an (h, w, c) array over a (2r+1) square, edges clamped (cumulative sums, no SciPy in Blender)."""
    for axis in (0, 1):
        pad = [(0, 0)] * a.ndim
        pad[axis] = (r + 1, r)
        c = np.cumsum(np.pad(a, pad, mode="edge"), axis=axis, dtype=np.float64)
        n = a.shape[axis]
        hi = np.take(c, np.arange(2 * r + 1, 2 * r + 1 + n), axis=axis)
        lo = np.take(c, np.arange(0, n), axis=axis)
        a = ((hi - lo) / (2 * r + 1)).astype(np.float32)
    return a


def _smooth_shadow(s, w, r):
    """The shadow factor blurred over the open ground only (normalised convolution, weights = the ground's coverage in
    the shadow pass). The animal is a holdout there, so its pixels carry no ground; counted as unshadowed (1.0) the blur
    lifted the shadow all along the silhouette into a light halo and washed out the contact shadow under the feet
    (owner 2026-11-18: "the halo effect around the model ... feels ugly")."""
    w = np.clip(w, 0.0, 1.0).astype(np.float32)[..., None]
    num = _blur(_blur(s * w, r), r)
    den = _blur(_blur(w, r), r)
    return np.where(den > 1e-4, num / np.maximum(den, 1e-4), 1.0).astype(np.float32)


def _pass(scene, kind, path):
    ground, animal = _ground(), _animal_objects()
    if kind == "animal":
        ground.is_holdout = True
        for o in animal:
            o.is_holdout = False
        scene.view_settings.view_transform = ST.COLOR["view"]
        scene.view_settings.look = ST.COLOR["look"]
    else:
        ground.is_holdout = False
        for o in animal:
            o.is_holdout = True
        scene.view_settings.view_transform = "Standard"
        scene.view_settings.look = "None"
    scene.render.film_transparent = True         # stills keep their approved look: no stacking bias (loops only)
    scene.render.filepath = path
    t = time.time()
    bpy.ops.render.render(write_still=True, scene=scene.name)
    return time.time() - t


def render(scene_name, profile, out_png, work_dir):
    """Render one composition at a profile and write the finished flat PNG (RGB, exact background)."""
    sc = bpy.data.scenes[scene_name]
    ratio = scene_name.split()[1]
    apply_profile(sc, profile, ratio)
    os.makedirs(work_dir, exist_ok=True)
    tag = scene_name.replace(" ", "_")
    pa, ps = os.path.join(work_dir, f"{tag}.animal.png"), os.path.join(work_dir, f"{tag}.shadow.png")
    P = ST.PROFILES[profile]
    sc.eevee.taa_render_samples = P["eevee"]["taa_render_samples"]
    ta = _pass(sc, "animal", pa)
    sc.eevee.taa_render_samples = P.get("shadow_samples", P["eevee"]["taa_render_samples"])
    ts = _pass(sc, "shadow", ps)
    sc.eevee.taa_render_samples = P["eevee"]["taa_render_samples"]
    # leave the file in its plain state: ground visible, animal visible, AgX
    _ground().is_holdout = False
    for o in _animal_objects():
        o.is_holdout = False
    sc.view_settings.view_transform, sc.view_settings.look = ST.COLOR["view"], ST.COLOR["look"]

    A, S = _load(pa), _load(ps)
    La, sa = _to_lin(S[..., :3]), S[..., 3]
    open_ = sa > 0.99
    if open_.sum() < 100:
        raise RuntimeError("shadow pass: almost no open ground in frame")
    g0 = np.percentile(La[open_], 90, axis=0)
    s = np.ones_like(La)
    ok = sa > 0.01
    s[ok] = np.clip(La[ok] / g0, 0.0, 1.0)
    r = max(1, round(ST.SHADOW["smooth"] * min(s.shape[:2])))
    s = _smooth_shadow(s, np.where(ok, sa, 0.0), r)
    t = ST.SHADOW["deadzone"]
    d = np.clip(((1.0 - s) - t) / (1.0 - t), 0.0, 1.0)          # darkening past the dead zone, ramping from 0
    s = 1.0 - ST.SHADOW["strength"] * d
    flat = np.all(d <= 0.0, axis=-1)
    bg_hex = sc["vf_background"]
    T = np.array([_lin(c) for c in srgb(bg_hex)], dtype=np.float32)
    bg = _to_srgb(T * s)
    alpha = A[..., 3:4]
    out = A[..., :3] * alpha + bg * (1.0 - alpha)
    exact = flat & (alpha[..., 0] <= 0.0)
    rng = np.random.default_rng(7)
    dither = (rng.random(out.shape, dtype=np.float32) - rng.random(out.shape, dtype=np.float32)) / 255.0
    dither[exact] = 0.0
    out = np.clip(np.round((out + dither) * 255.0) / 255.0, 0.0, 1.0)
    h, w = out.shape[:2]
    rgba_out = np.concatenate([out, np.ones((h, w, 1), dtype=np.float32)], axis=-1)
    img = bpy.data.images.new(f"out {tag}", w, h, alpha=False, float_buffer=False)
    img.colorspace_settings.name = "Non-Color"
    img.pixels.foreach_set(rgba_out.ravel())
    img.filepath_raw = out_png
    img.file_format = "PNG"
    img.save()
    bpy.data.images.remove(img)
    for p in (pa, ps):
        try:
            os.remove(p)
        except OSError:
            pass
    shadowed = float((~flat).mean())
    info = dict(scene=scene_name, profile=profile, size=(w, h), seconds=round(ta + ts, 1), animal_s=round(ta, 1),
                shadow_s=round(ts, 1), ground_light=[round(float(x), 4) for x in g0], shadow_share=round(shadowed, 3),
                animal_share=round(float((alpha > 0.5).mean()), 3), background=bg_hex)
    log(f"render {scene_name} {profile} {w}x{h}: {info['seconds']} s (animal {ta:.1f}, shadow {ts:.1f}), "
        f"animal {info['animal_share']:.0%} of frame, shadow {shadowed:.0%}")
    return info


def save(path, readme):
    t = bpy.data.texts.new("README")
    t.write(readme)
    bpy.context.window_manager  # noqa: B018
    try:
        bpy.context.window.scene = bpy.data.scenes["ILL 1x1"]
    except Exception:
        pass
    os.makedirs(os.path.dirname(path), exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=path, compress=True)
    log(f"saved {path}")
