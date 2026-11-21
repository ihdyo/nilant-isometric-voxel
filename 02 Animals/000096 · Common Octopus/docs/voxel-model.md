# 000096 · Common Octopus · voxel brief

*Octopus vulgaris* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#EC003F` | primary body / main colour |
| `shade` | `#A50036` | shade |
| `sucker` | `#FFCCD3` | sucker |
| `iris` | `#FFD230` | iris |
| `eye` | `#171717` | eye |

Background (not modelled): `#DFCAF3` (soft lilac).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 1.0 m (total arm span 0.6–1.0 m, up to 1.3 m).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `walker` (pose, idle, crawl, wave).

## Personality, pose and expression

- Personality: clever and inquisitive, a nimble seafloor escape artist.
- Pose: perched upright on curled tentacles with two front arms raised inquisitively.
- Expression: expressive golden eyes with horizontal bar pupils.

## Recognisable features (in order of importance)

1. bulbous rounded mantle head
2. eight flexible arms with double rows of pale suckers
3. horizontal-pupil golden eyes
4. side breathing siphon tube
5. rich coral-terracotta skin

## Colour map

- `skin`: `rose-600`
- `shade`: `rose-800`
- `sucker`: `rose-200`
- `iris`: `amber-300`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
