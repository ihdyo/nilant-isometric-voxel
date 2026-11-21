# 000024 · Red-eyed Tree Frog · voxel brief

*Agalychnis callidryas* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `green` | `#00C950` | the back, the head and the legs |
| `red` | `#FB2C36` | the big eyes |
| `blue` | `#155DFC` | the flanks and the inner legs |
| `yellow` | `#FFD230` | the stripes on the flanks |
| `toe` | `#FF8904` | the hands, the feet and the toe pads |
| `belly` | `#FAFAF9` | the belly and the throat |
| `pupil` | `#0A0A0A` | the pupils and the smile |

Background (not modelled): `#F4C5DA` (orchid pink).

## Size and pose

- Size: 18 × 15 × 11 voxels posed (L × W × H); longest side 18, budget 16–18 (target 16) from the real size 0.07 m (snout to vent: 4–7 cm, females larger).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, head, leg_fl, leg_hl, shin_hl, leg_fr, leg_hr, shin_hr.

## Personality, pose and expression

- Personality: a cheeky, bright-eyed show-off.
- Pose: Sitting low and squat, ready to jump: each hind leg two flat boards hinged at the knee like a clapperboard (the thigh on the flank, set into the body with one voxel showing, hinged inside; the lower leg with the long orange foot folded under it), short front arms in one piece with the orange hands spread, the head turned to the camera and a little up.
- Expression: huge red eyes bulging on top with a black pupil, and a wide grin across the front, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 8 | -4 to 4 | 1 to 6 |  |
| head | 9 to 13 | -4 to 4 | 2 to 9 | turned rx +3°, ry -6°, rz -14°; on body |
| leg_fl | 9 to 12 | -7 to -5 | 0 to 3 | on body |
| leg_hl | 0 to 5 | -5 to -4 | 2 to 5 | on body |
| shin_hl | -3 to 5 | -6 to -4 | 0 to 1 | on leg_hl |
| leg_fr | 9 to 12 | 5 to 7 | 0 to 3 | on body |
| leg_hr | 0 to 5 | 4 to 5 | 2 to 5 | on body |
| shin_hr | -3 to 5 | 4 to 6 | 0 to 1 | on leg_hr |

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
