# 26-008 · Lion · voxel brief

*Panthera leo* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `coat` | `orange-300` | body, legs, face, ears, tail |
| `mane` | `amber-800` | the mane and the tail tuft |
| `muzzle` | `orange-100` | the muzzle |
| `nose` | `stone-700` | the nose |
| `eye` | `neutral-950` | one voxel on the face front and one on the flank |

Background (not modelled): `violet-200`.

## Size and pose

- Size: 32 × 11 × 20 voxels (L × W × H); longest side 32 (budget 16–32).
- Pose: standing, head level, tail curving down to the tuft. Head towards +X, feet on z = 0, left flank at −Y, symmetric about y = 0.
- Parts: legs, body, mane, head, tail.

## Proportions (inclusive voxel ranges of each part, as built)

| Part | x | y | z |
|---|---|---|---|
| tail | -4 to 2 | -1 to 1 | 7 to 12 |
| body | 3 to 17 | -3 to 3 | 7 to 13 |
| legs | 4 to 16 | -3 to 3 | 0 to 6 |
| mane | 16 to 23 | -5 to 5 | 8 to 18 |
| head | 22 to 27 | -3 to 3 | 10 to 19 |

## Recognisable features (in order of importance)

1. the big rounded mane around head and neck (adult male)
2. the face sticking forward out of the mane, with a pale muzzle
3. the long tail ending in a dark tuft
4. a long, strong tawny body on long legs

## Colour map

- `coat`: body, legs, face, ears, tail
- `mane`: the mane and the tail tuft
- `muzzle`: the muzzle
- `nose`: the nose
- `eye`: one voxel on the face front and one on the flank

## Photos used

- `assets/photos/01-male-rock.jpg`: adult male lying, mane (CC BY 2.0)
- `assets/photos/02-male-standing.jpg`: adult male standing, side, tail tuft (CC BY 2.0)
