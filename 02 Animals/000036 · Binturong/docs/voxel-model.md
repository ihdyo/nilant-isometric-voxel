# 000036 · Binturong · voxel brief

*Arctictis binturong* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#292524` | shaggy body, thick prehensile tail, short legs and head |
| `frost` | `#A6A09B` | silver-grey frosted guard hairs across shoulders, head and flanks |
| `ear` | `#F5F5F4` | white-rimmed rounded ears with long dark ear tufts |
| `muzzle` | `#79716B` | grizzled grey-brown muzzle and long white whiskers |
| `white` | `#FAFAF9` | eye sclera highlight |
| `eye` | `#BB4D00` | warm reddish-brown pupils |

Background (not modelled): `#B5E1C4` (soft leaf green).

## Size and pose

- Size: 44 × 14 × 17 voxels posed (L × W × H); longest side 44, budget 40–48 (target 44) from the real size 1.65 m (nose to tail tip, about 1.65 m (body 61–96 cm plus thick prehensile tail 56–89 cm per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, tail_1, tail_2, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: unhurried and mellow, ambling along high rainforest boughs.
- Pose: a low, heavy-footed arboreal walk, thick muscular prehensile tail curling at the tip, frosted head turned toward the viewer.
- Expression: warm amber-brown eyes, silver-frosted face and white-edged tufted ears.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 16 to 18 | -4 to -2 | 0 to 4 | turned ry -10°; on body |
| leg_fr | 16 to 18 | 2 to 4 | 0 to 4 | turned ry +6°; on body |
| leg_hl | 2 to 4 | -4 to -2 | 0 to 4 | turned ry +8°; on body |
| leg_hr | 2 to 4 | 2 to 4 | 0 to 4 | on body |
| body | 1 to 21 | -4 to 4 | 4 to 11 |  |
| tail_1 | -8 to 0 | -2 to 2 | 6 to 9 | turned ry +10°; on body |
| tail_2 | -16 to -9 | -1 to 1 | 5 to 7 | turned ry -28°, rz -12°; on tail_1 |
| head | 20 to 27 | -4 to 4 | 7 to 14 | turned rx +4°, ry +3°, rz -10°; on body |
| ear_l | 21 to 22 | -4 to -3 | 14 to 16 | on head |
| ear_r | 21 to 22 | 3 to 4 | 14 to 16 | on head |

## Recognisable features (in order of importance)

1. long, muscular, thick-based prehensile tail curled at the tip
2. shaggy black coat frosted with silver-grey guard hairs
3. white-rimmed rounded ears with long black hair tufts
4. short, sturdy legs with broad plantigrade paws
5. grizzled pale muzzle

## Colour map

- `coat`: shaggy body, thick prehensile tail, short legs and head
- `frost`: silver-grey frosted guard hairs across shoulders, head and flanks
- `ear`: white-rimmed rounded ears with long dark ear tufts
- `muzzle`: grizzled grey-brown muzzle and long white whiskers
- `white`: eye sclera highlight
- `eye`: warm reddish-brown pupils

## Photos used

- `assets/photos/01-side-profile.jpg`: adult binturong profile reference (CC BY 3.0)
