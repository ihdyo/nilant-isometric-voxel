# 26-004 · Emperor Penguin · voxel brief

*Aptenodytes forsteri* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `black` | `slate-900` | back, flanks, head, flippers, feet, bill |
| `white` | `slate-50` | belly and front, a dot for each eye on the front of the head |
| `yellow` | `amber-400` | ear patch on the side of the head and neck |
| `cream` | `amber-100` | upper breast |
| `bill` | `orange-400` | stripe on the lower half of the bill |

Background (not modelled): `sky-200`.

## Size and pose

- Size: 15 × 20 × 28 voxels posed (L × W × H); longest side 28, budget 26–34 (target 30) from the real size 1.15 m (standing height 101–132 cm, mid-range).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: foot_l, foot_r, body, flipper_l, flipper_r, head, beak.

## Personality, pose and expression

- Personality: proud and a little pompous.
- Pose: chest out, head tipped back with the bill raised, flippers held out from the white flanks, black block feet with the toes turned out.
- Expression: smug closed eyes, white lines dipping towards the middle, painted flat on the face.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| foot_l | 6 to 10 | -4 to -1 | 0 to 0 | turned rz -12° |
| foot_r | 6 to 10 | 1 to 4 | 0 to 0 | turned rz +12° |
| body | -1 to 9 | -5 to 5 | 1 to 17 |  |
| flipper_l | 3 to 7 | -6 to -6 | 6 to 15 | turned rx -24°; on body |
| flipper_r | 3 to 7 | 6 to 6 | 6 to 15 | turned rx +24°; on body |
| head | 1 to 8 | -4 to 4 | 18 to 26 | turned rx +4°, ry -12°, rz -8°; on body |
| beak | 9 to 13 | 0 to 0 | 20 to 21 | turned ry +6°; on head |

## Recognisable features (in order of importance)

1. upright black body with a white front
2. the yellow ear patch on the side of the head
3. the pale yellow upper breast
4. a long thin bill with an orange stripe below
5. flippers hanging along the flanks

## Colour map

- `black`: back, flanks, head, flippers, feet, bill
- `white`: belly and front, a dot for each eye on the front of the head
- `yellow`: ear patch on the side of the head and neck
- `cream`: upper breast
- `bill`: stripe on the lower half of the bill

## Photos used

- `assets/photos/01-pair.jpg`: adults, yellow ear patches, chick (Public domain)
- `assets/photos/02-side.jpg`: adults standing, side profiles (Public domain)
