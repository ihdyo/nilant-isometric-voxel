# 000094 · Giant Manta Ray · voxel brief

*Mobula birostris* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `back` | `#171717` | primary body / main colour |
| `shoulder` | `#E7E5E4` | shoulder |
| `belly` | `#FAFAF9` | belly |
| `spot` | `#404040` | spot |
| `eye` | `#171717` | eye |

Background (not modelled): `#C7D2FD` (soft lavender).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 7.0 m (disc width (wingspan) 4.5–7 m (largest ray species in the world)).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `swimmer` (pose, idle, glide, loop).

## Personality, pose and expression

- Personality: graceful and curious, a flying wing of the reef.
- Pose: soaring with wide triangular wings arched gently and cephalic fins curled forward.
- Expression: wide-set lateral eyes flanking the broad plankton-filtering mouth.

## Recognisable features (in order of importance)

1. broad triangular wing-like pectoral fins
2. two forward-curled cephalic fins flanking the mouth
3. jet-black back with white shoulder patches
4. white spotted underbelly
5. long slender whip-like tail

## Colour map

- `back`: `neutral-900`
- `shoulder`: `stone-200`
- `belly`: `stone-50`
- `spot`: `neutral-700`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
