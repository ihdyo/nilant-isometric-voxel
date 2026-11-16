# 26-002 · Giant Panda · voxel brief

*Ailuropoda melanoleuca* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `white` | `stone-50` | body, head, muzzle, tail, the glint in each eye patch |
| `black` | `neutral-900` | legs, shoulder band, ears, eye patches, nose |

Background (not modelled): `#BFD7A7` (a calm pastel bamboo green).

## Size and pose

- Size: 31 × 17 × 27 voxels posed (L × W × H); longest side 31, budget 29–39 (target 34) from the real size 1.65 m (nose to tail: 1.5–1.8 m, mid-range).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, head, muzzle, ear_l, ear_r.

## Personality, pose and expression

- Personality: gentle and laid-back.
- Pose: a slow amble, the big head cocked towards the camera, ears following.
- Expression: content: drooping black eye patches with a white glint, a small v smile under the nose, all painted flat on the face.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 13 to 16 | -6 to -3 | 0 to 6 | turned ry -10°; on body |
| leg_fr | 13 to 16 | 3 to 6 | 0 to 6 | turned ry +6°; on body |
| leg_hl | 1 to 4 | -6 to -3 | 0 to 6 | turned ry +8°; on body |
| leg_hr | 1 to 4 | 3 to 6 | 0 to 6 | turned ry -6°; on body |
| body | -1 to 18 | -6 to 6 | 7 to 17 |  |
| head | 18 to 26 | -6 to 6 | 12 to 22 | turned rx +14°, ry +4°, rz -10°; on body |
| muzzle | 27 to 29 | -2 to 2 | 12 to 16 | on head |
| ear_l | 20 to 21 | -6 to -4 | 23 to 25 | turned rx +14°; on head |
| ear_r | 20 to 21 | 4 to 6 | 23 to 25 | turned rx -14°; on head |

## Recognisable features (in order of importance)

1. black eye patches on a big round white head
2. round black ears
3. black legs and the black band over the shoulders
4. a stocky, rounded barrel of a body
5. a short muzzle with a black nose

## Colour map

- `white`: body, head, muzzle, tail, the glint in each eye patch
- `black`: legs, shoulder band, ears, eye patches, nose

## Photos used

- `assets/photos/01-sitting.jpg`: adult sitting, eye patches, shoulder band (Public domain)
- `assets/photos/02-young-side.jpg`: young panda, side, black legs (CC BY 2.0)
