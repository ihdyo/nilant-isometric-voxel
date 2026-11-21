# 000099 · Atlas Moth · voxel brief

*Attacus atlas* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `wing` | `#BB4D00` | primary body / main colour |
| `band` | `#FFCCD3` | band |
| `window` | `#FAFAF9` | window |
| `tip` | `#FFD230` | tip |
| `body` | `#973C00` | body |
| `antenna` | `#FEE685` | antenna |

Background (not modelled): `#F9C5CC` (soft rose).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 0.25 m (wingspan 24–27 cm (among the largest moths in the world by wing area)).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `flier` (pose, idle, flutter, rest).

## Personality, pose and expression

- Personality: velvety and nocturnal, a gentle giant of tropical nights.
- Pose: resting with immense patterned wings spread flat and feathery antennae angled forward.
- Expression: dark compound eyes framed by wide golden-cream feathery antennae.

## Recognisable features (in order of importance)

1. immense rust-brown wings with hooked snake-head tips
2. four triangular translucent wing windows
3. wavy cream and blush-pink crossbands
4. wide feathery comb-like antennae
5. plump velvety thorax and abdomen

## Colour map

- `wing`: `amber-700`
- `band`: `rose-200`
- `window`: `stone-50`
- `tip`: `amber-300`
- `body`: `amber-800`
- `antenna`: `amber-200`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
