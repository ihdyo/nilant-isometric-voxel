# 26-012 · Bengal Tiger · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-012 · Bengal Tiger.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:11:12
- Model: the pose moves the lowest point to z = -0.18: the engine sets the animal back on the ground; posed size 43.0 x 16.1 x 25.6 voxels (L x W x H), 4244 voxels, colours eye, fur, nose, pupil, stripe, white, parts body, ear_l, ear_r, head, leg_fl, leg_fr, leg_hl, leg_hr, muzzle, shin_fl, shin_fr, shin_hl, shin_hr, tail, tail_tip; turned ear_l, ear_r, head, leg_fl, leg_fr, leg_hl, leg_hr, shin_fl, shin_hl, tail, tail_tip
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
