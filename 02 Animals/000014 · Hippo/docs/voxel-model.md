# 000014 · Hippo · voxel brief

*Hippopotamus amphibius* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#8E7C8F` | body, head, legs (a purple-grey hex: no hex colour has that slate-violet) |
| `pink` | `#FFCCD3` | the pinkish skin around the eyes and ears, the cheeks and the belly |
| `mouth` | `#FF637E` | the inside of the open mouth |
| `tusk` | `#FFFBEB` | the tusks and teeth |
| `eye` | `#0A0A0A` | the sleepy eye lines, the nostrils |

Background (not modelled): `#DAD7AA` (river-reed green).

## Size and pose

- Size: 45 × 22 × 28 voxels posed (L × W × H); longest side 45, budget 42–56 (target 49) from the real size 4.0 m (nose to tail: 2.9–5 m, mid-range).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, leg_fl, head, jaw, ear_l, leg_hr, leg_fr, ear_r.

## Personality, pose and expression

- Personality: grumpy-looking but sleepy and lovable.
- Pose: A heavy stance mid-step, caught mid-yawn: the broad muzzle tipped up and the lower jaw dropped open, the head turned to the camera, one ear flicked; it walks with a yawn.
- Expression: eyes squeezed into sleepy lines on top of the head by the yawn, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | -1 to 28 | -9 to 9 | 7 to 22 |  |
| leg_hl | 2 to 7 | -9 to -4 | 0 to 6 | turned ry +10°; on body |
| leg_fl | 21 to 26 | -9 to -4 | 0 to 6 | turned ry -12°; on body |
| head | 28 to 41 | -9 to 9 | 12 to 24 | turned rx +3°, ry -8°, rz -14°; on body |
| jaw | 34 to 41 | -8 to 8 | 9 to 15 | turned ry +30°; on head |
| ear_l | 28 to 29 | -7 to -6 | 25 to 26 | turned rx +14°; on head |
| leg_hr | 2 to 7 | 4 to 9 | 0 to 6 | turned ry -8°; on body |
| leg_fr | 21 to 26 | 4 to 9 | 0 to 6 | turned ry +8°; on body |
| ear_r | 28 to 29 | 6 to 7 | 25 to 26 | turned rx -12°, ry -26°; on head |

## Recognisable features (in order of importance)

1. the huge barrel body on short thick legs
2. the enormous head with a broad muzzle
3. eyes, ears and nostrils on top of the head
4. the mouth that opens very wide, with tusks
5. pinkish skin around the eyes and ears

## Colour map

- `skin`: body, head, legs (a purple-grey hex: no hex colour has that slate-violet)
- `pink`: the pinkish skin around the eyes and ears, the cheeks and the belly
- `mouth`: the inside of the open mouth
- `tusk`: the tusks and teeth
- `eye`: the sleepy eye lines, the nostrils

## Photos used

- `assets/photos/01-two-in-water.jpg`: two hippos face to face in the water, pink skin around eyes and ears (CC BY 2.0)
- `assets/photos/02-open-mouths.jpg`: two hippos with mouths wide open, tusks and teeth (Public domain)
