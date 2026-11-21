# 000090 · Beluga Whale · voxel brief

*Delphinapterus leucas* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#FAFAF9` | primary body / main colour |
| `shade` | `#E2E8F0` | shade |
| `lip` | `#D6D3D1` | lip |
| `eye` | `#171717` | eye |

Background (not modelled): `#AFDBF7` (soft sky blue).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 4.5 m (total length 3.5–5.5 m).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `swimmer` (pose, idle, swim, nod).

## Personality, pose and expression

- Personality: playful and expressive, the canary of the sea.
- Pose: swimming smoothly with head turned slightly toward the camera and tail curving.
- Expression: bulbous melon forehead above a cheerful, expressive smile.

## Recognisable features (in order of importance)

1. pure snow-white skin
2. prominent bulbous forehead melon
3. flexible neck able to turn and nod
4. smooth back with no dorsal fin
5. short upturned paddle flippers

## Colour map

- `skin`: `stone-50`
- `shade`: `slate-200`
- `lip`: `stone-300`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
