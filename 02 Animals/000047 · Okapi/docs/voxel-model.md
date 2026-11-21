# 000047 · Okapi · voxel brief

*Okapia johnstoni* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#7B3306` | velvety dark chestnut-chocolate torso, neck and upper thighs |
| `stripe` | `#FAFAF9` | horizontal white zebra-like stripes on hindquarters and forelegs |
| `sock` | `#F5F5F4` | white lower legs above dark fetlocks |
| `face` | `#D6D3D1` | pale silver-grey cheeks, muzzle and throat |
| `horn` | `#44403B` | skin-covered ossicones on males and large mobile ears |
| `eye` | `#1C1917` | large dark gentle eyes |

Background (not modelled): `#B5E1C4` (soft leaf green).

## Size and pose

- Size: 40 × 15 × 30 voxels posed (L × W × H); longest side 40, budget 36–44 (target 40) from the real size 2.4 m (nose to tail tip, about 2.4 m (body 1.9–2.5 m plus 30–42 cm tufted tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, neck, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: elusive and gentle, secret forest cousin of the giraffe.
- Pose: a quiet, graceful forest step, tall neck held upright, crisp white zebra-striped hindquarters and white lower stockings, large ears angled forward.
- Expression: large dark eyes on a pale silver-grey face topped with large ears and short ossicones.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 17 to 19 | -4 to -2 | 0 to 10 | turned ry -10°; on body |
| leg_fr | 17 to 19 | 2 to 4 | 0 to 10 | turned ry +5°; on body |
| leg_hl | 2 to 4 | -4 to -2 | 0 to 10 | turned ry +8°; on body |
| leg_hr | 2 to 4 | 2 to 4 | 0 to 10 | on body |
| body | 1 to 21 | -5 to 5 | 10 to 20 |  |
| neck | 17 to 22 | -3 to 3 | 18 to 26 | turned ry +10°; on body |
| tail | -1 to 0 | 0 to 0 | 12 to 18 | turned rx -8°; on body |
| head | 19 to 27 | -3 to 3 | 24 to 29 | turned rx +3°, ry +3°, rz -10°; on neck |
| ear_l | 19 to 21 | -5 to -3 | 28 to 31 | on head |
| ear_r | 19 to 21 | 3 to 5 | 28 to 31 | on head |

## Recognisable features (in order of importance)

1. velvety dark chocolate-brown body contrasting with white-striped rump and white lower legs
2. sloping giraffe-like back and tall graceful neck
3. pale silver-grey cheeks and tapering muzzle
4. large mobile ears and short skin-covered ossicone horns
5. slender tufted tail

## Colour map

- `coat`: velvety dark chestnut-chocolate torso, neck and upper thighs
- `stripe`: horizontal white zebra-like stripes on hindquarters and forelegs
- `sock`: white lower legs above dark fetlocks
- `face`: pale silver-grey cheeks, muzzle and throat
- `horn`: skin-covered ossicones on males and large mobile ears
- `eye`: large dark gentle eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult okapi profile reference (CC0)
