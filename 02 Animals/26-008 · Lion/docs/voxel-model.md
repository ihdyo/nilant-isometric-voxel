# 26-008 · Lion · voxel brief

*Panthera leo* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `coat` | `orange-300` | body, legs, face, ears, tail |
| `mane` | `amber-800` | the mane and the tail tuft |
| `muzzle` | `orange-100` | the muzzle, the outer half of each eye |
| `nose` | `stone-700` | the nose |
| `eye` | `neutral-950` | the dark inner half of each two-voxel eye on the front of the head |

Background (not modelled): `violet-200`.

## Size and pose

- Size: 47 × 21 × 28 voxels posed (L × W × H); longest side 47, budget 36–48 (target 42) from the real size 2.8 m (nose to tail tip: 2.4–3.3 m, mid-range).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: shin_fl, shin_fr, shin_hl, shin_hr, leg_fl, leg_fr, leg_hl, leg_hr, mane, body, head, muzzle, tail_tip, tail, ear_l, ear_r.

## Personality, pose and expression

- Personality: proud and confident, the king who naps a lot.
- Pose: mid-stride, chest out, the head and its thick mane turned to the camera and raised, the tail dropping and curling up to the dark tuft.
- Expression: steady pale eyes with the pupils to the inside under heavy brows slanting down to the middle, a calm smile, all painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| shin_fl | 14 to 17 | -6 to -3 | 0 to 3 | turned ry +24°; on leg_fl |
| shin_fr | 14 to 17 | 3 to 6 | 0 to 3 | on leg_fr |
| shin_hl | 1 to 4 | -6 to -3 | 0 to 3 | turned ry -10°; on leg_hl |
| shin_hr | 1 to 4 | 3 to 6 | 0 to 3 | on leg_hr |
| leg_fl | 14 to 17 | -6 to -3 | 4 to 8 | turned ry -12°; on body |
| leg_fr | 14 to 17 | 3 to 6 | 4 to 8 | turned ry +8°; on body |
| leg_hl | 1 to 4 | -6 to -3 | 4 to 8 | turned ry +10°; on body |
| leg_hr | 1 to 4 | 3 to 6 | 4 to 8 | turned ry -8°; on body |
| mane | 18 to 27 | -9 to 9 | 8 to 25 | turned rx +4°, ry -5°, rz -10°; on body |
| body | 0 to 19 | -6 to 6 | 9 to 18 |  |
| head | 24 to 29 | -6 to 6 | 11 to 21 | turned rx +4°; on mane |
| muzzle | 30 to 32 | -3 to 3 | 11 to 15 | on head |
| tail_tip | -14 to -7 | -2 to 2 | 14 to 17 | turned ry +38°; on tail |
| tail | -6 to -1 | -1 to 1 | 15 to 16 | turned ry -24°; on body |
| ear_l | 28 to 28 | -6 to -5 | 22 to 23 | turned rx +10°; on head |
| ear_r | 28 to 28 | 5 to 6 | 22 to 23 | turned rx -10°; on head |

## Recognisable features (in order of importance)

1. the big rounded mane around head and neck (adult male)
2. the face sticking forward out of the mane, with a pale muzzle
3. the long tail ending in a dark tuft
4. a long, strong tawny body on long legs

## Colour map

- `coat`: body, legs, face, ears, tail
- `mane`: the mane and the tail tuft
- `muzzle`: the muzzle, the outer half of each eye
- `nose`: the nose
- `eye`: the dark inner half of each two-voxel eye on the front of the head

## Photos used

- `assets/photos/01-male-rock.jpg`: adult male lying, mane (CC BY 2.0)
- `assets/photos/02-male-standing.jpg`: adult male standing, side, tail tuft (CC BY 2.0)
