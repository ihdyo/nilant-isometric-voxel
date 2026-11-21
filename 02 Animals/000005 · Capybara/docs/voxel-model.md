# 000005 · Capybara · voxel brief

*Hydrochoerus hydrochaeris* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour | Where |
|---|---|---|
| `fur` | `#973C00` | body, legs, head |
| `dark` | `#441306` | the front of the muzzle and nose, the ears |
| `eye` | `#0A0A0A` | one voxel high on each front corner of the head (seen from the front and the flank) |

Background (not modelled): `#A7DFED` (river blue).

## Size and pose

- Size: 29 × 14 × 19 voxels posed (L × W × H); longest side 29, budget 26–34 (target 30) from the real size 1.2 m (nose to rump: 106–134 cm, mid-range).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, leg_fl, head, snout, ear_l, leg_hr, leg_fr, ear_r.

## Personality, pose and expression

- Personality: calm, unbothered, everyone's friend.
- Pose: A slow, calm stride, the head low and turned to the camera, one ear flicked back.
- Expression: sleepy half-closed eyes (flat lines) and a small easy smile, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 17 | -6 to 6 | 4 to 14 |  |
| leg_hl | 1 to 3 | -6 to -4 | 0 to 3 | turned ry +10°; on body |
| leg_fl | 13 to 15 | -6 to -4 | 0 to 3 | turned ry -14°; on body |
| head | 17 to 24 | -5 to 5 | 8 to 16 | turned rx +2°, ry +6°, rz -14°; on body |
| snout | 25 to 27 | -4 to 4 | 8 to 13 | on head |
| ear_l | 19 to 20 | -5 to -4 | 17 to 17 | turned rx +20°; on head |
| leg_hr | 1 to 3 | 4 to 6 | 0 to 3 | turned ry -10°; on body |
| leg_fr | 13 to 15 | 4 to 6 | 0 to 3 | turned ry +10°; on body |
| ear_r | 19 to 20 | 4 to 5 | 17 to 17 | turned rx -10°, ry -24°; on head |

## Recognisable features (in order of importance)

1. a big barrel body on very short legs
2. a large blunt, boxy head with a deep square muzzle
3. small round ears and eyes high on the head
4. no tail

## Colour map

- `fur`: body, legs, head
- `dark`: the front of the muzzle and nose, the ears
- `eye`: one voxel high on each front corner of the head (seen from the front and the flank)

## Photos used

- `assets/photos/01-resting.jpg`: adult resting, side, blunt muzzle (CC0)
- `assets/photos/02-grazing-side.jpg`: adult grazing, full side, short legs (CC BY 4.0)
