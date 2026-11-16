# 26-004 · Emperor Penguin · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-004 · Emperor Penguin.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:06:11
- Model: posed size 14.7 x 20.2 x 28.0 voxels (L x W x H), 2677 voxels, colours bill, black, cream, white, yellow, parts beak, body, flipper_l, flipper_r, foot_l, foot_r, head; turned beak, flipper_l, flipper_r, foot_l, foot_r, head
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
