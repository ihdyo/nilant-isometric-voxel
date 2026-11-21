# 000058 · Short-beaked Echidna · voxel brief

*Tachyglossus aculeatus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#292524` | coarse dark-brown fur beneath the spines |
| `spine` | `#FEF3C6` | long cream-yellow keratin spines with dark tips |
| `snout` | `#44403B` | slender tubular snout and stout digging claws |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#171717` | the pupils and nostrils |

Background (not modelled): `#DCD6A9` (soft straw).

## Size and pose

- Size: 30 × 14 × 17 voxels rest (L × W × H); longest side 30, budget 48–56 (target 56) from the real size 0.45 m (total length, 35–53 cm).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, leg_fl, head.

## Personality, pose and expression

- Personality: shy and tenacious, a walking pincushion with a curious nose.
- Pose: a low waddle, slender snout angled down toward an anthill, spines bristling neatly.
- Expression: tiny bright eyes tucked at the base of a long tubular snout.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 2 to 19 | -7 to 6 | 3 to 16 |  |
| leg_hl | 4 to 7 | -6 to -3 | 0 to 3 | on body |
| leg_fl | 14 to 17 | -6 to -3 | 0 to 3 | turned ry -8°; on body |
| head | 19 to 31 | -4 to 4 | 4 to 10 | turned rx +3°, ry +8°, rz -8°; on body |

## Recognisable features (in order of importance)

1. the dome of long cream-and-black spines
2. the long slender tubular snout
3. the stout clawed feet
4. the low rounded body
5. the spiky tail tuft

## Colour map

- `coat`: coarse dark-brown fur beneath the spines
- `spine`: long cream-yellow keratin spines with dark tips
- `snout`: slender tubular snout and stout digging claws
- `white`: the white of each eye
- `eye`: the pupils and nostrils

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
