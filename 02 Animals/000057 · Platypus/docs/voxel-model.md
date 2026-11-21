# 000057 · Platypus · voxel brief

*Ornithorhynchus anatinus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#7B3306` | dense waterproof dark-brown fur |
| `belly` | `#FEE685` | paler golden-buff underside |
| `bill` | `#45556C` | rubbery electroreceptive duck-like bill and webbed feet |
| `tail` | `#461901` | broad flat fat-storing beaver-like tail |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#171717` | the pupils |

Background (not modelled): `#A9E2D6` (soft mint).

## Size and pose

- Size: 41 × 14 × 10 voxels rest (L × W × H); longest side 41, budget 48–56 (target 56) from the real size 0.5 m (total length, 43–50 cm (males up to 60 cm)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, leg_hl, leg_fl, head.

## Personality, pose and expression

- Personality: quirky and inquisitive, nocturnal river detective.
- Pose: a sleek paddling glide, broad duck bill tilted up, paddle tail trailing.
- Expression: beady bright eyes just behind a wide slate-grey bill.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 10 to 26 | -5 to 5 | 1 to 9 |  |
| tail | 0 to 10 | -4 to 4 | 3 to 5 | turned ry +6°; on body |
| leg_hl | 12 to 16 | -8 to -5 | 0 to 2 | turned rz +14°; on body |
| leg_fl | 22 to 26 | -8 to -5 | 0 to 2 | turned rz -16°; on body |
| head | 26 to 40 | -4 to 4 | 3 to 9 | turned rx +3°, ry -5°, rz -8°; on body |

## Recognisable features (in order of importance)

1. the wide flat slate-grey duck bill
2. the broad flat paddle tail
3. the webbed front and hind feet
4. the sleek dark-brown waterproof body
5. the pale golden-buff belly

## Colour map

- `coat`: dense waterproof dark-brown fur
- `belly`: paler golden-buff underside
- `bill`: rubbery electroreceptive duck-like bill and webbed feet
- `tail`: broad flat fat-storing beaver-like tail
- `white`: the white of each eye
- `eye`: the pupils

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
