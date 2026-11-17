# 26-018 · Green Sea Turtle · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-018 · Green Sea Turtle.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |
| `26-018 · Green Sea Turtle · Rig.blend` | the animation rig (`vf.py rig`, approved motion): armature `VF · armature` from the joints, mesh `VF · animal` skinned with rigid weights, actions pose (1 f), idle (48 f), swim (48 f) at 24 fps, scene `ANIM 1x1` |
| `26-018 · Green Sea Turtle · Rig.glb` | the same rig and actions as glTF binary (Y up, one animation per action) |
| `rig.json` | the rig's stamp: plan, bones, actions, the still and motion hashes |

- Build: **current**, built 2026-11-18T00:42:21
- Animation rig: **current**, swimmer plan, 7 bones, rigged 2026-11-18T00:42:24
- Model: posed size 26.8 x 30.8 x 7.4 voxels (L x W x H), 2151 voxels, colours belly, eye, seam, shell, skin, parts body, flipper_hl, flipper_hr, flipper_l, flipper_r, head; turned flipper_hl, flipper_hr, flipper_l, flipper_r, head
- Standards 2.2, rig `iso_top`, geometry `mob`, Blender 5.3.0
