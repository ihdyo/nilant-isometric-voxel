# 000011 · African Elephant · voxel brief

*Loxodonta africana* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#99A1AF` | body, head, ears, trunk, legs |
| `shade` | `#6A7282` | the inner ears and the creases under the trunk |
| `tusk` | `#FFFBEB` | the two tusks |
| `nail` | `#E7E5E4` | the toenails on the front of each foot |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#171717` | the pupils, the brows and the smile |

Background (not modelled): `#ECCFA9` (dry-grass gold).

## Size and pose

- Size: 53 × 33 × 38 voxels posed (L × W × H); longest side 53, budget 48–56 (target 56) from the real size 6.0 m (trunk tip to tail, about 6 m for a big adult (general knowledge; ADW gives shoulder heights of 2.2–4 m)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, shin_hl, leg_fl, shin_fl, tail, head, ear_l, tusk_l, trunk_1, trunk_2, trunk_3, leg_hr, shin_hr, leg_fr, shin_fr, ear_r, tusk_r.

## Personality, pose and expression

- Personality: wise and gentle, the herd's calm leader.
- Pose: A slow, heavy step, the big ears spread wide, the trunk curling up at the tip, the head turned to the camera.
- Expression: kind white eyes with the pupils to the inside under soft level brows, a small smile, all painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 29 | -9 to 9 | 14 to 31 |  |
| leg_hl | 1 to 6 | -9 to -4 | 7 to 13 | turned ry +10°; on body |
| shin_hl | 1 to 6 | -9 to -4 | 0 to 6 | turned ry -10°; on leg_hl |
| leg_fl | 23 to 28 | -9 to -4 | 7 to 13 | turned ry -14°; on body |
| shin_fl | 23 to 28 | -9 to -4 | 0 to 6 | turned ry +18°; on leg_fl |
| tail | -1 to -1 | 0 to 0 | 19 to 29 | turned rx -12°; on body |
| head | 29 to 39 | -7 to 7 | 20 to 36 | turned rx +3°, ry +4°, rz -14°; on body |
| ear_l | 30 to 31 | -17 to -8 | 18 to 36 | turned rz +30°; on head |
| tusk_l | 40 to 44 | -4 to -3 | 21 to 22 | turned ry -22°, rz -6°; on head |
| trunk_1 | 40 to 42 | -2 to 2 | 20 to 26 | turned ry -30°; on head |
| trunk_2 | 40 to 41 | -1 to 1 | 15 to 19 | turned ry -40°; on trunk_1 |
| trunk_3 | 40 to 41 | -1 to 1 | 11 to 14 | turned ry -40°; on trunk_2 |
| leg_hr | 1 to 6 | 4 to 9 | 7 to 13 | turned ry -8°; on body |
| shin_hr | 1 to 6 | 4 to 9 | 0 to 6 | on leg_hr |
| leg_fr | 23 to 28 | 4 to 9 | 7 to 13 | turned ry +8°; on body |
| shin_fr | 23 to 28 | 4 to 9 | 0 to 6 | on leg_fr |
| ear_r | 30 to 31 | 8 to 17 | 18 to 36 | turned rz -30°; on head |
| tusk_r | 40 to 44 | 3 to 4 | 21 to 22 | turned ry -22°, rz +6°; on head |

## Recognisable features (in order of importance)

1. the huge ears held out from the head
2. the long trunk, curled up at the tip
3. the two pale tusks
4. a big bulky body on four pillar legs
5. the small tail

## Colour map

- `skin`: body, head, ears, trunk, legs
- `shade`: the inner ears and the creases under the trunk
- `tusk`: the two tusks
- `nail`: the toenails on the front of each foot
- `white`: the white of each eye
- `eye`: the pupils, the brows and the smile

## Photos used

- `assets/photos/01-side-walking.jpg`: adult walking, left flank, trunk curled (CC0)
- `assets/photos/02-herd.jpg`: a family herd crossing a river, calves between the adults (CC BY 2.0)
