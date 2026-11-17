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

- Size: 22 × 22 × 22 voxels posed (L × W × H); longest side 22, budget 21–29 (target 25) from the real size 0.75 m (head and body 72–78 cm (sitting height with the ears)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, head, nose, ear_l, ear_r.

## Personality, pose and expression

- Personality: sleepy and cuddly.
- Pose: standing on all four short, thick legs in a slow amble (the front left paw reaching forward), the round body low, the big head held up on its front, drowsily tilted and turned to the camera, huge fluffy ears tipped out.
- Expression: eyes closed in a sleepy curve and a tiny smile under the big nose, painted flat on the face.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 9 to 11 | -5 to -3 | 0 to 5 | turned ry -12°; on body |
| leg_fr | 9 to 11 | 3 to 5 | 0 to 5 | turned ry +8°; on body |
| leg_hl | 1 to 3 | -5 to -3 | 0 to 5 | turned ry +10°; on body |
| leg_hr | 1 to 3 | 3 to 5 | 0 to 5 | turned ry -8°; on body |
| body | 0 to 12 | -5 to 5 | 6 to 14 |  |
| head | 12 to 19 | -6 to 6 | 10 to 18 | turned rx +10°, ry +4°, rz -10°; on body |
| nose | 20 to 21 | -1 to 1 | 11 to 15 | on head |
| ear_l | 14 to 16 | -10 to -6 | 14 to 20 | turned rx +14°, ry +6°; on head |
| ear_r | 14 to 16 | 6 to 10 | 14 to 20 | turned rx -14°, ry +6°; on head |

## Recognisable features (in order of importance)

1. the big dark nose
2. large round ears with white fluffy fringes
3. a big round head on a compact body
4. the white chest
5. standing on four short, thick legs, the big head held up

## Colour map

- `fur`: body, head, arms, legs
- `white`: chest, the ear fronts, the outer half of each eye
- `nose`: the nose
- `eye`: the dark inner half of each two-voxel eye on the front of the head
- `paw`: palms of the hands and soles of the feet, the claws

## Photos used

- `assets/photos/01-in-tree.jpg`: adult in a tree, nose and ear tufts (CC0)
- `assets/photos/02-walking.jpg`: adult on a branch, body and limbs (CC BY 3.0)
