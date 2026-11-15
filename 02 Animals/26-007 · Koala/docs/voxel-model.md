# 26-007 · Koala · voxel brief

*Phascolarctos cinereus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `fur` | `stone-400` | body, head, arms, legs |
| `white` | `stone-100` | chest and the ear fringes |
| `nose` | `stone-800` | the nose |
| `eye` | `neutral-950` | one voxel on the face front and one on the flank |

Background (not modelled): `amber-200`.

## Size and pose

- Size: 10 × 15 × 22 voxels (L × W × H); longest side 22 (budget 16–32).
- Pose: sitting upright, front paws resting on the knees. Head towards +X, feet on z = 0, left flank at −Y, symmetric about y = 0.
- Parts: body, legs, head, ears.

## Proportions (inclusive voxel ranges of each part, as built)

| Part | x | y | z |
|---|---|---|---|
| body | 1 to 8 | -4 to 4 | 0 to 11 |
| head | 1 to 10 | -5 to 5 | 12 to 20 |
| ears | 3 to 6 | -7 to 7 | 17 to 21 |
| legs | 8 to 10 | -4 to 4 | 0 to 9 |

## Recognisable features (in order of importance)

1. the big dark nose
2. large round ears with white fluffy fringes
3. a big round head on a compact body
4. the white chest
5. the sitting teddy-bear pose

## Colour map

- `fur`: body, head, arms, legs
- `white`: chest and the ear fringes
- `nose`: the nose
- `eye`: one voxel on the face front and one on the flank

## Photos used

- `assets/photos/01-in-tree.jpg`: adult in a tree, nose and ear tufts (CC0)
- `assets/photos/02-walking.jpg`: adult on a branch, body and limbs (CC BY 3.0)
