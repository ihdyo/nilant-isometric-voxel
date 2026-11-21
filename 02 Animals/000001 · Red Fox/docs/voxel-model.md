# 000001 · Red Fox · voxel brief

*Vulpes vulpes* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour | Where |
|---|---|---|
| `fur` | `#F54900` | body, head, tail, upper legs |
| `white` | `#FAFAF9` | tail tip, chest bib, cheeks and jaw, the underside of the snout, the outer half of each eye |
| `dark` | `#292524` | lower legs (stockings), ear tips, nose |
| `eye` | `#0A0A0A` | the dark inner half of each two-voxel eye on the front of the head |

Background (not modelled): `#A7E1DD` (forest-mist teal).

## Size and pose

- Size: 32 × 14 × 22 voxels posed (L × W × H); longest side 32, budget 25–33 (target 29) from the real size 1.1 m (nose to tail tip: head and body 46–90 cm plus tail 30–56 cm, mid-range).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: body, leg_hl, leg_fl, head, snout, ear_l, tail, tail_tip, leg_hr, leg_fr, ear_r.

## Personality, pose and expression

- Personality: clever and sly.
- Pose: Sneaking, the front left paw lifted and folded back, the head low and turned to the camera, the ears perked, one tipped back, the tail raised in a curve.
- Expression: white eyes with the pupils to the inside, one brow slanting down to the middle and the other raised, a crooked smirk, all painted flat on the face.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| body | 0 to 13 | -4 to 4 | 6 to 12 |  |
| leg_hl | 1 to 3 | -4 to -2 | 0 to 5 | turned ry -16°; on body |
| leg_fl | 10 to 12 | -4 to -2 | 0 to 5 | turned ry +34°; on body |
| head | 13 to 20 | -5 to 5 | 9 to 17 | turned rx +3°, ry +8°, rz -16°; on body |
| snout | 21 to 23 | -2 to 2 | 9 to 12 | on head |
| ear_l | 15 to 16 | -5 to -3 | 18 to 21 | turned rx +8°, ry +4°; on head |
| tail | -4 to -1 | -2 to 2 | 8 to 12 | turned ry +28°, rz +12°; on body |
| tail_tip | -7 to -5 | -2 to 2 | 8 to 12 | turned ry +16°; on tail |
| leg_hr | 1 to 3 | 2 to 4 | 0 to 5 | turned ry +12°; on body |
| leg_fr | 10 to 12 | 2 to 4 | 0 to 5 | turned ry -12°; on body |
| ear_r | 15 to 16 | 3 to 5 | 18 to 21 | turned rx -14°, ry +14°; on head |

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
