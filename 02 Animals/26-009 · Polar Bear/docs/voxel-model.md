# 26-009 · Polar Bear · voxel brief

*Ursus maritimus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `fur` | `amber-50` | everything else |
| `dark` | `neutral-900` | nose, eyes, claws at the front of the paws |
| `shine` | `white` | the light glint in each eye |

Background (not modelled): `blue-300`.

## Size and pose

- Size: 41 × 17 × 25 voxels posed (L × W × H); longest side 41, budget 32–44 (target 38) from the real size 2.2 m (nose to tail: 1.8–2.5 m, mid-range).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: shin_fl, shin_fr, shin_hl, shin_hr, leg_fl, leg_fr, leg_hl, leg_hr, body, head, snout, torso, ear_l, ear_r.

## Personality, pose and expression

- Personality: a curious, patient wanderer of the ice.
- Pose: a long walking stride in two body sections, the heavy hindquarters (the lower body, the highest point) and the shoulders (the upper body) turning at the waist towards the camera, no neck: the long head carried low on the front of the shoulders, the nose lifted to sniff.
- Expression: round white eyes with the dark pupils to the inside, a big black nose and a small open mouth, all painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| shin_fl | 20 to 24 | -6 to -2 | 0 to 4 | turned ry +22°; on leg_fl |
| shin_fr | 20 to 24 | 2 to 6 | 0 to 4 | on leg_fr |
| shin_hl | 2 to 6 | -7 to -3 | 0 to 4 | turned ry -14°; on leg_hl |
| shin_hr | 2 to 6 | 3 to 7 | 0 to 4 | on leg_hr |
| leg_fl | 20 to 24 | -6 to -2 | 5 to 8 | turned ry -16°; on torso |
| leg_fr | 20 to 24 | 2 to 6 | 5 to 8 | turned ry +12°; on torso |
| leg_hl | 2 to 6 | -7 to -3 | 5 to 8 | turned ry +14°; on body |
| leg_hr | 2 to 6 | 3 to 7 | 5 to 8 | turned ry -10°; on body |
| body | -1 to 14 | -7 to 7 | 9 to 23 |  |
| head | 28 to 34 | -5 to 5 | 9 to 17 | turned rx +5°, ry -8°, rz -12°; on torso |
| snout | 35 to 38 | -3 to 3 | 9 to 13 | on head |
| torso | 15 to 27 | -6 to 6 | 9 to 21 | turned ry +3°, rz -7°; on body |
| ear_l | 29 to 30 | -5 to -4 | 18 to 19 | turned rx +12°; on head |
| ear_r | 29 to 30 | 4 to 5 | 18 to 19 | turned rx -12°; on head |

## Recognisable features (in order of importance)

1. the long narrow head carried low on the front of the shoulders (no neck section; owner, 2026-11-17)
2. thick pillar legs with big paws
3. a long heavy body, highest at the hips
4. small round ears
5. the black nose and eyes on cream fur

## Colour map

- `fur`: everything else
- `dark`: nose, eyes, claws at the front of the paws
- `shine`: the light glint in each eye

## Photos used

- `assets/photos/01-on-ice.jpg`: adult on sea ice, side (CC BY 2.0)
- `assets/photos/02-walking.jpg`: adult male walking on pack ice (Public domain)
