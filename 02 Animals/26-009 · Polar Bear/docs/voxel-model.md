# 26-009 · Polar Bear · voxel brief

*Ursus maritimus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `fur` | `amber-50` | everything else |
| `dark` | `neutral-900` | nose, eyes, claws at the front of the paws |

Background (not modelled): `blue-300`.

## Size and pose

- Size: 25 × 9 × 15 voxels (L × W × H); longest side 25 (budget 16–32).
- Pose: walking, head held low and forward. Head towards +X, feet on z = 0, left flank at −Y, symmetric about y = 0.
- Parts: legs, body, head, tail.

## Proportions (inclusive voxel ranges of each part, as built)

| Part | x | y | z |
|---|---|---|---|
| tail | 1 to 1 | -1 to 1 | 11 to 12 |
| body | 2 to 17 | -4 to 4 | 7 to 14 |
| legs | 3 to 16 | -4 to 4 | 0 to 6 |
| head | 17 to 25 | -3 to 3 | 9 to 13 |

## Recognisable features (in order of importance)

1. the long neck and long narrow head carried low
2. thick pillar legs with big paws
3. a long heavy body, highest at the hips
4. small round ears
5. the black nose and eyes on cream fur

## Colour map

- `fur`: everything else
- `dark`: nose, eyes, claws at the front of the paws

## Photos used

- `assets/photos/01-on-ice.jpg`: adult on sea ice, side (CC BY 2.0)
- `assets/photos/02-walking.jpg`: adult male walking on pack ice (Public domain)
