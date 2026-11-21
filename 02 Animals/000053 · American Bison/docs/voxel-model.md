# 000053 · American Bison · voxel brief

*Bison bison* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `shag` | `#1C1917` | massive woolly head, beard, shoulders and front legs |
| `coat` | `#973C00` | shorter golden-brown coat on back and hindquarters |
| `horn` | `#A6A09B` | short curved black-tipped horns |
| `hoof` | `#171717` | cloven hooves and nose |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#171717` | the pupils |

Background (not modelled): `#E0D5A8` (soft straw).

## Size and pose

- Size: 38 × 17 × 30 voxels rest (L × W × H); longest side 38, budget 48–56 (target 56) from the real size 3.2 m (head-and-body length, 2.1–3.8 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, shin_hl, leg_fl, shin_fl, tail, head, horn_l, horn_r.

## Personality, pose and expression

- Personality: mighty and grounded, thunder of the open prairie.
- Pose: a heavy forward stance, massive shaggy head lowered slightly, tail flicking.
- Expression: determined dark eyes peeking beneath a thick woolly brow.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 2 to 28 | -8 to 8 | 10 to 29 |  |
| leg_hl | 3 to 6 | -7 to -4 | 5 to 10 | turned ry +8°; on body |
| shin_hl | 3 to 5 | -6 to -4 | 0 to 4 | on leg_hl |
| leg_fl | 21 to 24 | -7 to -4 | 5 to 10 | turned ry -8°; on body |
| shin_fl | 21 to 23 | -6 to -4 | 0 to 4 | on leg_fl |
| tail | 0 to 1 | -1 to 1 | 12 to 21 | turned rx -14°; on body |
| head | 27 to 37 | -6 to 6 | 7 to 24 | turned rx +4°, ry +6°, rz -8°; on body |
| horn_l | 30 to 32 | -8 to -6 | 20 to 26 | turned rz +10°; on head |
| horn_r | 30 to 32 | 6 to 8 | 20 to 26 | turned rz -10°; on head |

## Recognisable features (in order of importance)

1. the towering shaggy shoulder hump and woolly cape
2. the huge bearded head with short curved horns
3. the contrasting shorter tan hindquarters
4. four sturdy legs with cloven hooves
5. the tufted tail

## Colour map

- `shag`: massive woolly head, beard, shoulders and front legs
- `coat`: shorter golden-brown coat on back and hindquarters
- `horn`: short curved black-tipped horns
- `hoof`: cloven hooves and nose
- `white`: the white of each eye
- `eye`: the pupils

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
