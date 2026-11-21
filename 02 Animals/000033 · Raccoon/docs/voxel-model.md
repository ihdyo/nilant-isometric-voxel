# 000033 · Raccoon · voxel brief

*Procyon lotor* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#A6A09B` | arched furry body, head, legs and tail base |
| `mask` | `#171717` | iconic black bandit eye mask, tail rings and nose |
| `trim` | `#FAFAF9` | white muzzle, eyebrows, ear edges and tail rings |
| `dark` | `#57534D` | charcoal back shading and nimble paws |
| `white` | `#FAFAF9` | eye sclera highlight |
| `eye` | `#1C1917` | dark mischievous eyes |

Background (not modelled): `#D5CEF9` (soft lilac).

## Size and pose

- Size: 34 × 14 × 18 voxels posed (L × W × H); longest side 34, budget 30–38 (target 34) from the real size 0.8 m (nose to tail tip, about 0.8 m (body 40–70 cm plus 20–40 cm ringed tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: clever and inquisitive, always inspecting things with nimble paws.
- Pose: a slightly humped woodland amble, ringed bushy tail held out behind, masked head turned toward the viewer.
- Expression: bright dark eyes set inside a bold black bandit mask with white cheek trim.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 14 to 16 | -4 to -2 | 0 to 5 | turned ry -12°; on body |
| leg_fr | 14 to 16 | 2 to 4 | 0 to 5 | turned ry +6°; on body |
| leg_hl | 2 to 4 | -4 to -2 | 0 to 6 | turned ry +10°; on body |
| leg_hr | 2 to 4 | 2 to 4 | 0 to 6 | on body |
| body | 1 to 17 | -4 to 4 | 5 to 13 |  |
| tail | -10 to 0 | -2 to 2 | 7 to 10 | turned ry -10°, rz -6°; on body |
| head | 16 to 23 | -4 to 4 | 8 to 15 | turned rx +4°, ry +3°, rz -10°; on body |
| ear_l | 17 to 18 | -4 to -2 | 15 to 17 | on head |
| ear_r | 17 to 18 | 2 to 4 | 15 to 17 | on head |

## Recognisable features (in order of importance)

1. distinctive black bandit mask outlined in white fur
2. bushy tail with alternating dark and pale rings
3. hunched, rounded back with grizzled grey fur
4. dexterous dark five-toed front paws
5. white-rimmed rounded ears

## Colour map

- `coat`: arched furry body, head, legs and tail base
- `mask`: iconic black bandit eye mask, tail rings and nose
- `trim`: white muzzle, eyebrows, ear edges and tail rings
- `dark`: charcoal back shading and nimble paws
- `white`: eye sclera highlight
- `eye`: dark mischievous eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult raccoon profile reference (CC BY-SA 3.0)
