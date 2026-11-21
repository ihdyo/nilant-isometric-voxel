# 000062 · Eurasian Red Squirrel · voxel brief

*Sciurus vulgaris* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#F54900` | bright rufous-chestnut back, head and plume tail |
| `belly` | `#FAFAF9` | crisp white chest and belly |
| `tuft` | `#9F2D00` | long winter ear tufts and darker tail tip |
| `paw` | `#FEE685` | delicate grasping paws and muzzle |
| `eye` | `#171717` | large glossy black eyes and nose |

Background (not modelled): `#EBD0A9` (soft sand).

## Size and pose

- Size: 18 × 10 × 27 voxels rest (L × W × H); longest side 27, budget 48–56 (target 56) from the real size 0.42 m (total length, 34–43 cm including bushy tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, leg_hl, arm_l, head, ear_l, arm_r, ear_r.

## Personality, pose and expression

- Personality: nimble and spirited, acrobat of the pine canopy.
- Pose: perched upright on hind paws holding an acorn, huge fluffy tail curled behind in an S-curve.
- Expression: big glossy black eyes, twitching whiskers and tall tufted ears.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 6 to 15 | -4 to 4 | 3 to 14 |  |
| tail | 0 to 7 | -3 to 3 | 2 to 21 | turned ry -8°; on body |
| leg_hl | 8 to 14 | -5 to -3 | 0 to 3 | on body |
| arm_l | 13 to 17 | -4 to -2 | 10 to 13 | turned ry +10°, rz +14°; on body |
| head | 8 to 16 | -4 to 4 | 14 to 21 | turned rx +4°, ry +4°, rz -10°; on body |
| ear_l | 9 to 11 | -4 to -2 | 21 to 26 | turned rx -6°, rz +8°; on head |
| arm_r | 13 to 17 | 2 to 4 | 10 to 13 | turned ry +10°, rz -14°; on body |
| ear_r | 9 to 11 | 2 to 4 | 21 to 26 | turned rx +6°, rz -8°; on head |

## Recognisable features (in order of importance)

1. the huge fluffy rufous tail curled up behind the back
2. the tall winter ear tufts
3. the crisp white chest and belly
4. the delicate front paws clutching a nut
5. the bright chestnut coat

## Colour map

- `coat`: bright rufous-chestnut back, head and plume tail
- `belly`: crisp white chest and belly
- `tuft`: long winter ear tufts and darker tail tip
- `paw`: delicate grasping paws and muzzle
- `eye`: large glossy black eyes and nose

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
