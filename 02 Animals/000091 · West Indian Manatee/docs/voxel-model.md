# 000091 · West Indian Manatee · voxel brief

*Trichechus manatus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#A6A09B` | primary body / main colour |
| `shade` | `#79716B` | shade |
| `snout` | `#D6D3D1` | snout |
| `nail` | `#E7E5E4` | nail |
| `eye` | `#171717` | eye |

Background (not modelled): `#A9E2D6` (soft mint).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 3.2 m (total length 2.7–3.5 m).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `swimmer` (pose, idle, swim, graze).

## Personality, pose and expression

- Personality: gentle and placid, a slow-drifting sea cow.
- Pose: floating serenely with paddle flippers tucked forward and broad rounded tail curving.
- Expression: small gentle eyes behind a chubby whiskered snout.

## Recognisable features (in order of importance)

1. broad flat spoon-shaped paddle tail
2. chubby whiskered prehensile snout
3. plump barrel-shaped grey-brown torso
4. small paddle forelimbs with tiny nails
5. wrinkled neck folds

## Colour map

- `skin`: `stone-400`
- `shade`: `stone-500`
- `snout`: `stone-300`
- `nail`: `stone-200`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
