# 000082 · Galapagos Giant Tortoise · voxel brief

*Chelonoidis niger* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `shell` | `#44403B` | primary body / main colour |
| `scute` | `#57534D` | scute |
| `skin` | `#79716B` | skin |
| `nail` | `#D6D3D1` | nail |
| `white` | `#FAFAF9` | white |
| `eye` | `#171717` | eye |

Background (not modelled): `#E0D5A8` (soft straw).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 1.5 m (carapace length 1.2–1.5 m (largest living tortoise species)).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `walker` (pose, idle, walk, graze).

## Personality, pose and expression

- Personality: unhurried and venerable, a centenarian island wanderer.
- Pose: standing steady on four pillar legs with long neck extended forward and upward.
- Expression: gentle dark eyes and a calm, wise tortoise beak.

## Recognisable features (in order of importance)

1. high domed carapace with polygonal scutes
2. long wrinkled neck extended from the shell
3. stumpy elephant-like scaly legs
4. small blunt tail
5. beaked toothless head

## Colour map

- `shell`: `stone-700`
- `scute`: `stone-600`
- `skin`: `stone-500`
- `nail`: `stone-300`
- `white`: `stone-50`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
