"""26-006 · American Flamingo (Phoenicopterus ruber) · voxel model.
Built from docs/voxel-model.md. Palette keys: pink, light, black, bill, legs, eye. Size: 17 x 7 x 31 voxels."""


def build(g):
    # long thin legs (1 x 1) with flat feet, the backward-bending "knee" (ankle) halfway
    g.box((6, -1, 1), (6, -1, 6), "legs", part="legs")
    g.box((5, -1, 6), (5, -1, 12), "legs", part="legs")
    g.box((5, -1, 0), (7, -1, 0), "legs", part="legs")
    # body: an egg shape, black flight feathers along the rear edge
    g.box((2, -3, 14), (10, 3, 17), "pink", part="body")
    g.box((3, -2, 13), (9, 2, 13), "pink", part="body")
    g.box((4, -2, 18), (9, 2, 18), "pink", part="body")
    g.box((0, -2, 15), (1, 2, 17), "pink", part="body")
    g.paint((0, -3, 15), (3, -3, 16), "black")
    g.paint((0, -2, 15), (1, -2, 15), "black")
    # the long S-shaped neck (lighter pink)
    g.box((9, 0, 19), (10, 0, 22), "light", part="neck")
    g.box((8, 0, 23), (9, 0, 25), "light", part="neck")
    g.box((9, 0, 26), (10, 0, 27), "light", part="neck")
    # head, the eye, the bent bill (pale base, black tip)
    g.box((10, -1, 27), (13, 1, 30), "light", part="head")
    g.set(12, -1, 29, "eye", part="head")
    g.box((14, 0, 28), (15, 0, 30), "bill", part="beak")
    g.box((16, 0, 27), (16, 0, 29), "bill", part="beak")
    g.paint((16, 0, 27), (16, 0, 28), "black")
    g.set(15, 0, 27, "black", part="beak")
    g.mirror("-Y")
