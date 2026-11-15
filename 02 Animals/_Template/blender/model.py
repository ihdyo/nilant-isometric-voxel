"""{{CODE}} · {{COMMON}} ({{SCIENTIFIC}}) · voxel model.

The source of truth for this animal's Blender project: `python _system/studio/scripts/vf.py preview {{CODE}}` builds
`{{CODE}} · {{COMMON}}.blend` from it. Follow the skill voxel-animal-production (modelling standards):

  - head towards +X, back up (+Z), feet on z = 0, the left flank at -Y; model the left side, then g.mirror("-Y")
  - longest side 16-32 voxels (aim for 24); the smallest feature is one whole voxel
  - colours are keys of animal.json -> look.palette (never raw colours); parts name the Blender objects
    (body, head, legs, tail, ears, ...): parts meet with a visible seam, so split where a toy would be assembled
  - build from the reference photos in assets/photos/: proportions first (body : head : legs), then the 3-5 features
    that make the species recognisable, then colour; nothing smaller than a voxel, no noise

Grid API (_system/studio/blender/vf_voxel.py):
  g.box(a, b, colour, part)            inclusive box between corners a and b
  g.ellipsoid(centre, radii, colour, part)   radii >= 2
  g.paint(a, b, colour, part=None, only=None)  recolour what is there
  g.carve(a, b)                        remove
  g.set(x, y, z, colour, part)         one voxel
  g.mirror("-Y")                       copy the left side to the right
Check without Blender: python _system/studio/scripts/vf.py check {{CODE}}
"""


def build(g):
    # Replace this placeholder block with the animal (it only proves the folder works).
    g.box((0, -3, 0), (19, 3, 9), "main", part="body")
