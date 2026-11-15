# {{CODE}} · {{COMMON}} · voxel brief

*{{SCIENTIFIC}}* · attach this file together with `key-prompt.md` (project root) to write `blender/model.py`.

## Palette (must match `animal.json → look.palette`; the first key is the main colour)

| Key | Token | Where |
|---|---|---|
| `main` | `stone-400` | the coat |
| `light` | `stone-100` | belly, muzzle |
| `dark` | `stone-800` | paws, ear tips |
| `eye` | `neutral-950` | eyes, nose |

Background (not modelled): `sky-200`.

## Size and pose

- Longest side: NN voxels along X (head at +X). Width NN (odd, centred on y = 0). Height NN.
- Pose: standing, neutral, all feet on z = 0, head level, looking along +X.

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
