# 26-024 · Red-eyed Tree Frog · voxel brief

*Agalychnis callidryas* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (Tailwind token or #hex) | Where |
|---|---|---|
| `green` | `green-500` | the back, the head and the legs |
| `red` | `red-500` | the big eyes |
| `blue` | `blue-600` | the flanks and the inner legs |
| `yellow` | `amber-300` | the stripes on the flanks |
| `toe` | `orange-400` | the hands, the feet and the toe pads |
| `belly` | `stone-50` | the belly and the throat |
| `pupil` | `neutral-950` | the pupils and the smile |

Background (not modelled): `pink-200` (rendered as a calm pastel).

## Size and pose

- Size: 18 × 15 × 12 voxels posed (L × W × H); longest side 18, budget 16–18 (target 16) from the real size 0.07 m (snout to vent: 4–7 cm, females larger).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, head.

## Personality, pose and expression

- Personality: a cheeky, bright-eyed show-off.
- Pose: sitting tall on folded back legs with the front feet planted wide and the orange toes spread, the head tilted up to the camera.
- Expression: huge red eyes with a black pupil and a wide grin, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 10 to 13 | -7 to -5 | 0 to 3 | on body |
| leg_fr | 10 to 13 | 5 to 7 | 0 to 3 | on body |
| leg_hl | 1 to 8 | -7 to -5 | 0 to 3 | on body |
| leg_hr | 1 to 8 | 5 to 7 | 0 to 3 | on body |
| body | 0 to 10 | -4 to 4 | 2 to 6 |  |
| head | 11 to 16 | -5 to 5 | 3 to 9 | turned rx +8°, ry -12°, rz -14°; on body |

## Recognisable features (in order of importance)

1. huge bulging red eyes
2. a bright green body
3. blue flanks with yellow stripes
4. orange toes with sticky pads
5. a white belly

## Colour map

- `green`: the back, the head and the legs
- `red`: the big eyes
- `blue`: the flanks and the inner legs
- `yellow`: the stripes on the flanks
- `toe`: the hands, the feet and the toe pads
- `belly`: the belly and the throat
- `pupil`: the pupils and the smile

## Photos used

- `assets/photos/01-on-stem.jpg`: an adult gripping a stem, red eyes, orange toes, blue and yellow flank (CC0)
- `assets/photos/02-on-leaf.jpg`: an adult sitting on a leaf at night (CC BY 2.0)
