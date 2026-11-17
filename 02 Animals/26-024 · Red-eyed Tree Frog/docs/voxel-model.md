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

- Size: 17 × 17 × 11 voxels posed (L × W × H); longest side 17, budget 16–18 (target 16) from the real size 0.07 m (snout to vent: 4–7 cm, females larger).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: shin_fl, shin_fr, shin_hl, shin_hr, body, leg_hl, leg_hr, head, leg_fl, leg_fr.

## Personality, pose and expression

- Personality: a cheeky, bright-eyed show-off.
- Pose: sitting low and squat, as wide as it is long, the big hind thighs on the back corners standing on flat orange feet that reach out behind (each leg an upper and a lower part), short front arms with orange hands spread wide, the head tilted up to the camera.
- Expression: huge red eyes bulging on top with a black pupil, and a wide grin across the front, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| shin_fl | 9 to 12 | -7 to -5 | 0 to 1 | on leg_fl |
| shin_fr | 9 to 12 | 5 to 7 | 0 to 1 | on leg_fr |
| shin_hl | -2 to 3 | -8 to -5 | 0 to 0 | on leg_hl |
| shin_hr | -2 to 3 | 5 to 8 | 0 to 0 | on leg_hr |
| body | 0 to 8 | -4 to 4 | 1 to 6 |  |
| leg_hl | 0 to 4 | -7 to -5 | 1 to 5 | on body |
| leg_hr | 0 to 4 | 5 to 7 | 1 to 5 | on body |
| head | 9 to 13 | -4 to 4 | 2 to 9 | turned rx +4°, ry -6°, rz -10°; on body |
| leg_fl | 10 to 11 | -6 to -5 | 2 to 3 | on body |
| leg_fr | 10 to 11 | 5 to 6 | 2 to 3 | on body |

## Recognisable features (in order of importance)

1. huge bulging red eyes on top of the head of a squat, wide body (as wide as it is long)
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
