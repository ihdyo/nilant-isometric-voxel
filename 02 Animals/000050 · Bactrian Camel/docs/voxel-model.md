# 000050 · Bactrian Camel · voxel brief

*Camelus bactrianus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#973C00` | body, neck, head, legs and twin humps |
| `shag` | `#461901` | thick winter mane under the throat, shoulders and hump tips |
| `muzzle` | `#FEE685` | split upper lip, inner ears and foot pads |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#171717` | the pupils, long lashes and nostrils |

Background (not modelled): `#EECEAA` (soft sand).

## Size and pose

- Size: 43 × 16 × 40 voxels rest (L × W × H); longest side 43, budget 48–56 (target 56) from the real size 3.2 m (head-and-body length, 2.25–3.5 m plus tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, shin_hl, leg_fl, shin_fl, tail, neck, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: steadfast and unhurried, a seasoned desert navigator.
- Pose: a measured desert stride, neck dipped and raised proudly, twin humps standing tall.
- Expression: calm half-lidded eyes with long lashes and a gentle closed-mouth smile.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 2 to 26 | -7 to 7 | 16 to 39 |  |
| leg_hl | 3 to 6 | -7 to -4 | 8 to 15 | turned ry +10°; on body |
| shin_hl | 3 to 7 | -8 to -3 | 0 to 7 | on leg_hl |
| leg_fl | 21 to 24 | -7 to -4 | 8 to 15 | turned ry -12°; on body |
| shin_fl | 21 to 25 | -8 to -3 | 0 to 7 | turned ry +14°; on leg_fl |
| tail | 0 to 1 | -1 to 1 | 15 to 26 | turned rx -10°; on body |
| neck | 25 to 32 | -5 to 5 | 13 to 29 | turned ry -14°; on body |
| head | 29 to 42 | -4 to 4 | 28 to 35 | turned rx +4°, ry +6°, rz -8°; on neck |
| ear_l | 30 to 32 | -5 to -4 | 35 to 37 | turned rz +12°; on head |
| ear_r | 30 to 32 | 4 to 5 | 35 to 37 | turned rz -12°; on head |

## Recognisable features (in order of importance)

1. the two tall dorsal humps
2. the curved S-shaped neck and shaggy throat mane
3. the split upper lip and long eyelashes
4. four sturdy legs with broad padded feet
5. the tufted tail

## Colour map

- `coat`: body, neck, head, legs and twin humps
- `shag`: thick winter mane under the throat, shoulders and hump tips
- `muzzle`: split upper lip, inner ears and foot pads
- `white`: the white of each eye
- `eye`: the pupils, long lashes and nostrils

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
