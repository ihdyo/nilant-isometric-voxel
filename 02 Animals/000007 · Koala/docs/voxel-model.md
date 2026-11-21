# 000007 · Koala · voxel brief

*Phascolarctos cinereus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour | Where |
|---|---|---|
| `fur` | `#A6A09B` | body, head, arms, legs |
| `white` | `#F5F5F4` | chest, the ear fronts, the outer half of each eye |
| `nose` | `#292524` | the nose |
| `eye` | `#0A0A0A` | the dark inner half of each two-voxel eye on the front of the head |
| `paw` | `#57534D` | palms of the hands and soles of the feet, the claws |

Background (not modelled): `#B9E0C0` (eucalyptus sage).

## Size and pose

- Size: 23 × 22 × 21 voxels posed (L × W × H); longest side 23, budget 21–29 (target 25) from the real size 0.75 m (head and body 72–78 cm (sitting height with the ears)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, leg_fl, head, nose, ear_l, leg_hr, leg_fr, ear_r.

## Personality, pose and expression

- Personality: sleepy and cuddly.
- Pose: A careful stride on all four feet, the big head turned to the camera, the ears out.
- Expression: eyes closed in a sleepy curve and a tiny smile under the big nose, painted flat on the face.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 12 | -5 to 5 | 6 to 14 |  |
| leg_hl | 1 to 3 | -5 to -3 | 0 to 5 | turned ry +14°; on body |
| leg_fl | 9 to 11 | -5 to -3 | 0 to 5 | turned ry -18°; on body |
| head | 12 to 19 | -6 to 6 | 10 to 18 | turned rx +4°, ry +6°, rz -14°; on body |
| nose | 20 to 21 | -1 to 1 | 11 to 15 | on head |
| ear_l | 14 to 16 | -10 to -6 | 14 to 20 | turned rx +12°, ry +6°; on head |
| leg_hr | 1 to 3 | 3 to 5 | 0 to 5 | turned ry -12°; on body |
| leg_fr | 9 to 11 | 3 to 5 | 0 to 5 | turned ry +12°; on body |
| ear_r | 14 to 16 | 6 to 10 | 14 to 20 | turned rx -12°, ry +6°; on head |

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
