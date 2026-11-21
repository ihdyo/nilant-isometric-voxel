# 000055 · Red Kangaroo · voxel brief

*Osphranter rufus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#F54900` | rusty red-brown back, head and muscular tail |
| `belly` | `#FEF3C6` | pale cream chest, belly and inner limbs |
| `muzzle` | `#D6D3D1` | pale grey-white muzzle stripe and inner ears |
| `claw` | `#262626` | toes, claws and nose |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#171717` | the pupils |

Background (not modelled): `#EECEAA` (soft sand).

## Size and pose

- Size: 24 × 14 × 40 voxels rest (L × W × H); longest side 40, budget 48–56 (target 56) from the real size 2.4 m (head-and-body 1.3–1.6 m plus tail 1.0–1.2 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, tail, leg_hl, foot_hl, arm_l, head, ear_l, arm_r, ear_r.

## Personality, pose and expression

- Personality: energetic and alert, spring-loaded sprinter of the red centre.
- Pose: upright poised stance balanced on long hind feet and heavy tail, ears perked forward.
- Expression: bright curious eyes and a twitching nose.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 8 to 19 | -5 to 5 | 9 to 25 |  |
| tail | 0 to 8 | -2 to 2 | 2 to 11 | turned ry +8°; on body |
| leg_hl | 9 to 15 | -7 to -4 | 4 to 12 | turned ry -10°; on body |
| foot_hl | 11 to 22 | -7 to -4 | 0 to 2 | on leg_hl |
| arm_l | 16 to 21 | -6 to -4 | 18 to 22 | turned ry +18°; on body |
| head | 12 to 23 | -4 to 4 | 25 to 32 | turned rx +4°, ry +4°, rz -10°; on body |
| ear_l | 13 to 15 | -4 to -2 | 32 to 39 | turned rx -8°, ry +6°, rz +8°; on head |
| arm_r | 16 to 21 | 4 to 6 | 18 to 22 | turned ry +18°; on body |
| ear_r | 13 to 15 | 2 to 4 | 32 to 39 | turned rx +8°, ry +6°, rz -8°; on head |

## Recognisable features (in order of importance)

1. the huge hind legs and long narrow feet
2. the thick muscular balancing tail
3. the tall pointed ears
4. the short forepaws held near the chest
5. the pale cream belly

## Colour map

- `coat`: rusty red-brown back, head and muscular tail
- `belly`: pale cream chest, belly and inner limbs
- `muzzle`: pale grey-white muzzle stripe and inner ears
- `claw`: toes, claws and nose
- `white`: the white of each eye
- `eye`: the pupils

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
