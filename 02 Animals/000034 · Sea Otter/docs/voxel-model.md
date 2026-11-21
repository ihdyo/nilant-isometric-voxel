# 000034 · Sea Otter · voxel brief

*Enhydra lutris* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#7B3306` | thick water-repellent dark brown body and flattened tail |
| `head` | `#E7E5E4` | characteristic pale silver-cream head, neck and whiskers |
| `paw` | `#171717` | mitten-like front paws and webbed hind flippers |
| `nose` | `#171717` | broad diamond-shaped black nose |
| `white` | `#FAFAF9` | eye sclera highlight |
| `eye` | `#1C1917` | dark round eyes |

Background (not modelled): `#A9E2D6` (soft mint).

## Size and pose

- Size: 38 × 14 × 15 voxels posed (L × W × H); longest side 38, budget 34–42 (target 38) from the real size 1.3 m (nose to tail tip, about 1.3 m (total length 1–1.5 m including 25–35 cm tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, flipper_hl, flipper_hr, body, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: playful and resourceful, cozy in the kelp beds.
- Pose: a low, sleek coastal waddle, short mitten-like front paws and wide webbed hind flippers, pale creamy head turned toward the viewer.
- Expression: round dark eyes, broad black nose and prominent cream whisker cheeks.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 17 to 19 | -4 to -2 | 0 to 3 | turned ry -10°; on body |
| leg_fr | 17 to 19 | 2 to 4 | 0 to 3 | turned ry +6°; on body |
| flipper_hl | 0 to 4 | -5 to -2 | 0 to 2 | turned ry +8°; on body |
| flipper_hr | 0 to 4 | 2 to 5 | 0 to 2 | on body |
| body | 2 to 20 | -4 to 4 | 3 to 10 |  |
| tail | -10 to 1 | -2 to 2 | 4 to 6 | turned ry +6°; on body |
| head | 19 to 26 | -4 to 4 | 6 to 13 | turned rx +4°, ry +3°, rz -10°; on body |
| ear_l | 20 to 21 | -4 to -3 | 13 to 14 | on head |
| ear_r | 20 to 21 | 3 to 4 | 13 to 14 | on head |

## Recognisable features (in order of importance)

1. pale silver-cream head contrasting with dark brown body
2. broad diamond-shaped black nose and thick whisker pads
3. short mitten-like front paws for holding rocks and prey
4. wide webbed hind flippers and flattened rudder tail
5. plush, dense fur coat

## Colour map

- `coat`: thick water-repellent dark brown body and flattened tail
- `head`: characteristic pale silver-cream head, neck and whiskers
- `paw`: mitten-like front paws and webbed hind flippers
- `nose`: broad diamond-shaped black nose
- `white`: eye sclera highlight
- `eye`: dark round eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult sea otter profile reference (CC BY 2.0)
