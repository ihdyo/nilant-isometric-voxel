# 26-010 · Giraffe · voxel brief

*Giraffa camelopardalis* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `patch` | `amber-700` | patches on the body, neck, upper legs and head |
| `base` | `amber-100` | the cream network between patches, lower legs, head |
| `mane` | `amber-800` | the mane along the back of the neck |
| `dark` | `stone-800` | hooves, ossicone tufts, tail tuft |
| `eye` | `neutral-950` | one voxel on each side of the head |

Background (not modelled): `sky-300`.

## Size and pose

- Size: 19 × 5 × 32 voxels (L × W × H); longest side 32 (budget 16–32).
- Pose: standing, the long neck rising almost straight up, head forward. Head towards +X, feet on z = 0, left flank at −Y, symmetric about y = 0.
- Parts: legs, body, neck, head, tail.

## Proportions (inclusive voxel ranges of each part, as built)

| Part | x | y | z |
|---|---|---|---|
| tail | 1 to 1 | 0 to 0 | 9 to 14 |
| body | 2 to 13 | -2 to 2 | 11 to 16 |
| legs | 3 to 12 | -2 to 2 | 0 to 10 |
| neck | 11 to 15 | -1 to 1 | 17 to 27 |
| head | 14 to 19 | -2 to 2 | 27 to 31 |

## Recognisable features (in order of importance)

1. the very long neck
2. long legs, the body high at the shoulders
3. square brown patches separated by cream lines
4. the ossicones with dark tufts on top of the head
5. the short dark mane along the back of the neck

## Colour map

- `patch`: patches on the body, neck, upper legs and head
- `base`: the cream network between patches, lower legs, head
- `mane`: the mane along the back of the neck
- `dark`: hooves, ossicone tufts, tail tuft
- `eye`: one voxel on each side of the head

## Photos used

- `assets/photos/01-standing.jpg`: adult standing, full body, patches (CC BY 2.0)
- `assets/photos/02-head.jpg`: head, ossicones, neck pattern (CC0)
