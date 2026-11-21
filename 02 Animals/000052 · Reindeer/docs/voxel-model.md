# 000052 · Reindeer · voxel brief

*Rangifer tarandus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#79716B` | back, flanks and face |
| `ruff` | `#F5F5F4` | creamy white neck mane, rump and belly |
| `antler` | `#FEE685` | tall branching antlers with brow tines |
| `hoof` | `#262626` | broad snowshoe hooves and nose |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#171717` | the pupils |

Background (not modelled): `#A6E0E7` (soft aqua).

## Size and pose

- Size: 36 × 19 × 42 voxels rest (L × W × H); longest side 42, budget 48–56 (target 56) from the real size 2.0 m (head-and-body length, 1.6–2.2 m).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, shin_hl, leg_fl, shin_fl, tail, head, ear_l, antler_l, ear_r, antler_r.

## Personality, pose and expression

- Personality: resilient and spirited, tireless traveller of the frozen north.
- Pose: a brisk trot, branching antlers swept back, white chest ruff puffed out.
- Expression: bright alert eyes and a fuzzy dark nose.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 1 to 25 | -6 to 6 | 12 to 24 |  |
| leg_hl | 3 to 5 | -5 to -3 | 6 to 12 | turned ry +12°; on body |
| shin_hl | 2 to 6 | -6 to -2 | 0 to 5 | on leg_hl |
| leg_fl | 19 to 21 | -5 to -3 | 6 to 12 | turned ry -14°; on body |
| shin_fl | 18 to 22 | -6 to -2 | 0 to 5 | on leg_fl |
| tail | 0 to 1 | -1 to 1 | 19 to 22 | turned rx -12°; on body |
| head | 23 to 35 | -4 to 4 | 21 to 29 | turned rx +4°, ry +4°, rz -8°; on body |
| ear_l | 24 to 26 | -6 to -4 | 29 to 32 | turned rz +16°; on head |
| antler_l | 22 to 32 | -9 to -4 | 30 to 41 | turned ry -8°, rz +8°; on head |
| ear_r | 24 to 26 | 4 to 6 | 29 to 32 | turned rz -16°; on head |
| antler_r | 22 to 32 | 4 to 9 | 30 to 41 | turned ry -8°, rz -8°; on head |

## Recognisable features (in order of importance)

1. the tall multi-pointed branching antlers
2. the fluffy white chest and neck ruff
3. the broad crescent snowshoe hooves
4. the fur-covered muzzle
5. the short white-edged tail

## Colour map

- `coat`: back, flanks and face
- `ruff`: creamy white neck mane, rump and belly
- `antler`: tall branching antlers with brow tines
- `hoof`: broad snowshoe hooves and nose
- `white`: the white of each eye
- `eye`: the pupils

## Photos used

- `assets/photos/01-side.jpg`: adult profile reference (Wikimedia Commons, CC0 / CC BY)
