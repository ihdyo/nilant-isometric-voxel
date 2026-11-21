# 000021 · Bottlenose Dolphin · voxel brief

*Tursiops truncatus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `grey` | `#90A1B9` | the flanks, the head, the flippers and the flukes |
| `back` | `#62748E` | the darker back and the dorsal fin |
| `belly` | `#F1F5F9` | the pale belly and the lower jaw |
| `eye` | `#0A0A0A` | the eye and the smile line |

Background (not modelled): `#F4CBAF` (warm-sand peach).

## Size and pose

- Size: 41 × 16 × 13 voxels posed (L × W × H); longest side 41, budget 37–49 (target 43) from the real size 3.0 m (beak to tail flukes: 2.3–3.8 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, flipper_l, head, beak, tail, tail_tip, flukes, flipper_r.

## Personality, pose and expression

- Personality: playful, smart and sociable.
- Pose: Mid-swim, the body arching up through the tail and the flukes, the head turned to the camera, a flipper out.
- Expression: a bright eye with a glint and the dolphin's built-in smile, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 15 | -4 to 4 | 0 to 10 |  |
| flipper_l | 12 to 15 | -7 to -5 | 1 to 1 | turned rx +14°, rz -18°; on body |
| head | 16 to 22 | -3 to 3 | 1 to 7 | turned rx +3°, ry -4°; on body |
| beak | 23 to 27 | -1 to 1 | 1 to 3 | on head |
| tail | -7 to -1 | -3 to 3 | 1 to 6 | turned ry +26°; on body |
| tail_tip | -13 to -8 | -1 to 1 | 2 to 5 | turned ry +20°; on tail |
| flukes | -16 to -14 | -6 to 6 | 3 to 4 | turned ry +14°; on tail_tip |
| flipper_r | 12 to 15 | 5 to 7 | 1 to 1 | turned rx -14°, rz +18°; on body |

## Recognisable features (in order of importance)

1. the long rounded beak
2. a tall curved dorsal fin
3. a dark grey back and pale belly
4. the tail flukes
5. the smile line

## Colour map

- `grey`: the flanks, the head, the flippers and the flukes
- `back`: the darker back and the dorsal fin
- `belly`: the pale belly and the lower jaw
- `eye`: the eye and the smile line

## Photos used

- `assets/photos/01-face.jpg`: a dolphin's head out of the water, beak and smile (Public domain)
- `assets/photos/02-jumping.jpg`: dolphins leaping off Catalina Island (CC0)
