# 000051 · Moose · voxel brief

*Alces alces* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#292524` | body, neck, head and humped shoulders |
| `antler` | `#FEF3C6` | broad palmate antlers |
| `leg` | `#D6D3D1` | long pale lower legs |
| `muzzle` | `#44403B` | overhanging bulbous snout and throat bell |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#171717` | the pupils and nostrils |

Background (not modelled): `#ADDCF5` (soft sky blue).

## Size and pose

- Size: 43 × 31 × 43 voxels rest (L × W × H); longest side 43, budget 48–56 (target 56) from the real size 2.9 m (head-and-body length, 2.4–3.1 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, shin_hl, leg_fl, shin_fl, tail, head, ear_l, antler_l, ear_r, antler_r.

## Personality, pose and expression

- Personality: dignified and tranquil, lord of the misty northern marsh.
- Pose: a high-stepping wade, broad palmate antlers tilted slightly forward, throat bell swaying.
- Expression: steady dark eyes under thick brow ridges and a long overhanging muzzle.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 2 to 26 | -7 to 7 | 17 to 33 |  |
| leg_hl | 3 to 6 | -6 to -3 | 9 to 16 | turned ry +8°; on body |
| shin_hl | 3 to 6 | -6 to -3 | 0 to 8 | on leg_hl |
| leg_fl | 21 to 24 | -6 to -3 | 9 to 16 | turned ry -10°; on body |
| shin_fl | 21 to 24 | -6 to -3 | 0 to 8 | on leg_fl |
| tail | 0 to 1 | -1 to 1 | 25 to 28 | turned rx -8°; on body |
| head | 26 to 42 | -5 to 5 | 17 to 33 | turned rx +4°, ry +5°, rz -8°; on body |
| ear_l | 27 to 29 | -7 to -5 | 33 to 37 | turned rz +18°; on head |
| antler_l | 28 to 36 | -15 to -4 | 34 to 42 | turned ry -6°, rz +10°; on head |
| ear_r | 27 to 29 | 5 to 7 | 33 to 37 | turned rz -18°; on head |
| antler_r | 28 to 36 | 4 to 15 | 34 to 42 | turned ry -6°, rz -10°; on head |

## Recognisable features (in order of importance)

1. the huge broad palmate antlers
2. the long overhanging snout and dangling throat bell
3. the tall humped shoulders
4. the very long pale lower legs
5. the stubby tail

## Colour map

- `coat`: body, neck, head and humped shoulders
- `antler`: broad palmate antlers
- `leg`: long pale lower legs
- `muzzle`: overhanging bulbous snout and throat bell
- `white`: the white of each eye
- `eye`: the pupils and nostrils

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
