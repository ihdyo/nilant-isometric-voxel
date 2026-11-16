# 26-020 · Scarlet Macaw · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-020 · Scarlet Macaw.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:16:13
- Model: posed size 26.2 x 19.7 x 23.6 voxels (L x W x H), 1489 voxels, colours bill, blue, dark, eye, face, red, yellow, parts beak, body, head, leg_l, leg_r, tail, tail_tip, wing_l, wing_r; turned beak, head, tail, tail_tip, wing_l, wing_r
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
