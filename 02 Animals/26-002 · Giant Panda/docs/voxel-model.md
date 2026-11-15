# 26-002 · Giant Panda · voxel brief

*Ailuropoda melanoleuca* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `white` | `stone-50` | body, head, muzzle, tail |
| `black` | `neutral-900` | legs, shoulder band, ears, eye patches, nose |
| `eye` | `stone-400` | one light voxel inside each eye patch so the eye reads |

Background (not modelled): `lime-200`.

## Size and pose

- Size: 22 × 9 × 19 voxels (L × W × H); longest side 22 (budget 16–32).
- Pose: standing on four legs, head level. Head towards +X, feet on z = 0, left flank at −Y, symmetric about y = 0.
- Parts: legs, body, head, ears, tail.

## Proportions (inclusive voxel ranges of each part, as built)

| Part | x | y | z |
|---|---|---|---|
| tail | 1 to 1 | -1 to 1 | 9 to 10 |
| body | 2 to 14 | -4 to 4 | 6 to 13 |
| legs | 3 to 13 | -4 to 4 | 0 to 5 |
| head | 14 to 22 | -4 to 4 | 9 to 17 |
| ears | 15 to 16 | -4 to 4 | 17 to 18 |

## Recognisable features (in order of importance)

1. black eye patches on a big round white head
2. round black ears
3. black legs and the black band over the shoulders
4. a stocky, rounded barrel of a body
5. a short muzzle with a black nose

## Colour map

- `white`: body, head, muzzle, tail
- `black`: legs, shoulder band, ears, eye patches, nose
- `eye`: one light voxel inside each eye patch so the eye reads

## Photos used

- `assets/photos/01-sitting.jpg`: adult sitting, eye patches, shoulder band (Public domain)
- `assets/photos/02-young-side.jpg`: young panda, side, black legs (CC BY 2.0)
