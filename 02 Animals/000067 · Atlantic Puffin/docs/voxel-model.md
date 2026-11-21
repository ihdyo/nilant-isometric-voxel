# 000067 · Atlantic Puffin · voxel brief

*Fratercula arctica* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `back` | `#171717` | glossy black crown, back, wings and collar |
| `belly` | `#FAFAF9` | crisp white chest and belly |
| `face` | `#D6D3D1` | pale grey rounded cheek patches |
| `beak` | `#FF6900` | large grooved orange-red and slate-blue breeding bill and webbed feet |
| `eye` | `#171717` | dark triangular-rimmed eyes |

Background (not modelled): `#A6E0E7` (soft aqua).

## Size and pose

- Size: 15 × 11 × 22 voxels rest (L × W × H); longest side 22, budget 48–56 (target 56) from the real size 0.3 m (body length 26–30 cm; wingspan 47–63 cm).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, wing_l, leg_l, head, wing_r, leg_r.

## Personality, pose and expression

- Personality: plucky and dapper, charming clown of the North Atlantic cliffs.
- Pose: standing upright on bright orange webbed feet, chest puffed, head cocked inquisitively.
- Expression: soulful dark eyes framed by triangular red-orange eye rings and pale grey cheeks.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 2 to 12 | -4 to 4 | 4 to 15 |  |
| wing_l | 2 to 9 | -5 to -4 | 4 to 14 | on body |
| leg_l | 6 to 10 | -4 to -1 | 0 to 4 | on body |
| head | 3 to 16 | -4 to 4 | 15 to 21 | turned rx +4°, ry +4°, rz -12°; on body |
| wing_r | 2 to 9 | 4 to 5 | 4 to 14 | on body |
| leg_r | 6 to 10 | 1 to 4 | 0 to 4 | on body |

## Recognisable features (in order of importance)

1. the large colorful striped orange-and-blue triangular beak
2. the pale grey rounded cheek patches
3. the black tuxedo back and crisp white belly
4. the bright orange webbed feet
5. the compact stubby wings

## Colour map

- `back`: glossy black crown, back, wings and collar
- `belly`: crisp white chest and belly
- `face`: pale grey rounded cheek patches
- `beak`: large grooved orange-red and slate-blue breeding bill and webbed feet
- `eye`: dark triangular-rimmed eyes

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
