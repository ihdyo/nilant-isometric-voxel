# 000078 · Veiled Chameleon · voxel brief

*Chamaeleo calyptratus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#00BC7D` | primary body / main colour |
| `stripe` | `#FFDF20` | stripe |
| `band` | `#00BCFF` | band |
| `casque` | `#5EA500` | casque |
| `eye_cone` | `#FFB900` | eye cone |
| `eye` | `#171717` | eye |

Background (not modelled): `#CCDCB1` (soft lime green).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 0.55 m (total length 45–60 cm in adult males (including coiled prehensile tail)).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `walker` (pose, idle, walk, look).

## Personality, pose and expression

- Personality: deliberate and observant, a master of disguise.
- Pose: stepping carefully forward with one grasping foot raised and tail curled into a tight spiral.
- Expression: conical turret eyes swiveled forward with intense curiosity.

## Recognisable features (in order of importance)

1. tall helmet-like casque on top of the head
2. tightly coiled prehensile tail
3. conical turret eyes
4. vertical yellow and turquoise flank bars
5. pincer-like zygodactylous feet

## Colour map

- `skin`: `emerald-500`
- `stripe`: `yellow-300`
- `band`: `sky-400`
- `casque`: `lime-600`
- `eye_cone`: `amber-400`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
