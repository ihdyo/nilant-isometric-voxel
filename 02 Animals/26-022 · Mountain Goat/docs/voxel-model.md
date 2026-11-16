# 26-022 · Mountain Goat · voxel brief

*Oreamnos americanus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (Tailwind token or #hex) | Where |
|---|---|---|
| `coat` | `stone-50` | the shaggy white coat |
| `shade` | `stone-200` | the beard, the shoulder hump and the leg shading |
| `horn` | `neutral-900` | the horns, the hooves, the eyes and the mouth |
| `nose` | `stone-700` | the nose |

Background (not modelled): `violet-300` (rendered as a calm pastel).

## Size and pose

- Size: 31 × 13 × 29 voxels posed (L × W × H); longest side 31, budget 28–38 (target 33) from the real size 1.5 m (nose to tail: 1.25–1.79 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: shin_fl, shin_fr, shin_hl, shin_hr, leg_fl, leg_fr, leg_hl, leg_hr, body, head, muzzle, ear_l, ear_r, horn_l, horn_r.

## Personality, pose and expression

- Personality: brave, sure-footed and a bit stubborn.
- Pose: standing square with one front hoof raised as if stepping up a ledge, the bearded chin lifted, the head turned to the camera.
- Expression: calm dark eyes under a level brow and a small smile, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| shin_fl | 14 to 17 | -5 to -2 | 0 to 5 | turned ry +34°; on leg_fl |
| shin_fr | 14 to 17 | 2 to 5 | 0 to 5 | on leg_fr |
| shin_hl | 2 to 5 | -5 to -2 | 0 to 5 | on leg_hl |
| shin_hr | 2 to 5 | 2 to 5 | 0 to 5 | on leg_hr |
| leg_fl | 14 to 17 | -5 to -2 | 6 to 10 | turned ry -30°; on body |
| leg_fr | 14 to 17 | 2 to 5 | 6 to 10 | on body |
| leg_hl | 2 to 5 | -5 to -2 | 6 to 10 | on body |
| leg_hr | 2 to 5 | 2 to 5 | 6 to 10 | on body |
| body | -1 to 19 | -6 to 6 | 11 to 22 |  |
| head | 19 to 25 | -3 to 3 | 13 to 23 | turned rx +6°, ry -10°, rz -18°; on body |
| muzzle | 26 to 28 | -2 to 2 | 17 to 20 | on head |
| ear_l | 20 to 21 | -5 to -4 | 22 to 23 | turned rx +14°; on head |
| ear_r | 20 to 21 | 4 to 5 | 22 to 23 | turned rx -14°; on head |
| horn_l | 20 to 21 | -3 to -2 | 24 to 28 | turned rx +6°, ry -22°; on head |
| horn_r | 20 to 21 | 2 to 3 | 24 to 28 | turned rx -6°, ry -22°; on head |

## Recognisable features (in order of importance)

1. the shaggy white coat
2. short black dagger horns
3. a white beard
4. black hooves
5. a hump of thick fur at the shoulders

## Colour map

- `coat`: the shaggy white coat
- `shade`: the beard, the shoulder hump and the leg shading
- `horn`: the horns, the hooves, the eyes and the mouth
- `nose`: the nose

## Photos used

- `assets/photos/01-lying.jpg`: an adult billy lying on a mountain ridge, horns, beard and shaggy coat (Public domain)
- `assets/photos/02-face.jpg`: a young goat's face close up (Public domain)
