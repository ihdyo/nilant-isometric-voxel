# 000070 · Secretarybird · voxel brief

*Sagittarius serpentarius* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `plumage` | `#D6D3D1` | silver-grey body, wings and long central tail feathers |
| `legging` | `#171717` | black feathered upper legs and flight-feather tips |
| `face` | `#FF6900` | vivid bare red-orange facial skin |
| `crest` | `#292524` | long black-tipped quill feathers behind the head |
| `leg` | `#FFCCD3` | long pale pink-grey stilt legs and hooked beak |

Background (not modelled): `#E0D5A8` (soft straw).

## Size and pose

- Size: 30 × 9 × 48 voxels rest (L × W × H); longest side 48, budget 48–56 (target 56) from the real size 1.4 m (standing height 1.2–1.5 m; wingspan 1.9–2.1 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, leg_l, shin_l, neck, head, leg_r, shin_r.

## Personality, pose and expression

- Personality: poised and fearless, martial-arts aristocrat of the savanna.
- Pose: a high-stepping stride on stilt legs, quill crest fanned behind the head, wings tucked.
- Expression: keen eyes with long lashes set in vivid orange-red facial skin.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 9 to 21 | -4 to 4 | 21 to 30 |  |
| tail | 0 to 10 | -2 to 2 | 11 to 23 | turned ry +10°; on body |
| leg_l | 14 to 16 | -4 to -2 | 14 to 21 | turned ry -10°; on body |
| shin_l | 14 to 15 | -3 to -2 | 0 to 13 | on leg_l |
| neck | 18 to 22 | -2 to 2 | 29 to 41 | on body |
| head | 13 to 29 | -3 to 3 | 41 to 47 | turned rx +4°, ry +4°, rz -10°; on neck |
| leg_r | 14 to 16 | 2 to 4 | 14 to 21 | on body |
| shin_r | 14 to 15 | 2 to 3 | 0 to 13 | on leg_r |

## Recognisable features (in order of importance)

1. the extremely long stilt legs with black feathered thighs
2. the crown of long black-tipped quill feathers
3. the vivid bare orange-red face and hooked beak
4. the silver-grey body with black flight-feather tips
5. the two elongated central tail feathers

## Colour map

- `plumage`: silver-grey body, wings and long central tail feathers
- `legging`: black feathered upper legs and flight-feather tips
- `face`: vivid bare red-orange facial skin
- `crest`: long black-tipped quill feathers behind the head
- `leg`: long pale pink-grey stilt legs and hooked beak

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
