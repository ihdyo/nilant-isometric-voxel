# 26-015 · European Hedgehog · voxel brief

*Erinaceus europaeus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (Tailwind token or #hex) | Where |
|---|---|---|
| `spines` | `amber-800` | the spiny coat over the back and sides |
| `tips` | `amber-100` | the pale spine tips: single voxels standing out of the dome in staggered rows |
| `face` | `#C8A47E` | the furry face, belly and legs (a soft tan hex: the Tailwind ambers and stones are too yellow or too grey) |
| `nose` | `neutral-900` | the nose tip |
| `eye` | `neutral-950` | the beady eyes |
| `feet` | `stone-500` | the little feet |

Background (not modelled): `emerald-100` (rendered as a calm pastel).

## Size and pose

- Size: 18 × 11 × 11 voxels posed (L × W × H); longest side 18, budget 16–18 (target 16) from the real size 0.25 m (nose to tail: head and body 13.5–26.5 cm plus a 2 cm tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, head.

## Personality, pose and expression

- Personality: shy, snuffly and curious.
- Pose: trundling forward with the nose lifted to sniff the air, the head tilted, one front foot stepping out.
- Expression: beady black eyes and a little black nose on a soft furry face, painted flat; pale one-voxel spines stand out of the dome.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 8 to 9 | -3 to -2 | 0 to 1 | turned ry -14°; on body |
| leg_fr | 8 to 9 | 2 to 3 | 0 to 1 | on body |
| leg_hl | 1 to 2 | -3 to -2 | 0 to 1 | on body |
| leg_hr | 1 to 2 | 2 to 3 | 0 to 1 | on body |
| body | 0 to 13 | -5 to 5 | 2 to 10 |  |
| head | 12 to 17 | -3 to 3 | 2 to 5 | turned rx +8°, ry -12°, rz -10°; on body |

## Recognisable features (in order of importance)

1. the dome of brown spines with pale tips
2. the pointed furry face with a black nose
3. beady black eyes
4. tiny legs hidden under the spines
5. the round, low body

## Colour map

- `spines`: the spiny coat over the back and sides
- `tips`: the pale spine tips: single voxels standing out of the dome in staggered rows
- `face`: the furry face, belly and legs (a soft tan hex: the Tailwind ambers and stones are too yellow or too grey)
- `nose`: the nose tip
- `eye`: the beady eyes
- `feet`: the little feet

## Photos used

- `assets/photos/01-walking.jpg`: adult snuffling through grass, face and spines (CC0)
- `assets/photos/02-curled.jpg`: adult curled into a ball, spines up (CC BY 4.0)
