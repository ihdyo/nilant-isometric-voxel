# 26-004 · Emperor Penguin · voxel brief

*Aptenodytes forsteri* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `black` | `slate-900` | back, flanks, head, flippers, feet, bill |
| `white` | `slate-50` | belly and front |
| `yellow` | `amber-400` | ear patch on the side of the head and neck |
| `cream` | `amber-100` | upper breast |
| `bill` | `orange-400` | stripe on the lower half of the bill |

Background (not modelled): `sky-200`.

## Size and pose

- Size: 12 × 11 × 26 voxels (L × W × H); longest side 26 (budget 16–32).
- Pose: standing upright, flippers down, bill forward. Head towards +X, feet on z = 0, left flank at −Y, symmetric about y = 0.
- Parts: legs, body, head, beak, wings, tail.

## Proportions (inclusive voxel ranges of each part, as built)

| Part | x | y | z |
|---|---|---|---|
| tail | -1 to -1 | -1 to 1 | 1 to 2 |
| body | 0 to 7 | -4 to 4 | 1 to 17 |
| head | 1 to 7 | -3 to 3 | 18 to 25 |
| wings | 2 to 4 | -5 to 5 | 7 to 15 |
| legs | 4 to 7 | -3 to 3 | 0 to 0 |
| beak | 8 to 10 | 0 to 0 | 22 to 23 |

## Recognisable features (in order of importance)

1. upright black body with a white front
2. the yellow ear patch on the side of the head
3. the pale yellow upper breast
4. a long thin bill with an orange stripe below
5. flippers hanging along the flanks

## Colour map

- `black`: back, flanks, head, flippers, feet, bill
- `white`: belly and front
- `yellow`: ear patch on the side of the head and neck
- `cream`: upper breast
- `bill`: stripe on the lower half of the bill

## Photos used

- `assets/photos/01-pair.jpg`: adults, yellow ear patches, chick (Public domain)
- `assets/photos/02-side.jpg`: adults standing, side profiles (Public domain)
