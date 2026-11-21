# 000048 · Llama · voxel brief

*Lama glama* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#FEF3C6` | thick woolly cream fleece covering body, long neck and upper legs |
| `patch` | `#973C00` | warm chestnut-brown saddle patches on back and neck |
| `face` | `#44403B` | short-haired dark-grey muzzle, lower legs and inner ears |
| `pad` | `#57534D` | leathery two-toed foot pads |
| `white` | `#FAFAF9` | eye sclera highlight |
| `eye` | `#1C1917` | large dark long-lashed eyes |

Background (not modelled): `#C3B88C` (soft straw).

## Size and pose

- Size: 34 × 14 × 34 voxels posed (L × W × H); longest side 34, budget 30–38 (target 34) from the real size 1.8 m (standing height at head about 1.7–1.8 m (body 1.2–2.2 m plus 20–25 cm tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, neck, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: proud and composed, steady-footed pack companion of the high Andes.
- Pose: an upright, confident mountain stride, tall woolly neck held straight, curved banana-shaped ears perked and head angled toward the viewer.
- Expression: large dark eyes on a clean dark-grey muzzle with tall inward-curving ears.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 14 to 16 | -4 to -2 | 0 to 10 | turned ry -10°; on body |
| leg_fr | 14 to 16 | 2 to 4 | 0 to 10 | turned ry +5°; on body |
| leg_hl | 2 to 4 | -4 to -2 | 0 to 10 | turned ry +8°; on body |
| leg_hr | 2 to 4 | 2 to 4 | 0 to 10 | on body |
| body | 1 to 18 | -4 to 4 | 10 to 18 |  |
| neck | 13 to 18 | -3 to 3 | 18 to 28 | on body |
| tail | -1 to 0 | -1 to 1 | 14 to 17 | turned rx -12°; on body |
| head | 14 to 22 | -3 to 3 | 27 to 31 | turned rx +3°, ry +2°, rz -10°; on neck |
| ear_l | 15 to 17 | -3 to -2 | 31 to 35 | on head |
| ear_r | 15 to 17 | 2 to 3 | 31 to 35 | on head |

## Recognisable features (in order of importance)

1. tall vertical neck covered in fluffy cream-and-chestnut fleece
2. distinctive long banana-shaped ears
3. clean short-haired dark muzzle and slender lower legs
4. level back without humps
5. two-toed padded camelid feet

## Colour map

- `coat`: thick woolly cream fleece covering body, long neck and upper legs
- `patch`: warm chestnut-brown saddle patches on back and neck
- `face`: short-haired dark-grey muzzle, lower legs and inner ears
- `pad`: leathery two-toed foot pads
- `white`: eye sclera highlight
- `eye`: large dark long-lashed eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult llama profile reference (CC0)
