# {{CODE}} · {{COMMON}} · voxel brief

*{{SCIENTIFIC}}* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Colour (#RRGGBB) | Where |
|---|---|---|
| `main` | `stone-400` | the coat |
| `light` | `stone-100` | belly, muzzle |
| `dark` | `stone-800` | paws, ear tips |
| `eye` | `neutral-950` | eyes, nose |

Background (not modelled): `#ACDCF5` (its name, e.g. sky blue): OKLCH lightness 0.87, chroma 0.06, the hue chosen
for the animal (its habitat, or the complement of its coat); `vf_color.background(hue, 0.87, 0.06)`.

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

## Motion (every animal is rigged and animated; set in `animal.json → motion`)

- Plan: walker, sitter, bird, swimmer, sprawler or hopper (four-legged animals stand on four feet and walk).
- Actions: `pose`, `idle`, the gait (`walk`, `flap`, `hop`, `swim`, `waddle`) and the species specials it is known
  for (`howl`, `doze`, `shake`, `yawn`, `fan`, `reach`, `sniff`, or a new one added to the library in `vf_rig.py`).
- Sections the rig needs, named as in `key-prompt.md` rule 5: `head`, the legs (`leg_fl` … with `shin_fl` … for
  knees; `leg_l` + `shin_l` + `foot_l` on two legs), `ear_l`, `tail` + `tail_tip`, `wing_l`, `flipper_l` …
  Only the stems in `vf_standards.SECTION_STEMS` (`vf.py check` rejects others): the loops draw limbs (`leg`, `shin`,
  `foot`, `flipper`, `arm`) behind the body and every other section over it, by name.
- Done when `vf.py preview` (or `vf.py rig`) reports rig check PASS and the loops look right.

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
