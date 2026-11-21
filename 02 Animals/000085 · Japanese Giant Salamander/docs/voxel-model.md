# 000085 · Japanese Giant Salamander · voxel brief

*Andrias japonicus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#7B3306` | primary body / main colour |
| `mottle` | `#292524` | mottle |
| `fold` | `#44403B` | fold |
| `belly` | `#A6A09B` | belly |
| `eye` | `#171717` | eye |

Background (not modelled): `#A9E2D6` (soft mint).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 1.4 m (total length 1.0–1.5 m (second-largest amphibian in the world)).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `walker` (pose, idle, walk, swim).

## Personality, pose and expression

- Personality: ancient and tranquil, a living fossil of mountain rivers.
- Pose: crawling smoothly along the riverbed with lateral skin folds rippling and paddle tail curving.
- Expression: tiny bead-like eyes set wide on a broad, friendly flat head.

## Recognisable features (in order of importance)

1. broad flat head with tiny widely spaced eyes
2. wrinkled lateral skin folds along the flanks
3. mottled dark brown and black skin
4. short stubby four- and five-toed legs
5. vertically flattened paddle tail

## Colour map

- `skin`: `amber-900`
- `mottle`: `stone-800`
- `fold`: `stone-700`
- `belly`: `stone-400`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
