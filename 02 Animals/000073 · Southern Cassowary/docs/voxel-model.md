# 000073 · Southern Cassowary · voxel brief

*Casuarius casuarius* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `plumage` | `#171717` | glossy hair-like black drooping body plumage |
| `neck` | `#155DFC` | vivid cobalt-blue and turquoise bare neck skin |
| `wattle` | `#E7000B` | two bright crimson dangling throat wattles |
| `casque` | `#44403B` | tall keratin-sheathed horn helmet (casque) |
| `leg` | `#A6A09B` | thick dinosaur-like grey legs with 12-cm inner dagger claws |

Background (not modelled): `#D5CEF9` (soft lilac).

## Size and pose

- Size: 29 × 15 × 51 voxels rest (L × W × H); longest side 51, budget 48–56 (target 56) from the real size 1.65 m (standing height 1.5–1.8 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_l, neck, wattle_l, head, leg_r, wattle_r.

## Personality, pose and expression

- Personality: bold and prehistoric, living dinosaur of the tropical rainforest.
- Pose: a powerful forest stride, helmet casque held high, twin crimson wattles swinging.
- Expression: fierce dark eyes above a vivid cobalt-blue neck and straight dark beak.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 2 to 22 | -7 to 7 | 14 to 30 |  |
| leg_l | 10 to 16 | -5 to -2 | 0 to 16 | turned ry -10°; on body |
| neck | 19 to 24 | -3 to 3 | 28 to 39 | on body |
| wattle_l | 23 to 25 | -2 to -1 | 26 to 31 | turned rz +8°; on neck |
| head | 19 to 30 | -3 to 3 | 39 to 50 | turned rx +4°, ry +4°, rz -10°; on neck |
| leg_r | 10 to 16 | 2 to 5 | 0 to 16 | on body |
| wattle_r | 23 to 25 | 1 to 2 | 26 to 31 | turned rz -8°; on neck |

## Recognisable features (in order of importance)

1. the tall dark keratin helmet (casque) on the head
2. the vivid cobalt-blue bare neck and twin crimson wattles
3. the shaggy drooping black hair-like body plumage
4. the thick dinosaur-like legs with long inner claws
5. the hidden wing quills

## Colour map

- `plumage`: glossy hair-like black drooping body plumage
- `neck`: vivid cobalt-blue and turquoise bare neck skin
- `wattle`: two bright crimson dangling throat wattles
- `casque`: tall keratin-sheathed horn helmet (casque)
- `leg`: thick dinosaur-like grey legs with 12-cm inner dagger claws

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
