# 000065 · Snowy Owl · voxel brief

*Bubo scandiacus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `plumage` | `#FAFAF9` | thick snow-white plumage across head, body and feathered feet |
| `bar` | `#57534D` | dark brown crescent bars on wings and flanks |
| `beak` | `#171717` | curved black beak partially tucked in facial feathers |
| `iris` | `#FFB900` | piercing golden-yellow eyes |
| `eye` | `#171717` | large black pupils |

Background (not modelled): `#BAD7FC` (soft periwinkle).

## Size and pose

- Size: 16 × 13 × 26 voxels rest (L × W × H); longest side 26, budget 48–56 (target 56) from the real size 0.65 m (body length 52–71 cm; wingspan 1.25–1.5 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, wing_l, tail, leg_l, head, wing_r, leg_r.

## Personality, pose and expression

- Personality: serene and watchful, silent ghost of the Arctic tundra.
- Pose: a poised upright perch, round head swivelled toward the camera, feathered toes gripping.
- Expression: huge glowing golden eyes framed by a fluffy white facial disc.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 3 to 13 | -5 to 5 | 4 to 17 |  |
| wing_l | 3 to 11 | -6 to -5 | 3 to 16 | on body |
| tail | 0 to 4 | -3 to 3 | 2 to 6 | turned ry +12°; on body |
| leg_l | 7 to 10 | -4 to -2 | 0 to 4 | on body |
| head | 4 to 15 | -5 to 5 | 17 to 25 | turned rx +5°, rz -16°; on body |
| wing_r | 3 to 11 | 5 to 6 | 3 to 16 | on body |
| leg_r | 7 to 10 | 2 to 4 | 0 to 4 | on body |

## Recognisable features (in order of importance)

1. the round snow-white head without ear tufts
2. the bright golden-yellow eyes
3. the white plumage with subtle dark barring on the wings
4. the densely feathered snow-boot feet
5. the neat black beak

## Colour map

- `plumage`: thick snow-white plumage across head, body and feathered feet
- `bar`: dark brown crescent bars on wings and flanks
- `beak`: curved black beak partially tucked in facial feathers
- `iris`: piercing golden-yellow eyes
- `eye`: large black pupils

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
