# 000077 · Komodo Dragon · voxel brief

*Varanus komodoensis* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `scales` | `#57534D` | primary body / main colour |
| `shade` | `#44403B` | shade |
| `belly` | `#A6A09B` | belly |
| `claw` | `#262626` | claw |
| `tongue` | `#FFD230` | tongue |
| `eye` | `#171717` | eye |

Background (not modelled): `#EECEAA` (soft sand).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 3.0 m (total length 2–3 m from snout to tail tip (heaviest living lizard)).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `walker` (pose, idle, walk, flick).

## Personality, pose and expression

- Personality: ancient and formidable, an unhurried island apex predator.
- Pose: striding low with heavy tail curving behind and forked yellow tongue flicking forward.
- Expression: calm, watchful dark eyes set in a broad, armored snout.

## Recognisable features (in order of importance)

1. heavy muscular tail nearly half its length
2. broad armored head with forked yellow tongue
3. bowed muscular legs with curved claws
4. textured charcoal-brown osteoderm scales
5. thick, low-slung torso

## Colour map

- `scales`: `stone-600`
- `shade`: `stone-700`
- `belly`: `stone-400`
- `claw`: `neutral-800`
- `tongue`: `amber-300`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
