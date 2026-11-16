# {{CODE}} · {{COMMON}} · voxel brief

*{{SCIENTIFIC}}* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (Tailwind token or #hex) | Where |
|---|---|---|
| `main` | `stone-400` | the coat |
| `light` | `stone-100` | belly, muzzle |
| `dark` | `stone-800` | paws, ear tips |
| `eye` | `neutral-950` | eyes, nose |

Background (not modelled): `sky-200` (rendered muted).

## Size and pose

- Size: the posed longest side inside the budget from the real size (`vf.py check` prints it): target 28 × L^0.4
  voxels for a real longest dimension of L metres (`animal.json → look.size`). Width odd, centred on y = 0.
- Pose: see Personality, pose and expression. Head towards +X, feet on z = 0 in the rest pose, left flank at −Y;
  modelled symmetric, mirrored, then posed at the joints.

## Personality, pose and expression

- Personality: two or three words from the research (calm, sly, curious, proud, sleepy ...).
- Pose: what the joints do (head turned to the camera and cocked, ears, tail, a stride or a lifted paw, wings or
  flippers out, one leg up); every turn under 40°.
- Expression: eyes (2 × 2 with a glint, a closed line, a smug tilt), brows or lids (tilted plates), mouth (a smile,
  a smirk, a surprised dot).

## Proportions (from the photos, in voxels)

| Part | x from–to | y half-width | z from–to | Notes |
|---|---|---|---|---|
| body | | | | |
| head | | | | |
| legs | | | | |
| tail | | | | |

## Recognisable features (3–5, in order of importance)

1. …
2. …
3. …

## Colour map

- `main`: …
- `light`: …
- `dark`: …
- `eye`: one voxel each side on the head's flank (and front where it shows).

## Photos used

- `assets/photos/01-….jpg`: …
