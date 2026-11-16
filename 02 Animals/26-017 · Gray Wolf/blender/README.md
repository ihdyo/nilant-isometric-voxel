# 26-017 · Gray Wolf · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-017 · Gray Wolf.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:14:21
- Model: posed size 28.7 x 15.0 x 26.4 voxels (L x W x H), 3127 voxels, colours back, fur, light, nose, parts body, ear_l, ear_r, head, leg_fl, leg_fr, leg_hl, leg_hr, snout, tail, tail_tip, torso; turned ear_l, ear_r, head, tail, tail_tip, torso
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
