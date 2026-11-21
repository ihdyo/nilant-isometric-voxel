# 000064 · Bald Eagle · voxel brief

*Haliaeetus leucocephalus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `plumage` | `#292524` | dark chocolate-brown body and broad wings |
| `head` | `#FAFAF9` | snow-white feathered head, neck and wedge tail |
| `beak` | `#FFB900` | heavy hooked golden-yellow beak, cere and talons |
| `iris` | `#FFF085` | piercing pale-yellow eyes |
| `eye` | `#171717` | the pupils and sharp black talon tips |

Background (not modelled): `#ACDDF4` (soft sky blue).

## Size and pose

- Size: 21 × 13 × 30 voxels rest (L × W × H); longest side 30, budget 48–56 (target 56) from the real size 0.9 m (body length 70–102 cm; wingspan 1.8–2.3 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, wing_l, tail, leg_l, head, wing_r, leg_r.

## Personality, pose and expression

- Personality: commanding and keen-eyed, sovereign of the open sky.
- Pose: a proud perched stance with chest puffed, wings folded crisply, head turned sharply.
- Expression: fierce golden-yellow eyes under a prominent white brow ridge and heavy hooked beak.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 6 to 16 | -5 to 5 | 8 to 22 |  |
| wing_l | 6 to 14 | -6 to -5 | 7 to 21 | turned ry +4°, rz +6°; on body |
| tail | 0 to 7 | -3 to 3 | 4 to 10 | turned ry +14°; on body |
| leg_l | 10 to 14 | -5 to -1 | 0 to 8 | on body |
| head | 8 to 20 | -4 to 4 | 22 to 29 | turned rx +4°, ry +4°, rz -14°; on body |
| wing_r | 6 to 14 | 5 to 6 | 7 to 21 | turned ry +4°, rz -6°; on body |
| leg_r | 10 to 14 | 1 to 5 | 0 to 8 | on body |

## Recognisable features (in order of importance)

1. the snow-white feathered head and neck
2. the heavy hooked golden-yellow beak
3. the dark chocolate-brown body and folded wings
4. the snow-white wedge tail
5. the yellow legs and curved black talons

## Colour map

- `plumage`: dark chocolate-brown body and broad wings
- `head`: snow-white feathered head, neck and wedge tail
- `beak`: heavy hooked golden-yellow beak, cere and talons
- `iris`: piercing pale-yellow eyes
- `eye`: the pupils and sharp black talon tips

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
