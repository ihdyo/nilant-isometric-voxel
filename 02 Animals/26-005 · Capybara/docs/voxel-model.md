# 26-005 · Capybara · voxel brief

*Hydrochoerus hydrochaeris* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `fur` | `amber-800` | body, legs, head |
| `dark` | `orange-950` | the front of the muzzle and nose, the ears |
| `eye` | `neutral-950` | one voxel high on each side of the head |

Background (not modelled): `indigo-200`.

## Size and pose

- Size: 23 × 9 × 15 voxels (L × W × H); longest side 23 (budget 16–32).
- Pose: standing, head level, relaxed. Head towards +X, feet on z = 0, left flank at −Y, symmetric about y = 0.
- Parts: legs, body, head, ears.

## Proportions (inclusive voxel ranges of each part, as built)

| Part | x | y | z |
|---|---|---|---|
| body | 1 to 16 | -4 to 4 | 4 to 12 |
| legs | 3 to 14 | -3 to 3 | 0 to 3 |
| head | 17 to 23 | -3 to 3 | 6 to 13 |
| ears | 17 to 18 | -3 to 3 | 14 to 14 |

## Recognisable features (in order of importance)

1. a big barrel body on very short legs
2. a large blunt, boxy head with a deep square muzzle
3. small round ears and eyes high on the head
4. no tail

## Colour map

- `fur`: body, legs, head
- `dark`: the front of the muzzle and nose, the ears
- `eye`: one voxel high on each side of the head

## Photos used

- `assets/photos/01-resting.jpg`: adult resting, side, blunt muzzle (CC0)
- `assets/photos/02-grazing-side.jpg`: adult grazing, full side, short legs (CC BY 4.0)
