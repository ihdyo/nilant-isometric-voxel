# 000049 · Alpaca · voxel brief

*Vicugna pacos* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `fleece` | `#FAFAF9` | plush, cloud-like wool covering body, neck, legs and topknot |
| `shade` | `#FEF3C6` | warm cream shading under belly and neck |
| `face` | `#FEE685` | short-fleeced warm beige muzzle and inner ears |
| `nose` | `#44403B` | small dark cleft nose and padded toes |
| `white` | `#FAFAF9` | eye sclera highlight |
| `eye` | `#1C1917` | large round dark gentle eyes |

Background (not modelled): `#F1C5E0` (soft orchid).

## Size and pose

- Size: 30 × 14 × 30 voxels posed (L × W × H); longest side 30, budget 26–34 (target 30) from the real size 1.45 m (standing height at head about 1.4–1.5 m (body 1.2–1.5 m plus 15–20 cm tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, neck, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: sweet-natured and fluffy, bouncing gently across Andean meadows.
- Pose: a light, fluffy-coated stride, thick woolly neck and cloud-like body, short straight spear-shaped ears and topknot puff turned toward the camera.
- Expression: big soulful dark eyes peeking out from a fluffy wool crown and soft beige muzzle.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 12 to 14 | -4 to -2 | 0 to 8 | turned ry -10°; on body |
| leg_fr | 12 to 14 | 2 to 4 | 0 to 8 | turned ry +5°; on body |
| leg_hl | 2 to 4 | -4 to -2 | 0 to 8 | turned ry +8°; on body |
| leg_hr | 2 to 4 | 2 to 4 | 0 to 8 | on body |
| body | 1 to 16 | -5 to 5 | 8 to 16 |  |
| neck | 11 to 16 | -3 to 3 | 16 to 24 | on body |
| tail | -1 to 0 | -1 to 1 | 12 to 15 | turned rx -12°; on body |
| head | 12 to 19 | -3 to 3 | 23 to 28 | turned rx +3°, ry +2°, rz -10°; on neck |
| ear_l | 13 to 15 | -3 to -2 | 28 to 30 | on head |
| ear_r | 13 to 15 | 2 to 3 | 28 to 30 | on head |

## Recognisable features (in order of importance)

1. ultra-fluffy, cloud-like fleece covering body, legs and crown topknot
2. shorter, straight spear-shaped ears (distinct from llama's banana ears)
3. smaller, more compact frame than a llama
4. soft beige short-haired muzzle
5. fluffy stub tail

## Colour map

- `fleece`: plush, cloud-like wool covering body, neck, legs and topknot
- `shade`: warm cream shading under belly and neck
- `face`: short-fleeced warm beige muzzle and inner ears
- `nose`: small dark cleft nose and padded toes
- `white`: eye sclera highlight
- `eye`: large round dark gentle eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult alpaca profile reference (CC0)
