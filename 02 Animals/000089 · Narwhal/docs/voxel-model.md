# 000089 · Narwhal · voxel brief

*Monodon monoceros* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#90A1B9` | primary body / main colour |
| `mottle` | `#314158` | mottle |
| `belly` | `#F5F5F4` | belly |
| `tusk` | `#FEF3C6` | tusk |
| `eye` | `#171717` | eye |

Background (not modelled): `#A6E0E7` (soft aqua).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 4.7 m (body length 4–5 m, plus spiral ivory tusk up to 2–3 m).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `swimmer` (pose, idle, swim, dive).

## Personality, pose and expression

- Personality: mysterious and hardy, the unicorn of Arctic seas.
- Pose: gliding calmly forward with long spiral tusk angled slightly upward.
- Expression: gentle dark eyes on a blunt, friendly Arctic whale face.

## Recognisable features (in order of importance)

1. long straight spiral ivory tusk
2. mottled slate-grey and white skin
3. no dorsal fin (smooth low ridge instead)
4. blunt rounded forehead
5. upturned small flippers and fan tail flukes

## Colour map

- `skin`: `slate-400`
- `mottle`: `slate-700`
- `belly`: `stone-100`
- `tusk`: `amber-100`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
