# 26-021 · Bottlenose Dolphin · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-021 · Bottlenose Dolphin.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |
| `26-021 · Bottlenose Dolphin · Rig.blend` | the animation rig (`vf.py rig`, approved motion): armature `VF · armature` from the joints, mesh `VF · animal` skinned with rigid weights, actions pose (1 f), idle (48 f), swim (32 f) at 24 fps, scene `ANIM 1x1` |
| `26-021 · Bottlenose Dolphin · Rig.glb` | the same rig and actions as glTF binary (Y up, one animation per action) |
| `rig.json` | the rig's stamp: plan, bones, actions, the still and motion hashes |

- Build: **current**, built 2026-11-17T15:20:13
- Animation rig: **current**, swimmer plan, 9 bones, rigged 2026-11-17T15:21:12
- Model: posed size 42.0 x 16.2 x 12.2 voxels (L x W x H), 1986 voxels, colours back, belly, eye, grey, parts beak, body, flipper_l, flipper_r, flukes, head, tail, tail_tip; turned flipper_l, flipper_r, flukes, head, tail, tail_tip
- Standards 2.2, rig `iso_top`, geometry `mob`, Blender 5.3.0
