# 000008 · Lion · voxel brief

*Panthera leo* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour | Where |
|---|---|---|
| `coat` | `#FFB86A` | body, legs, face, ears, tail |
| `mane` | `#973C00` | the mane and the tail tuft |
| `muzzle` | `#FFEDD4` | the muzzle, the outer half of each eye |
| `nose` | `#44403B` | the nose |
| `eye` | `#0A0A0A` | the dark inner half of each two-voxel eye on the front of the head |

Background (not modelled): `#D3CEFA` (dusk lavender).

## Size and pose

- Size: 47 × 19 × 26 voxels posed (L × W × H); longest side 47, budget 36–48 (target 42) from the real size 2.8 m (nose to tail tip: 2.4–3.3 m, mid-range).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, shin_hl, leg_fl, shin_fl, mane, head, muzzle, ear_l, tail, tail_tip, leg_hr, shin_hr, leg_fr, shin_fr, ear_r.

## Personality, pose and expression

- Personality: proud and confident, the king who naps a lot.
- Pose: A proud strut, the front left paw reaching with its knee folding, the head held high inside a shorter mane and turned to the camera, the tail dropping and curling up to the dark tuft.
- Expression: steady pale eyes with the pupils to the inside under heavy brows slanting down to the middle, a calm smile, all painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 19 | -6 to 6 | 9 to 18 |  |
| leg_hl | 1 to 4 | -6 to -3 | 4 to 8 | turned ry +14°; on body |
| shin_hl | 1 to 4 | -6 to -3 | 0 to 3 | turned ry -14°; on leg_hl |
| leg_fl | 14 to 17 | -6 to -3 | 4 to 8 | turned ry -20°; on body |
| shin_fl | 14 to 17 | -6 to -3 | 0 to 3 | turned ry +30°; on leg_fl |
| mane | 18 to 25 | -8 to 8 | 9 to 24 | turned rx +2°, ry -4°, rz -14°; on body |
| head | 24 to 29 | -6 to 6 | 11 to 21 | on mane |
| muzzle | 30 to 32 | -3 to 3 | 11 to 15 | on head |
| ear_l | 28 to 28 | -6 to -5 | 22 to 23 | turned rx +10°; on head |
| tail | -6 to -1 | -1 to 1 | 15 to 16 | turned ry -20°, rz +10°; on body |
| tail_tip | -14 to -7 | -2 to 2 | 14 to 17 | turned ry +38°; on tail |
| leg_hr | 1 to 4 | 3 to 6 | 4 to 8 | turned ry -12°; on body |
| shin_hr | 1 to 4 | 3 to 6 | 0 to 3 | on leg_hr |
| leg_fr | 14 to 17 | 3 to 6 | 4 to 8 | turned ry +12°; on body |
| shin_fr | 14 to 17 | 3 to 6 | 0 to 3 | on leg_fr |
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
