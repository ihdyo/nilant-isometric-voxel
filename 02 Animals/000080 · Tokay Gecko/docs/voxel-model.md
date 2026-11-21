# 000080 · Tokay Gecko · voxel brief

*Gekko gecko* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#90A1B9` | primary body / main colour |
| `spot` | `#FF6900` | spot |
| `blue_spot` | `#74D4FF` | blue spot |
| `belly` | `#E7E5E4` | belly |
| `iris` | `#FFB900` | iris |
| `eye` | `#171717` | eye |

Background (not modelled): `#ADDCF5` (soft sky blue).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 0.35 m (total length 25–35 cm from snout to tail tip).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `walker` (pose, idle, walk, call).

## Personality, pose and expression

- Personality: bold and vocal, a nocturnal wall-climber.
- Pose: perched mid-stride with splayed sticky toes and banded tail curved in an S-shape.
- Expression: wide golden eyes with vertical pupils and a confident gecko grin.

## Recognisable features (in order of importance)

1. bluish-grey skin with bright orange-red spots
2. wide fanned adhesive toe pads
3. large golden eyes with vertical slit pupils
4. broad triangular gecko head
5. thick banded tail

## Colour map

- `skin`: `slate-400`
- `spot`: `orange-500`
- `blue_spot`: `sky-300`
- `belly`: `stone-200`
- `iris`: `amber-400`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
