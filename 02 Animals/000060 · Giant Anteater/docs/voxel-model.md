# 000060 · Giant Anteater · voxel brief

*Myrmecophaga tridactyla* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#57534D` | coarse grizzled grey-brown body and head |
| `stripe` | `#171717` | bold black wedge stripe on chest and shoulders |
| `trim` | `#F5F5F4` | crisp white border along the shoulder stripe and front legs |
| `tail` | `#44403B` | massive long-haired plumed tail |
| `eye` | `#171717` | small dark eyes and nostrils |

Background (not modelled): `#E0D5A8` (soft straw).

## Size and pose

- Size: 49 × 11 × 21 voxels rest (L × W × H); longest side 49, budget 48–56 (target 56) from the real size 2.1 m (total length, 1.8–2.4 m including bushy tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, leg_hl, leg_fl, head.

## Personality, pose and expression

- Personality: focused and eccentric, methodical termite-mound inspector.
- Pose: a knuckle-walking stride, long tubular snout sweeping low, huge bushy tail streaming behind.
- Expression: small earnest eyes set high on a remarkably long slender snout.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 12 to 32 | -5 to 5 | 9 to 20 |  |
| tail | 0 to 12 | -4 to 4 | 4 to 18 | turned ry -6°; on body |
| leg_hl | 14 to 17 | -5 to -3 | 0 to 9 | on body |
| leg_fl | 27 to 30 | -5 to -3 | 0 to 9 | turned ry -12°; on body |
| head | 32 to 48 | -3 to 3 | 11 to 18 | turned rx +3°, ry +10°, rz -8°; on body |

## Recognisable features (in order of importance)

1. the extremely long slender tubular snout
2. the huge plumed broom-like tail
3. the bold black shoulder wedge bordered in white
4. the white front legs with tucked digging claws
5. the small rounded ears

## Colour map

- `coat`: coarse grizzled grey-brown body and head
- `stripe`: bold black wedge stripe on chest and shoulders
- `trim`: crisp white border along the shoulder stripe and front legs
- `tail`: massive long-haired plumed tail
- `eye`: small dark eyes and nostrils

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
