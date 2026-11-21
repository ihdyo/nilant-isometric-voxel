# 000068 · Common Kingfisher · voxel brief

*Alcedo atthis* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `back` | `#00B8DB` | electric turquoise-blue back, crown and wings |
| `belly` | `#FF6900` | vivid rufous-orange chest, belly and ear patches |
| `throat` | `#FAFAF9` | crisp white throat and neck patches |
| `beak` | `#171717` | long straight dagger-like black beak |
| `foot` | `#FB2C36` | tiny bright coral-red feet |

Background (not modelled): `#AAE2D5` (soft mint).

## Size and pose

- Size: 20 × 7 × 18 voxels rest (L × W × H); longest side 20, budget 48–56 (target 56) from the real size 0.17 m (body length 16–17 cm; wingspan 24–26 cm).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, leg_l, head, leg_r.

## Personality, pose and expression

- Personality: focused and vibrant, a living sapphire darting over the stream.
- Pose: perched intently on an overhanging twig, body compact, long dagger beak aimed slightly down.
- Expression: sharp dark eyes locked onto the water surface below.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 3 to 12 | -3 to 3 | 3 to 11 |  |
| tail | 1 to 4 | -2 to 2 | 2 to 4 | turned ry +16°; on body |
| leg_l | 6 to 8 | -2 to -1 | 0 to 3 | on body |
| head | 5 to 20 | -3 to 3 | 11 to 17 | turned rx +3°, ry +12°, rz -10°; on body |
| leg_r | 6 to 8 | 1 to 2 | 0 to 3 | on body |

## Recognisable features (in order of importance)

1. the long straight dagger-like black beak
2. the dazzling turquoise-blue crown, back and wings
3. the vivid rufous-orange belly and cheek patch
4. the crisp white throat and neck spots
5. the tiny bright coral-red feet

## Colour map

- `back`: electric turquoise-blue back, crown and wings
- `belly`: vivid rufous-orange chest, belly and ear patches
- `throat`: crisp white throat and neck patches
- `beak`: long straight dagger-like black beak
- `foot`: tiny bright coral-red feet

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
