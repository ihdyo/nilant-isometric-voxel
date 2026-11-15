# 26-003 · Red Panda · voxel brief

*Ailurus fulgens* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `fur` | `orange-700` | back, flanks, head, tail |
| `white` | `stone-50` | muzzle, cheeks, brows, ear fronts |
| `dark` | `orange-950` | legs, belly, nose, tail tip |
| `ring` | `orange-300` | two pale rings on the tail |
| `eye` | `neutral-950` | one voxel on the face front and one on the flank |

Background (not modelled): `cyan-200`.

## Size and pose

- Size: 27 × 7 × 16 voxels (L × W × H); longest side 27 (budget 16–32).
- Pose: walking on four legs, tail held straight out behind. Head towards +X, feet on z = 0, left flank at −Y, symmetric about y = 0.
- Parts: legs, body, head, ears, tail.

## Proportions (inclusive voxel ranges of each part, as built)

| Part | x | y | z |
|---|---|---|---|
| tail | -7 to 1 | -1 to 1 | 6 to 9 |
| body | 2 to 13 | -3 to 3 | 5 to 10 |
| legs | 3 to 12 | -3 to 3 | 0 to 4 |
| head | 13 to 19 | -3 to 3 | 8 to 13 |
| ears | 14 to 15 | -3 to 3 | 14 to 15 |

## Recognisable features (in order of importance)

1. the long thick ringed tail
2. the white face mask (cheeks, brows, muzzle) around dark eyes
3. white-fronted pointed ears
4. dark legs and belly under rusty red fur

## Colour map

- `fur`: back, flanks, head, tail
- `white`: muzzle, cheeks, brows, ear fronts
- `dark`: legs, belly, nose, tail tip
- `ring`: two pale rings on the tail
- `eye`: one voxel on the face front and one on the flank

## Photos used

- `assets/photos/01-front.jpg`: adult on a branch, face mask, dark legs (CC0)
- `assets/photos/02-side-walking.jpg`: adult walking, full side, ringed tail (Public domain)
