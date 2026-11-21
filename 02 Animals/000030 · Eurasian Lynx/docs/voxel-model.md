# 000030 · Eurasian Lynx · voxel brief

*Lynx lynx* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#D6D3D1` | body, head, long legs and outer ears |
| `tuft` | `#171717` | long black ear tufts, cheek-ruff tips and black tail tip |
| `ruff` | `#F5F5F4` | flared facial cheek ruff, chest and underbelly |
| `spot` | `#79716B` | subtle dark spots along flanks and limbs |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#FFB900` | yellow-amber pupils |

Background (not modelled): `#C7D2FD` (soft lavender).

## Size and pose

- Size: 34 × 15 × 26 voxels posed (L × W × H); longest side 34, budget 32–38 (target 34) from the real size 1.3 m (nose to tail tip, about 1.3 m (body 0.8–1.3 m plus short 11–24 cm bobbed tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: shin_fl, shin_fr, shin_hl, shin_hr, leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: keen-eared and poised, silent watcher of the northern woods.
- Pose: a tall, long-legged woodland stride, short black-tipped bobtail lifted slightly, tufted ears pricked forward.
- Expression: sharp golden eyes framed by flared white cheek ruffs.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| shin_fl | 17 to 19 | -4 to -2 | 0 to 5 | turned ry +12°; on leg_fl |
| shin_fr | 17 to 19 | 2 to 4 | 0 to 5 | on leg_fr |
| shin_hl | 3 to 5 | -4 to -2 | 0 to 5 | turned ry -8°; on leg_hl |
| shin_hr | 3 to 5 | 2 to 4 | 0 to 5 | on leg_hr |
| leg_fl | 17 to 19 | -4 to -2 | 6 to 10 | turned ry -10°; on body |
| leg_fr | 17 to 19 | 2 to 4 | 6 to 10 | turned ry +5°; on body |
| leg_hl | 3 to 5 | -4 to -2 | 6 to 10 | turned ry +8°; on body |
| leg_hr | 3 to 5 | 2 to 4 | 6 to 10 | on body |
| body | 2 to 20 | -4 to 4 | 10 to 18 |  |
| tail | -2 to 1 | -1 to 1 | 15 to 18 | turned ry -20°; on body |
| head | 19 to 26 | -5 to 5 | 14 to 22 | turned rx +4°, ry +3°, rz -10°; on body |
| ear_l | 21 to 23 | -4 to -3 | 22 to 26 | on head |
| ear_r | 21 to 23 | 3 to 4 | 22 to 26 | on head |

## Recognisable features (in order of importance)

1. tall triangular ears topped with long black tufts
2. flared facial cheek ruffs around the jaw
3. short, black-tipped bobbed tail
4. long, muscular hind legs built for bounding
5. large snowshoe-like paws

## Colour map

- `coat`: body, head, long legs and outer ears
- `tuft`: long black ear tufts, cheek-ruff tips and black tail tip
- `ruff`: flared facial cheek ruff, chest and underbelly
- `spot`: subtle dark spots along flanks and limbs
- `white`: the white of each eye
- `eye`: yellow-amber pupils

## Photos used

- `assets/photos/01-side-profile.jpg`: adult eurasian lynx profile reference (CC BY-SA 3.0)
