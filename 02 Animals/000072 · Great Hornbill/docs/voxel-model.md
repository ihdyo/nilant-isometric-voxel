# 000072 · Great Hornbill · voxel brief

*Buceros bicornis* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `plumage` | `#171717` | glossy black body, wings and face mask |
| `neck` | `#FEE685` | creamy golden-yellow neck, wing bars and banded tail |
| `casque` | `#FFB900` | huge curved yellow-and-orange bill and hollow U-shaped casque |
| `trim` | `#171717` | black front edge on the casque and black tail band |
| `eye` | `#FB2C36` | ruby-red eyes in males (white in females) |

Background (not modelled): `#DCD6A9` (soft straw).

## Size and pose

- Size: 31 × 11 × 33 voxels rest (L × W × H); longest side 33, budget 48–56 (target 56) from the real size 1.15 m (body length 95–130 cm; wingspan 1.5–1.8 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, leg_l, head, leg_r.

## Personality, pose and expression

- Personality: majestic and resonant, trumpet-voiced guardian of the rainforest canopy.
- Pose: perched on a high bough, huge yellow casque bill held proudly, banded tail hanging down.
- Expression: striking ruby-red eye set in a black facial mask behind an enormous golden bill.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 7 to 18 | -5 to 5 | 11 to 23 |  |
| tail | 0 to 8 | -3 to 3 | 2 to 12 | turned ry +12°; on body |
| leg_l | 11 to 13 | -4 to -2 | 0 to 11 | on body |
| head | 11 to 30 | -4 to 4 | 23 to 32 | turned rx +4°, ry +4°, rz -10°; on body |
| leg_r | 11 to 13 | 2 to 4 | 0 to 11 | on body |

## Recognisable features (in order of importance)

1. the huge curved yellow bill with its U-shaped casque
2. the golden-yellow neck and wing bars
3. the glossy black body and wings
4. the long white tail with a bold black band
5. the sturdy grey-black feet

## Colour map

- `plumage`: glossy black body, wings and face mask
- `neck`: creamy golden-yellow neck, wing bars and banded tail
- `casque`: huge curved yellow-and-orange bill and hollow U-shaped casque
- `trim`: black front edge on the casque and black tail band
- `eye`: ruby-red eyes in males (white in females)

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
