# 000017 · Gray Wolf · voxel brief

*Canis lupus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `fur` | `#A6A09B` | body, head, legs and tail |
| `back` | `#57534D` | the darker saddle on the back, the ear backs and the tail tip |
| `light` | `#F5F5F4` | the chest, the belly, the muzzle and the cheeks |
| `nose` | `#171717` | the nose, the closed eyes and the open mouth |

Background (not modelled): `#C8D2FD` (twilight indigo).

## Size and pose

- Size: 37 × 13 × 23 voxels posed (L × W × H); longest side 37, budget 29–39 (target 34) from the real size 1.6 m (nose to tail tip: head and body 0.87–1.3 m plus a 0.35–0.52 m tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, shin_hl, leg_fl, shin_fl, head, snout, ear_l, tail, tail_tip, leg_hr, shin_hr, leg_fr, shin_fr, ear_r.

## Personality, pose and expression

- Personality: loyal and a little dramatic, the pack's singer.
- Pose: Standing on long legs with knees, mid-step, the thick neck ruff part of the body and the head straight on it (no neck), turned to the camera and a little up, the ears perked, the bushy tail low and curving; the howl throws the head back.
- Expression: Calm dark eyes with a pale glint, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 16 | -6 to 6 | 9 to 18 |  |
| leg_hl | 0 to 3 | -5 to -3 | 5 to 8 | turned ry +12°; on body |
| shin_hl | 1 to 3 | -5 to -3 | 0 to 4 | turned ry -10°; on leg_hl |
| leg_fl | 12 to 14 | -5 to -3 | 5 to 8 | turned ry -16°; on body |
| shin_fl | 12 to 14 | -5 to -3 | 0 to 4 | turned ry +22°; on leg_fl |
| head | 17 to 22 | -4 to 4 | 12 to 18 | turned rx +3°, ry -6°, rz -14°; on body |
| snout | 23 to 26 | -2 to 2 | 12 to 15 | on head |
| ear_l | 18 to 19 | -4 to -2 | 19 to 21 | turned rx +8°, ry -4°; on head |
| tail | -5 to -1 | -2 to 2 | 12 to 15 | turned ry -22°, rz +10°; on body |
| tail_tip | -9 to -6 | -2 to 2 | 12 to 15 | turned ry -10°, rz +6°; on tail |
| leg_hr | 0 to 3 | 3 to 5 | 5 to 8 | turned ry -10°; on body |
| shin_hr | 1 to 3 | 3 to 5 | 0 to 4 | on leg_hr |
| leg_fr | 12 to 14 | 3 to 5 | 5 to 8 | turned ry +10°; on body |
| shin_fr | 12 to 14 | 3 to 5 | 0 to 4 | on leg_fr |
| ear_r | 18 to 19 | 2 to 4 | 19 to 21 | turned rx -12°, ry +4°; on head |

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
