# 26-013 · Toco Toucan · voxel brief

*Ramphastos toco* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (Tailwind token or #hex) | Where |
|---|---|---|
| `body` | `neutral-900` | body, wings, tail, the back of the head, the black tip of the bill |
| `throat` | `stone-50` | the white throat and cheeks |
| `bill` | `yellow-400` | the big bill |
| `ring` | `orange-400` | the bare orange skin around each eye |
| `eye` | `sky-500` | the blue eye skin |
| `vent` | `red-600` | the red patch under the tail |
| `feet` | `slate-400` | the blue-grey legs and feet |

Background (not modelled): `blue-200` (rendered as a calm pastel).

## Size and pose

- Size: 23 × 11 × 21 voxels posed (L × W × H); longest side 23, budget 20–26 (target 23) from the real size 0.61 m (bill tip to tail tip: about 61 cm, a third of it bill).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: foot_l, foot_r, leg_l, leg_r, body, wing_l, wing_r, tail, beak, head.

## Personality, pose and expression

- Personality: cheerful, chatty and curious.
- Pose: hopping on the ground with the head cocked and the big bill tilted up, the tail raised, one wing lifted a little.
- Expression: round blue eyes in their orange rings, wide and curious, painted flat.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| foot_l | 3 to 6 | -3 to -1 | 0 to 0 | on leg_l |
| foot_r | 3 to 6 | 1 to 3 | 0 to 0 | on leg_r |
| leg_l | 4 to 4 | -2 to -2 | 1 to 4 | on body |
| leg_r | 4 to 4 | 2 to 2 | 1 to 4 | on body |
| body | 0 to 7 | -3 to 3 | 5 to 13 |  |
| wing_l | 1 to 6 | -4 to -4 | 7 to 13 | turned rx -16°; on body |
| wing_r | 1 to 6 | 4 to 4 | 7 to 13 | on body |
| tail | -5 to -1 | -2 to 2 | 9 to 11 | turned ry +20°; on body |
| beak | 10 to 17 | -2 to 2 | 14 to 18 | turned ry -10°; on head |
| head | 3 to 9 | -3 to 3 | 14 to 19 | turned rx +14°, ry -4°, rz -12°; on body |

## Recognisable features (in order of importance)

1. the huge orange bill with a black tip
2. the white throat on a black body
3. the blue eye in an orange ring
4. the red patch under the tail
5. blue-grey legs and feet

## Colour map

- `body`: body, wings, tail, the back of the head, the black tip of the bill
- `throat`: the white throat and cheeks
- `bill`: the big bill
- `ring`: the bare orange skin around each eye
- `eye`: the blue eye skin
- `vent`: the red patch under the tail
- `feet`: the blue-grey legs and feet

## Photos used

- `assets/photos/01-side.jpg`: adult on the ground, left side, bill, throat and red vent (CC BY 4.0)
- `assets/photos/02-perched.jpg`: adult perched on a branch, three-quarter front (CC0)
