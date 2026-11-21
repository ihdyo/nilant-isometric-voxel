# 000028 · Jaguar · voxel brief

*Panthera onca* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#FFB900` | stocky muscular body, broad head, legs, ears and tail |
| `rosette` | `#171717` | large black rosettes with central spots across coat |
| `belly` | `#FFFBEB` | chin, throat, chest and underbelly |
| `muzzle` | `#FEE685` | broad jaw and whisker pads |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#FE9A00` | golden-amber pupils |

Background (not modelled): `#EECEAA` (soft sand).

## Size and pose

- Size: 42 × 16 × 23 voxels posed (L × W × H); longest side 42, budget 38–46 (target 42) from the real size 2.3 m (nose to tail tip, about 2.3 m for a large adult (body 1.1–1.85 m plus 0.45–0.75 m tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: shin_fl, shin_fr, shin_hl, shin_hr, leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: powerful and unhurried, sovereign of river and forest.
- Pose: a heavy, confident jungle walk, broad shoulders rolling, sturdy tail curving down and wide head angled toward the camera.
- Expression: steady golden-amber eyes, powerful jaw and alert rounded ears.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| shin_fl | 17 to 20 | -5 to -2 | 0 to 4 | turned ry +12°; on leg_fl |
| shin_fr | 17 to 20 | 2 to 5 | 0 to 4 | on leg_fr |
| shin_hl | 2 to 5 | -5 to -2 | 0 to 4 | turned ry -8°; on leg_hl |
| shin_hr | 2 to 5 | 2 to 5 | 0 to 4 | on leg_hr |
| leg_fl | 17 to 20 | -5 to -2 | 5 to 9 | turned ry -10°; on body |
| leg_fr | 17 to 20 | 2 to 5 | 5 to 9 | turned ry +5°; on body |
| leg_hl | 2 to 5 | -5 to -2 | 5 to 9 | turned ry +8°; on body |
| leg_hr | 2 to 5 | 2 to 5 | 5 to 9 | on body |
| body | 1 to 22 | -5 to 5 | 9 to 18 |  |
| tail | -11 to 0 | -1 to 1 | 12 to 14 | turned ry +16°, rz -8°; on body |
| head | 21 to 29 | -5 to 5 | 13 to 22 | turned rx +4°, ry +3°, rz -10°; on body |
| ear_l | 23 to 24 | -5 to -3 | 22 to 23 | on head |
| ear_r | 23 to 24 | 3 to 5 | 22 to 23 | on head |

## Recognisable features (in order of importance)

1. broad, muscular head and heavy jaw
2. golden-orange coat marked with large dark rosettes enclosing spots
3. compact, stocky torso and thick muscular legs
4. shorter, sturdy tail compared to a leopard
5. pale cream chest and underbelly

## Colour map

- `coat`: stocky muscular body, broad head, legs, ears and tail
- `rosette`: large black rosettes with central spots across coat
- `belly`: chin, throat, chest and underbelly
- `muzzle`: broad jaw and whisker pads
- `white`: the white of each eye
- `eye`: golden-amber pupils

## Photos used

- `assets/photos/01-side-profile.jpg`: adult jaguar profile reference (CC BY-SA 4.0)
