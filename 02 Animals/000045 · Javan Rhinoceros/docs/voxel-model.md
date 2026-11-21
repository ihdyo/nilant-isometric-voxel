# 000045 · Javan Rhinoceros · voxel brief

*Rhinoceros sondaicus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#A6A09B` | dusky grey mosaic-textured skin plates on torso, head and legs |
| `fold` | `#57534D` | deep armor-like skin folds across neck, shoulders, back and rump |
| `horn` | `#FEF3C6` | single short horn on adult males |
| `nail` | `#E7E5E4` | three pale toenails per foot |
| `white` | `#FAFAF9` | eye sclera highlight |
| `eye` | `#171717` | small dark eyes |

Background (not modelled): `#B1E1C9` (soft mint).

## Size and pose

- Size: 42 × 16 × 23 voxels posed (L × W × H); longest side 42, budget 38–46 (target 42) from the real size 3.5 m (lip to tail tip, about 3.5 m (body 3.1–3.2 m plus 60–70 cm tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, horn, ear_l, ear_r.

## Personality, pose and expression

- Personality: quiet and elusive, ancient forest wanderer of Ujung Kulon.
- Pose: a steady rainforest stride, distinctive saddle-like armor skin folds carved across shoulders and rump, single short horn on the pointed-lip head.
- Expression: calm dark eyes, pointed prehensile upper lip and erect rounded ears.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 17 to 20 | -5 to -2 | 0 to 8 | turned ry -10°; on body |
| leg_fr | 17 to 20 | 2 to 5 | 0 to 8 | turned ry +5°; on body |
| leg_hl | 2 to 5 | -5 to -2 | 0 to 8 | turned ry +8°; on body |
| leg_hr | 2 to 5 | 2 to 5 | 0 to 8 | on body |
| body | 0 to 23 | -6 to 6 | 8 to 20 |  |
| tail | -2 to 0 | -1 to 1 | 11 to 17 | turned rx -10°; on body |
| head | 22 to 33 | -4 to 4 | 9 to 18 | turned rx +4°, ry +3°, rz -8°; on body |
| horn | 30 to 32 | -1 to 1 | 18 to 22 | turned ry +12°; on head |
| ear_l | 23 to 24 | -4 to -3 | 18 to 21 | on head |
| ear_r | 23 to 24 | 3 to 4 | 18 to 21 | on head |

## Recognisable features (in order of importance)

1. deep armor-like skin folds forming a saddle over the shoulders and back
2. single short keratin horn (unlike two-horned African rhinos)
3. pointed, prehensile upper lip for browsing forest twigs
4. sturdy pillar legs with three pale toenails
5. dusky slate-grey skin

## Colour map

- `skin`: dusky grey mosaic-textured skin plates on torso, head and legs
- `fold`: deep armor-like skin folds across neck, shoulders, back and rump
- `horn`: single short horn on adult males
- `nail`: three pale toenails per foot
- `white`: eye sclera highlight
- `eye`: small dark eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult javan rhinoceros profile reference (CC BY 3.0)
