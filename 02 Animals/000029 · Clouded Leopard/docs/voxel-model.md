# 000029 · Clouded Leopard · voxel brief

*Neofelis nebulosa* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#A6A09B` | supple body, head, short stout legs and long thick tail |
| `cloud` | `#44403B` | large cloud-shaped dark-edged blotches on flanks and tail rings |
| `belly` | `#F5F5F4` | chin, throat, chest and underbelly |
| `muzzle` | `#E7E5E4` | pale muzzle and whisker area |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#FE9A00` | amber-green pupils |

Background (not modelled): `#B0E1CA` (soft mint).

## Size and pose

- Size: 44 × 14 × 20 voxels posed (L × W × H); longest side 44, budget 40–48 (target 44) from the real size 1.8 m (nose to tail tip, about 1.8 m (body 0.69–1.08 m plus 0.61–0.91 m tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: shin_fl, shin_fr, shin_hl, shin_hr, leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: acrobatic and secretive, master of the forest canopy.
- Pose: a low, agile branch-walking crouch on short sturdy legs, long thick tail trailing for balance, head turned toward the viewer.
- Expression: wide amber eyes with subtle facial stripes and rounded ears.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| shin_fl | 17 to 19 | -4 to -2 | 0 to 3 | turned ry +12°; on leg_fl |
| shin_fr | 17 to 19 | 2 to 4 | 0 to 3 | on leg_fr |
| shin_hl | 2 to 4 | -4 to -2 | 0 to 3 | turned ry -8°; on leg_hl |
| shin_hr | 2 to 4 | 2 to 4 | 0 to 3 | on leg_hr |
| leg_fl | 17 to 19 | -4 to -2 | 4 to 7 | turned ry -10°; on body |
| leg_fr | 17 to 19 | 2 to 4 | 4 to 7 | turned ry +5°; on body |
| leg_hl | 2 to 4 | -4 to -2 | 4 to 7 | turned ry +8°; on body |
| leg_hr | 2 to 4 | 2 to 4 | 4 to 7 | on body |
| body | 1 to 21 | -4 to 4 | 7 to 14 |  |
| tail | -15 to 0 | -1 to 1 | 10 to 12 | turned ry +6°, rz -8°; on body |
| head | 20 to 27 | -4 to 4 | 11 to 19 | turned rx +4°, ry +3°, rz -10°; on body |
| ear_l | 22 to 23 | -4 to -3 | 19 to 20 | on head |
| ear_r | 22 to 23 | 3 to 4 | 19 to 20 | on head |

## Recognisable features (in order of importance)

1. large cloud-shaped blotches edged in dark brown-black
2. exceptionally long, thick tail nearly equal to body length
3. short, stout legs with large paws for gripping branches
4. elongated skull with distinct cheek stripes
5. pale creamy chest and underbelly

## Colour map

- `coat`: supple body, head, short stout legs and long thick tail
- `cloud`: large cloud-shaped dark-edged blotches on flanks and tail rings
- `belly`: chin, throat, chest and underbelly
- `muzzle`: pale muzzle and whisker area
- `white`: the white of each eye
- `eye`: amber-green pupils

## Photos used

- `assets/photos/01-side-profile.jpg`: adult clouded leopard profile reference (CC BY-SA 3.0)
