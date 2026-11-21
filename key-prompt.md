# Voxel Fauna · key prompt (write an animal's `model.py`)

**How to use:** open a new chat (Claude Sonnet, high effort), attach **this file** and **one animal's
`docs/voxel-model.md`**, and send them with no other message (or just "go"). The answer is one Python file. Save it as
`02 Animals/<code> · <Name>/blender/model.py`, then build and look at it: double-click `render.bat` → `1` (build) →
`2` (LOW previews), or `python _system/studio/scripts/vf.py preview <code>`. If something looks wrong, paste the
preview sheet and the problem back into the same chat and ask for a corrected file.

---

## Your task

You are a voxel artist writing code. Read the attached **voxel brief** (`voxel-model.md`) and write the file
`model.py` that builds that animal on a voxel grid. Your file is run by a fixed engine that turns each part into
sharp-edged matte blocks in flat solid colours (a **bulky blocky-mob** look: an animal assembled from a few big
sections, turned a little at their joints, with its face painted flat on the front of the head, like a mob in a
block-building game) and renders it from a true-isometric camera in Blender. You only place voxels and joints. Do not
import Blender, do not set colours as RGB (the palette's hex colours are named by their keys), do not add lights, cameras or anything else.

**Answer with exactly one fenced ```python code block** containing the whole file, and nothing after it. Before
the block you may write at most three short lines (for example, what you simplified). No other prose.

## The grid (the only API you have)

`build(g)` receives `g`, an empty grid. A voxel is an integer cell `(x, y, z)` filling `[x, x+1] × [y, y+1] × [z, z+1]`
(one voxel = 0.1 m; you never need metres). Build every part **in place, standing straight** (the rest pose); then
turn sections at their joints to pose the animal.

| Call | Does |
|---|---|
| `g.box((x0, y0, z0), (x1, y1, z1), colour, part="body")` | fills every voxel of the box between the two corners, **both corners included**, in that part's own layer |
| `g.paint((x0, y0, z0), (x1, y1, z1), colour, part=None, only=None, of=None)` | recolours voxels **already there** inside the box (`only="fur"` limits it to one colour key, `of="head"` to one part); `part` moves them to another part |
| `g.carve((x0, y0, z0), (x1, y1, z1))` | removes every voxel inside the box |
| `g.set(x, y, z, colour, part="body")` | one voxel |
| `g.plate((x0, y0, z0), (x1, y1, z1), colour, part, keep=None)` | a **flat surface**: a box one voxel thick on one axis, squashed to a thin plate. `keep` is the face that stays put: by default the bottom of a lying plate, the back of a plate on a +X face, the inner side of a plate on a flank. Feet under a leg: `keep="+z"` (the leg stands on the plate; the engine puts the plate on the ground). **Switched off for now** (owner, 2026-11-16: "disable flat pixel for now"): `vf.py check` refuses it; build feet, ears and wing tips from whole voxels |
| `g.joint(part, pivot=(x, y, z), rotate=(rx, ry, rz), parent=None)` | turns a whole part about its hinge `pivot` (halves allowed: a hinge sits on a face) by degrees, after its `parent`'s turn (ears, brows and snout follow the head; the head and legs follow the body). Every part that sits on a turned part needs a `parent` |
| `g.mirror()` | copies every voxel with `y < 0` to `-y`; parts named `..._l` or `..._?l` (`ear_l`, `leg_fl`, `leg_hl`, `arm_l`) become `..._r` with their joints mirrored. Call it once after the left side; joints set **after** it override (an asymmetric pose) |
| `g.ellipsoid(...)` | not used in this style |

**Every part is its own layer of voxels.** Blocks of different parts may overlap and simply stack: an ear set into
the head, the head set into the mane, a leg into the body. A box never cuts a hole in another part, so a section that
turns never leaves a gap in its neighbour; just build each section whole. Within one part, later calls overwrite
earlier ones. `colour` is always a **palette key** from the brief's palette table (for example `"fur"`), never a
colour name or hex. `part` names the Blender object the voxel lands in.

**Rotation signs** (`rotate=(rx, ry, rz)`, degrees, applied X then Y then Z):
- `rx` roll about the length axis: **+ tips the top towards −Y** (the camera side; a left ear tips out); a hanging
  part's lower end swings towards +Y (so a left flipper held out from the body is **−**).
- `ry` pitch: **+ puts a +X end down** (nose down, beak bent down) and a −X end up (a raised tail is **+**); a hanging
  leg's foot goes back with **+** and forward with **−**.
- `rz` yaw: + turns +X towards +Y (away from the camera); **− turns the face towards the camera** (the dynamic
  pose turns the head to the camera, owner 2026-11-21).
- Mirrored joints flip `rx` and `rz` (a left ear at `rx=+15` gives a right ear at `rx=−15`: both tip outwards).

## Orientation (fixed for the whole collection)

- **+X is where the head points.** The tail end is at low X.
- **The column y = 0 is the centre line.** −Y is the animal's **left** side, +Y its right. Widths are odd and
  symmetric (y from −h to +h). As a coordinate the centre plane is **y = 0.5** (the middle of that column): a centred
  hinge (head, neck, tail) has pivot y = 0.5.
- **+Z is up. The feet stand on z = 0** in the rest pose (nothing below z = 0); after posing, the engine sets the
  lowest point back on the ground.
- The camera looks from the front-left and above (true isometric): it sees the **+X face** (the face), the **−Y face**
  (the left flank) and the **top**. Put eyes, nose and markings where they show from there.

## Hard rules (the engine refuses the model otherwise)

1. **Budget:** the posed longest side (in X, Y or Z) is inside the range the brief's **Size** line gives. It comes from
   the species' real size: bigger animals get more voxels (a fox about 29, a lion about 42, a giraffe about 53).
2. **Ground:** in the rest pose the lowest voxel is at **z = 0** and every foot touches it.
3. **One piece in the rest pose:** every voxel must touch the body through faces (not just edges or corners). No
   floating eyes, ears, spots or tail tips.
4. **Palette keys only:** use exactly the keys of the brief's palette table, and use **every** key at least once.
5. **Parts:** one part per section a toy would have as its own piece: `body`, `head`, `snout` / `muzzle` / `beak` /
   `jaw`, `neck`, `tail` (+ `tail_tip`), `trunk_1`…, `leg_fl`, `leg_hl` (front and hind left), `arm_l`, `ear_l`,
   `wing_l`, `flipper_l`, `tusk_l`, `foot_l`. Split them so they can turn; never in the middle of a colour patch.
   Eyes, brows and mouths are not parts: they are painted on the head or snout. **Use these exact names** (and
   `shin_fl`, `leg_l` for a two-legged animal, `flipper_hl`, `gill_l`, `tongue`, `torso`, `mane`, `flukes`): the
   animation rig finds the legs, ears, tails and wings by name to make them walk, flick and flap, and the loops draw
   every limb (`leg_*`, `shin_*`, `foot_*`, `flipper_*`, `arm_*`) behind the body and every other section over it.
   Any other name (`paw_fl`, `thigh_l`, `hoof_fl`) fails `vf.py check`: a paw or hoof is the end of its leg or foot,
   not a part of its own.
6. **Joints:** a pivot touches its part (within a voxel and a half of it); at most **40°** on any axis (subtle,
   believable turns, not contortions). A section that turns (head, neck, tail, ear, snout, trunk) should overlap its
   parent; where it only touches it, the engine sinks it one voxel into the parent near its hinge (`Grid.anchor()`, owner
   2026-11-21: necks and tails "floating" in the loops), so build necks and tails growing out of the body, not
   standing on it.
7. **Symmetry:** build the left side (y ≤ 0) and the centre column, call `g.mirror()` once, then add the asymmetric
   pose joints (one paw lifted, one ear back) and one-sided details.

## Style: bulky blocky mob, posed, with an expression

The collection's look (owner, 2026-11-16) is the **bulky blocky-mob** style of block-building games: an animal
assembled from a few big rectangular sections, turned a little at their joints so it looks alive, with an expressive
face drawn on the front of the head. Make it our own animal from the brief and the photos; never copy a particular
game's creature.

- **Knees for long legs:** a leg longer than about 8 voxels is two sections, the upper leg (`leg_fl`) and the shin
  (`shin_fl`, parent the leg) hinged at the knee, so a lifted or striding leg can fold. Bird legs (`leg_l` + `shin_l`
  + `foot_l`) and frog legs (`leg_hl` for the thigh + `shin_hl` for the shank and foot) are two parts as well.
- **Stand on four feet:** a four-legged animal stands on all four feet, never sits (owner, 2026-11-17), so it can
  walk; show its character with the head, ears, tail and a stride instead. A big head goes high on the front of the
  body, or it hides the front legs.
- **Long bodies in two sections:** a heavy, long body can be the lower body (`body`, the hindquarters) and the upper
  body (`torso`, the shoulders, parent `body`, hinged at the waist) with the front legs and the head on the torso.
- **Bulky sections.** Body = one big box (wide: about half its length or more); head = one big box, often as wide as
  the body or wider; legs = thick pillars (3 × 3 for most mammals, 4 × 4 or 5 × 5 for heavy ones, 1 × 1 for long bird
  legs); tail = one or two blocks; ears = small blocks or plates. A second box only for a real feature (a bear's
  hips, a mane block, a giraffe's shoulder step). **No `ellipsoid`, no stair-stepped curves**: flat faces, sharp
  corners. Exaggerate the brief's features like a toy.
- **A lively pose, looking at the camera** (owner, 2026-11-21: "make it more dynamic", then "make it look at camera
  except for the static basic pose"): the body in motion, a real stride (the diagonal legs 14–22° forward and back,
  a knee folding) or one paw lifted, the tail raised or curled (two blocks), the ears asymmetric, wings or flippers
  held out; the head turned to the camera (yaw `rz` about −14; a neck, mane or torso under it stays straight), roll
  `rx` at most ±5 (never tilted hard), pitch `ry` for the mood (nose down to sniff or stalk, up to look or call).
  Every animal, birds included; every one gets its own pose; keep each turn under 40°.
- **Short-legged hoppers** (rabbits, frogs; owner 2026-11-21, after the block-game rabbit): the body is one block;
  each hind thigh is a slab two voxels wide on the flank, one voxel inside the body and one showing on its side, its
  hinge inside the body (`leg_hl`); the lower leg and long foot (`shin_hl`) hinge at the knee or heel; a frog's hind
  leg is two flat boards hinged like a clapperboard. Front legs start beside the chest (on the flank); a frog's arm is
  one piece (no elbow).
- **An expression, painted flat on the face** (owner, 2026-11-16: "dont extrude the mouth and eyebrow ... they should
  flat"): eyes, brows and mouths are colours on the front voxels of the head and snout (`g.set` / `g.box` into the
  `head` part), flush with the surface, never plates or blocks standing out:
  - **eyes:** a white eye with the pupil on the inner side (towards the nose), one voxel wide and two tall, as on a
    character in a block game; or a dark eye with a light glint; sleepy or smug eyes are a dark (or light) line,
    stepped one voxel down at one end for a curve.
  - **brows:** a darker strip one row above the eyes; its shape is the mood: stepping down towards the middle =
    determined or sly; stepping up towards the middle = curious or worried; level = calm; one brow higher = sly.
  - **mouth:** dark voxels on the front of the snout: a U smile (corners one voxel higher), a lopsided line (a smirk),
    one dark voxel (surprised). The nose is a dark row on the snout's top front edge.
- **Colour in clean shapes** with `paint` after the boxes: bib, socks, mask, patches, rings. Flat solid colours only:
  never scattered voxels, speckles, noise or shading made with colour.
- **The 3–5 recognisable features** in the brief matter most; make each one big enough to read at thumbnail size.
- Do not add a base, ground, plinth, food, plants, text or anything that is not the animal.

## Worked example (format only; a generic creature, not a species)

```python
"""Selftest creature · voxel model (format example).
Palette keys: fur, belly, dark."""


def build(g):
    # body: one big bulky box, pale belly
    g.box((0, -4, 5), (14, 4, 12), "fur", part="body")
    g.paint((2, -4, 5), (12, 4, 5), "belly", of="body")
    # legs: 3 x 3 pillars hinged under the body, dark paws
    for name, x in (("leg_hl", 1), ("leg_fl", 10)):
        g.box((x, -4, 0), (x + 2, -2, 4), "fur", part=name)
        g.box((x, -4, 0), (x + 2, -2, 0), "dark", part=name)
        g.joint(name, pivot=(x + 1.5, -3, 5), parent="body")
    # head: a big box on the front of the body, turned to the camera
    g.box((14, -5, 9), (21, 5, 17), "fur", part="head")
    g.joint("head", pivot=(15, 0.5, 12), rotate=(4, 4, -14), parent="body")
    # face, painted flat on the front of the head: a light eye with the dark pupil to the inside, a dark brow
    # stepping down towards the middle (a determined look)
    g.box((21, -4, 13), (21, -4, 14), "belly", part="head")
    g.box((21, -3, 13), (21, -3, 14), "dark", part="head")
    g.box((21, -5, 16), (21, -4, 16), "dark", part="head")
    g.box((21, -3, 15), (21, -2, 15), "dark", part="head")
    # snout: a box on the face, the dark nose on its top front edge, a small smile painted under it
    g.box((22, -2, 9), (24, 2, 12), "belly", part="snout")
    g.paint((24, -1, 12), (24, 1, 12), "dark", of="snout")
    g.set(24, -2, 10, "dark", part="snout")
    g.box((24, -1, 9), (24, 0, 9), "dark", part="snout")
    g.joint("snout", pivot=(22, 0.5, 10.5), parent="head")
    # ears: flat plates on top of the head, tipped outwards
    g.plate((17, -5, 18), (17, -3, 20), "fur", part="ear_l")
    g.joint("ear_l", pivot=(17, -4, 18), rotate=(18, 0, 0), parent="head")
    # tail: one block raised from its root
    g.box((-4, -1, 10), (-1, 1, 12), "fur", part="tail")
    g.box((-5, -1, 10), (-5, 1, 12), "belly", part="tail")
    g.joint("tail", pivot=(0, 0.5, 11), rotate=(0, 25, 0), parent="body")
    g.mirror()
    # an asymmetric step: the front-left leg forward, the hind-left back (set after the mirror)
    g.joint("leg_fl", pivot=(11.5, -3, 5), rotate=(0, -18, 0), parent="body")
    g.joint("leg_hl", pivot=(2.5, -3, 5), rotate=(0, 14, 0), parent="body")
```

## File format

```python
"""<code> · <Common name> (<Scientific name>) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: <keys>. Size: <L> x <W> x <H> voxels.
Personality: <...>. Pose: <...>. Expression: <...>."""


def build(g):
    # one short comment per part, in the order: body, legs, neck, head, face (eyes, brows, snout, mouth), ears, tail
    ...
    g.mirror()
    # asymmetric pose joints and one-sided details after the mirror
```

Plain Python 3, no imports (you may use `range` and simple loops), no randomness, no file or network access, no
`print`. Only `def build(g):` at top level (helper functions inside it are fine).

## Self-check before you answer (do it, silently)

1. In the rest pose the lowest z is 0 and every foot reaches it; nothing is below 0.
2. The posed longest side is inside the brief's size range.
3. Every voxel connects to the body through faces (eyes, ears, tail tip, spots overlap their part).
4. Every palette key is used; no other colour names appear.
5. Head at +X, left flank at −Y, `g.mirror()` called once.
6. The 3–5 features of the brief are each clearly visible from the front-left above.
7. Bulky blocky mob: one box per section (no `ellipsoid`, no stair-stepped curves), thick legs, a big head, each
   section built whole (sections stack, no holes), the expression painted flat on the front of the head (eyes,
   brows, mouth), flat colour shapes.
8. Posed: every turned part has a pivot on it, a `parent` if it sits on another turned part, and turns under 40°;
   the pose matches the brief's personality; `g.mirror()` comes before the asymmetric joints.
