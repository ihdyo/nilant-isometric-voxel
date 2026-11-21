# 000061 · Sunda Pangolin · voxel brief

*Manis javanica* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `scale` | `#57534D` | overlapping olive-brown keratin scales across back, sides and tail |
| `shade` | `#44403B` | darker scale edges and shading |
| `skin` | `#FEE685` | soft pale-tan belly, inner legs and tapered face |
| `claw` | `#D6D3D1` | curved digging claws |
| `eye` | `#171717` | small dark eyes and nostrils |

Background (not modelled): `#B0E1CA` (soft mint).

## Size and pose

- Size: 35 × 11 × 19 voxels rest (L × W × H); longest side 35, budget 48–56 (target 56) from the real size 1.1 m (total length, 0.9–1.2 m including prehensile tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, leg_hl, arm_l, head, arm_r.

## Personality, pose and expression

- Personality: humble and armored, quiet guardian of the Sunda rainforest.
- Pose: a cautious bipedal-leaning amble, heavy scaly tail balanced behind, head angled down.
- Expression: gentle dark eyes on a narrow pale-tan conical snout.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 10 to 26 | -5 to 5 | 5 to 18 |  |
| tail | 0 to 10 | -3 to 3 | 4 to 11 | turned ry +8°; on body |
| leg_hl | 12 to 15 | -5 to -3 | 0 to 6 | on body |
| arm_l | 21 to 26 | -5 to -3 | 2 to 7 | turned ry +14°; on body |
| head | 26 to 34 | -3 to 3 | 8 to 14 | turned rx +4°, ry +12°, rz -10°; on body |
| arm_r | 21 to 26 | 3 to 5 | 2 to 7 | turned ry +14°; on body |

## Recognisable features (in order of importance)

1. the coat of overlapping olive-brown keratin scales
2. the long thick prehensile scaly tail
3. the narrow tapered pale-tan snout
4. the strong curved digging claws
5. the soft pale underside

## Colour map

- `scale`: overlapping olive-brown keratin scales across back, sides and tail
- `shade`: darker scale edges and shading
- `skin`: soft pale-tan belly, inner legs and tapered face
- `claw`: curved digging claws
- `eye`: small dark eyes and nostrils

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
