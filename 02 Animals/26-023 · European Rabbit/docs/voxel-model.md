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

- Size: 17 × 11 × 17 voxels posed (L × W × H); longest side 17, budget 17–23 (target 20) from the real size 0.45 m (nose to tail: 38–50 cm).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, head, muzzle, ear_l, ear_r.

## Personality, pose and expression

- Personality: alert, jumpy and sweet.
- Pose: crouched in a round loaf on all four feet, the long hind feet flat on the ground, the big head turned to the camera, the ears standing tall with one bent forward, the cotton tail showing.
- Expression: a big round eye with a glint, a pink nose and a little split lip, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 8 to 9 | -3 to -2 | 0 to 1 | on body |
| leg_fr | 8 to 9 | 2 to 3 | 0 to 1 | on body |
| leg_hl | 1 to 7 | -5 to -4 | 0 to 5 | on body |
| leg_hr | 1 to 7 | 4 to 5 | 0 to 5 | on body |
| body | -1 to 9 | -4 to 4 | 1 to 8 |  |
| head | 9 to 14 | -3 to 3 | 5 to 10 | turned rx +6°, ry -4°, rz -16°; on body |
| muzzle | 15 to 15 | -1 to 1 | 5 to 7 | on head |
| ear_l | 10 to 11 | -3 to -2 | 11 to 16 | turned rx +8°, ry -6°; on head |
| ear_r | 10 to 11 | 2 to 3 | 11 to 16 | turned rx -8°, ry +26°; on head |

## Recognisable features (in order of importance)

1. long upright ears
2. big dark eyes
3. a white cotton tail
4. a round sitting shape with big hind feet
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
