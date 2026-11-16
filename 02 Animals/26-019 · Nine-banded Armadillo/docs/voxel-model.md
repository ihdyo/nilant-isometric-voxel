# 26-019 · Nine-banded Armadillo · voxel brief

*Dasypus novemcinctus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (Tailwind token or #hex) | Where |
|---|---|---|
| `shell` | `stone-400` | the armour shell over the back, the head shield and the tail rings |
| `band` | `stone-500` | the nine bands across the middle of the shell and the rings of the tail |
| `skin` | `stone-300` | the ears, the snout, the legs and the belly |
| `eye` | `neutral-950` | the small eyes, the claws and the smile |

Background (not modelled): `lime-200` (rendered as a calm pastel).

## Size and pose

- Size: 32 × 11 × 12 voxels posed (L × W × H); longest side 32, budget 24–32 (target 28) from the real size 1.0 m (nose to tail tip: body about 75 cm plus a 30 cm tail).
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Parts: leg_fl, leg_fr, leg_hl, leg_hr, body, head, tail, tail_tip, ear_l, ear_r.

## Personality, pose and expression

- Personality: curious and busy, a little shy.
- Pose: trundling forward with the nose down and turned to the camera to sniff, the ears up, the long ringed tail curving behind, one front foot lifted.
- Expression: small beady eyes on the head, painted flat, a dark nose tip.

## Proportions (inclusive voxel ranges of each part in the rest pose, as built)

| Part | x | y | z | Pose |
|---|---|---|---|---|
| leg_fl | 13 to 15 | -4 to -3 | 0 to 2 | turned ry -24°; on body |
| leg_fr | 13 to 15 | 3 to 4 | 0 to 2 | on body |
| leg_hl | 2 to 4 | -4 to -3 | 0 to 2 | on body |
| leg_hr | 2 to 4 | 3 to 4 | 0 to 2 | on body |
| body | 0 to 16 | -5 to 5 | 3 to 10 |  |
| head | 17 to 23 | -2 to 2 | 4 to 8 | turned rx +6°, ry +12°, rz -16°; on body |
| tail | -5 to -1 | -1 to 1 | 5 to 6 | turned ry -14°, rz +10°; on body |
| tail_tip | -8 to -6 | 0 to 0 | 5 to 5 | turned ry -12°, rz +14°; on tail |
| ear_l | 18 to 18 | -2 to -2 | 9 to 11 | turned rx +12°, ry -8°; on head |
| ear_r | 18 to 18 | 2 to 2 | 9 to 11 | turned rx -12°, ry -8°; on head |

## Recognisable features (in order of importance)

1. the banded armour shell over the back
2. a long pointed snout
3. tall ears
4. a long ringed tail
5. short legs with claws

## Colour map

- `shell`: the armour shell over the back, the head shield and the tail rings
- `band`: the nine bands across the middle of the shell and the rings of the tail
- `skin`: the ears, the snout, the legs and the belly
- `eye`: the small eyes, the claws and the smile

## Photos used

- `assets/photos/01-uruguay.jpg`: an adult digging at a burrow in Uruguay, shell, ears and tail (CC BY 4.0)
- `assets/photos/02-bahia.jpg`: an adult held in the hand in Bahia, Brazil, the banded shell (CC BY 2.0)
