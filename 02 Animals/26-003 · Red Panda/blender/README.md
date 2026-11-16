# 26-003 · Red Panda · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-003 · Red Panda.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |

- Build: **current**, built 2026-11-16T17:05:34
- Model: the pose moves the lowest point to z = -0.13: the engine sets the animal back on the ground; posed size 31.8 x 14.9 x 20.4 voxels (L x W x H), 1821 voxels, colours dark, eye, fur, ring, white, parts body, ear_l, ear_r, head, leg_fl, leg_fr, leg_hl, leg_hr, muzzle, tail, tail_tip; turned ear_l, ear_r, head, leg_fl, leg_hl, leg_hr, tail, tail_tip
- Standards 2.1, rig `iso_top`, geometry `mob`, Blender 5.3.0
