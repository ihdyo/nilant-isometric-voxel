# 000063 · North American Beaver · voxel brief

*Castor canadensis* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#7B3306` | waterproof glossy chestnut-brown fur |
| `belly` | `#BB4D00` | softer underfur on cheeks and belly |
| `tail` | `#44403B` | broad flat leathery black-grey paddle tail |
| `tooth` | `#FF6900` | iron-enamel orange front incisors |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#171717` | the pupils and nose |

Background (not modelled): `#ADDCF5` (soft sky blue).

## Size and pose

- Size: 32 × 13 × 15 voxels rest (L × W × H); longest side 32, budget 48–56 (target 56) from the real size 1.1 m (total length, 0.9–1.2 m including flat tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, leg_hl, leg_fl, head.

## Personality, pose and expression

- Personality: industrious and cheerful, tireless woodland architect.
- Pose: a sturdy waddle, broad flat paddle tail resting behind, holding a birch twig.
- Expression: cheerful dark eyes, chubby cheeks and two prominent orange front teeth.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 9 to 24 | -6 to 6 | 2 to 14 |  |
| tail | 0 to 9 | -4 to 4 | 2 to 3 | turned ry +6°; on body |
| leg_hl | 11 to 15 | -6 to -3 | 0 to 3 | on body |
| leg_fl | 20 to 23 | -6 to -3 | 0 to 4 | on body |
| head | 23 to 31 | -5 to 5 | 4 to 14 | turned rx +4°, ry -4°, rz -8°; on body |

## Recognisable features (in order of importance)

1. the broad flat leathery paddle tail
2. the two bright orange chisel front teeth
3. the chunky chestnut waterproof body
4. the webbed hind feet and dexterous front paws
5. the small rounded ears

## Colour map

- `coat`: waterproof glossy chestnut-brown fur
- `belly`: softer underfur on cheeks and belly
- `tail`: broad flat leathery black-grey paddle tail
- `tooth`: iron-enamel orange front incisors
- `white`: the white of each eye
- `eye`: the pupils and nose

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
