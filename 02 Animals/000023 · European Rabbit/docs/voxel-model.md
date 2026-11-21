# 000023 · European Rabbit · voxel brief

*Oryctolagus cuniculus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `fur` | `#A6A09B` | body, head, ears and legs |
| `belly` | `#E7E5E4` | the belly, the chest and the muzzle |
| `tail` | `#FAFAF9` | the white cotton tail and the eye glint |
| `ear` | `#FFCCD3` | the inside of the ears |
| `nose` | `#FFA1AD` | the nose |
| `eye` | `#0A0A0A` | the eyes and the mouth |

Background (not modelled): `#D0DAAE` (spring-meadow green).

## Size and pose

- Size: 17 × 9 × 19 voxels posed (L × W × H); longest side 19, budget 17–23 (target 20) from the real size 0.45 m (nose to tail: 38–50 cm).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, shin_hl, leg_fl, head, ear_l, leg_hr, shin_hr, leg_fr, ear_r.

## Personality, pose and expression

- Personality: alert, jumpy and sweet.
- Pose: Crouched on all four feet, ready to hop: one block of a body, a small slab thigh on each flank set into the body (one voxel showing on its side, the hinge inside), the long hind foot flat under it, thin front legs starting beside the chest, the head turned to the camera, the two tall ears side by side, one tipped back, the cotton tail showing.
- Expression: big dark eyes with a glint on the front corners of the face, a pink nose over a pale muzzle and a little split lip, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | -1 to 10 | -3 to 3 | 3 to 8 |  |
| leg_hl | 0 to 4 | -4 to -3 | 2 to 6 | on body |
| shin_hl | -1 to 5 | -4 to -3 | 0 to 1 | on leg_hl |
| leg_fl | 8 to 9 | -4 to -4 | 0 to 6 | turned ry -8°; on body |
| head | 10 to 14 | -3 to 3 | 6 to 11 | turned rx +3°, ry +4°, rz -14°; on body |
| ear_l | 11 to 12 | -2 to -1 | 12 to 18 | turned rx +6°, ry -4°; on head |
| leg_hr | 0 to 4 | 3 to 4 | 2 to 6 | on body |
| shin_hr | -1 to 5 | 3 to 4 | 0 to 1 | on leg_hr |
| leg_fr | 8 to 9 | 4 to 4 | 0 to 6 | turned ry +6°; on body |
| ear_r | 11 to 12 | 1 to 2 | 12 to 18 | turned rx -8°, ry -16°; on head |

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
