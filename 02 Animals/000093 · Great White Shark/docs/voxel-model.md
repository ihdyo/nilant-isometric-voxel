# 000093 · Great White Shark · voxel brief

*Carcharodon carcharias* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `back` | `#62748E` | primary body / main colour |
| `belly` | `#FAFAF9` | belly |
| `gill` | `#314158` | gill |
| `tooth` | `#F5F5F4` | tooth |
| `eye` | `#171717` | eye |

Background (not modelled): `#B7D8FB` (soft periwinkle).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 5.0 m (total length 4–6 m).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `swimmer` (pose, idle, swim, bite).

## Personality, pose and expression

- Personality: swift and focused, the ocean's iconic apex shark.
- Pose: cruising forward with jaws slightly open showing triangular teeth and crescent tail sweeping.
- Expression: pitch-black eyes above a sharp conical snout and jagged smile.

## Recognisable features (in order of importance)

1. countershaded slate-grey back and white belly
2. pointed conical snout with serrated teeth
3. tall triangular dorsal fin and five gill slits
4. long swept-back pectoral fins
5. symmetrical crescent caudal fin

## Colour map

- `back`: `slate-500`
- `belly`: `stone-50`
- `gill`: `slate-700`
- `tooth`: `stone-100`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
