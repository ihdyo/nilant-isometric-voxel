# 26-006 · American Flamingo · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `26-006 · American Flamingo.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |
| `26-006 · American Flamingo · Rig.blend` | the animation rig (`vf.py rig`, approved motion): armature `VF · armature` from the joints, mesh `VF · animal` skinned with rigid weights, actions pose (1 f), idle (48 f), walk (48 f), flap (48 f) at 24 fps, scene `ANIM 1x1` |
| `26-006 · American Flamingo · Rig.glb` | the same rig and actions as glTF binary (Y up, one animation per action) |
| `rig.json` | the rig's stamp: plan, bones, actions, the still and motion hashes |

- Build: **current**, built 2026-11-18T00:41:30
- Animation rig: **current**, bird plan, 13 bones, rigged 2026-11-18T00:41:32
- Model: posed size 16.2 x 11.0 x 34.3 voxels (L x W x H), 1059 voxels, colours bill, black, eye, feet, legs, light, pink, parts beak, body, foot_l, foot_r, head, leg_l, leg_r, neck, shin_l, shin_r, wing_l, wing_r; turned beak, foot_l, foot_r, head, leg_l, neck, shin_l, wing_l, wing_r
- Standards 2.2, rig `iso_top`, geometry `mob`, Blender 5.3.0
