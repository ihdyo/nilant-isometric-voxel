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
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import vf_standards as ST  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PALETTE = json.load(open(os.path.join(ROOT, "03 Design", "Color", "tailwind-v4-palette.json"), encoding="utf-8"))["colors"]
REPORT = []

CORNERS = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1))
CUBE = ((0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (2, 3, 7, 6), (0, 4, 7, 3), (1, 2, 6, 5))


def log(line):
    REPORT.append(line)
    print("VF:", line, flush=True)


# ---- colour ---------------------------------------------------------------------------------------------------------
def hex_of(token):
    return {"white": "FFFFFF", "black": "000000"}.get(token) or PALETTE[token]["hex"]


def _lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def srgb(token):
    h = hex_of(token)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


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


def plastic(key, token):
    P = ST.PLASTIC
    m = bpy.data.materials.new(f"VF · {key} · {token}")
    nt = _nodes(m)
    b = next((n for n in nt.nodes if n.type == "BSDF_PRINCIPLED"), None) or nt.nodes.new("ShaderNodeBsdfPrincipled")
    _set(b, "Base Color", rgba(token))
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


def animal_meshes(grid, palette, coll, geometry=None):
    """One object per part, one material per palette key. "block": every visible voxel its own bevelled cube.
    "merged": a part's outer faces share vertices, so its flat planes carry no seams; faces against another part are
    kept, so parts meet with a visible seam."""
    geometry = geometry or ST.GEOMETRY
    s = ST.VOXEL
    keys = sorted(palette)
    mats = {k: plastic(k, palette[k]) for k in keys}
    missing = [c for c in grid.colors() if c not in palette]
    if missing:
        raise KeyError(f"model uses colour keys not in animal.json look.palette: {missing}")
    objs, culled = [], 0
    for part, voxels in sorted(grid.parts().items()):
        used = sorted({c for _, c in voxels})
        index = {c: i for i, c in enumerate(used)}
        mine = {k for k, _ in voxels}
        bm = bmesh.new()
        cache = {}

        def vert(p):
            v = cache.get(p)
            if v is None:
                v = cache[p] = bm.verts.new((p[0] * s, p[1] * s, p[2] * s))
            return v

        for (x, y, z), color in voxels:
            if ST.CULL_HIDDEN and not grid.visible((x, y, z)):
                culled += 1
                continue
            if geometry == "block":
                vs = [bm.verts.new(((x + dx) * s, (y + dy) * s, (z + dz) * s)) for dx, dy, dz in CORNERS]
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
            p.use_smooth = True
        o = bpy.data.objects.new(f"VF · {part}", me)
        coll.objects.link(o)
        b = o.modifiers.new("VF bevel", "BEVEL")
        b.width = ST.BEVEL["width"]
        b.segments = ST.BEVEL["segments"]
        b.profile = ST.BEVEL["profile"]
        b.limit_method = ST.GEOMETRIES[geometry]["limit"]
        b.angle_limit = math.radians(ST.BEVEL_ANGLE)
        b.use_clamp_overlap = True
        try:
            b.harden_normals = True
        except Exception:
            pass
        objs.append(o)
    log(f"model: {len(objs)} parts ({geometry}), {len(grid.v)} voxels, {culled} hidden voxels not built, "
        f"{len(mats)} materials")
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
    s = ST.VOXEL
    pts = []
    for (x, y, z) in grid.v:
        if grid.visible((x, y, z)):
            for dx, dy, dz in CORNERS:
                pts.append(Vector(((x + dx) * s, (y + dy) * s, (z + dz) * s)))
    return pts


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
            sc["vf_background"] = look["background"]
            sc["vf_profile"] = "ULTRA"
            frames[name] = dict(ortho_scale=fr["ortho_scale"], view=fr["view"], box_size=fr["box_size"])
    bpy.context.window_manager  # noqa: B018 (keeps the context alive in background runs)
    log(f"build: {len(frames)} composition scenes, ground and {len(objs)} animal objects")
    return frames


# ---- passes and the composite ---------------------------------------------------------------------------------------
def _animal_objects():
    return list(bpy.data.collections["Animal"].all_objects)


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
    scene.render.film_transparent = True
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
    s = _blur(_blur(s, r), r)
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
