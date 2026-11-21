# 000020 · Scarlet Macaw · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `000020 · Scarlet Macaw.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |
| `000020 · Scarlet Macaw · Rig.blend` | the animation rig (`vf.py rig`, approved motion): armature `VF · armature` from the joints, mesh `VF · animal` skinned with rigid weights, actions pose (1 f), idle (48 f), flap (48 f) at 24 fps, scene `ANIM 1x1` |
| `000020 · Scarlet Macaw · Rig.glb` | the same rig and actions as glTF binary (Y up, one animation per action) |
| `rig.json` | the rig's stamp: plan, bones, actions, the still and motion hashes |

- Build: **current**, built 2026-11-21T16:56:54
- Animation rig: **current**, bird plan, 10 bones, rigged 2026-11-21T16:56:58
- Model: posed size 26.0 x 18.3 x 23.7 voxels (L x W x H), 1477 voxels, colours bill, blue, dark, eye, face, red, yellow, parts beak, body, head, leg_l, leg_r, tail, tail_tip, wing_l, wing_r; turned beak, head, tail, tail_tip, wing_l, wing_r
- Standards 2.3, rig `iso_top`, geometry `mob`, Blender 5.3.0
