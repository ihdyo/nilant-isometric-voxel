# 000071 · Shoebill · voxel brief

*Balaeniceps rex* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `plumage` | `#62748E` | blue-grey slate plumage across body, neck and wings |
| `bill` | `#FEE685` | enormous straw-tan clog-shaped hooked bill with dark mottling |
| `leg` | `#171717` | long black wading legs and large splayed toes |
| `iris` | `#FFDF20` | intense pale-gold forward-facing eyes |
| `eye` | `#171717` | the pupils and hooked bill nail |

Background (not modelled): `#B7D8FB` (soft periwinkle).

## Size and pose

- Size: 26 × 11 × 40 voxels rest (L × W × H); longest side 40, budget 48–56 (target 56) from the real size 1.35 m (standing height 1.1–1.4 m; wingspan 2.3–2.6 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, leg_l, head, leg_r.

## Personality, pose and expression

- Personality: stoic and prehistoric, an ancient swamp statue with a secret grin.
- Pose: standing motionless with head tucked slightly into the shoulders, massive clog bill resting downward.
- Expression: intense forward-facing pale-gold eyes and a subtle hooked grin on its huge clog bill.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 4 to 16 | -5 to 5 | 16 to 29 |  |
| tail | 1 to 5 | -3 to 3 | 12 to 18 | turned ry +12°; on body |
| leg_l | 9 to 13 | -5 to -1 | 0 to 16 | on body |
| head | 6 to 26 | -5 to 5 | 26 to 39 | turned rx +3°, ry +8°, rz -10°; on body |
| leg_r | 9 to 13 | 1 to 5 | 0 to 16 | on body |

## Recognisable features (in order of importance)

1. the enormous tan clog-shaped hooked bill
2. the wispy feather tuft at the back of the head
3. the blue-grey slate plumage and broad wings
4. the long black stilt legs and big toes
5. the forward-looking golden eyes

## Colour map

- `plumage`: blue-grey slate plumage across body, neck and wings
- `bill`: enormous straw-tan clog-shaped hooked bill with dark mottling
- `leg`: long black wading legs and large splayed toes
- `iris`: intense pale-gold forward-facing eyes
- `eye`: the pupils and hooked bill nail

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
