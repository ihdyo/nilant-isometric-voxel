# 000092 · Walrus · voxel brief

*Odobenus rosmarus* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (hex colour or #hex) | Where |
|---|---|---|
| `skin` | `#973C00` | primary body / main colour |
| `fold` | `#7B3306` | fold |
| `whisker` | `#E7E5E4` | whisker |
| `tusk` | `#FFFBEB` | tusk |
| `eye` | `#171717` | eye |

Background (not modelled): `#EBD0A9` (soft sand).

## Size and pose

- Size: longest side budget 48–56 voxels (target 56) calibrated from the real size 3.2 m (total length 2.7–3.6 m in adult males).
- Pose: see Personality, pose and expression. Head towards +X, base/feet on z = 0 in the rest pose, left flank at −Y; modelled symmetric, mirrored, then posed at the joints.
- Rig plan: `walker` (pose, idle, waddle, bellow).

## Personality, pose and expression

- Personality: gruff yet sociable, a whiskered Arctic heavyweight.
- Pose: propped up on its front flippers with head lifted and twin ivory tusks pointing down.
- Expression: small expressive eyes above a bushy mustache and long tusks.

## Recognisable features (in order of importance)

1. two long downward-pointing ivory tusks
2. broad muzzle covered in dense cream whiskers
3. thick wrinkled cinnamon-brown skin folds
4. four wide paddle flippers
5. bulky barrel-shaped torso

## Colour map

- `skin`: `amber-800`
- `fold`: `amber-900`
- `whisker`: `stone-200`
- `tusk`: `amber-50`
- `eye`: `neutral-900`

## Photos used

- Pending Phase 1 photo selection in `assets/photos/` (CC0 or CC BY from Wikimedia Commons).
