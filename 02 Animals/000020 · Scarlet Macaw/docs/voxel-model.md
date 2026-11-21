# 000020 · Scarlet Macaw · voxel brief

*Ara macao* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `red` | `#E7000B` | the head, the body and most of the tail |
| `yellow` | `#FFB900` | the yellow band across the wings |
| `blue` | `#155DFC` | the wing tips and the tail tip |
| `face` | `#FAFAF9` | the bare white face patch |
| `bill` | `#E7E5E4` | the pale upper bill |
| `dark` | `#171717` | the black lower bill, the legs and the pupil |
| `eye` | `#FEF3C6` | the pale yellow eye |

Background (not modelled): `#B6E1C3` (canopy green).

## Size and pose

- Size: 26 × 18 × 24 voxels posed (L × W × H); longest side 26, budget 23–31 (target 27) from the real size 0.89 m (bill tip to tail tip: about 89 cm, a third to a half of it tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_l, body, wing_l, tail, tail_tip, head, beak, leg_r, wing_r.

## Personality, pose and expression

- Personality: loud, cheeky and a show-off.
- Pose: On the ground, both wings lifted, the left one more, the head turned to the camera, the long tail down, the small feet.
- Expression: a pale eye with the dark pupil to the front in its white face patch, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_l | 4 to 6 | -3 to -2 | 0 to 3 | on body |
| body | 0 to 8 | -3 to 3 | 4 to 15 |  |
| wing_l | 0 to 7 | -4 to -4 | 5 to 15 | turned rx -32°, rz -10°; on body |
| tail | -7 to -1 | -1 to 1 | 7 to 8 | turned ry -24°; on body |
| tail_tip | -13 to -8 | -1 to 1 | 7 to 8 | turned ry -10°; on tail |
| head | 2 to 9 | -3 to 3 | 16 to 22 | turned rx +3°, ry -6°; on body |
| beak | 10 to 13 | -1 to 1 | 16 to 20 | turned ry +8°; on head |
| leg_r | 4 to 6 | 2 to 3 | 0 to 3 | on body |
| wing_r | 0 to 7 | 4 to 4 | 5 to 15 | turned rx +20°, rz +6°; on body |

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
