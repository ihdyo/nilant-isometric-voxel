# 26-021 · Bottlenose Dolphin · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-021 · Bottlenose Dolphin.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:16:52
- Model: posed size 42.0 x 16.2 x 12.2 voxels (L x W x H), 1986 voxels, colours back, belly, eye, grey, parts beak, body, flipper_l, flipper_r, flukes, head, tail, tail_tip; turned flipper_l, flipper_r, flukes, head, tail, tail_tip
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
