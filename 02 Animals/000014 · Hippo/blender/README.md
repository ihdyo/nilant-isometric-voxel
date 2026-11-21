# 000014 · Hippo · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `000014 · Hippo.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |
| `000014 · Hippo · Rig.blend` | the animation rig (`vf.py rig`, approved motion): armature `VF · armature` from the joints, mesh `VF · animal` skinned with rigid weights, actions pose (1 f), idle (48 f), walk (64 f), yawn (48 f) at 24 fps, scene `ANIM 1x1` |
| `000014 · Hippo · Rig.glb` | the same rig and actions as glTF binary (Y up, one animation per action) |
| `rig.json` | the rig's stamp: plan, bones, actions, the still and motion hashes |

- Build: **current**, built 2026-11-21T16:56:13
- Animation rig: **current**, walker plan, 10 bones, rigged 2026-11-21T16:56:18
- Model: the pose moves the lowest point to z = -0.47: the engine sets the animal back on the ground; posed size 45.1 x 22.1 x 28.4 voxels (L x W x H), 12343 voxels, colours eye, mouth, pink, skin, tusk, parts body, ear_l, ear_r, head, jaw, leg_fl, leg_fr, leg_hl, leg_hr; turned ear_l, ear_r, head, jaw, leg_fl, leg_fr, leg_hl, leg_hr
- Standards 2.3, rig `iso_top`, geometry `mob`, Blender 5.3.0
