# 000039 · Western Gorilla · voxel brief

*Gorilla gorilla* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#171717` | massive muscular torso, thick arms, legs and domed head |
| `silver` | `#D6D3D1` | characteristic silver-grey saddle across the back and hips |
| `skin` | `#292524` | broad brow ridge, wide nostrils, ears and knuckles |
| `chest` | `#44403B` | broad bare charcoal-grey chest |
| `white` | `#FAFAF9` | eye sclera highlight |
| `eye` | `#7B3306` | deep warm brown eyes |

Background (not modelled): `#B0E1CA` (soft mint).

## Size and pose

- Size: 26 × 24 × 30 voxels posed (L × W × H); longest side 30, budget 26–34 (target 30) from the real size 1.7 m (standing height about 1.6–1.75 m for an adult silverback (1.4–1.8 m per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_l, leg_r, body, arm_l, arm_r, head.

## Personality, pose and expression

- Personality: dignified and protective, calm guardian of the forest family.
- Pose: a powerful knuckle-walking stance with broad silverback shoulders hunched forward, thick arms planted and crested head turned toward the viewer.
- Expression: calm dark eyes beneath a prominent brow ridge and wide nostrils.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_l | 2 to 7 | -7 to -3 | 0 to 7 | on body |
| leg_r | 2 to 7 | 3 to 7 | 0 to 7 | on body |
| body | 0 to 14 | -8 to 8 | 7 to 22 |  |
| arm_l | 10 to 15 | -11 to -8 | 0 to 21 | turned rx +6°, ry -10°; on body |
| arm_r | 10 to 15 | 8 to 11 | 0 to 21 | turned rx -6°, ry +5°; on body |
| head | 8 to 17 | -6 to 6 | 22 to 30 | turned rx +3°, ry +3°, rz -10°; on body |

## Recognisable features (in order of importance)

1. broad silver-grey saddle across the back and flanks
2. massive muscular chest and thick knuckle-walking arms
3. domed sagittal-crest head with heavy brow ridge
4. short sturdy legs planted wide
5. charcoal-black coat contrasting with slate-grey skin

## Colour map

- `coat`: massive muscular torso, thick arms, legs and domed head
- `silver`: characteristic silver-grey saddle across the back and hips
- `skin`: broad brow ridge, wide nostrils, ears and knuckles
- `chest`: broad bare charcoal-grey chest
- `white`: eye sclera highlight
- `eye`: deep warm brown eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult western gorilla profile reference (CC BY 4.0)
