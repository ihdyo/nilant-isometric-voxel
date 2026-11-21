# 000074 · North Island Brown Kiwi · voxel brief

*Apteryx mantelli* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `plumage` | `#7B3306` | streaked chestnut-brown hair-like plumage |
| `shade` | `#44403B` | darker back and rump feather tips |
| `beak` | `#FEF3C6` | long slender ivory-cream probing bill |
| `leg` | `#79716B` | short stout grey-brown legs and four-toed feet |
| `eye` | `#171717` | small dark button eyes and whisker bristles |

Background (not modelled): `#CCDCB1` (soft lime green).

## Size and pose

- Size: 32 × 13 × 19 voxels rest (L × W × H); longest side 32, budget 48–56 (target 56) from the real size 0.4 m (body length 35–45 cm).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_l, head, leg_r.

## Personality, pose and expression

- Personality: curious and endearing, whisker-twitching midnight forager.
- Pose: a low bustling waddle, pear-shaped body pitched forward, long ivory beak probing downward.
- Expression: tiny bright black button eyes and cat-like bristles at the base of a long ivory bill.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 16 | -6 to 6 | 4 to 18 |  |
| leg_l | 7 to 12 | -5 to -2 | 0 to 4 | turned ry -8°; on body |
| head | 14 to 31 | -4 to 4 | 11 to 18 | turned rx +4°, ry +16°, rz -8°; on body |
| leg_r | 7 to 12 | 2 to 5 | 0 to 4 | on body |

## Recognisable features (in order of importance)

1. the pear-shaped tailless body covered in streaked brown plumage
2. the extremely long slender ivory-cream bill
3. the short stout grey-brown legs
4. the tiny dark eyes and sensory whiskers
5. the hidden vestigial wings

## Colour map

- `plumage`: streaked chestnut-brown hair-like plumage
- `shade`: darker back and rump feather tips
- `beak`: long slender ivory-cream probing bill
- `leg`: short stout grey-brown legs and four-toed feet
- `eye`: small dark button eyes and whisker bristles

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
