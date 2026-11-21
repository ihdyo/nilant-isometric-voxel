# 000097 · Blue-ringed Octopus · voxel brief

*Hapalochlaena lunulata* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#FFB900` | primary body / main colour |
| `patch` | `#BB4D00` | patch |
| `ring` | `#00D3F2` | ring |
| `ring_dark` | `#171717` | ring dark |
| `sucker` | `#FEF3C6` | sucker |
| `eye` | `#171717` | eye |

Background (not modelled): `#DCD6A9` (soft straw).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 0.12 m (mantle length ~5 cm, total length with arms 10–12 cm).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `walker` (pose, idle, crawl, flash).

## Personality, pose and expression

- Personality: tiny yet formidable, a neon-ringed reef jewel.
- Pose: poised alertly with arms splayed radially and glowing cyan rings displayed.
- Expression: sharp dark eyes set above glowing blue warning rings.

## Recognisable features (in order of importance)

1. iridescent electric-cyan rings outlined in black
2. golden-ochre compact mantle and eight short arms
3. tiny golf-ball body proportion
4. pale undersides with small suckers
5. prominent lateral eyes

## Colour map

- `skin`: `amber-400`
- `patch`: `amber-700`
- `ring`: `cyan-400`
- `ring_dark`: `neutral-900`
- `sucker`: `amber-100`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
