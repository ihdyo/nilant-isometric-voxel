# 000044 · White Rhinoceros · voxel brief

*Ceratotherium simum* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#A6A09B` | massive barrel body, neck hump, square-lipped head and pillar legs |
| `shade` | `#79716B` | heavy skin folds around shoulders, thighs and inner ears |
| `horn` | `#FFFBEB` | long front keratin horn and shorter rear horn |
| `nail` | `#E7E5E4` | three broad pale toenails on each foot |
| `white` | `#FAFAF9` | eye sclera highlight |
| `eye` | `#171717` | small dark steady eyes |

Background (not modelled): `#BAD7FC` (soft periwinkle).

## Size and pose

- Size: 48 × 18 × 26 voxels posed (L × W × H); longest side 48, budget 44–52 (target 48) from the real size 4.2 m (lip to tail tip, about 4.2 m (body 3.4–4.2 m plus 50–70 cm tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, horn_1, horn_2, ear_l, ear_r.

## Personality, pose and expression

- Personality: stoic and peaceful, gentle giant of the short-grass plains.
- Pose: a heavy, unhurried grazing stride, massive nuchal hump prominent behind the low-slung square-lipped head, twin horns sweeping upward.
- Expression: calm dark eyes set low on a long rectangular head with tubular ears turned forward.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 20 to 24 | -6 to -3 | 0 to 9 | turned ry -10°; on body |
| leg_fr | 20 to 24 | 3 to 6 | 0 to 9 | turned ry +5°; on body |
| leg_hl | 2 to 6 | -6 to -3 | 0 to 9 | turned ry +8°; on body |
| leg_hr | 2 to 6 | 3 to 6 | 0 to 9 | on body |
| body | 0 to 26 | -7 to 7 | 9 to 23 |  |
| tail | -2 to 0 | -1 to 1 | 13 to 19 | turned rx -10°; on body |
| head | 25 to 38 | -5 to 5 | 8 to 19 | turned rx +4°, ry +5°, rz -8°; on body |
| horn_1 | 35 to 37 | -1 to 1 | 19 to 26 | turned ry +10°; on head |
| horn_2 | 31 to 33 | -1 to 1 | 19 to 22 | on head |
| ear_l | 26 to 28 | -5 to -4 | 19 to 22 | on head |
| ear_r | 26 to 28 | 4 to 5 | 19 to 22 | on head |

## Recognisable features (in order of importance)

1. two keratin horns on the snout (long front horn, shorter rear horn)
2. distinctive muscular nuchal hump behind the head
3. wide, flat, square grazing lip
4. massive barrel body with vertical skin folds
5. four thick pillar legs with pale toenails

## Colour map

- `skin`: massive barrel body, neck hump, square-lipped head and pillar legs
- `shade`: heavy skin folds around shoulders, thighs and inner ears
- `horn`: long front keratin horn and shorter rear horn
- `nail`: three broad pale toenails on each foot
- `white`: eye sclera highlight
- `eye`: small dark steady eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult white rhinoceros profile reference (CC BY 4.0)
