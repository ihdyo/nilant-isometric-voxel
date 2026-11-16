# 26-007 · Koala · voxel brief

*Phascolarctos cinereus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `fur` | `stone-400` | body, head, arms, legs |
| `white` | `stone-100` | chest, the ear fronts, the outer half of each eye |
| `nose` | `stone-800` | the nose |
| `eye` | `neutral-950` | the dark inner half of each two-voxel eye on the front of the head |
| `paw` | `stone-600` | palms of the hands and soles of the feet, the claws |

Background (not modelled): `amber-200`.

## Size and pose

- Size: 14 × 24 × 25 voxels posed (L × W × H); longest side 25, budget 21–29 (target 25) from the real size 0.75 m (head and body 72–78 cm (sitting height with the ears)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_l, leg_r, arm_l, arm_r, head, nose, ear_l, ear_r.

## Personality, pose and expression

- Personality: sleepy and cuddly.
- Pose: sitting, arms hanging from the sides of the body and swung forward so the dark-palmed hands rest beside the knees, feet forward with dark soles, the big head drowsily tilted, huge fluffy ears tipped out.
- Expression: eyes closed in a sleepy curve and a tiny smile under the big nose, painted flat on the face.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 7 | -5 to 5 | 0 to 11 |  |
| leg_l | 5 to 10 | -5 to -3 | 0 to 3 | turned rz -10°; on body |
| leg_r | 5 to 10 | 3 to 5 | 0 to 3 | turned rz +10°; on body |
| arm_l | 3 to 5 | -7 to -6 | 4 to 10 | turned rx +8°, ry -28°; on body |
| arm_r | 3 to 5 | 6 to 7 | 4 to 10 | turned rx -8°, ry -28°; on body |
| head | -1 to 8 | -7 to 7 | 12 to 21 | turned rx +12°, ry +4°, rz -8°; on body |
| nose | 9 to 10 | -2 to 2 | 13 to 18 | on head |
| ear_l | 2 to 4 | -11 to -6 | 16 to 23 | turned rx +14°, ry +6°; on head |
| ear_r | 2 to 4 | 6 to 11 | 16 to 23 | turned rx -14°, ry +6°; on head |

## Recognisable features (in order of importance)

1. the big dark nose
2. large round ears with white fluffy fringes
3. a big round head on a compact body
4. the white chest
5. the sitting teddy-bear pose

## Colour map

- `fur`: body, head, arms, legs
- `white`: chest, the ear fronts, the outer half of each eye
- `nose`: the nose
- `eye`: the dark inner half of each two-voxel eye on the front of the head
- `paw`: palms of the hands and soles of the feet, the claws

## Photos used

- `assets/photos/01-in-tree.jpg`: adult in a tree, nose and ear tufts (CC0)
- `assets/photos/02-walking.jpg`: adult on a branch, body and limbs (CC BY 3.0)
