# 000084 · Blue Poison Dart Frog · voxel brief

*Dendrobates tinctorius azureus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#155DFC` | primary body / main colour |
| `limbs` | `#432DD7` | limbs |
| `spot` | `#171717` | spot |
| `belly` | `#00BCFF` | belly |
| `white` | `#FAFAF9` | white |
| `eye` | `#171717` | eye |

Background (not modelled): `#B7D8FB` (soft periwinkle).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 0.045 m (snout-to-vent length 3–4.5 cm).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `walker` (pose, idle, hop, croak).

## Personality, pose and expression

- Personality: vivid and fearless, a jewel-toned forest dweller.
- Pose: perched upright on its front legs with hunched back and splayed disc-tipped toes.
- Expression: large glossy black eyes with tiny white highlights.

## Recognisable features (in order of importance)

1. electric azure-blue skin with black spots
2. hunched posture propped on front legs
3. darker blue legs with rounded toe pads
4. compact tailless frog body
5. large prominent dark eyes

## Colour map

- `skin`: `blue-600`
- `limbs`: `indigo-700`
- `spot`: `neutral-900`
- `belly`: `sky-400`
- `white`: `stone-50`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
