# 000100 · Hercules Beetle · voxel brief

*Dynastes hercules* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `elytra` | `#7CCF00` | primary body / main colour |
| `spot` | `#171717` | spot |
| `thorax` | `#171717` | thorax |
| `horn` | `#262626` | horn |
| `leg` | `#171717` | leg |

Background (not modelled): `#CCDCB1` (soft pastel).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 0.17 m (total length 5–17 cm in adult males including the long thoracic horn).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `walker` (pose, idle, walk, pinch).

## Personality, pose and expression

- Personality: armored and mighty, the heavyweight champion of the rainforest floor.
- Pose: braced firmly on six clawed legs with twin pincer horns jutting proudly forward.
- Expression: gleaming black beetle armor with formidable opposing horns.

## Recognisable features (in order of importance)

1. giant forward-curving thoracic horn and lower head horn
2. olive-lime wing covers speckled with black spots
3. glossy black armoured pronotum shield
4. six sturdy jointed legs with hooked claws
5. compact heavy scarab body

## Colour map

- `elytra`: `lime-500`
- `spot`: `neutral-900`
- `thorax`: `neutral-900`
- `horn`: `neutral-800`
- `leg`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
