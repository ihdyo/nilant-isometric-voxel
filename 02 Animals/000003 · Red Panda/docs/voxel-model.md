# 000003 · Red Panda · voxel brief

*Ailurus fulgens* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour | Where |
|---|---|---|
| `fur` | `#CA3500` | back, flanks, head, tail |
| `white` | `#FAFAF9` | muzzle, cheeks, brows, ear rims, the outer half of each eye |
| `dark` | `#441306` | legs, belly, nose, tail tip |
| `ring` | `#FFB86A` | two pale rings on the tail |
| `eye` | `#0A0A0A` | the dark inner half of each two-voxel eye on the front of the head |

Background (not modelled): `#AFE2CD` (moss green).

## Size and pose

- Size: 30 × 13 × 20 voxels posed (L × W × H); longest side 30, budget 24–32 (target 28) from the real size 1.0 m (nose to tail tip: head and body 56–63 cm plus tail 37–47 cm).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, leg_fl, head, muzzle, ear_l, tail, tail_tip, leg_hr, leg_fr, ear_r.

## Personality, pose and expression

- Personality: curious and playful.
- Pose: One front paw reaching forward, the head turned to the camera and up, curious, the ringed tail curling up in two blocks.
- Expression: wide white eyes with the pupils to the inside, white brows rising towards the middle, a small round mouth, all painted flat on the face.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 11 | -4 to 4 | 5 to 10 |  |
| leg_hl | 1 to 3 | -4 to -2 | 0 to 4 | turned ry +10°; on body |
| leg_fl | 8 to 10 | -4 to -2 | 0 to 4 | turned ry -32°; on body |
| head | 11 to 18 | -5 to 5 | 8 to 15 | turned rx +4°, ry -8°, rz -14°; on body |
| muzzle | 19 to 20 | -2 to 2 | 8 to 10 | on head |
| ear_l | 13 to 14 | -5 to -3 | 16 to 18 | turned rx +16°, ry +8°; on head |
| tail | -5 to -1 | -1 to 1 | 7 to 9 | turned ry +24°, rz +8°; on body |
| tail_tip | -9 to -6 | -1 to 1 | 7 to 9 | turned ry +22°; on tail |
| leg_hr | 1 to 3 | 2 to 4 | 0 to 4 | turned ry -8°; on body |
| leg_fr | 8 to 10 | 2 to 4 | 0 to 4 | turned ry +8°; on body |
| ear_r | 13 to 14 | 3 to 5 | 16 to 18 | turned rx -16°, ry +8°; on head |

## Recognisable features (in order of importance)

1. the long thick ringed tail
2. the white face mask (cheeks, brows, muzzle) around dark eyes
3. pointed ears with white rims
4. dark legs and belly under rusty red fur

## Colour map

- `fur`: back, flanks, head, tail
- `white`: muzzle, cheeks, brows, ear rims, the outer half of each eye
- `dark`: legs, belly, nose, tail tip
- `ring`: two pale rings on the tail
- `eye`: the dark inner half of each two-voxel eye on the front of the head

## Photos used

- `assets/photos/01-front.jpg`: adult on a branch, face mask, dark legs (CC0)
- `assets/photos/02-side-walking.jpg`: adult walking, full side, ringed tail (Public domain)
