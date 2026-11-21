# 000038 · Bornean Orangutan · voxel brief

*Pongo pygmaeus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#CA3500` | long shaggy reddish-orange hair on torso, long arms and legs |
| `skin` | `#292524` | dark grey-brown face, cheek flanges, chest patch, hands and feet |
| `beard` | `#FF6900` | brighter copper-orange beard and shoulder fringe |
| `shade` | `#7E2A0C` | deep russet shading under arms and torso |
| `white` | `#FAFAF9` | eye sclera highlight |
| `eye` | `#1C1917` | expressive dark brown eyes |

Background (not modelled): `#EECEAA` (soft sand).

## Size and pose

- Size: 22 × 22 × 28 voxels posed (L × W × H); longest side 28, budget 24–32 (target 28) from the real size 1.4 m (standing height about 1.2–1.4 m (adult males 1.2–1.4 m tall with arm span over 2 m per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_l, leg_r, body, arm_l, arm_r, head.

## Personality, pose and expression

- Personality: gentle and thoughtful, red-haired sage of Borneo's treetops.
- Pose: a relaxed, semi-upright knuckle-supported stance with extra-long arms reaching nearly to the ground and bearded head tilted warmly toward the camera.
- Expression: kind dark eyes set in a dark-skinned flanged face framed by shaggy copper-orange hair.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_l | 3 to 7 | -6 to -3 | 0 to 6 | on body |
| leg_r | 3 to 7 | 3 to 6 | 0 to 6 | on body |
| body | 1 to 11 | -7 to 7 | 6 to 20 |  |
| arm_l | 7 to 11 | -10 to -7 | 1 to 19 | turned rx +8°, ry -12°; on body |
| arm_r | 7 to 11 | 7 to 10 | 1 to 19 | turned rx -8°, ry +6°; on body |
| head | 5 to 13 | -6 to 6 | 20 to 28 | turned rx +4°, ry +3°, rz -10°; on body |

## Recognisable features (in order of importance)

1. extra-long shaggy arms reaching down to the ankles
2. rich reddish-orange coat with long shoulder fringes
3. dark grey-brown face with broad cheek pads (flanges)
4. stocky barrel-shaped torso and short curved legs
5. copper-orange chin beard

## Colour map

- `coat`: long shaggy reddish-orange hair on torso, long arms and legs
- `skin`: dark grey-brown face, cheek flanges, chest patch, hands and feet
- `beard`: brighter copper-orange beard and shoulder fringe
- `shade`: deep russet shading under arms and torso
- `white`: eye sclera highlight
- `eye`: expressive dark brown eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult bornean orangutan profile reference (CC BY 3.0)
