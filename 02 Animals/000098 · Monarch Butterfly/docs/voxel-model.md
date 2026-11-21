# 000098 · Monarch Butterfly · voxel brief

*Danaus plexippus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `wing` | `#FF6900` | primary body / main colour |
| `vein` | `#171717` | vein |
| `spot` | `#FAFAF9` | spot |
| `body` | `#171717` | body |
| `eye` | `#171717` | eye |

Background (not modelled): `#E0D5A8` (soft straw).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 0.1 m (wingspan 8.9–10.2 cm).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `flier` (pose, idle, flutter, glide).

## Personality, pose and expression

- Personality: buoyant and tireless, a long-distance sky traveler.
- Pose: gliding with broad patterned wings spread open in a gentle V-angle.
- Expression: large compound eyes and delicate clubbed antennae swept forward.

## Recognisable features (in order of importance)

1. vivid orange wings with bold black veins
2. black wing borders dotted with double rows of white spots
3. white-spotted black body
4. slender clubbed antennae
5. broad forewings and rounded hindwings

## Colour map

- `wing`: `orange-500`
- `vein`: `neutral-900`
- `spot`: `stone-50`
- `body`: `neutral-900`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
