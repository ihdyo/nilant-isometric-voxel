# 26-001 · Red Fox · voxel brief

*Vulpes vulpes* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `fur` | `orange-600` | body, head, tail, upper legs |
| `white` | `stone-50` | tail tip, chest bib, cheeks and jaw, the underside of the snout, the outer half of each eye |
| `dark` | `stone-800` | lower legs (stockings), ear tips, nose |
| `eye` | `neutral-950` | the dark inner half of each two-voxel eye on the front of the head |

Background (not modelled): `teal-200`.

## Size and pose

- Size: 32 × 14 × 23 voxels posed (L × W × H); longest side 32, budget 25–33 (target 29) from the real size 1.1 m (nose to tail tip: head and body 46–90 cm plus tail 30–56 cm, mid-range).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, tail, tail_tip, head, snout, ear_l, ear_r.

## Personality, pose and expression

- Personality: clever and sly.
- Pose: head turned to the camera and cocked, ears perked forward, tail raised, the front left paw lifted mid-sneak.
- Expression: white eyes with the pupils to the inside, one brow slanting down to the middle and the other raised, a crooked smirk, all painted flat on the face.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 10 to 12 | -4 to -2 | 0 to 5 | turned ry +24°; on body |
| leg_fr | 10 to 12 | 2 to 4 | 0 to 5 | turned ry -6°; on body |
| leg_hl | 1 to 3 | -4 to -2 | 0 to 5 | turned ry -8°; on body |
| leg_hr | 1 to 3 | 2 to 4 | 0 to 5 | turned ry +6°; on body |
| body | 0 to 13 | -4 to 4 | 6 to 12 |  |
| tail | -4 to -1 | -2 to 2 | 8 to 12 | turned ry +18°, rz +8°; on body |
| tail_tip | -7 to -5 | -2 to 2 | 8 to 12 | turned ry +12°; on tail |
| head | 13 to 20 | -5 to 5 | 9 to 17 | turned rx +8°, ry -4°, rz -16°; on body |
| snout | 21 to 23 | -2 to 2 | 9 to 12 | on head |
| ear_l | 15 to 16 | -5 to -3 | 18 to 21 | turned rx +12°, ry +10°; on head |
| ear_r | 15 to 16 | 3 to 5 | 18 to 21 | turned rx -12°, ry +10°; on head |

## Recognisable features (in order of importance)

1. the long bushy tail with a white tip, as long as half the body
2. big pointed ears with black tips
3. a long narrow snout with a black nose
4. the white bib and white cheeks
5. black stockings on the legs

## Colour map

- `fur`: body, head, tail, upper legs
- `white`: tail tip, chest bib, cheeks and jaw, the underside of the snout, the outer half of each eye
- `dark`: lower legs (stockings), ear tips, nose
- `eye`: the dark inner half of each two-voxel eye on the front of the head

## Photos used

- `assets/photos/01-side-standing.jpg`: adult standing, left flank, head right (CC BY 4.0)
- `assets/photos/02-three-quarter.jpg`: adult three-quarter front, ears and white chest (CC BY 4.0)
