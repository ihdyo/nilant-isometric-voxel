# 26-022 · Mountain Goat · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-022 · Mountain Goat.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:17:31
- Model: posed size 30.5 x 13.0 x 29.3 voxels (L x W x H), 3943 voxels, colours coat, horn, nose, shade, parts body, ear_l, ear_r, head, horn_l, horn_r, leg_fl, leg_fr, leg_hl, leg_hr, muzzle, shin_fl, shin_fr, shin_hl, shin_hr; turned ear_l, ear_r, head, horn_l, horn_r, leg_fl, shin_fl
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
