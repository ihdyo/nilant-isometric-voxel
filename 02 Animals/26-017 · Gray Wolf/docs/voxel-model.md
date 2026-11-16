# 26-017 · Gray Wolf · voxel brief

*Canis lupus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (Tailwind token or #hex) | Where |
|---|---|---|
| `fur` | `stone-400` | body, head, legs and tail |
| `back` | `stone-600` | the darker saddle on the back, the ear backs and the tail tip |
| `light` | `stone-100` | the chest, the belly, the muzzle and the cheeks |
| `nose` | `neutral-900` | the nose, the closed eyes and the open mouth |

Background (not modelled): `indigo-200` (rendered as a calm pastel).

## Size and pose

- Size: 29 × 15 × 26 voxels posed (L × W × H); longest side 29, budget 29–39 (target 34) from the real size 1.6 m (nose to tail tip: head and body 0.87–1.3 m plus a 0.35–0.52 m tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_fl, leg_fr, leg_hl, leg_hr, tail, tail_tip, torso, head, snout, ear_l, ear_r.

## Personality, pose and expression

- Personality: loyal and a little dramatic, the pack's singer.
- Pose: sitting on its haunches, the back sloping up from the hips to the shoulders, the front legs straight, the head thrown back to howl at the sky, the ears laid back, the bushy tail curled round on the ground.
- Expression: eyes shut tight and a round open mouth, mid-howl, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 9 | -6 to 6 | 0 to 7 |  |
| leg_fl | 12 to 14 | -5 to -3 | 0 to 12 | on body |
| leg_fr | 12 to 14 | 3 to 5 | 0 to 12 | on body |
| leg_hl | 1 to 11 | -7 to -6 | 0 to 6 | on body |
| leg_hr | 1 to 11 | 6 to 7 | 0 to 6 | on body |
| tail | -6 to -1 | -2 to 2 | 0 to 2 | turned rz +18°; on body |
| tail_tip | -10 to -7 | -2 to 2 | 0 to 2 | turned rz +30°; on tail |
| torso | 3 to 17 | -5 to 5 | 3 to 11 | turned ry -34°; on body |
| head | 15 to 22 | -5 to 5 | 9 to 15 | turned rx +6°, ry -12°, rz -12°; on torso |
| snout | 23 to 26 | -2 to 2 | 9 to 12 | on head |
| ear_l | 16 to 17 | -5 to -3 | 16 to 18 | turned rx +10°, ry -14°; on head |
| ear_r | 16 to 17 | 3 to 5 | 16 to 18 | turned rx -10°, ry -14°; on head |

## Recognisable features (in order of importance)

1. the raised head and the howl
2. pointed upright ears
3. a long snout with a black nose
4. a grey coat with a darker saddle and a pale chest and muzzle
5. a bushy tail

## Colour map

- `fur`: body, head, legs and tail
- `back`: the darker saddle on the back, the ear backs and the tail tip
- `light`: the chest, the belly, the muzzle and the cheeks
- `nose`: the nose, the closed eyes and the open mouth

## Photos used

- `assets/photos/01-front.jpg`: an adult lying down, face to the camera (Public domain)
- `assets/photos/02-pair.jpg`: two wolves meeting, flanks and tails (CC0)
