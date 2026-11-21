# 000041 · Japanese Macaque · voxel brief

*Macaca fuscata* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#A6A09B` | thick woolly grey-brown winter fur across body, limbs and head |
| `face` | `#FF637E` | iconic bare rosy-red face, ears and rump |
| `belly` | `#E7E5E4` | lighter silver-grey chest and belly |
| `shade` | `#57534D` | darker brown-grey shading on shoulders and back |
| `white` | `#FAFAF9` | eye sclera highlight |
| `eye` | `#973C00` | warm brown expressive eyes |

Background (not modelled): `#F9C5CC` (soft rose).

## Size and pose

- Size: 24 × 15 × 20 voxels posed (L × W × H); longest side 24, budget 22–28 (target 24) from the real size 0.65 m (head to rump about 0.5–0.65 m plus short 8–10 cm tail (body 47–60 cm per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: serene and sociable, cozy in a thick winter coat.
- Pose: a compact quadrupedal winter stance with fluffy shoulders, short stubby tail and red face turned warmly toward the camera.
- Expression: expressive brown eyes set in a bright rosy-red bare face framed by thick woolly fur.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 12 to 14 | -4 to -2 | 0 to 5 | turned ry -10°; on body |
| leg_fr | 12 to 14 | 2 to 4 | 0 to 5 | turned ry +6°; on body |
| leg_hl | 2 to 4 | -4 to -2 | 0 to 5 | turned ry +8°; on body |
| leg_hr | 2 to 4 | 2 to 4 | 0 to 5 | on body |
| body | 1 to 15 | -4 to 4 | 5 to 13 |  |
| tail | -2 to 0 | -1 to 1 | 9 to 11 | turned ry -15°; on body |
| head | 14 to 20 | -4 to 4 | 10 to 18 | turned rx +4°, ry +3°, rz -10°; on body |
| ear_l | 16 to 17 | -5 to -4 | 14 to 16 | on head |
| ear_r | 16 to 17 | 4 to 5 | 14 to 16 | on head |

## Recognisable features (in order of importance)

1. distinctive bare rosy-red face and ears
2. dense, fluffy grey-brown winter fur coat
3. short stubby tail (8–10 cm) adapted to cold climates
4. stocky, sturdy limbs
5. pale cheek whiskers framing the red muzzle

## Colour map

- `coat`: thick woolly grey-brown winter fur across body, limbs and head
- `face`: iconic bare rosy-red face, ears and rump
- `belly`: lighter silver-grey chest and belly
- `shade`: darker brown-grey shading on shoulders and back
- `white`: eye sclera highlight
- `eye`: warm brown expressive eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult japanese macaque profile reference (CC BY 3.0)
