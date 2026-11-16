# 26-020 · Scarlet Macaw · voxel brief

*Ara macao* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (Tailwind token or #hex) | Where |
|---|---|---|
| `red` | `red-600` | the head, the body and most of the tail |
| `yellow` | `amber-400` | the yellow band across the wings |
| `blue` | `blue-600` | the wing tips and the tail tip |
| `face` | `stone-50` | the bare white face patch |
| `bill` | `stone-200` | the pale upper bill |
| `dark` | `neutral-900` | the black lower bill, the legs and the pupil |
| `eye` | `amber-100` | the pale yellow eye |

Background (not modelled): `emerald-200` (rendered as a calm pastel).

## Size and pose

- Size: 26 × 20 × 24 voxels posed (L × W × H); longest side 26, budget 23–31 (target 27) from the real size 0.89 m (bill tip to tail tip: about 89 cm, a third to a half of it tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_l, leg_r, body, wing_l, wing_r, tail, tail_tip, beak, head.

## Personality, pose and expression

- Personality: loud, cheeky and a show-off.
- Pose: standing tall with both wings half open to flash the yellow and blue, the head cocked to the camera, the long tail sweeping down behind.
- Expression: a pale eye with the dark pupil to the front in its white face patch, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_l | 4 to 7 | -3 to -1 | 0 to 3 | on body |
| leg_r | 4 to 7 | 1 to 3 | 0 to 3 | on body |
| body | 0 to 8 | -3 to 3 | 4 to 15 |  |
| wing_l | 0 to 7 | -4 to -4 | 5 to 15 | turned rx -30°, rz -10°; on body |
| wing_r | 0 to 7 | 4 to 4 | 5 to 15 | turned rx +30°, rz +10°; on body |
| tail | -7 to -1 | -1 to 1 | 7 to 8 | turned ry -24°; on body |
| tail_tip | -13 to -8 | -1 to 1 | 7 to 8 | turned ry -10°; on tail |
| beak | 10 to 13 | -1 to 1 | 16 to 20 | turned ry +8°; on head |
| head | 2 to 9 | -3 to 3 | 16 to 22 | turned rx +12°, rz -14°; on body |

## Recognisable features (in order of importance)

1. the scarlet body
2. yellow and blue bands on the wings
3. a very long red-and-blue tail
4. the bare white face patch
5. a big hooked bill, pale on top and black below

## Colour map

- `red`: the head, the body and most of the tail
- `yellow`: the yellow band across the wings
- `blue`: the wing tips and the tail tip
- `face`: the bare white face patch
- `bill`: the pale upper bill
- `dark`: the black lower bill, the legs and the pupil
- `eye`: the pale yellow eye

## Photos used

- `assets/photos/01-flying.jpg`: an adult taking off from a tree, wings spread, red, yellow and blue (CC BY 4.0)
- `assets/photos/02-pair.jpg`: two macaws in flight, the long tails (CC0)
