# 000079 · Green Iguana · voxel brief

*Iguana iguana* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `scales` | `#00C950` | primary body / main colour |
| `crest` | `#BBF451` | crest |
| `dewlap` | `#00D492` | dewlap |
| `stripe` | `#404040` | stripe |
| `claw` | `#44403B` | claw |
| `eye` | `#171717` | eye |

Background (not modelled): `#B0E1CA` (soft mint).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 1.8 m (total length 1.5–2.0 m including the long banded whip-like tail).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `walker` (pose, idle, walk, nod).

## Personality, pose and expression

- Personality: sun-loving and serene, a treetop herbivore.
- Pose: basking alertly with head held high, dorsal spines bristling, and banded tail sweeping behind.
- Expression: bright alert eyes with a calm, prehistoric profile.

## Recognisable features (in order of importance)

1. row of tall comb-like dorsal spines
2. large hanging throat dewlap
3. long dark-banded whip tail
4. round cheek scale below the jaw
5. long toes with climbing claws

## Colour map

- `scales`: `green-500`
- `crest`: `lime-300`
- `dewlap`: `emerald-400`
- `stripe`: `neutral-700`
- `claw`: `stone-700`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
