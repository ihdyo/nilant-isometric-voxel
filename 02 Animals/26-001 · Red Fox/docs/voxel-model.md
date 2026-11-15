# 26-001 · Red Fox · voxel brief

*Vulpes vulpes* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `fur` | `orange-600` | body, head, tail, upper legs |
| `white` | `stone-50` | tail tip, chest bib, cheeks and the underside of the snout |
| `dark` | `stone-800` | lower legs (stockings), ear tips, nose |
| `eye` | `neutral-950` | one voxel on each corner of the face |

Background (not modelled): `teal-200`.

## Size and pose

- Size: 31 × 7 × 18 voxels (L × W × H); longest side 31 (budget 16–32).
- Pose: standing, head level, tail held out behind. Head towards +X, feet on z = 0, left flank at −Y, symmetric about y = 0.
- Parts: legs, body, head, ears, tail.

## Proportions (inclusive voxel ranges of each part, as built)

| Part | x | y | z |
|---|---|---|---|
| tail | -6 to 3 | -2 to 2 | 6 to 10 |
| body | 4 to 16 | -3 to 3 | 6 to 11 |
| legs | 5 to 15 | -3 to 3 | 0 to 5 |
| head | 16 to 24 | -2 to 2 | 9 to 14 |
| ears | 18 to 19 | -2 to 2 | 15 to 17 |

## Recognisable features (in order of importance)

1. the long bushy tail with a white tip, as long as half the body
2. big pointed ears with black tips
3. a long narrow snout with a black nose
4. the white bib and white cheeks
5. black stockings on the legs

## Colour map

- `fur`: body, head, tail, upper legs
- `white`: tail tip, chest bib, cheeks and the underside of the snout
- `dark`: lower legs (stockings), ear tips, nose
- `eye`: one voxel on each corner of the face

## Photos used

- `assets/photos/01-side-standing.jpg`: adult standing, left flank, head right (CC BY 4.0)
- `assets/photos/02-three-quarter.jpg`: adult three-quarter front, ears and white chest (CC BY 4.0)
