# 000042 · Proboscis Monkey · voxel brief

*Nasalis larvatus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#FF6900` | cinnamon-orange cap, back and shoulders |
| `face` | `#FFA1AD` | pinkish-tan bare face and famous oversized pendulous nose |
| `pants` | `#E7E5E4` | pale grey-white lower limbs and long white tail |
| `belly` | `#FEF3C6` | creamy-buff pot-belly and chest |
| `white` | `#FAFAF9` | eye sclera highlight |
| `eye` | `#1C1917` | dark round eyes |

Background (not modelled): `#A9E2D6` (soft mint).

## Size and pose

- Size: 34 × 14 × 24 voxels posed (L × W × H); longest side 34, budget 30–38 (target 34) from the real size 1.35 m (head to tail tip, about 1.35 m for an adult male (body 66–76 cm plus 55–75 cm white tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, nose.

## Personality, pose and expression

- Personality: quirky and noble, proud river-bank sentinel of Borneo.
- Pose: an upright-chested riverside stance with rounded pot-belly, pale grey limbs, long white tail curving behind and famous pendulous nose prominent in profile.
- Expression: calm dark eyes beneath a russet hair cap with a large, bulbous pinkish-tan nose.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 12 to 14 | -4 to -2 | 0 to 7 | turned ry -10°; on body |
| leg_fr | 12 to 14 | 2 to 4 | 0 to 7 | turned ry +6°; on body |
| leg_hl | 2 to 4 | -4 to -2 | 0 to 7 | turned ry +8°; on body |
| leg_hr | 2 to 4 | 2 to 4 | 0 to 7 | on body |
| body | 1 to 15 | -4 to 4 | 7 to 16 |  |
| tail | -12 to 0 | -1 to 1 | 11 to 13 | turned ry +14°; on body |
| head | 13 to 19 | -4 to 4 | 15 to 22 | turned rx +4°, ry +3°, rz -10°; on body |
| nose | 20 to 22 | -1 to 1 | 14 to 19 | on head |

## Recognisable features (in order of importance)

1. large, bulbous, pendulous pinkish-tan nose
2. cinnamon-orange cap and mantle over pale grey limbs
3. prominent rounded pot-belly from its four-chambered stomach
4. long, slender white tail
5. pinkish bare face framed by buff cheek fur

## Colour map

- `coat`: cinnamon-orange cap, back and shoulders
- `face`: pinkish-tan bare face and famous oversized pendulous nose
- `pants`: pale grey-white lower limbs and long white tail
- `belly`: creamy-buff pot-belly and chest
- `white`: eye sclera highlight
- `eye`: dark round eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult proboscis monkey profile reference (CC BY 4.0)
