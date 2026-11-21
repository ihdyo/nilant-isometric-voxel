# 000059 · Brown-throated Sloth · voxel brief

*Bradypus variegatus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#79716B` | shaggy grey-brown fur often tinted green with algae |
| `face` | `#FEF3C6` | pale cream facial mask |
| `stripe` | `#292524` | dark eye mask stripes and throat |
| `claw` | `#E7E5E4` | three long curved hook-like claws on each limb |
| `eye` | `#171717` | dark button eyes and nose |

Background (not modelled): `#B5E1C4` (soft leaf green).

## Size and pose

- Size: 22 × 15 × 26 voxels rest (L × W × H); longest side 26, budget 48–56 (target 56) from the real size 0.65 m (head-and-body length, 42–80 cm).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, arm_l, leg_hl, head, arm_r.

## Personality, pose and expression

- Personality: blissfully unhurried, smiling zen master of the treetops.
- Pose: a cozy seated hug pose with long arms reaching forward and hooked claws curved inward.
- Expression: a permanent gentle smile and dark bandit-mask eye stripes on a pale cream face.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 2 to 14 | -6 to 6 | 3 to 18 |  |
| tail | 0 to 2 | -2 to 2 | 4 to 7 |  |
| arm_l | 8 to 21 | -7 to -5 | 11 to 17 | turned ry -12°, rz +16°; on body |
| leg_hl | 7 to 19 | -7 to -4 | 1 to 6 | turned rz +12°; on body |
| head | 5 to 15 | -5 to 5 | 18 to 26 | turned rx +6°, ry +4°, rz -12°; on body |
| arm_r | 8 to 21 | 5 to 7 | 11 to 17 | turned ry -12°, rz -16°; on body |

## Recognisable features (in order of importance)

1. the pale cream face with dark eye stripes and permanent smile
2. the three long curved claws on every limb
3. the long arms and shaggy grey-brown coat
4. the rounded head with no visible external ears
5. the tiny stub tail

## Colour map

- `coat`: shaggy grey-brown fur often tinted green with algae
- `face`: pale cream facial mask
- `stripe`: dark eye mask stripes and throat
- `claw`: three long curved hook-like claws on each limb
- `eye`: dark button eyes and nose

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
