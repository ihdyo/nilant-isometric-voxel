# 000066 · Barn Owl · voxel brief

*Tyto alba* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `face` | `#FAFAF9` | heart-shaped pure white facial disc and chest |
| `back` | `#FFD230` | golden-buff and warm ochre upperparts |
| `speckle` | `#79716B` | fine grey-brown mottling and wing tips |
| `beak` | `#FEF3C6` | pale ivory hooked beak and long feathered legs |
| `eye` | `#171717` | large soulful black eyes and facial rim |

Background (not modelled): `#C7D2FD` (soft lavender).

## Size and pose

- Size: 16 × 13 × 26 voxels rest (L × W × H); longest side 26, budget 48–56 (target 56) from the real size 0.36 m (body length 33–39 cm; wingspan 80–95 cm).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, wing_l, tail, leg_l, head, wing_r, leg_r.

## Personality, pose and expression

- Personality: mysterious and graceful, silent ghost of the moonlit meadow.
- Pose: perched alertly with wings folded neatly, heart-shaped face tilted forward.
- Expression: large soulful black eyes set in a crisp white heart-shaped facial disc.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 3 to 13 | -5 to 5 | 4 to 17 |  |
| wing_l | 3 to 11 | -6 to -5 | 3 to 16 | on body |
| tail | 0 to 4 | -3 to 3 | 2 to 6 | turned ry +12°; on body |
| leg_l | 7 to 10 | -4 to -2 | 0 to 4 | on body |
| head | 4 to 15 | -5 to 5 | 17 to 25 | turned rx +5°, rz -16°; on body |
| wing_r | 3 to 11 | 5 to 6 | 3 to 16 | on body |
| leg_r | 7 to 10 | 2 to 4 | 0 to 4 | on body |

## Recognisable features (in order of importance)

1. the iconic white heart-shaped facial disc
2. the golden-buff wings speckled with grey
3. the pure white speckled chest
4. the long slender feathered legs
5. the large dark black eyes

## Colour map

- `face`: heart-shaped pure white facial disc and chest
- `back`: golden-buff and warm ochre upperparts
- `speckle`: fine grey-brown mottling and wing tips
- `beak`: pale ivory hooked beak and long feathered legs
- `eye`: large soulful black eyes and facial rim

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
