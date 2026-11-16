# 26-014 · Hippo · voxel brief

*Hippopotamus amphibius* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (Tailwind token or #hex) | Where |
|---|---|---|
| `skin` | `#8E7C8F` | body, head, legs (a purple-grey hex: no Tailwind token has that slate-violet) |
| `pink` | `rose-200` | the pinkish skin around the eyes and ears, the cheeks and the belly |
| `mouth` | `rose-400` | the inside of the open mouth |
| `tusk` | `amber-50` | the tusks and teeth |
| `eye` | `neutral-950` | the sleepy eye lines, the nostrils |

Background (not modelled): `yellow-200` (rendered as a calm pastel).

## Size and pose

- Size: 45 × 21 × 28 voxels posed (L × W × H); longest side 45, budget 42–56 (target 49) from the real size 4.0 m (nose to tail: 2.9–5 m, mid-range).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, jaw, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: grumpy-looking but sleepy and lovable.
- Pose: standing in a slow, heavy stance, caught mid-yawn: the broad muzzle tipped up and the lower jaw dropped open to show the pink mouth and the tusks, one ear flicked.
- Expression: eyes squeezed into sleepy lines on top of the head by the yawn, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 21 to 26 | -9 to -4 | 0 to 6 | turned ry -6°; on body |
| leg_fr | 21 to 26 | 4 to 9 | 0 to 6 | on body |
| leg_hl | 2 to 7 | -9 to -4 | 0 to 6 | on body |
| leg_hr | 2 to 7 | 4 to 9 | 0 to 6 | turned ry +5°; on body |
| body | -1 to 28 | -9 to 9 | 7 to 22 |  |
| jaw | 34 to 41 | -8 to 8 | 9 to 15 | turned ry +28°; on head |
| head | 28 to 41 | -9 to 9 | 12 to 24 | turned rx +4°, ry -14°, rz -10°; on body |
| ear_l | 28 to 29 | -7 to -6 | 25 to 26 | turned rx +14°; on head |
| ear_r | 28 to 29 | 6 to 7 | 25 to 26 | turned rx -12°, ry -26°; on head |

## Recognisable features (in order of importance)

1. the huge barrel body on short thick legs
2. the enormous head with a broad muzzle
3. eyes, ears and nostrils on top of the head
4. the mouth that opens very wide, with tusks
5. pinkish skin around the eyes and ears

## Colour map

- `skin`: body, head, legs (a purple-grey hex: no Tailwind token has that slate-violet)
- `pink`: the pinkish skin around the eyes and ears, the cheeks and the belly
- `mouth`: the inside of the open mouth
- `tusk`: the tusks and teeth
- `eye`: the sleepy eye lines, the nostrils

## Photos used

- `assets/photos/01-two-in-water.jpg`: two hippos face to face in the water, pink skin around eyes and ears (CC BY 2.0)
- `assets/photos/02-open-mouths.jpg`: two hippos with mouths wide open, tusks and teeth (Public domain)
