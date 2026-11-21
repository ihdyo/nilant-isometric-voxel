# 000087 · Humpback Whale · voxel brief

*Megaptera novaeangliae* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#262626` | primary body / main colour |
| `belly` | `#F5F5F4` | belly |
| `flipper` | `#E7E5E4` | flipper |
| `tubercle` | `#79716B` | tubercle |
| `eye` | `#171717` | eye |

Background (not modelled): `#BAD7FC` (soft periwinkle).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 15.0 m (total length 12–16 m with pectoral flippers up to 5 m long).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `swimmer` (pose, idle, swim, breach).

## Personality, pose and expression

- Personality: acrobatic and soulful, an ocean singer and leaper.
- Pose: banking gracefully with its long white wing-like flippers spread and tail curved.
- Expression: gentle dark eye set behind the bumpy rostrum.

## Recognisable features (in order of importance)

1. extraordinarily long white scalloped pectoral flippers
2. knobby tubercles along the snout and jaw
3. arched back with a stubby humped dorsal fin
4. pleated white-and-black throat grooves
5. broad notched tail flukes

## Colour map

- `skin`: `neutral-800`
- `belly`: `stone-100`
- `flipper`: `stone-200`
- `tubercle`: `stone-500`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
