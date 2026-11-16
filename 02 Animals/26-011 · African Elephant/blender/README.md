# 26-011 · African Elephant · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-011 · African Elephant.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:10:32
- Model: the pose moves the lowest point to z = -0.21: the engine sets the animal back on the ground; posed size 53.1 x 34.7 x 38.5 voxels (L x W x H), 15871 voxels, colours eye, nail, shade, skin, tusk, white, parts body, ear_l, ear_r, head, leg_fl, leg_fr, leg_hl, leg_hr, shin_fl, shin_fr, shin_hl, shin_hr, tail, trunk_1, trunk_2, trunk_3, tusk_l, tusk_r; turned ear_l, ear_r, head, leg_fl, leg_fr, leg_hl, shin_fl, shin_hl, tail, trunk_1, trunk_2, trunk_3, tusk_l, tusk_r
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
