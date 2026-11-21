# 000043 · Spectral Tarsier · voxel brief

*Tarsius tarsier* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#A6A09B` | soft velvety grey-buff fur on body, head and limbs |
| `ear` | `#FFCCD3` | large thin membranous bat-like ears |
| `belly` | `#E7E5E4` | pale buff chest and underbelly |
| `finger` | `#FFA1AD` | elongated suction-pad fingers, toes and naked tail shaft |
| `white` | `#FAFAF9` | eye sclera rim |
| `eye` | `#FE9A00` | enormous golden-amber nocturnal eyes |

Background (not modelled): `#C7D2FD` (soft lavender).

## Size and pose

- Size: 22 × 13 × 22 voxels posed (L × W × H); longest side 22, budget 20–26 (target 22) from the real size 0.35 m (nose to tail tip, about 0.35 m (body 9.5–14 cm plus 20–26 cm tufted tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_hl, leg_hr, body, arm_l, arm_r, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: wide-eyed and spring-loaded, tiny nocturnal acrobat of Sulawesi.
- Pose: an upright clinging-and-leaping stance with long folded hind legs, slender tufted tail propping behind and oversized head swiveled toward the viewer.
- Expression: enormous golden-amber eyes dominating a tiny round face with large bat-like ears.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_hl | 1 to 5 | -4 to -2 | 0 to 6 | on body |
| leg_hr | 1 to 5 | 2 to 4 | 0 to 6 | on body |
| body | 0 to 7 | -3 to 3 | 4 to 13 |  |
| arm_l | 5 to 8 | -4 to -3 | 8 to 12 | turned rx +12°; on body |
| arm_r | 5 to 8 | 3 to 4 | 8 to 12 | turned rx -12°; on body |
| tail | -12 to 0 | -1 to 1 | 3 to 5 | turned ry +12°; on body |
| head | 0 to 8 | -4 to 4 | 13 to 20 | turned rx +4°, ry -4°, rz -16°; on body |
| ear_l | 3 to 5 | -6 to -4 | 17 to 21 | turned rz +15°; on head |
| ear_r | 3 to 5 | 4 to 6 | 17 to 21 | turned rz -15°; on head |

## Recognisable features (in order of importance)

1. enormous forward-facing golden eyes
2. large thin membranous ears
3. long elongated hind legs and slender pad-tipped fingers
4. long thin naked tail with a furry tuft at the tip
5. compact round body covered in velvety grey-buff fur

## Colour map

- `coat`: soft velvety grey-buff fur on body, head and limbs
- `ear`: large thin membranous bat-like ears
- `belly`: pale buff chest and underbelly
- `finger`: elongated suction-pad fingers, toes and naked tail shaft
- `white`: eye sclera rim
- `eye`: enormous golden-amber nocturnal eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult spectral tarsier profile reference (CC BY 2.0)
