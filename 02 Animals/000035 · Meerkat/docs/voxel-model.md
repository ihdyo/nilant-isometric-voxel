# 000035 · Meerkat · voxel brief

*Suricata suricatta* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#FEE685` | slender upright torso, head, limbs and tail |
| `stripe` | `#57534D` | dark horizontal bands across the lower back and tail tip |
| `mask` | `#171717` | dark eye patches, small rounded ears and nose |
| `belly` | `#FFFBEB` | lightly furred pale chest and belly |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#171717` | dark alert sentry eyes |

Background (not modelled): `#ECCFA9` (soft sand).

## Size and pose

- Size: 16 × 11 × 26 voxels posed (L × W × H); longest side 26, budget 24–30 (target 26) from the real size 0.5 m (nose to tail tip, about 0.5 m (body 25–35 cm plus 17–25 cm slender tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_hl, leg_hr, tail, body, arm_l, arm_r, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: vigilant and loyal, ever on lookout for the clan.
- Pose: classic upright sentry stance balanced on hind feet and slender tail tripod, short arms tucked against the belly and head scanning the sky.
- Expression: wide alert eyes ringed by dark sun-glare patches, pointed snout and tiny dark crescent ears.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_hl | 1 to 4 | -3 to -1 | 0 to 3 | on body |
| leg_hr | 1 to 4 | 1 to 3 | 0 to 3 | on body |
| tail | -7 to 0 | -1 to 1 | 0 to 2 | turned ry +8°; on body |
| body | 0 to 6 | -3 to 3 | 3 to 18 |  |
| arm_l | 5 to 7 | -4 to -3 | 11 to 16 | turned rx +10°; on body |
| arm_r | 5 to 7 | 3 to 4 | 11 to 16 | turned rx -10°; on body |
| head | 0 to 7 | -3 to 3 | 18 to 25 | turned rx +4°, ry -6°, rz -12°; on body |
| ear_l | 2 to 3 | -4 to -3 | 21 to 23 | on head |
| ear_r | 2 to 3 | 3 to 4 | 21 to 23 | on head |

## Recognisable features (in order of importance)

1. classic upright bipedal sentry posture using tail as a third leg
2. dark eye patches around bright alert eyes
3. pointed snout and small dark crescent ears set low on the sides
4. dark transverse stripes across the lower back
5. slender black-tipped tail

## Colour map

- `coat`: slender upright torso, head, limbs and tail
- `stripe`: dark horizontal bands across the lower back and tail tip
- `mask`: dark eye patches, small rounded ears and nose
- `belly`: lightly furred pale chest and belly
- `white`: the white of each eye
- `eye`: dark alert sentry eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult meerkat profile reference (CC BY-SA 3.0)
