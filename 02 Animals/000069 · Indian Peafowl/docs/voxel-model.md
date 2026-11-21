# 000069 · Indian Peafowl · voxel brief

*Pavo cristatus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `neck` | `#1447E6` | iridescent cobalt-blue neck, breast and fan-shaped crest |
| `train` | `#009966` | long trailing upper-tail coverts |
| `eye_spot` | `#FFB900` | bronze-gold and turquoise eyespots (ocelli) on the train |
| `face` | `#FAFAF9` | white facial skin patches and pale beak |
| `eye` | `#171717` | dark eyes and legs |

Background (not modelled): `#B0E1CA` (soft mint).

## Size and pose

- Size: 38 × 13 × 42 voxels rest (L × W × H); longest side 42, budget 48–56 (target 56) from the real size 2.1 m (total length 1.8–2.3 m (male including 1.5 m train)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, leg_l, neck, head, leg_r.

## Personality, pose and expression

- Personality: regal and theatrical, proud showstopper of the forest clearing.
- Pose: a stately strut with cobalt chest held high, crown crest erect, long eyespot train sweeping behind.
- Expression: aristocratic dark eyes framed by crisp white cheek patches.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 18 to 30 | -5 to 5 | 11 to 21 |  |
| tail | 0 to 19 | -6 to 6 | 2 to 13 | turned ry +8°; on body |
| leg_l | 22 to 24 | -4 to -2 | 0 to 11 | on body |
| neck | 27 to 31 | -2 to 2 | 20 to 32 | on body |
| head | 27 to 37 | -3 to 3 | 32 to 41 | turned rx +4°, rz -10°; on neck |
| leg_r | 22 to 24 | 2 to 4 | 0 to 11 | on body |

## Recognisable features (in order of importance)

1. the long trailing emerald train with golden-blue eyespots
2. the iridescent royal-blue neck and breast
3. the delicate fan-shaped head crest
4. the white facial patches
5. the sturdy legs with spurs

## Colour map

- `neck`: iridescent cobalt-blue neck, breast and fan-shaped crest
- `train`: long trailing upper-tail coverts
- `eye_spot`: bronze-gold and turquoise eyespots (ocelli) on the train
- `face`: white facial skin patches and pale beak
- `eye`: dark eyes and legs

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
