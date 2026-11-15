# Voxel Fauna · key prompt (write an animal's `model.py`)

**How to use:** open a new chat (Claude Sonnet, high effort), attach **this file** and **one animal's
`docs/voxel-model.md`**, and send them with no other message (or just "go"). The answer is one Python file. Save it as
`02 Animals/<code> · <Name>/blender/model.py`, then build and look at it: double-click `render.bat` → `1` (build) →
`2` (LOW previews), or `python _system/studio/scripts/vf.py preview <code>`. If something looks wrong, paste the
preview sheet and the problem back into the same chat and ask for a corrected file.

---

## Your task

You are a voxel artist writing code. Read the attached **voxel brief** (`voxel-model.md`) and write the file
`model.py` that builds that animal on a voxel grid. Your file is run by a fixed engine that turns every voxel into a
satin-plastic block and renders it from a true-isometric camera in Blender. You only place voxels. Do not import
Blender, do not set colours as RGB, do not add lights, cameras or anything else.

**Answer with exactly one fenced ```python code block** containing the whole file, and nothing after it. Before
the block you may write at most three short lines (for example, what you simplified). No other prose.

## The grid (the only API you have)

`build(g)` receives `g`, an empty grid. A voxel is an integer cell `(x, y, z)` filling `[x, x+1] × [y, y+1] × [z, z+1]`
(one voxel = 0.1 m; you never need metres).

| Call | Does |
|---|---|
| `g.box((x0, y0, z0), (x1, y1, z1), colour, part="body")` | fills every voxel of the box between the two corners, **both corners included** |
| `g.ellipsoid((cx, cy, cz), (rx, ry, rz), colour, part="body")` | fills voxels whose centre lies inside the ellipsoid (centre and radii in voxels; halves allowed); keep radii ≥ 2 |
| `g.paint((x0, y0, z0), (x1, y1, z1), colour, part=None, only=None)` | recolours voxels **already there** inside the box (`only="fur"` limits it to one colour key); can also move them to another `part` |
| `g.carve((x0, y0, z0), (x1, y1, z1))` | removes every voxel inside the box |
| `g.set(x, y, z, colour, part="body")` | one voxel |
| `g.mirror("-Y")` | copies every voxel with `y < 0` to `-y` (the column `y = 0` stays): model the left side and the centre, then mirror once at the end |

Later calls overwrite earlier ones on the same voxel. `colour` is always a **palette key** from the brief's palette
table (for example `"fur"`), never a colour name or hex. `part` names the Blender object the voxel lands in.

## Orientation (fixed for the whole collection)

- **+X is where the head points.** The tail end is at low X.
- **y = 0 is the centre line.** −Y is the animal's **left** side, +Y its right. Widths are odd and symmetric
  (y from −h to +h).
- **+Z is up. The feet stand on z = 0.** Nothing below z = 0; the lowest voxels must be at z = 0.
- The camera looks from the front-left and above (true isometric): it sees the **+X face** (the face), the **−Y face**
  (the left flank) and the **top**. Put eyes, nose and markings where they show from there.

## Hard rules (the engine refuses the model otherwise)

1. **Budget:** the longest side (in X, Y or Z) is **16 to 32 voxels**; aim for the size the brief gives (usually 24–30).
2. **Ground:** the lowest voxel is at **z = 0**; every foot touches it.
3. **One piece:** every voxel must touch the body through faces (not just edges or corners). No floating eyes, ears,
   spots or tail tips: overlap them into the head or body by at least one voxel.
4. **Palette keys only:** use exactly the keys of the brief's palette table, and use **every** key at least once.
5. **Parts:** use the parts the brief lists (usually `body`, `head`, `legs`, `tail`, sometimes `ears`, `neck`, `wings`,
   `beak`). A part becomes one Blender object; where two parts touch, the render shows a thin seam like an assembled
   toy, so split parts where a toy would be assembled (head from body, legs from body), not in the middle of a
   colour patch.
6. **Symmetry:** build the left side (y ≤ 0) and the centre column, then call `g.mirror("-Y")` once as the last line.
   Asymmetric details (a lifted paw) are allowed only if the brief asks for them.
7. **Smallest feature = one voxel.** No detail smaller than a voxel, no single-voxel noise or speckles.

## Style (what makes it look right)

- **Large blocks, clear steps.** Build from a few boxes per part: one for the mass, one or two to step the silhouette
  (a rounder back, a tapering snout, a thicker neck). Rounded forms are made with 2–3 stacked boxes of shrinking size or
  an ellipsoid with radii ≥ 2, never with noise.
- **Proportions first, from the brief's table.** Body length : height : head : leg length decide whether it reads as
  the species. A little exaggeration helps (bigger head, bigger ears, bushier tail) like a toy.
- **The 3–5 recognisable features** in the brief matter most; make each one big enough to read at thumbnail size
  (a fox's white tail tip, a panda's eye patches, a lion's mane).
- **Colour in big patches** with `paint` after the shapes: belly, muzzle, socks, mask. Patches follow the voxel grid,
  at least 2 voxels across where possible.
- **Eyes:** usually one voxel per side on the head's flank (−Y face, mirrored), at about 60 % of the head's height,
  plus the same row on the front face if the face is flat. A dark eye on a dark patch is invisible: put it on a light
  voxel or give it a light rim.
- **Legs:** 2 × 2 voxels for most mammals (1 × 1 for birds), straight down to z = 0, front legs under the shoulders and
  hind legs under the hips, with a gap between them along X so they read as four legs.
- **Tails, ears, horns:** stepped blocks that taper; anchor them into the body/head by one voxel.
- Do not add a base, ground, plinth, food, plants, text or anything that is not the animal.

## Worked example (format only; a generic creature, not a species)

```python
"""Selftest creature · voxel model (format example).
Palette keys: fur, belly, dark."""


def build(g):
    # legs: 2 x 2, left side (mirrored at the end); dark paws
    for x in (2, 11):
        g.box((x, -3, 0), (x + 1, -2, 5), "fur", part="legs")
        g.box((x, -3, 0), (x + 1, -2, 0), "dark", part="legs")
    # body with a pale belly
    g.box((1, -3, 6), (14, 3, 11), "fur", part="body")
    g.paint((3, -2, 6), (12, 2, 6), "belly")
    # head, muzzle, nose, eye, ear
    g.box((14, -3, 9), (19, 3, 15), "fur", part="head")
    g.box((20, -2, 9), (22, 2, 12), "belly", part="head")
    g.box((22, -1, 11), (22, 1, 12), "dark", part="head")
    g.paint((19, -2, 13), (19, -2, 13), "dark")
    g.box((15, -3, 16), (16, -2, 17), "fur", part="head")
    # tail
    g.box((-1, -1, 10), (0, 1, 11), "fur", part="tail")
    g.box((-3, -1, 11), (-2, 1, 13), "belly", part="tail")
    g.mirror("-Y")
```

## File format

```python
"""<code> · <Common name> (<Scientific name>) · voxel model.
Built from docs/voxel-model.md. Palette keys: <keys>. Size: <L> x <W> x <H> voxels."""


def build(g):
    # one short comment per part, in the order: legs, body, neck, head, ears, tail, colour patches, eyes
    ...
    g.mirror("-Y")
```

Plain Python 3, no imports (you may use `range` and simple loops), no randomness, no file or network access, no
`print`. Only `def build(g):` at top level (helper functions inside it are fine).

## Self-check before you answer (do it, silently)

1. Lowest z is 0 and every foot reaches it; nothing is below 0.
2. Longest side between 16 and 32; the sizes match the brief.
3. Every voxel connects to the body through faces (eyes, ears, tail tip, spots overlap their part).
4. Every palette key is used; no other colour names appear.
5. Head at +X, left flank at −Y, `g.mirror("-Y")` called once, last.
6. The 3–5 features of the brief are each clearly visible from the front-left above.
