# 26-006 · American Flamingo · voxel brief

*Phoenicopterus ruber* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `pink` | `rose-400` | body |
| `light` | `rose-200` | neck and head |
| `black` | `neutral-900` | rear edge of the wings, bill tip |
| `bill` | `rose-100` | pale bill base |
| `legs` | `rose-500` | legs and feet |
| `feet` | `rose-700` | the webbed feet, a shade darker than the legs so they read on the ground |
| `eye` | `amber-300` | one voxel on each side of the head |

Background (not modelled): `emerald-200`.

## Size and pose

- Size: 16 × 11 × 34 voxels posed (L × W × H); longest side 34, budget 26–34 (target 30) from the real size 1.2 m (standing height about 1.2 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: foot_l, foot_r, shin_l, shin_r, leg_l, leg_r, body, wing_l, wing_r, neck, beak, head.

## Personality, pose and expression

- Personality: elegant and a little snooty.
- Pose: standing on one leg, the other (the camera side) lifted and bent at the knee with the toes curled down, both legs built the same (an upper and a lower part on a webbed foot one voxel thick) so it can walk on them, a long straight neck rising from the front of a bulky body, chin up, the big bill bent down, wings lifted at the back.
- Expression: a half-lidded amber eye, the pink lid painted over its top half.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| foot_l | 5 to 7 | -3 to -1 | 0 to 0 | turned ry +34°; on shin_l |
| foot_r | 5 to 7 | 1 to 3 | 0 to 0 | turned rz +8°; on shin_r |
| shin_l | 6 to 6 | -2 to -2 | 1 to 5 | turned ry +40°; on leg_l |
| shin_r | 6 to 6 | 2 to 2 | 1 to 5 | on leg_r |
| leg_l | 6 to 6 | -2 to -2 | 6 to 11 | turned ry -38°; on body |
| leg_r | 6 to 6 | 2 to 2 | 6 to 11 | on body |
| body | 0 to 10 | -4 to 4 | 12 to 18 |  |
| wing_l | 0 to 8 | -5 to -5 | 13 to 18 | turned ry +14°; on body |
| wing_r | 0 to 8 | 5 to 5 | 13 to 18 | turned ry +14°; on body |
| neck | 8 to 9 | -1 to 1 | 19 to 28 | turned ry -6°; on body |
| beak | 13 to 16 | -1 to 1 | 27 to 31 | turned ry +24°; on head |
| head | 7 to 12 | -2 to 2 | 29 to 32 | turned rx +10°, ry -10°, rz -6°; on neck |

## Recognisable features (in order of importance)

1. the long S-shaped neck
2. long thin pink legs with the backward-bending ankle
3. the bent bill with a black tip
4. the egg-shaped pink body
5. black flight feathers along the rear edge

## Colour map

- `pink`: body
- `light`: neck and head
- `black`: rear edge of the wings, bill tip
- `bill`: pale bill base
- `legs`: legs and feet
- `feet`: the webbed feet, a shade darker than the legs so they read on the ground
- `eye`: one voxel on each side of the head

## Photos used

- `assets/photos/01-head.jpg`: adult head and neck, bent bill (CC0)
- `assets/photos/02-standing.jpg`: adult standing, full body, long legs (CC0)
