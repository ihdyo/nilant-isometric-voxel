# 000086 · Blue Whale · voxel brief

*Balaenoptera musculus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#62748E` | primary body / main colour |
| `mottle` | `#90A1B9` | mottle |
| `pleat` | `#CAD5E2` | pleat |
| `belly` | `#DFF2FE` | belly |
| `eye` | `#171717` | eye |

Background (not modelled): `#ACDDF4` (soft sky blue).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 28.0 m (total length 24–30 m (largest animal ever known to have lived on Earth)).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `swimmer` (pose, idle, swim, breach).

## Personality, pose and expression

- Personality: majestic and serene, a gentle titan of the open ocean.
- Pose: gliding effortlessly forward with throat pleats gently curved and wide tail flukes flexing.
- Expression: calm dark eye set above the long sweeping jawline.

## Recognisable features (in order of importance)

1. enormous streamlined slate-blue body
2. pleated ventral throat grooves
3. broad flat U-shaped head with twin blowholes
4. tiny dorsal fin set far toward the tail
5. wide horizontal tail flukes

## Colour map

- `skin`: `slate-500`
- `mottle`: `slate-400`
- `pleat`: `slate-300`
- `belly`: `sky-100`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
