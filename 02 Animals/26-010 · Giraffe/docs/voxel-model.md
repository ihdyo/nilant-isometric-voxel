# 26-010 · Giraffe · voxel brief

*Giraffa camelopardalis* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `patch` | `amber-700` | patches on the body, neck, upper legs and head |
| `base` | `amber-100` | the cream network between patches, lower legs, head |
| `mane` | `amber-800` | the mane along the back of the neck |
| `dark` | `stone-800` | hooves, ossicone tufts, tail tuft |
| `eye` | `neutral-950` | one voxel on each front corner of the head (seen from the front and the flank) |

Background (not modelled): `sky-300`.

## Size and pose

- Size: 28 × 11 × 55 voxels posed (L × W × H); longest side 55, budget 45–56 (target 53) from the real size 5.0 m (height to the ossicones: up to 5.7 m, a typical adult about 5 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: shin_fl, shin_fr, shin_hl, shin_hr, leg_fl, leg_fr, leg_hl, leg_hr, tail, body, neck, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: gentle, curious and a little goofy.
- Pose: the long neck leaning forward and turned to the camera, the head cocked, ears out, the tail swishing.
- Expression: big friendly dark eyes with a cream glint under a row of long lashes, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| shin_fl | 13 to 15 | -4 to -2 | 0 to 9 | turned ry +18°; on leg_fl |
| shin_fr | 13 to 15 | 2 to 4 | 0 to 9 | on leg_fr |
| shin_hl | 1 to 3 | -4 to -2 | 0 to 9 | on leg_hl |
| shin_hr | 1 to 3 | 2 to 4 | 0 to 9 | turned ry -10°; on leg_hr |
| leg_fl | 13 to 15 | -4 to -2 | 10 to 19 | turned ry -8°; on body |
| leg_fr | 13 to 15 | 2 to 4 | 10 to 19 | on body |
| leg_hl | 1 to 3 | -4 to -2 | 10 to 19 | on body |
| leg_hr | 1 to 3 | 2 to 4 | 10 to 19 | turned ry +6°; on body |
| tail | -1 to -1 | -1 to 1 | 19 to 28 | turned rx -16°; on body |
| body | 0 to 16 | -4 to 4 | 20 to 31 |  |
| neck | 11 to 16 | -2 to 2 | 32 to 45 | turned ry +10°, rz -8°; on body |
| head | 12 to 23 | -3 to 3 | 46 to 54 | turned rx +14°, ry +6°; on neck |
| ear_l | 15 to 17 | -4 to -4 | 49 to 50 | turned rx +20°; on head |
| ear_r | 15 to 17 | 4 to 4 | 49 to 50 | turned rx -20°; on head |

## Recognisable features (in order of importance)

1. the very long neck
2. long legs, the body high at the shoulders
3. square brown patches separated by cream lines
4. the ossicones with dark tufts on top of the head
5. the short dark mane along the back of the neck

## Colour map

- `patch`: patches on the body, neck, upper legs and head
- `base`: the cream network between patches, lower legs, head
- `mane`: the mane along the back of the neck
- `dark`: hooves, ossicone tufts, tail tuft
- `eye`: one voxel on each front corner of the head (seen from the front and the flank)

## Photos used

- `assets/photos/01-standing.jpg`: adult standing, full body, patches (CC BY 2.0)
- `assets/photos/02-head.jpg`: head, ossicones, neck pattern (CC0)
