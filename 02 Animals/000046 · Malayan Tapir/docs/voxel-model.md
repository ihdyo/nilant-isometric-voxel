# 000046 · Malayan Tapir · voxel brief

*Tapirus indicus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `dark` | `#171717` | jet-black head, neck, shoulders, front legs, hind legs and rump |
| `saddle` | `#FAFAF9` | crisp white-grey blanket wrapping the middle torso |
| `ear` | `#FAFAF9` | characteristic white tips on the rounded black ears |
| `nail` | `#E7E5E4` | four front and three hind pale hooves |
| `white` | `#FAFAF9` | eye sclera highlight |
| `eye` | `#1C1917` | small dark gentle eyes |

Background (not modelled): `#A9E2D6` (soft mint).

## Size and pose

- Size: 42 × 16 × 22 voxels posed (L × W × H); longest side 42, budget 38–46 (target 42) from the real size 2.3 m (snout tip to tail tip, about 2.3 m (body 1.8–2.5 m plus 5–10 cm stubby tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, snout, ear_l, ear_r.

## Personality, pose and expression

- Personality: gentle and shy, nocturnal browser of misty jungle trails.
- Pose: a steady forest walk, iconic white midsection saddle contrasting with jet-black shoulders and rump, flexible proboscis snout probing forward.
- Expression: gentle dark eyes, white-tipped rounded ears and a short flexible trunk-snout.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 18 to 20 | -5 to -2 | 0 to 7 | turned ry -10°; on body |
| leg_fr | 18 to 20 | 2 to 5 | 0 to 7 | turned ry +5°; on body |
| leg_hl | 2 to 4 | -5 to -2 | 0 to 7 | turned ry +8°; on body |
| leg_hr | 2 to 4 | 2 to 5 | 0 to 7 | on body |
| body | 0 to 23 | -6 to 6 | 7 to 19 |  |
| tail | -1 to 0 | -1 to 1 | 12 to 14 | on body |
| head | 22 to 31 | -4 to 4 | 10 to 18 | turned rx +4°, ry +4°, rz -10°; on body |
| snout | 31 to 34 | -2 to 2 | 10 to 13 | turned ry +16°; on head |
| ear_l | 23 to 24 | -4 to -3 | 18 to 20 | on head |
| ear_r | 23 to 24 | 3 to 4 | 18 to 20 | on head |

## Recognisable features (in order of importance)

1. high-contrast white saddle wrapping the middle body between black forequarters and hindquarters
2. short, flexible, prehensile proboscis snout
3. black rounded ears edged with bright white tips
4. plump, rounded torso sloping forward
5. sturdy black legs with pale hoof nails

## Colour map

- `dark`: jet-black head, neck, shoulders, front legs, hind legs and rump
- `saddle`: crisp white-grey blanket wrapping the middle torso
- `ear`: characteristic white tips on the rounded black ears
- `nail`: four front and three hind pale hooves
- `white`: eye sclera highlight
- `eye`: small dark gentle eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult malayan tapir profile reference (CC BY 4.0)
