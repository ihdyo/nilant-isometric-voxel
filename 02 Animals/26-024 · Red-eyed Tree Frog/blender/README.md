# 26-024 · Red-eyed Tree Frog · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-024 · Red-eyed Tree Frog.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |
| `26-024 · Red-eyed Tree Frog · Rig.blend` | the animation rig (`vf.py rig`, approved motion): armature `VF · armature` from the joints, mesh `VF · animal` skinned with rigid weights, actions pose (1 f), idle (48 f), hop (48 f) at 24 fps, scene `ANIM 1x1` |
| `26-024 · Red-eyed Tree Frog · Rig.glb` | the same rig and actions as glTF binary (Y up, one animation per action) |
| `rig.json` | the rig's stamp: plan, bones, actions, the still and motion hashes |

- Build: **current**, built 2026-11-17T21:42:25
- Animation rig: **current**, hopper plan, 11 bones, rigged 2026-11-17T21:42:27
- Model: posed size 16.9 x 17.0 x 10.7 voxels (L x W x H), 1011 voxels, colours belly, blue, green, pupil, red, toe, yellow, parts body, head, leg_fl, leg_fr, leg_hl, leg_hr, shin_fl, shin_fr, shin_hl, shin_hr; turned head
- Standards 2.2, rig `iso_top`, geometry `mob`, Blender 5.3.0
