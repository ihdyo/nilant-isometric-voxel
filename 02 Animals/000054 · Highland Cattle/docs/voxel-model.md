# 000054 · Highland Cattle · voxel brief

*Bos taurus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#CA3500` | long wavy ginger-red double coat |
| `fringe` | `#F54900` | shaggy forehead fringe (dossan) hanging over the eyes |
| `horn` | `#FEF3C6` | long wide-sweeping pale horns with dark tips |
| `muzzle` | `#FEE685` | broad wet pale nose and hooves |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#171717` | the pupils |

Background (not modelled): `#F0CDAB` (soft sand).

## Size and pose

- Size: 36 × 25 × 27 voxels rest (L × W × H); longest side 36, budget 48–56 (target 56) from the real size 2.4 m (head-and-body length, 2.0–2.5 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, shin_hl, leg_fl, shin_fl, tail, head, horn_l, horn_r.

## Personality, pose and expression

- Personality: gentle and cozy, unbothered by Scottish drizzle.
- Pose: a relaxed pasture stroll, head tilted slightly so one eye peeks out from under the fringe.
- Expression: a warm friendly eye peeking beneath a thick ginger fringe and a broad pale nose.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 2 to 24 | -8 to 8 | 7 to 21 |  |
| leg_hl | 3 to 6 | -6 to -3 | 4 to 8 | turned ry +6°; on body |
| shin_hl | 3 to 6 | -6 to -3 | 0 to 3 | on leg_hl |
| leg_fl | 19 to 22 | -6 to -3 | 4 to 8 | turned ry -8°; on body |
| shin_fl | 19 to 22 | -6 to -3 | 0 to 3 | on leg_fl |
| tail | 0 to 1 | -1 to 1 | 8 to 18 | turned rx -10°; on body |
| head | 24 to 35 | -5 to 5 | 11 to 22 | turned rx +5°, ry +4°, rz -10°; on body |
| horn_l | 27 to 30 | -12 to -5 | 19 to 26 | turned ry -8°, rz +12°; on head |
| horn_r | 27 to 30 | 5 to 12 | 19 to 26 | turned ry -8°, rz -12°; on head |

## Recognisable features (in order of importance)

1. the shaggy ginger fringe (dossan) hanging over the eyes
2. the wide sweeping pale horns
3. the long wavy ginger-red coat
4. the broad pale muzzle
5. the stocky legs and tufted tail

## Colour map

- `coat`: long wavy ginger-red double coat
- `fringe`: shaggy forehead fringe (dossan) hanging over the eyes
- `horn`: long wide-sweeping pale horns with dark tips
- `muzzle`: broad wet pale nose and hooves
- `white`: the white of each eye
- `eye`: the pupils

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
