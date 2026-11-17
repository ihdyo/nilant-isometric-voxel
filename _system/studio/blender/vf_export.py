"""Voxel Fauna · the ULTRA export renders: one Blender run per animal, from its rig .blend.

    blender -b --factory-startup --python vf_export.py -- <job.json>

PROPOSED 2026-11-17 (owner: "the master ultra render for single animal is 2, the dynamic pose and the regular blocky
pose ... 1:1 dynamic (this pic is for stock image) ... looped dynamic animated ... card pdf"; "render.bat should be
rendering only (2 image and 1 motion)"). APPROVED by the owner 2026-11-17 ("i approve everything"): this file, with
EXPORT below, and scripts/package.py are in the standards lock (v2.2 + the export package).

What it renders (everything else, the stock crop, the GIF and the cards, is built offline by scripts/package.py):
  - the two master renders, each a 4096 square on the animal's background with the composited shadow: the dynamic
    pose (the action "pose", the approved still) and the regular blocky pose (the rest pose: every joint straight,
    set on the ground). The animal sits inside the centre safe square (EXPORT.safe), so a centred 1:1, 9:16
    (2304 x 4096) or 16:9 (4096 x 2304) crop never cuts it;
  - each master's animal pass with its alpha (a cut-out for the card);
  - the frames of the looped dynamic animation: the animal's signature action, framed on everything it does.

job.json (written by scripts/vf.py final, never by hand):
    {"open": ".../<code> · <Name> · Rig.blend", "profile": "ULTRA" | "LOW",
     "masters": {"dyn": ".../VF-<code>-MASTER-DYN.png", "block": ".../VF-<code>-MASTER-BLOCK.png"},
     "cutouts": {"dyn": ".../cut-dyn.png", "block": ".../cut-block.png"},
     "loop": {"action": "walk", "dir": ".../loop", "profile": "LOOP" | "LOOP_LOW"},
     "work": "...", "result": "..."}
"""
import json
import math
import os
import shutil
import sys
import time
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# ---- the export package (APPROVED 2026-11-17, locked with this file) --------------------------------------------------------
EXPORT = dict(
    master=4096,             # px, square: one master per pose (owner, 2026-11-17: "4096 x 4096")
    safe=2304,               # px: the centre square that a centred 1:1, 9:16 (2304 x 4096) and 16:9 (4096 x 2304) crop
                             # all keep (2304 = 4096 x 9/16): the animal lives inside it
    fill=0.86,               # of the safe square, on the binding side, that the animal's projected box takes
    stock=2880,              # px: the 1:1 stock image, the centre square of the dynamic master (the animal fills about
                             # 0.69 of it, like the approved 1:1 illustration's 0.70); 8.3 MP, over every site's minimum
    loop=dict(size=1080,     # px, square GIF (owner, 2026-11-17: "GIF 1080 x 1080")
              fill=0.72,     # of the frame that everything the loop does takes
              samples=64, shadow_samples=32, rt_resolution="2", fast_gi_resolution="2",
                             # Nilant's film quality for one frame of footage (64 samples), ray tracing at half
                             # resolution: about 8 s a frame at 1080 on the RTX 3050
              fps=24),
    card=dict(trim_mm=(148.0, 210.0),       # A5 portrait (owner: "card in a5 size in pdf")
              bleed_mm=3.0, dpi=300),
    items=(                  # the export folder, by Image ID suffix: (suffix, extension, what)
        ("MASTER-DYN", "png", "master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9)"),
        ("MASTER-BLOCK", "png", "master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9)"),
        ("STOCK-1x1", "png", "1:1 dynamic for stock sites, the centre square of the dynamic master"),
        ("LOOP", "gif", "looped dynamic animation, 1080 square"),
        ("CARD-EN", "pdf", "A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose"),
        ("CARD-ID", "pdf", "A5 card, Bahasa Indonesia: the same card in Indonesian"),
    ),
)


def log(line):
    print("VF:", line, flush=True)


def install(ST):
    """The export's profiles and framings, added to the standards at run time (until they move into vf_standards)."""
    U, L = ST.PROFILES["ULTRA"], EXPORT["loop"]
    ST.PROFILES["LOOP"] = dict(U, scale=L["size"] / ST.SIZES["1x1"][0],
                               eevee=dict(U["eevee"], taa_render_samples=L["samples"],
                                          fast_gi_resolution=L["fast_gi_resolution"]),
                               rt_resolution=L["rt_resolution"], shadow_samples=L["shadow_samples"])
    ST.PROFILES["LOOP_LOW"] = dict(ST.PROFILES["LOW"], scale=ST.MOTION["preview_scale"])
    m = (1.0 - EXPORT["safe"] / EXPORT["master"]) / 2.0
    ST.FRAMING["MASTER"] = {"1x1": dict(zone=(m, m, 1.0 - m, 1.0 - m), fill=EXPORT["fill"])}
    ST.FRAMING["LOOP"] = {"1x1": dict(zone=(0.0, 0.0, 1.0, 1.0), fill=L["fill"])}


def _set_action(arm, name):
    import bpy
    ad = arm.animation_data
    if name is None:
        ad.action = None
        return
    act = bpy.data.actions[name]
    ad.action = act
    try:
        if ad.action_slot is None and len(act.slots):
            ad.action_slot = act.slots[0]
    except Exception:
        pass


def _extremes(co, R):
    from mathutils import Vector
    pr = co @ R.T
    return [Vector(tuple(co[int(pr[:, k].argmin())])) for k in range(3)] + \
           [Vector(tuple(co[int(pr[:, k].argmax())])) for k in range(3)]


def pose(arm, mesh, scene, which):
    """Put the rig in one master pose: "dyn" = the action "pose" (the approved still); "block" = the rest pose, every
    joint straight, the lowest voxel corner set on the ground."""
    import bpy
    from mathutils import Vector
    import vf_rig as VR
    vl = bpy.context.view_layer
    if which == "dyn":
        _set_action(arm, "pose")
        scene.frame_set(0)
        vl.update()
        return
    _set_action(arm, None)
    for pb in arm.pose.bones:
        pb.rotation_mode = "QUATERNION"
        pb.rotation_quaternion = (1, 0, 0, 0)
        pb.location = (0, 0, 0)
    vl.update()
    z = float(VR._coords(mesh)[:, 2].min())
    root = arm.pose.bones["root"]
    root.location = arm.data.bones["root"].matrix_local.to_3x3().inverted() @ Vector((0.0, 0.0, -z))
    vl.update()


def _flat(A, S, bg_hex, dither=True):
    """The animal pass over the exact background, darkened by the shadow pass: the maths of vf_scene.render."""
    import numpy as np
    import vf_standards as ST
    import vf_scene as V
    La, sa = V._to_lin(S[..., :3]), S[..., 3]
    open_ = sa > 0.99
    if open_.sum() < 100:
        raise RuntimeError("shadow pass: almost no open ground in frame")
    g0 = np.percentile(La[open_], 90, axis=0)
    s = np.ones_like(La)
    ok = sa > 0.01
    s[ok] = np.clip(La[ok] / g0, 0.0, 1.0)
    r = max(1, round(ST.SHADOW["smooth"] * min(s.shape[:2])))
    s = V._blur(V._blur(s, r), r)
    t = ST.SHADOW["deadzone"]
    d = np.clip(((1.0 - s) - t) / (1.0 - t), 0.0, 1.0)
    s = 1.0 - ST.SHADOW["strength"] * d
    flat = np.all(d <= 0.0, axis=-1)
    T = np.array([V._lin(c) for c in V.srgb(bg_hex)], dtype=np.float32)
    bg = V._to_srgb(T * s)
    alpha = A[..., 3:4]
    out = A[..., :3] * alpha + bg * (1.0 - alpha)
    if dither:
        exact = flat & (alpha[..., 0] <= 0.0)
        rng = np.random.default_rng(7)
        dz = (rng.random(out.shape, dtype=np.float32) - rng.random(out.shape, dtype=np.float32)) / 255.0
        dz[exact] = 0.0
        out = out + dz
    return np.clip(np.round(out * 255.0) / 255.0, 0.0, 1.0)


def _save(out, path):
    import bpy
    import numpy as np
    h, w = out.shape[:2]
    img = bpy.data.images.new("vf export", w, h, alpha=False, float_buffer=False)
    img.colorspace_settings.name = "Non-Color"
    img.pixels.foreach_set(np.concatenate([out, np.ones((h, w, 1), dtype=np.float32)], axis=-1).ravel())
    img.filepath_raw = path
    img.file_format = "PNG"
    img.save()
    bpy.data.images.remove(img)


def master(arm, mesh, scene, which, profile, out_png, cut_png, work):
    """One master render: framed in the centre safe square, the two passes, the flat composite and the cut-out."""
    import numpy as np
    import vf_standards as ST
    import vf_scene as V
    import vf_rig as VR
    pose(arm, mesh, scene, which)
    q, right, up, back = V.view_axes()
    R = np.array([list(right), list(up), list(back)])
    w, h = ST.SIZES["1x1"]
    fr = V.frame("MASTER", "1x1", _extremes(VR._coords(mesh), R), w, h)
    V.camera(scene, f"CAM · MASTER {which}", fr)
    V.apply_profile(scene, profile, "1x1")
    os.makedirs(work, exist_ok=True)
    pa, ps = os.path.join(work, f"master-{which}.animal.png"), os.path.join(work, f"master-{which}.shadow.png")
    P = ST.PROFILES[profile]
    t0 = time.time()
    scene.eevee.taa_render_samples = P["eevee"]["taa_render_samples"]
    V._pass(scene, "animal", pa)
    scene.eevee.taa_render_samples = P.get("shadow_samples", P["eevee"]["taa_render_samples"])
    V._pass(scene, "shadow", ps)
    V._ground().is_holdout = False
    for o in V._animal_objects():
        o.is_holdout = False
    scene.view_settings.view_transform, scene.view_settings.look = ST.COLOR["view"], ST.COLOR["look"]
    for p in (out_png, cut_png):
        os.makedirs(os.path.dirname(p), exist_ok=True)
    shutil.copyfile(pa, cut_png)
    _save(_flat(V._load(pa), V._load(ps), scene["vf_background"], dither=True), out_png)
    for p in (pa, ps):
        try:
            os.remove(p)
        except OSError:
            pass
    secs = round(time.time() - t0, 1)
    log(f"master {which} {profile}: {scene.render.resolution_x} px in {secs} s, safe square "
        f"{EXPORT['safe'] / EXPORT['master']:.4f} of the frame")
    return dict(which=which, profile=profile, seconds=secs, out=out_png, cutout=cut_png,
                ortho_scale=fr["ortho_scale"])


def loop(arm, mesh, scene, action, out_dir, profile, work):
    """The frames of the looped animation: framed on every frame of the action, each pass rendered as one animation,
    composited frame by frame like the stills."""
    import bpy
    import numpy as np
    import vf_standards as ST
    import vf_scene as V
    import vf_rig as VR
    _set_action(arm, action)
    act = bpy.data.actions[action]
    n = max(1, int(act.frame_end))
    q, right, up, back = V.view_axes()
    R = np.array([list(right), list(up), list(back)])
    pts = []
    for f in range(n):
        scene.frame_set(f)
        pts += _extremes(VR._coords(mesh), R)
    w, h = ST.SIZES["1x1"]
    fr = V.frame("LOOP", "1x1", pts, w, h)
    V.camera(scene, "CAM · LOOP", fr)
    V.apply_profile(scene, profile, "1x1")
    P = ST.PROFILES[profile]
    os.makedirs(out_dir, exist_ok=True)
    for old in os.listdir(out_dir):
        if old.endswith(".png"):
            os.remove(os.path.join(out_dir, old))
    tmp = os.path.join(work, "loop")
    os.makedirs(tmp, exist_ok=True)
    scene.frame_start, scene.frame_end, scene.frame_step = 0, n - 1, 1
    scene.render.film_transparent = True
    ground, animal = V._ground(), V._animal_objects()
    t0 = time.time()
    for kind in ("a", "s"):
        ground.is_holdout = kind == "a"
        for o in animal:
            o.is_holdout = kind == "s"
        if kind == "a":
            scene.view_settings.view_transform, scene.view_settings.look = ST.COLOR["view"], ST.COLOR["look"]
            scene.eevee.taa_render_samples = P["eevee"]["taa_render_samples"]
        else:
            scene.view_settings.view_transform, scene.view_settings.look = "Standard", "None"
            scene.eevee.taa_render_samples = P.get("shadow_samples", P["eevee"]["taa_render_samples"])
        scene.render.filepath = os.path.join(tmp, f"{kind}_####")
        bpy.ops.render.render(animation=True, scene=scene.name)
    ground.is_holdout = False
    for o in animal:
        o.is_holdout = False
    scene.view_settings.view_transform, scene.view_settings.look = ST.COLOR["view"], ST.COLOR["look"]
    outs = []
    for f in range(n):
        p = os.path.join(out_dir, f"{f:03d}.png")
        VR._composite(os.path.join(tmp, f"a_{f:04d}.png"), os.path.join(tmp, f"s_{f:04d}.png"),
                      scene["vf_background"], p)
        outs.append(p)
    secs = round(time.time() - t0, 1)
    log(f"loop {action} {profile}: {n} frames at {scene.render.resolution_x} px in {secs} s")
    return dict(action=action, profile=profile, frames=outs, fps=ST.MOTION["fps"], seconds=secs)


def main():
    job_path = sys.argv[sys.argv.index("--") + 1]
    job = json.load(open(job_path, encoding="utf-8"))
    result = dict(ok=False, started=time.strftime("%Y-%m-%d %H:%M:%S"))
    try:
        import bpy
        import vf_standards as ST
        install(ST)
        result["blender"] = bpy.app.version_string
        bpy.ops.wm.open_mainfile(filepath=job["open"])
        log(f"opened {job['open']}")
        arm, mesh = bpy.data.objects["VF · armature"], bpy.data.objects["VF · animal"]
        scene = bpy.context.scene
        result["masters"] = {}
        for which, out_png in (job.get("masters") or {}).items():
            result["masters"][which] = master(arm, mesh, scene, which, job.get("profile", "ULTRA"), out_png,
                                              job["cutouts"][which], job["work"])
            json.dump(result, open(job["result"] + ".partial", "w", encoding="utf-8"), default=str)
        if job.get("loop"):
            L = job["loop"]
            result["loop"] = loop(arm, mesh, scene, L["action"], L["dir"], L.get("profile", "LOOP"), job["work"])
        result["ok"] = True
    except Exception as e:
        result["error"] = f"{type(e).__name__}: {e}"
        result["trace"] = traceback.format_exc()
        print("VF: FAILED", result["error"], flush=True)
    result["finished"] = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(job["result"], "w", encoding="utf-8") as f:
        json.dump(result, f, indent=1, default=str)


if __name__ == "__main__":
    main()
