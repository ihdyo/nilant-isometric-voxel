# 26-008 · Lion · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-008 · Lion.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:08:40
- Model: the pose moves the lowest point to z = -0.22: the engine sets the animal back on the ground; posed size 47.0 x 21.4 x 27.6 voxels (L x W x H), 6875 voxels, colours coat, eye, mane, muzzle, nose, parts body, ear_l, ear_r, head, leg_fl, leg_fr, leg_hl, leg_hr, mane, muzzle, shin_fl, shin_fr, shin_hl, shin_hr, tail, tail_tip; turned ear_l, ear_r, head, leg_fl, leg_fr, leg_hl, leg_hr, mane, shin_fl, shin_hl, tail, tail_tip
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
