# 000075 · Ruby-throated Hummingbird · voxel brief

*Archilochus colubris* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `back` | `#009966` | iridescent metallic emerald-green crown, back and wings |
| `throat` | `#EC003F` | iridescent ruby-red gorget on the male's throat |
| `belly` | `#F5F5F4` | soft off-white breast and belly |
| `beak` | `#171717` | needle-thin straight black nectar bill and forked tail |
| `eye` | `#171717` | tiny dark eyes and minuscule feet |

Background (not modelled): `#F2C5DE` (soft orchid).

## Size and pose

- Size: 25 × 25 × 17 voxels rest (L × W × H); longest side 25, budget 48–56 (target 56) from the real size 0.09 m (body length 7–9 cm; wingspan 8–11 cm).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, wing_l, head, wing_r.

## Personality, pose and expression

- Personality: dazzling and fearless, a pocket-sized emerald rocket.
- Pose: hovering mid-air with swept-back wings and tail fanned slightly, needle bill poised forward.
- Expression: bright dark bead eyes above a shimmering ruby-red throat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 5 to 14 | -3 to 3 | 5 to 13 |  |
| tail | 0 to 5 | -3 to 3 | 2 to 6 | turned ry +18°; on body |
| wing_l | 6 to 11 | -12 to -3 | 11 to 13 | turned rx +18°, ry -12°, rz +14°; on body |
| head | 9 to 24 | -3 to 3 | 13 to 18 | turned rx +3°, ry +4°, rz -8°; on body |
| wing_r | 6 to 11 | 3 to 12 | 11 to 13 | turned rx -18°, ry -12°, rz -14°; on body |

## Recognisable features (in order of importance)

1. the iridescent emerald-green back and crown
2. the glowing ruby-red throat patch
3. the long needle-thin black bill
4. the crisp off-white belly
5. the swept-back wings and forked tail

## Colour map

- `back`: iridescent metallic emerald-green crown, back and wings
- `throat`: iridescent ruby-red gorget on the male's throat
- `belly`: soft off-white breast and belly
- `beak`: needle-thin straight black nectar bill and forked tail
- `eye`: tiny dark eyes and minuscule feet

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
