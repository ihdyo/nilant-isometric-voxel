# 26-013 · Toco Toucan · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-013 · Toco Toucan.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:11:50
- Model: posed size 22.8 x 10.6 x 21.4 voxels (L x W x H), 1129 voxels, colours bill, body, eye, feet, ring, throat, vent, parts beak, body, foot_l, foot_r, head, leg_l, leg_r, tail, wing_l, wing_r; turned beak, head, tail, wing_l
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
