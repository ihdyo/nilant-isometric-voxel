# 26-013 · Toco Toucan · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-013 · Toco Toucan.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |
| `26-013 · Toco Toucan · Rig.blend` | the animation rig (`vf.py rig`, approved motion): armature `VF · armature` from the joints, mesh `VF · animal` skinned with rigid weights, actions pose (1 f), idle (48 f), hop (24 f), flap (24 f) at 24 fps, scene `ANIM 1x1` |
| `26-013 · Toco Toucan · Rig.glb` | the same rig and actions as glTF binary (Y up, one animation per action) |
| `rig.json` | the rig's stamp: plan, bones, actions, the still and motion hashes |

- Build: **current**, built 2026-11-17T17:27:16
- Animation rig: **stale** (the still .blend was rebuilt, vf_rig.py changed), bird plan, 11 bones, rigged 2026-11-17T15:20:55
- Model: posed size 22.8 x 10.6 x 21.4 voxels (L x W x H), 1129 voxels, colours bill, body, eye, feet, ring, throat, vent, parts beak, body, foot_l, foot_r, head, leg_l, leg_r, tail, wing_l, wing_r; turned beak, head, tail, wing_l
- Standards 2.2, rig `iso_top`, geometry `mob`, Blender 5.3.0
