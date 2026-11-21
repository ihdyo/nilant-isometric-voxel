# 000010 · Giraffe · voxel brief

*Giraffa camelopardalis* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour | Where |
|---|---|---|
| `patch` | `#BB4D00` | patches on the body, neck, upper legs and head |
| `base` | `#FEF3C6` | the cream network between patches, lower legs, head |
| `mane` | `#973C00` | the mane along the back of the neck |
| `dark` | `#292524` | hooves, ossicone tufts, tail tuft |
| `eye` | `#0A0A0A` | one voxel on each front corner of the head (seen from the front and the flank) |

Background (not modelled): `#AADDF2` (savanna-sky blue).

## Size and pose

- Size: 33 × 10 × 55 voxels posed (L × W × H); longest side 55, budget 45–56 (target 53) from the real size 5.0 m (height to the ossicones: up to 5.7 m, a typical adult about 5 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_hl, shin_hl, leg_fl, shin_fl, body, neck, tail, head, ear_l, leg_hr, shin_hr, leg_fr, shin_fr, ear_r.

## Personality, pose and expression

- Personality: gentle, curious and a little goofy.
- Pose: Mid-stride, the long neck leaning forward and a little away, the head level and turned to the camera, the tail swinging out behind the rump.
- Expression: big friendly dark eyes with a cream glint under a row of long lashes, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_hl | 1 to 3 | -4 to -2 | 10 to 19 | turned ry +12°; on body |
| shin_hl | 1 to 3 | -4 to -2 | 0 to 9 | turned ry -10°; on leg_hl |
| leg_fl | 13 to 15 | -4 to -2 | 10 to 19 | turned ry -16°; on body |
| shin_fl | 13 to 15 | -4 to -2 | 0 to 9 | turned ry +26°; on leg_fl |
| body | 0 to 16 | -4 to 4 | 20 to 31 |  |
| neck | 11 to 16 | -2 to 2 | 32 to 45 | turned ry +10°; on body |
| tail | -1 to -1 | -1 to 1 | 19 to 28 | turned rx -24°, ry +30°; on body |
| head | 12 to 23 | -3 to 3 | 46 to 54 | turned rx +3°, ry -6°, rz -14°; on neck |
| ear_l | 15 to 17 | -4 to -4 | 49 to 50 | turned rx +20°; on head |
| leg_hr | 1 to 3 | 2 to 4 | 10 to 19 | turned ry -10°; on body |
| shin_hr | 1 to 3 | 2 to 4 | 0 to 9 | on leg_hr |
| leg_fr | 13 to 15 | 2 to 4 | 10 to 19 | turned ry +10°; on body |
| shin_fr | 13 to 15 | 2 to 4 | 0 to 9 | on leg_fr |
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
