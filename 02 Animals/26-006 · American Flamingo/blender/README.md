# 26-006 · American Flamingo · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-006 · American Flamingo.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:07:27
- Model: 27 voxels are not mirrored across y = 0 (fine for a pose or a marking; check it is meant); posed size 17.7 x 11.0 x 34.3 voxels (L x W x H), 1062 voxels, colours bill, black, eye, feet, legs, light, pink, parts beak, body, foot_l, foot_r, head, leg_l, leg_r, neck, wing_l, wing_r; turned beak, foot_r, head, leg_l, neck, wing_l, wing_r
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
