# 26-001 · Red Fox · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-001 · Red Fox.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T02:12:14
- Model: size 31 x 7 x 18 voxels (L x W x H), 970 voxels, 633 visible, colours dark, eye, fur, white, parts body, ears, head, legs, tail
- Standards 1.0, rig `iso_top`, geometry `merged`, Blender 5.3.0
