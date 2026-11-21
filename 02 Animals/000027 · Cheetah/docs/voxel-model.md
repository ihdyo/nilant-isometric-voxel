# 000027 · Cheetah · voxel brief

*Acinonyx jubatus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#FFD230` | slender body, head, long legs, ears and tail |
| `spot` | `#171717` | solid round spots across body, legs and tail rings |
| `belly` | `#FFFBEB` | throat, chest and underbelly |
| `tear` | `#1C1917` | characteristic black tear-tracks from eyes to mouth |
| `white` | `#FAFAF9` | the white of each eye and tail tip |
| `eye` | `#E17100` | amber pupils |

Background (not modelled): `#E0D5A8` (soft straw).

## Size and pose

- Size: 46 × 14 × 24 voxels posed (L × W × H); longest side 46, budget 42–50 (target 46) from the real size 2.1 m (nose to tail tip, about 2.1 m (body length 1.1–1.5 m plus 0.6–0.8 m tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: shin_fl, shin_fr, shin_hl, shin_hr, leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: alert and aerodynamic, built for pure speed.
- Pose: a long, athletic stride with deep chest, slender waist, long tail streaming behind and head lifted toward the horizon.
- Expression: focused amber eyes framed by bold black tear streaks.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| shin_fl | 19 to 21 | -4 to -2 | 0 to 5 | turned ry +18°; on leg_fl |
| shin_fr | 19 to 21 | 2 to 4 | 0 to 5 | on leg_fr |
| shin_hl | 2 to 4 | -4 to -2 | 0 to 5 | turned ry -14°; on leg_hl |
| shin_hr | 2 to 4 | 2 to 4 | 0 to 5 | on leg_hr |
| leg_fl | 19 to 21 | -4 to -2 | 6 to 11 | turned ry -16°; on body |
| leg_fr | 19 to 21 | 2 to 4 | 6 to 11 | turned ry +8°; on body |
| leg_hl | 2 to 4 | -4 to -2 | 6 to 11 | turned ry +12°; on body |
| leg_hr | 2 to 4 | 2 to 4 | 6 to 11 | on body |
| body | 1 to 23 | -4 to 4 | 11 to 18 |  |
| tail | -14 to 0 | -1 to 1 | 14 to 16 | turned ry +8°, rz -6°; on body |
| head | 22 to 29 | -4 to 4 | 16 to 23 | turned rx +3°, ry +2°, rz -8°; on body |
| ear_l | 23 to 24 | -4 to -3 | 24 to 25 | on head |
| ear_r | 23 to 24 | 3 to 4 | 24 to 25 | on head |

## Recognisable features (in order of importance)

1. bold black tear marks running from the eyes to the mouth
2. sleek golden coat covered in solid round black spots
3. aerodynamic deep chest and narrow waist
4. long, slender legs with semi-retractable claws
5. long ringed tail tipped with white

## Colour map

- `coat`: slender body, head, long legs, ears and tail
- `spot`: solid round spots across body, legs and tail rings
- `belly`: throat, chest and underbelly
- `tear`: characteristic black tear-tracks from eyes to mouth
- `white`: the white of each eye and tail tip
- `eye`: amber pupils

## Photos used

- `assets/photos/01-side-profile.jpg`: adult cheetah profile reference (CC BY-SA 4.0)
