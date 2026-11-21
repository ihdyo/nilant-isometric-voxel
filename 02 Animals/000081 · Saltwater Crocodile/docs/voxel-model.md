# 000081 · Saltwater Crocodile · voxel brief

*Crocodylus porosus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `scales` | `#474739` | primary body / main colour |
| `ridge` | `#44403B` | ridge |
| `belly` | `#FEF3C6` | belly |
| `tooth` | `#FAFAF9` | tooth |
| `iris` | `#FFD230` | iris |
| `eye` | `#171717` | eye |

Background (not modelled): `#B5E1C4` (soft leaf green).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 5.5 m (total length 4.3–5.2 m in adult males, up to 6+ m (largest living reptile)).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `walker` (pose, idle, walk, snap).

## Personality, pose and expression

- Personality: patient and sovereign, ruler of tidal estuaries.
- Pose: prowling low with jaws slightly parted showing interlocking teeth and tail sweeping to one side.
- Expression: amber eyes peering forward above a toothy crocodile grin.

## Recognisable features (in order of importance)

1. broad snout with interlocking white teeth
2. rows of armored dorsal scutes
3. long laterally flattened swimming tail
4. short muscular legs with webbed toes
5. high-set amber eyes and nostrils

## Colour map

- `scales`: `olive-700`
- `ridge`: `stone-700`
- `belly`: `amber-100`
- `tooth`: `stone-50`
- `iris`: `amber-300`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
