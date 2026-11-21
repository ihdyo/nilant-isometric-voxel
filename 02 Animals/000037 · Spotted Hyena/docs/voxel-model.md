# 000037 · Spotted Hyena · voxel brief

*Crocuta crocuta* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#FFD230` | sloping muscular torso, neck, head and long front legs |
| `spot` | `#44403B` | irregular dark brown-black spots on flanks and legs |
| `muzzle` | `#292524` | broad dark snout, lower legs and bushy tail tip |
| `mane` | `#E17100` | coarse erectile neck-and-shoulder crest |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#1C1917` | dark alert eyes |

Background (not modelled): `#DBD6A9` (soft straw).

## Size and pose

- Size: 38 × 15 × 24 voxels posed (L × W × H); longest side 38, budget 34–42 (target 38) from the real size 1.6 m (nose to tail tip, about 1.6 m (body 95–165 cm plus 25–36 cm tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: bold and tenacious, trotting across the open savanna.
- Pose: characteristic sloped-back lope with tall muscular shoulders, lower hindquarters, rounded ears upright and head angled toward the viewer.
- Expression: dark inquisitive eyes, broad charcoal snout and upright rounded ears.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 17 to 19 | -4 to -2 | 0 to 9 | turned ry -12°; on body |
| leg_fr | 17 to 19 | 2 to 4 | 0 to 9 | turned ry +6°; on body |
| leg_hl | 2 to 4 | -4 to -2 | 0 to 7 | turned ry +10°; on body |
| leg_hr | 2 to 4 | 2 to 4 | 0 to 7 | on body |
| body | 1 to 21 | -4 to 4 | 7 to 17 |  |
| tail | -7 to 0 | -1 to 1 | 11 to 13 | turned ry +25°; on body |
| head | 20 to 28 | -4 to 4 | 14 to 21 | turned rx +4°, ry +3°, rz -10°; on body |
| ear_l | 21 to 23 | -4 to -2 | 21 to 23 | on head |
| ear_r | 21 to 23 | 2 to 4 | 21 to 23 | on head |

## Recognisable features (in order of importance)

1. distinctive sloping profile with taller front legs than hind legs
2. thick muscular neck and broad dark muzzle
3. sandy-tan coat patterned with irregular dark spots
4. large rounded ears set high on the head
5. short dark-tipped tail

## Colour map

- `coat`: sloping muscular torso, neck, head and long front legs
- `spot`: irregular dark brown-black spots on flanks and legs
- `muzzle`: broad dark snout, lower legs and bushy tail tip
- `mane`: coarse erectile neck-and-shoulder crest
- `white`: the white of each eye
- `eye`: dark alert eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult spotted hyena profile reference (CC BY 4.0)
