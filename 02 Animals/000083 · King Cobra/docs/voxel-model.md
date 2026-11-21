# 000083 · King Cobra · voxel brief

*Ophiophagus hannah* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `scales` | `#2B2B22` | primary body / main colour |
| `band` | `#FEE685` | band |
| `hood` | `#FFD230` | hood |
| `belly` | `#FEF9C2` | belly |
| `tongue` | `#FF2056` | tongue |
| `eye` | `#171717` | eye |

Background (not modelled): `#DCD6A9` (soft straw).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 4.0 m (total length 3–4 m, up to 5.5 m (longest venomous snake)).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `crawler` (pose, idle, slither, hood).

## Personality, pose and expression

- Personality: regal and intimidating, the sovereign of forest snakes.
- Pose: coiled in a sturdy base with upper third reared upright and neck hood flared wide.
- Expression: piercing dark eyes beneath heavy brow scales, forked tongue flicking out.

## Recognisable features (in order of importance)

1. reared upright stance with flared neck hood
2. pale cream throat and chevron body bands
3. coiled muscular lower body
4. large plated cobra head
5. forked red tongue

## Colour map

- `scales`: `olive-800`
- `band`: `amber-200`
- `hood`: `amber-300`
- `belly`: `yellow-100`
- `tongue`: `rose-500`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
