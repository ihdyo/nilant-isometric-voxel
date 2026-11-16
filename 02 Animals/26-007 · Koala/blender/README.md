# 26-007 · Koala · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-007 · Koala.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:08:01
- Model: posed size 13.6 x 24.4 x 25.3 voxels (L x W x H), 2988 voxels, colours eye, fur, nose, paw, white, parts arm_l, arm_r, body, ear_l, ear_r, head, leg_l, leg_r, nose; turned arm_l, arm_r, ear_l, ear_r, head, leg_l, leg_r
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
