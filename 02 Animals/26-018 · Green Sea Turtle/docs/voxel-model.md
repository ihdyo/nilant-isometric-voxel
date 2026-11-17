# 26-018 · Green Sea Turtle · voxel brief

*Chelonia mydas* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (Tailwind token or #hex) | Where |
|---|---|---|
| `shell` | `amber-800` | the low shell |
| `seam` | `amber-500` | the lines between the shell plates |
| `skin` | `lime-800` | the head, the flippers and the tail |
| `belly` | `amber-100` | the pale underside and the jaw |
| `eye` | `neutral-950` | the eyes and the smile |

Background (not modelled): `sky-200` (rendered as a calm pastel).

## Size and pose

- Size: 27 × 31 × 7 voxels posed (L × W × H); longest side 31, budget 26–36 (target 31) from the real size 1.3 m (beak to tail with the flippers: a 1–1.2 m shell).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, flipper_hl, flipper_hr, head, flipper_l, flipper_r.

## Personality, pose and expression

- Personality: calm, wise and unhurried.
- Pose: crawling up the beach: the front flippers raised mid-stroke, one higher than the other, the head lifted and turned to the camera, the back flippers splayed.
- Expression: content, half-closed eyes and a small smile, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | -1 to 19 | -7 to 7 | 0 to 6 |  |
| flipper_hl | 1 to 3 | -10 to -8 | 1 to 1 | turned rz -20°; on body |
| flipper_hr | 1 to 3 | 8 to 10 | 1 to 1 | turned rz +20°; on body |
| head | 20 to 24 | -2 to 2 | 1 to 5 | turned rx +6°, ry -14°, rz -16°; on body |
| flipper_l | 11 to 14 | -15 to -8 | 2 to 2 | turned rx -24°, rz +14°; on body |
| flipper_r | 11 to 14 | 8 to 15 | 2 to 2 | turned rx +10°, rz -14°; on body |

## Recognisable features (in order of importance)

1. the low shell in two steps with its pattern of plates
2. big paddle flippers
3. a small rounded head
4. a pale yellow underside
5. olive skin

## Colour map

- `shell`: the low shell
- `seam`: the lines between the shell plates
- `skin`: the head, the flippers and the tail
- `belly`: the pale underside and the jaw
- `eye`: the eyes and the smile

## Photos used

- `assets/photos/01-on-sand.jpg`: an adult on wet sand, head, shell and front flipper (CC0)
- `assets/photos/02-reef.jpg`: an adult swimming over a reef, shell pattern (CC BY 2.0)
