# 000012 · Bengal Tiger · voxel brief

*Panthera tigris tigris* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `fur` | `#FF6900` | body, head, legs, tail |
| `stripe` | `#171717` | the stripes, the tail rings, the brows and the mouth |
| `white` | `#FAFAF9` | the muzzle, cheeks, belly, the spots above the eyes and on the ears |
| `nose` | `#FFA1AD` | the pink nose |
| `eye` | `#FFB900` | the amber eyes |
| `pupil` | `#0A0A0A` | the pupils |

Background (not modelled): `#BAE0BE` (jungle green).

## Size and pose

- Size: 43 × 16 × 25 voxels posed (L × W × H); longest side 43, budget 37–49 (target 43) from the real size 3.0 m (nose to tail tip: males up to 3 m, females up to 2.7 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, shin_hl, leg_fl, shin_fl, head, muzzle, ear_l, tail, tail_tip, leg_hr, shin_hr, leg_fr, shin_fr, ear_r.

## Personality, pose and expression

- Personality: confident and playful, a proud hunter.
- Pose: A prowling stride, the front left paw reaching with its knee folding, the head low and turned to the camera, the striped tail raised in a curve.
- Expression: amber eyes under black brows slanting down to the middle, a cheeky grin, all painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 21 | -5 to 5 | 10 to 18 |  |
| leg_hl | 1 to 4 | -5 to -2 | 5 to 9 | turned ry +14°; on body |
| shin_hl | 1 to 4 | -5 to -2 | 0 to 4 | turned ry -14°; on leg_hl |
| leg_fl | 17 to 20 | -5 to -2 | 5 to 9 | turned ry -20°; on body |
| shin_fl | 17 to 20 | -5 to -2 | 0 to 4 | turned ry +30°; on leg_fl |
| head | 21 to 29 | -6 to 6 | 12 to 22 | turned rx +3°, ry +8°, rz -14°; on body |
| muzzle | 30 to 32 | -3 to 3 | 11 to 16 | on head |
| ear_l | 24 to 25 | -6 to -4 | 23 to 24 | turned rx +10°, ry +6°; on head |
| tail | -6 to -1 | -1 to 1 | 15 to 16 | turned ry +26°, rz +10°; on body |
| tail_tip | -11 to -7 | -1 to 1 | 15 to 16 | turned ry +30°; on tail |
| leg_hr | 1 to 4 | 2 to 5 | 5 to 9 | turned ry -12°; on body |
| shin_hr | 1 to 4 | 2 to 5 | 0 to 4 | on leg_hr |
| leg_fr | 17 to 20 | 2 to 5 | 5 to 9 | turned ry +12°; on body |
| shin_fr | 17 to 20 | 2 to 5 | 0 to 4 | on leg_fr |
| ear_r | 24 to 25 | 4 to 6 | 23 to 24 | turned rx -10°, ry +6°; on head |

## Recognisable features (in order of importance)

1. the orange coat with black stripes
2. the white muzzle, cheeks and the spots above the eyes
3. the long striped tail with a black tip
4. big paws and a strong, low body
5. the pink nose

## Colour map

- `fur`: body, head, legs, tail
- `stripe`: the stripes, the tail rings, the brows and the mouth
- `white`: the muzzle, cheeks, belly, the spots above the eyes and on the ears
- `nose`: the pink nose
- `eye`: the amber eyes
- `pupil`: the pupils

## Photos used

- `assets/photos/01-bandhavgarh.jpg`: adult walking towards the camera, face and stripes (CC BY 4.0)
- `assets/photos/02-kanha.jpg`: adult standing, left flank, full length with tail (CC BY 4.0)
