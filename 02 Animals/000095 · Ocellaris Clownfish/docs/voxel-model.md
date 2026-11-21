# 000095 · Ocellaris Clownfish · voxel brief

*Amphiprion ocellaris* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `body` | `#FF6900` | primary body / main colour |
| `stripe` | `#FAFAF9` | stripe |
| `outline` | `#171717` | outline |
| `iris` | `#FFB900` | iris |
| `eye` | `#171717` | eye |

Background (not modelled): `#EECEAA` (soft sand).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 0.11 m (total length 8–11 cm).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `swimmer` (pose, idle, swim, wiggle).

## Personality, pose and expression

- Personality: lively and plucky, a colorful reef guardian.
- Pose: darting forward with rounded pectoral fins flared and tail fin gently curved.
- Expression: bright orange-rimmed eyes and a cheerful little reef-fish mouth.

## Recognisable features (in order of importance)

1. vivid orange body with three white vertical bands
2. thin black outlines bordering the white stripes and fins
3. rounded paddle-like pectoral fins
4. notched two-part dorsal fin
5. rounded fan tail

## Colour map

- `body`: `orange-500`
- `stripe`: `stone-50`
- `outline`: `neutral-900`
- `iris`: `amber-400`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
