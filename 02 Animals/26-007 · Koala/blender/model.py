"""26-007 · Koala (Phascolarctos cinereus) · voxel model.
Built from docs/voxel-model.md. Palette keys: fur, white, nose, eye. Size: 11 x 15 x 22 voxels."""


def build(g):
    # sitting: the hind legs and rump make a wide seat, the feet poke forward
    g.box((1, -4, 0), (8, 4, 3), "fur", part="body")
    g.box((9, -4, 0), (10, -2, 1), "fur", part="legs")
    # upright body with a white chest
    g.box((1, -4, 4), (7, 4, 11), "fur", part="body")
    g.paint((7, -2, 4), (7, 2, 10), "white")
    # front arms resting down the front
    g.box((8, -4, 3), (9, -3, 9), "fur", part="legs")
    # the big round head
    g.box((1, -5, 12), (9, 5, 19), "fur", part="head")
    g.box((2, -4, 20), (8, 4, 20), "fur", part="head")
    g.carve((9, -5, 19), (9, -5, 19))
    # the famous big dark nose, and the eyes
    g.box((10, -1, 13), (10, 1, 16), "nose", part="head")
    g.set(9, -3, 16, "eye", part="head")
    g.set(8, -5, 16, "eye", part="head")
    # big fluffy ears, white fringe
    g.box((3, -7, 17), (6, -6, 21), "fur", part="ears")
    g.paint((3, -7, 17), (6, -7, 21), "white")
    g.paint((3, -6, 21), (6, -6, 21), "white")
    g.mirror("-Y")
