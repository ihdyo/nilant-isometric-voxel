# 000088 · Orca · voxel brief

*Orcinus orca* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `black` | `#171717` | primary body / main colour |
| `white` | `#FAFAF9` | white |
| `saddle` | `#90A1B9` | saddle |
| `eye` | `#171717` | eye |

Background (not modelled): `#C7D2FD` (soft lavender).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 8.0 m (total length 6–8 m in adult males, up to 9.8 m).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `swimmer` (pose, idle, swim, spyhop).

## Personality, pose and expression

- Personality: intelligent and cohesive, a strategic ocean apex predator.
- Pose: surging forward through the water with tall dorsal fin upright and flippers angled.
- Expression: sleek streamlined head with iconic white eye patch and confident smile line.

## Recognisable features (in order of importance)

1. striking jet-black and snow-white coloration
2. large white patch behind each eye
3. tall erect triangular dorsal fin
4. grey saddle patch behind the dorsal fin
5. broad rounded paddle flippers

## Colour map

- `black`: `neutral-900`
- `white`: `stone-50`
- `saddle`: `slate-400`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
