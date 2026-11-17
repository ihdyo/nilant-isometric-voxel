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

- Size: 33 × 13 × 30 voxels posed (L × W × H); longest side 33, budget 29–39 (target 34) from the real size 1.6 m (nose to tail tip: head and body 0.87–1.3 m plus a 0.35–0.52 m tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: shin_fl, shin_fr, shin_hl, shin_hr, leg_fl, leg_fr, leg_hl, leg_hr, body, tail, tail_tip, neck, head, snout, ear_l, ear_r.

## Personality, pose and expression

- Personality: loyal and a little dramatic, the pack's singer.
- Pose: standing four-square on long legs with knees, the thick neck ruff raised and the head thrown back to howl at the sky, turned to the camera, the ears laid back, the bushy tail hanging low.
- Expression: eyes shut tight and a round open mouth, mid-howl, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| shin_fl | 12 to 14 | -5 to -3 | 0 to 4 | on leg_fl |
| shin_fr | 12 to 14 | 3 to 5 | 0 to 4 | on leg_fr |
| shin_hl | 1 to 3 | -5 to -3 | 0 to 4 | on leg_hl |
| shin_hr | 1 to 3 | 3 to 5 | 0 to 4 | on leg_hr |
| leg_fl | 12 to 14 | -5 to -3 | 5 to 8 | turned ry -6°; on body |
| leg_fr | 12 to 14 | 3 to 5 | 5 to 8 | on body |
| leg_hl | 0 to 3 | -5 to -3 | 5 to 8 | on body |
| leg_hr | 0 to 3 | 3 to 5 | 5 to 8 | turned ry +5°; on body |
| body | 0 to 15 | -5 to 5 | 9 to 17 |  |
| tail | -5 to -1 | -2 to 2 | 12 to 15 | turned ry -28°, rz +8°; on body |
| tail_tip | -9 to -6 | -2 to 2 | 12 to 15 | turned ry -12°, rz +6°; on tail |
| neck | 14 to 17 | -4 to 4 | 14 to 20 | turned ry -20°, rz -6°; on body |
| head | 16 to 22 | -5 to 5 | 19 to 25 | turned rx +6°, ry -22°, rz -10°; on neck |
| snout | 23 to 26 | -2 to 2 | 19 to 22 | on head |
| ear_l | 17 to 18 | -5 to -3 | 26 to 28 | turned rx +10°, ry -14°; on head |
| ear_r | 17 to 18 | 3 to 5 | 26 to 28 | turned rx -10°, ry -14°; on head |

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
