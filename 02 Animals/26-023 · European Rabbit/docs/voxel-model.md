# 26-023 · European Rabbit · voxel brief

*Oryctolagus cuniculus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (Tailwind token or #hex) | Where |
|---|---|---|
| `fur` | `stone-400` | body, head, ears and legs |
| `belly` | `stone-200` | the belly, the chest and the muzzle |
| `tail` | `stone-50` | the white cotton tail and the eye glint |
| `ear` | `rose-200` | the inside of the ears |
| `nose` | `rose-300` | the nose |
| `eye` | `neutral-950` | the eyes and the mouth |

Background (not modelled): `lime-200` (rendered as a calm pastel).

## Size and pose

- Size: 18 × 11 × 21 voxels posed (L × W × H); longest side 21, budget 17–23 (target 20) from the real size 0.45 m (nose to tail: 38–50 cm).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, shin_hl, shin_hr, leg_hl, leg_hr, body, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: alert, jumpy and sweet.
- Pose: standing on all four feet, the back rising from the low rump to the chest held up on long, thin front legs, slanted thighs on the flanks over long hind feet flat on the ground (one voxel high), the head on the front of the chest turned to the camera, the two tall ears side by side, one bent forward, the cotton tail showing.
- Expression: big dark eyes with a glint on the front corners of the face, a pink nose over a pale muzzle and a little split lip, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 9 to 10 | -3 to -2 | 0 to 5 | on body |
| leg_fr | 9 to 10 | 2 to 3 | 0 to 5 | on body |
| shin_hl | 0 to 7 | -5 to -4 | 0 to 0 | turned ry +14°; on leg_hl |
| shin_hr | 0 to 7 | 4 to 5 | 0 to 0 | turned ry +14°; on leg_hr |
| leg_hl | 0 to 4 | -5 to -4 | 1 to 7 | turned ry -14°; on body |
| leg_hr | 0 to 4 | 4 to 5 | 1 to 7 | turned ry -14°; on body |
| body | -1 to 10 | -3 to 3 | 4 to 10 |  |
| head | 11 to 15 | -3 to 3 | 8 to 13 | turned rx +4°, ry -4°, rz -14°; on body |
| ear_l | 12 to 13 | -2 to -1 | 14 to 20 | turned rx +6°, ry -6°; on head |
| ear_r | 12 to 13 | 1 to 2 | 14 to 20 | turned rx -6°, ry +20°; on head |

## Recognisable features (in order of importance)

1. long upright ears
2. big dark eyes
3. a white cotton tail
4. a high rump sloping to the chest, slanted thighs over long flat hind feet, thin front legs (standing on all four feet)
5. a grey-brown coat

## Colour map

- `fur`: body, head, ears and legs
- `belly`: the belly, the chest and the muzzle
- `tail`: the white cotton tail and the eye glint
- `ear`: the inside of the ears
- `nose`: the nose
- `eye`: the eyes and the mouth

## Photos used

- `assets/photos/01-close-up.jpg`: a wild rabbit close up in grass, ear, eye and coat (CC BY 2.0)
- `assets/photos/02-portugal.jpg`: a wild rabbit under bushes in Portugal, its native range (CC BY 4.0)
