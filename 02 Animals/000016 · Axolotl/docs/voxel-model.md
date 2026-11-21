# 000016 · Axolotl · voxel brief

*Ambystoma mexicanum* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#FFCCD3` | body, head, legs and tail (the pale pink form kept in aquariums) |
| `gill` | `#FF637E` | the feathery gill stalks, the tail fin edge and the painted smile |
| `belly` | `#FFE4E6` | the belly and the underside of the head |
| `eye` | `#0A0A0A` | the small dark eyes |

Background (not modelled): `#A6E1E4` (lake teal).

## Size and pose

- Size: 18 × 15 × 7 voxels posed (L × W × H); longest side 18, budget 16–18 (target 16) from the real size 0.23 m (snout to tail tip: about 23 cm on average, some over 30 cm).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_fl, leg_hl, head, gill_l, tail, tail_tip, leg_fr, leg_hr, gill_r.

## Personality, pose and expression

- Personality: happy-go-lucky and a little goofy.
- Pose: A sprawling stride, the legs swept forward and back, the tail curving, the head turned to the camera, the gills fanned.
- Expression: a wide smile and small dark eyes set far apart, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 3 to 10 | -2 to 2 | 1 to 3 |  |
| leg_fl | 9 to 9 | -4 to -3 | 0 to 1 | turned rz +28°; on body |
| leg_hl | 4 to 4 | -4 to -3 | 0 to 1 | turned rz -26°; on body |
| head | 11 to 14 | -3 to 3 | 1 to 5 | turned rx +3°, ry +6°, rz -14°; on body |
| gill_l | 11 to 11 | -6 to -4 | 2 to 6 | turned rx +18°, rz -10°; on head |
| tail | 0 to 2 | -1 to 1 | 1 to 4 | turned rz +20°; on body |
| tail_tip | -2 to -1 | -1 to 1 | 1 to 3 | turned rz +26°; on tail |
| leg_fr | 9 to 9 | 3 to 4 | 0 to 1 | turned rz -14°; on body |
| leg_hr | 4 to 4 | 3 to 4 | 0 to 1 | turned rz +14°; on body |
| gill_r | 11 to 11 | 4 to 6 | 2 to 6 | turned rx -18°, rz +10°; on head |

## Recognisable features (in order of importance)

1. feathery gill stalks on both sides of the head
2. a wide flat head with a big smile
3. a long finned tail
4. four small splayed legs
5. pale pink skin

## Colour map

- `skin`: body, head, legs and tail (the pale pink form kept in aquariums)
- `gill`: the feathery gill stalks, the tail fin edge and the painted smile
- `belly`: the belly and the underside of the head
- `eye`: the small dark eyes

## Photos used

- `assets/photos/01-pale-pair.jpg`: two pale (leucistic) axolotls on the bottom of a tank, gills and smile (CC BY 3.0)
- `assets/photos/02-wild-type.jpg`: a dark wild-type axolotl among plants (CC0)
