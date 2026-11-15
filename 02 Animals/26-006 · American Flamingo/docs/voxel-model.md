# 26-006 · American Flamingo · voxel brief

*Phoenicopterus ruber* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `pink` | `rose-400` | body |
| `light` | `rose-200` | neck and head |
| `black` | `neutral-900` | rear edge of the wings, bill tip |
| `bill` | `rose-100` | pale bill base |
| `legs` | `rose-500` | legs and feet |
| `eye` | `amber-300` | one voxel on each side of the head |

Background (not modelled): `emerald-200`.

## Size and pose

- Size: 17 × 7 × 31 voxels (L × W × H); longest side 31 (budget 16–32).
- Pose: standing on both legs, S-shaped neck, head level. Head towards +X, feet on z = 0, left flank at −Y, symmetric about y = 0.
- Parts: legs, body, neck, head, beak.

## Proportions (inclusive voxel ranges of each part, as built)

| Part | x | y | z |
|---|---|---|---|
| body | 0 to 10 | -3 to 3 | 13 to 18 |
| legs | 5 to 7 | -1 to 1 | 0 to 12 |
| neck | 8 to 10 | 0 to 0 | 19 to 27 |
| head | 10 to 13 | -1 to 1 | 27 to 30 |
| beak | 14 to 16 | 0 to 0 | 27 to 30 |

## Recognisable features (in order of importance)

1. the long S-shaped neck
2. long thin pink legs with the backward-bending ankle
3. the bent bill with a black tip
4. the egg-shaped pink body
5. black flight feathers along the rear edge

## Colour map

- `pink`: body
- `light`: neck and head
- `black`: rear edge of the wings, bill tip
- `bill`: pale bill base
- `legs`: legs and feet
- `eye`: one voxel on each side of the head

## Photos used

- `assets/photos/01-head.jpg`: adult head and neck, bent bill (CC0)
- `assets/photos/02-standing.jpg`: adult standing, full body, long legs (CC0)
