# 000004 · Emperor Penguin · voxel brief

*Aptenodytes forsteri* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour | Where |
|---|---|---|
| `black` | `#0F172B` | back, flanks, head, flippers, feet, bill |
| `white` | `#F8FAFC` | belly and front, a dot for each eye on the front of the head |
| `yellow` | `#FFB900` | ear patch on the side of the head and neck |
| `cream` | `#FEF3C6` | upper breast |
| `bill` | `#FF8904` | stripe on the lower half of the bill |

Background (not modelled): `#ADDCF5` (sea-ice blue).

## Size and pose

- Size: 15 × 20 × 28 voxels posed (L × W × H); longest side 28, budget 26–34 (target 30) from the real size 1.15 m (standing height 101–132 cm, mid-range).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: foot_l, body, flipper_l, head, beak, foot_r, flipper_r.

## Personality, pose and expression

- Personality: proud and a little pompous.
- Pose: Standing tall, chin up, turned to the camera, the left flipper held out wide, the right one lifted a little, the small feet turned out.
- Expression: smug closed eyes, white lines dipping towards the middle, painted flat on the face.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| foot_l | 7 to 9 | -3 to -1 | 0 to 0 | turned rz -12° |
| body | -1 to 9 | -5 to 5 | 1 to 17 |  |
| flipper_l | 3 to 7 | -6 to -6 | 6 to 15 | turned rx -32°; on body |
| head | 1 to 8 | -4 to 4 | 18 to 26 | turned rx +3°, ry -8°; on body |
| beak | 9 to 13 | 0 to 0 | 20 to 21 | turned ry +4°; on head |
| foot_r | 7 to 9 | 1 to 3 | 0 to 0 | turned rz +12° |
| flipper_r | 3 to 7 | 6 to 6 | 6 to 15 | turned rx +12°; on body |

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
