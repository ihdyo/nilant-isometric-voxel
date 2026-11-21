# 000043 · Spectral Tarsier · Blender

> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and build again; never edit the .blend by hand.

| File | What |
|---|---|
| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |
| `000043 · Spectral Tarsier.blend` | the editable project, built from `model.py`: collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |
| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |
| `000043 · Spectral Tarsier · Rig.blend` | the animation rig (`vf.py rig`, approved motion) |
| `000043 · Spectral Tarsier · Rig.glb` | the same rig and actions as glTF binary (Y up, one animation per action) |
| `rig.json` | the rig's stamp: plan, bones, actions, the still and motion hashes |

- Build: **pending** (run `python _system/studio/scripts/vf.py build 000043`)
- Animation rig: **pending** (biped_upright plan)
