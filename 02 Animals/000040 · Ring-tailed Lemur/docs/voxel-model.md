# 000040 · Ring-tailed Lemur · voxel brief

*Lemur catta* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#A6A09B` | slender grey-brown back, shoulders and outer limbs |
| `black` | `#171717` | 13 alternating black tail rings, eye masks, crown and nose |
| `white` | `#FAFAF9` | 13 alternating white tail rings, face cheeks and ears |
| `belly` | `#F5F5F4` | white chest, throat and underbelly |
| `muzzle` | `#292524` | pointed dark-tipped snout |
| `eye` | `#FE9A00` | bright golden-amber eyes |

Background (not modelled): `#CCDBB0` (soft lime green).

## Size and pose

- Size: 28 × 12 × 30 voxels posed (L × W × H); longest side 30, budget 26–34 (target 30) from the real size 1.0 m (nose to tail tip, about 1.0 m (body 39–46 cm plus 56–63 cm ringed tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, tail_1, tail_2, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: lively and theatrical, waving its striped banner tail.
- Pose: an agile terrestrial strut with long hind legs, tall S-curved black-and-white ringed tail held high like a question mark, and face turned toward the viewer.
- Expression: bright golden-amber eyes ringed in black triangular eye masks on a crisp white face.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 11 to 13 | -3 to -2 | 0 to 6 | turned ry -12°; on body |
| leg_fr | 11 to 13 | 2 to 3 | 0 to 6 | turned ry +6°; on body |
| leg_hl | 2 to 4 | -3 to -2 | 0 to 8 | turned ry +10°; on body |
| leg_hr | 2 to 4 | 2 to 3 | 0 to 8 | on body |
| body | 1 to 14 | -3 to 3 | 6 to 12 |  |
| tail_1 | -2 to 0 | -1 to 1 | 11 to 22 | turned ry -8°; on body |
| tail_2 | -6 to -1 | -1 to 1 | 22 to 29 | turned ry -18°; on tail_1 |
| head | 13 to 19 | -3 to 3 | 10 to 16 | turned rx +4°, ry +3°, rz -10°; on body |
| ear_l | 14 to 15 | -3 to -2 | 16 to 18 | on head |
| ear_r | 14 to 15 | 2 to 3 | 16 to 18 | on head |

## Recognisable features (in order of importance)

1. extra-long tail with alternating black and white rings held aloft
2. black triangular eye patches and black snout on a white face
3. slender grey back with white chest and belly
4. long hind legs built for leaping
5. white triangular ears

## Colour map

- `coat`: slender grey-brown back, shoulders and outer limbs
- `black`: 13 alternating black tail rings, eye masks, crown and nose
- `white`: 13 alternating white tail rings, face cheeks and ears
- `belly`: white chest, throat and underbelly
- `muzzle`: pointed dark-tipped snout
- `eye`: bright golden-amber eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult ring-tailed lemur profile reference (CC BY 4.0)
