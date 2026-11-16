# 26-010 · Giraffe · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-010 · Giraffe.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:09:55
- Model: the pose moves the lowest point to z = -0.03: the engine sets the animal back on the ground; 223 voxels are not mirrored across y = 0 (fine for a pose or a marking; check it is meant); posed size 28.2 x 11.3 x 54.9 voxels (L x W x H), 3215 voxels, colours base, dark, eye, mane, patch, tongue, parts body, ear_l, ear_r, head, leg_fl, leg_fr, leg_hl, leg_hr, neck, shin_fl, shin_fr, shin_hl, shin_hr, tail, tongue; turned ear_l, ear_r, head, leg_fl, leg_hr, neck, shin_fl, shin_hr, tail, tongue
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
