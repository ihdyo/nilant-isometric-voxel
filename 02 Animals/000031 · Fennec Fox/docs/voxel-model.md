# 000031 · Fennec Fox · voxel brief

*Vulpes zerda* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `coat` | `#FEE685` | small body, head, outer ears, legs and bushy tail |
| `ear_in` | `#FFCCD3` | warm pinkish-cream inner surfaces of the giant ears |
| `belly` | `#FAFAF9` | face mask, throat, chest and underbelly |
| `tip` | `#171717` | black tail tip and tiny black nose |
| `white` | `#FAFAF9` | the white of each eye |
| `eye` | `#1C1917` | large dark desert-adapted eyes |

Background (not modelled): `#D3C89C` (soft straw).

## Size and pose

- Size: 28 × 14 × 24 voxels posed (L × W × H); longest side 28, budget 24–32 (target 28) from the real size 0.65 m (nose to tail tip, about 0.65 m (body 24–41 cm plus 18–31 cm tail per ADW)).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, tail, head, ear_l, ear_r.

## Personality, pose and expression

- Personality: curious and bright-eyed, listening to every rustle in the dunes.
- Pose: a light, nimble desert trot, giant bat-like ears angled outward, fluffy black-tipped tail held up and head tilted toward the camera.
- Expression: big dark eyes on a cream face mask with a tiny black nose.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 12 to 13 | -3 to -2 | 0 to 5 | turned ry -12°; on body |
| leg_fr | 12 to 13 | 2 to 3 | 0 to 5 | turned ry +8°; on body |
| leg_hl | 2 to 3 | -3 to -2 | 0 to 5 | turned ry +10°; on body |
| leg_hr | 2 to 3 | 2 to 3 | 0 to 5 | on body |
| body | 1 to 14 | -3 to 3 | 5 to 10 |  |
| tail | -8 to 0 | -1 to 1 | 7 to 10 | turned ry -22°, rz -10°; on body |
| head | 13 to 19 | -4 to 4 | 8 to 15 | turned rx +5°, ry +2°, rz -10°; on body |
| ear_l | 14 to 16 | -6 to -2 | 15 to 23 | turned rz +14°; on head |
| ear_r | 14 to 16 | 2 to 6 | 15 to 23 | turned rz -14°; on head |

## Recognisable features (in order of importance)

1. enormous triangular ears nearly half as tall as the body
2. petite sandy-cream body and delicate legs
3. fluffy bushy tail with a black tip
4. pointed muzzle and large dark eyes
5. pale cream face mask and chest

## Colour map

- `coat`: small body, head, outer ears, legs and bushy tail
- `ear_in`: warm pinkish-cream inner surfaces of the giant ears
- `belly`: face mask, throat, chest and underbelly
- `tip`: black tail tip and tiny black nose
- `white`: the white of each eye
- `eye`: large dark desert-adapted eyes

## Photos used

- `assets/photos/01-side-profile.jpg`: adult fennec fox profile reference (CC BY 2.0)
