# 000025 · Plains Zebra · voxel brief

*Equus quagga* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `white` | `#FAFAF9` | the white between the stripes |
| `stripe` | `#171717` | the stripes, the mane, the tail tuft, the hooves and the eye |
| `muzzle` | `#44403B` | the dark muzzle |

Background (not modelled): `#EDCFAA` (savanna gold).

## Size and pose

- Size: 38 × 11 × 40 voxels posed (L × W × H); longest side 40, budget 36–48 (target 42) from the real size 2.8 m (nose to tail tip: head and body 2.17–2.46 m plus a 0.47–0.56 m tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_hl, shin_hl, leg_fl, shin_fl, body, tail, neck, head, muzzle, ear_l, leg_hr, shin_hr, leg_fr, shin_fr, ear_r.

## Personality, pose and expression

- Personality: lively, sociable and a little cheeky.
- Pose: Trotting with one front leg lifted, the neck growing out of the shoulders, the head held high and turned to the camera, the tail swinging out behind.
- Expression: a big dark eye with a white glint and a cheeky smirk, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_hl | 2 to 4 | -5 to -3 | 8 to 14 | on body |
| shin_hl | 2 to 4 | -5 to -3 | 0 to 7 | on leg_hl |
| leg_fl | 18 to 20 | -5 to -3 | 8 to 14 | turned ry -28°; on body |
| shin_fl | 18 to 20 | -5 to -3 | 0 to 7 | turned ry +40°; on leg_fl |
| body | 0 to 21 | -5 to 5 | 15 to 24 |  |
| tail | -1 to -1 | -1 to 1 | 13 to 23 | turned rx -24°, ry +28°; on body |
| neck | 15 to 22 | -2 to 2 | 25 to 34 | turned ry -6°; on body |
| head | 22 to 29 | -3 to 3 | 30 to 35 | turned rx +3°, ry -4°, rz -14°; on neck |
| muzzle | 30 to 32 | -2 to 2 | 30 to 33 | on head |
| ear_l | 24 to 25 | -3 to -2 | 36 to 38 | turned rx +10°; on head |
| leg_hr | 2 to 4 | 3 to 5 | 8 to 14 | turned ry +14°; on body |
| shin_hr | 2 to 4 | 3 to 5 | 0 to 7 | turned ry -12°; on leg_hr |
| leg_fr | 18 to 20 | 3 to 5 | 8 to 14 | on body |
| shin_fr | 18 to 20 | 3 to 5 | 0 to 7 | on leg_fr |
| ear_r | 24 to 25 | 2 to 3 | 36 to 38 | turned rx -10°; on head |

## Recognisable features (in order of importance)

1. bold black-and-white stripes, vertical on the neck and horizontal on the rump
2. a short upright striped mane along the top and down the back of the neck
3. a dark muzzle
4. a tufted tail
5. stripes running down the legs

## Colour map

- `white`: the white between the stripes
- `stripe`: the stripes, the mane, the tail tuft, the hooves and the eye
- `muzzle`: the dark muzzle

## Photos used

- `assets/photos/01-kenya.jpg`: a pair of Grant's zebras by a road in Kenya, stripes and mane (Public domain)
- `assets/photos/02-serengeti.jpg`: a zebra trotting in the Serengeti, leg stripes and tail (CC BY 2.0)
