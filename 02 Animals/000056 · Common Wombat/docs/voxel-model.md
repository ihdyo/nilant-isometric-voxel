# 000056 · Common Wombat · voxel brief

*Vombatus ursinus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#57534D` | stout coarse brown-grey fur |
| `shade` | `#44403B` | darker rump plate and back shading |
| `nose` | `#171717` | broad bare black nose and strong digging claws |
| `ear` | `#FEE685` | inner rounded ears |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#171717` | the pupils |

Background (not modelled): `#CCDCB1` (soft lime green).

## Size and pose

- Size: 30 × 15 × 17 voxels rest (L × W × H); longest side 30, budget 48–56 (target 56) from the real size 1.0 m (head-and-body length, 0.85–1.15 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, leg_fl, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: sturdy and stubborn, the cuddly tank of the bush.
- Pose: a low waddling stride, chunky head held up, broad black nose sniffing the air.
- Expression: round dark eyes and a tiny tucked smile beneath a big black nose.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 21 | -7 to 7 | 4 to 15 |  |
| leg_hl | 3 to 7 | -7 to -4 | 0 to 4 | turned ry +10°; on body |
| leg_fl | 16 to 20 | -7 to -4 | 0 to 4 | turned ry -10°; on body |
| head | 20 to 29 | -6 to 6 | 5 to 14 | turned rx +4°, ry -4°, rz -8°; on body |
| ear_l | 21 to 23 | -6 to -4 | 14 to 16 | turned rz +12°; on head |
| ear_r | 21 to 23 | 4 to 6 | 14 to 16 | turned rz -12°; on head |

## Recognisable features (in order of importance)

1. the barrel-shaped chunky body close to the ground
2. the broad head with a big bare black nose
3. the short rounded ears
4. the stubby powerful legs with digging claws
5. the virtually absent tail

## Colour map

- `coat`: stout coarse brown-grey fur
- `shade`: darker rump plate and back shading
- `nose`: broad bare black nose and strong digging claws
- `ear`: inner rounded ears
- `white`: the white of each eye
- `eye`: the pupils

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
