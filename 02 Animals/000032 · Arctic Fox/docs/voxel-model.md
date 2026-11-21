# 000032 · Arctic Fox · voxel brief

*Vulpes lagopus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#FAFAF9` | thick winter-white body, head, rounded ears, legs and plume tail |
| `shade` | `#E2E8F0` | subtle cool-grey shading under belly, chin and tail underside |
| `nose` | `#171717` | small black nose tip |
| `pad` | `#D6D3D1` | furred winter paw undersides |
| `white` | `#DFF2FE` | eye sclera highlight |
| `eye` | `#FE9A00` | golden-amber pupils |

Background (not modelled): `#A6E0E6` (soft teal).

## Size and pose

- Size: 34 × 13 × 18 voxels posed (L × W × H); longest side 34, budget 30–38 (target 34) from the real size 0.85 m (nose to tail tip, about 0.85 m (body 46–68 cm plus 25–35 cm bushy tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: plucky and cozy, wrapped in a thick winter coat.
- Pose: a brisk tundra trot, big bottle-brush tail held out behind, compact rounded ears alert and head turned toward the viewer.
- Expression: bright golden-amber eyes and a tiny black button nose in fluffy white fur.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 14 to 16 | -4 to -2 | 0 to 5 | turned ry -12°; on body |
| leg_fr | 14 to 16 | 2 to 4 | 0 to 5 | turned ry +6°; on body |
| leg_hl | 2 to 4 | -4 to -2 | 0 to 5 | turned ry +10°; on body |
| leg_hr | 2 to 4 | 2 to 4 | 0 to 5 | on body |
| body | 1 to 17 | -4 to 4 | 5 to 12 |  |
| tail | -10 to 0 | -2 to 2 | 7 to 11 | turned ry -12°, rz -6°; on body |
| head | 16 to 23 | -4 to 4 | 9 to 16 | turned rx +4°, ry +2°, rz -10°; on body |
| ear_l | 17 to 19 | -4 to -2 | 16 to 18 | on head |
| ear_r | 17 to 19 | 2 to 4 | 16 to 18 | on head |

## Recognisable features (in order of importance)

1. dense, puffy snow-white winter coat
2. thick, cylindrical plume tail used as a blanket
3. short muzzle and small, heavily furred rounded ears
4. short legs with fur-covered soles (lagopus = 'hare-foot')
5. subtle cool-slate shadow planes

## Colour map

- `coat`: thick winter-white body, head, rounded ears, legs and plume tail
- `shade`: subtle cool-grey shading under belly, chin and tail underside
- `nose`: small black nose tip
- `pad`: furred winter paw undersides
- `white`: eye sclera highlight
- `eye`: golden-amber pupils

## Photos used

- `assets/photos/01-side-profile.jpg`: adult arctic fox profile reference (CC BY 2.0)
