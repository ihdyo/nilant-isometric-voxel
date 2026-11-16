# 26-018 · Green Sea Turtle · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-018 · Green Sea Turtle.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:14:59
- Model: posed size 26.8 x 30.8 x 8.0 voxels (L x W x H), 2259 voxels, colours belly, eye, seam, shell, skin, parts body, flipper_hl, flipper_hr, flipper_l, flipper_r, head; turned flipper_hl, flipper_hr, flipper_l, flipper_r, head
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
