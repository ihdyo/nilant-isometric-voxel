# 000026 · Snow Leopard · voxel brief

*Panthera uncia* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#D6D3D1` | body, head, legs, ears, long fluffy tail |
| `spot` | `#57534D` | rosettes across back, flanks, head and tail bands |
| `belly` | `#F5F5F4` | chest, underbelly, chin and inner paws |
| `nose` | `#FFA1AD` | small pink-grey nose pad |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#00BC7D` | pale green-grey pupils and brows |

Background (not modelled): `#AFDBF7` (soft sky blue).

## Size and pose

- Size: 46 × 16 × 23 voxels posed (L × W × H); longest side 46, budget 42–50 (target 46) from the real size 2.1 m (nose to tail tip, about 2.1 m including the 0.9 m tail (body length 1–1.3 m per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: shin_fl, shin_fr, shin_hl, shin_hr, leg_fl, leg_fr, leg_hl, leg_hr, body, tail_1, tail_2, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: quiet and elusive, the ghost of the high peaks.
- Pose: a low, stealthy mountain stride, the long thick tail curving behind for balance, the round head turned slightly toward the camera.
- Expression: calm pale-green eyes with inward pupils, small rounded ears and a soft pink nose.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| shin_fl | 17 to 20 | -5 to -2 | 0 to 4 | turned ry +14°; on leg_fl |
| shin_fr | 17 to 20 | 2 to 5 | 0 to 4 | on leg_fr |
| shin_hl | 2 to 5 | -5 to -2 | 0 to 4 | turned ry -10°; on leg_hl |
| shin_hr | 2 to 5 | 2 to 5 | 0 to 4 | on leg_hr |
| leg_fl | 17 to 20 | -5 to -2 | 5 to 9 | turned ry -12°; on body |
| leg_fr | 17 to 20 | 2 to 5 | 5 to 9 | turned ry +6°; on body |
| leg_hl | 2 to 5 | -5 to -2 | 5 to 9 | turned ry +10°; on body |
| leg_hr | 2 to 5 | 2 to 5 | 5 to 9 | on body |
| body | 1 to 22 | -5 to 5 | 9 to 17 |  |
| tail_1 | -8 to 0 | -2 to 2 | 12 to 15 | turned ry +12°, rz -8°; on body |
| tail_2 | -17 to -9 | -2 to 2 | 11 to 14 | turned ry -18°, rz -12°; on tail_1 |
| head | 21 to 29 | -5 to 5 | 13 to 22 | turned rx +4°, ry +3°, rz -10°; on body |
| ear_l | 23 to 25 | -5 to -3 | 22 to 24 | on head |
| ear_r | 23 to 25 | 3 to 5 | 22 to 24 | on head |

## Recognisable features (in order of importance)

1. the extra-long, thick, dark-banded tail
2. the smoky-grey coat patterned with dark rosettes
3. wide, fur-padded paws built for deep snow
4. compact round head with small rounded ears
5. creamy white chest and underbelly

## Colour map

- `coat`: body, head, legs, ears, long fluffy tail
- `spot`: rosettes across back, flanks, head and tail bands
- `belly`: chest, underbelly, chin and inner paws
- `nose`: small pink-grey nose pad
- `white`: the white of each eye
- `eye`: pale green-grey pupils and brows

## Photos used

- `assets/photos/01-side-profile.jpg`: adult snow leopard profile reference (CC BY 2.0)
