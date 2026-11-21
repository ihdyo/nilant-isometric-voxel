# 000076 · Greater Bird-of-paradise · voxel brief

*Paradisaea apoda* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `plumage` | `#BB4D00` | primary body / main colour |
| `crown` | `#FFDF20` | crown |
| `throat` | `#00BC7D` | throat |
| `plume` | `#FFD230` | plume |
| `beak` | `#74D4FF` | beak |
| `eye` | `#171717` | eye |

Background (not modelled): `#F9C5CC` (soft rose).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 0.43 m (body length 43–44 cm (excluding long ornamental tail wires up to ~75 cm)).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `flier` (pose, idle, fly, display).

## Personality, pose and expression

- Personality: flamboyant and theatrical, a proud canopy dancer.
- Pose: perched upright with wings raised and golden flank plumes fanned wide in courtship display.
- Expression: bright dark eyes under a golden crown, head tilted alertly toward the viewer.

## Recognisable features (in order of importance)

1. cascading golden-yellow flank plumes
2. iridescent emerald throat and yellow crown
3. two long wire-like central tail feathers
4. pale blue-grey bill
5. compact chestnut-brown body

## Colour map

- `plumage`: `amber-700`
- `crown`: `yellow-300`
- `throat`: `emerald-500`
- `plume`: `amber-300`
- `beak`: `sky-300`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
