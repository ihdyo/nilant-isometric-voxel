# 26-010 · Giraffe · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-010 · Giraffe.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |
| `26-010 · Giraffe · Rig.blend` | the animation rig (`vf.py rig`, approved motion): armature `VF · armature` from the joints, mesh `VF · animal` skinned with rigid weights, actions pose (1 f), idle (48 f), walk (48 f), reach (48 f) at 24 fps, scene `ANIM 1x1` |
| `26-010 · Giraffe · Rig.glb` | the same rig and actions as glTF binary (Y up, one animation per action) |
| `rig.json` | the rig's stamp: plan, bones, actions, the still and motion hashes |

- Build: **current**, built 2026-11-17T17:25:38
- Animation rig: **current**, walker plan, 15 bones, rigged 2026-11-17T19:36:26
- Model: the pose moves the lowest point to z = -0.03: the engine sets the animal back on the ground; 220 voxels are not mirrored across y = 0 (fine for a pose or a marking; check it is meant); posed size 28.2 x 11.3 x 54.9 voxels (L x W x H), 3212 voxels, colours base, dark, eye, mane, patch, parts body, ear_l, ear_r, head, leg_fl, leg_fr, leg_hl, leg_hr, neck, shin_fl, shin_fr, shin_hl, shin_hr, tail; turned ear_l, ear_r, head, leg_fl, leg_hr, neck, shin_fl, shin_hr, tail
- Standards 2.2, rig `iso_top`, geometry `mob`, Blender 5.3.0
