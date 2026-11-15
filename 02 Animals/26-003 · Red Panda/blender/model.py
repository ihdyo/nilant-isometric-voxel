"""26-003 · Red Panda (Ailurus fulgens) · voxel model.
Built from docs/voxel-model.md. Palette keys: fur, white, dark, ring, eye. Size: 27 x 7 x 16 voxels."""


def build(g):
    # legs: 2 x 2, dark brown-black like the belly
    for x in (3, 11):
        g.box((x, -3, 0), (x + 1, -2, 4), "dark", part="legs")
    # body: rusty red, a dark belly
    g.box((2, -3, 5), (13, 3, 9), "fur", part="body")
    g.box((4, -2, 10), (11, 2, 10), "fur", part="body")
    g.paint((3, -2, 5), (12, 2, 5), "dark")
    # head: round, rusty red
    g.box((13, -3, 8), (17, 3, 13), "fur", part="head")
    # white muzzle, dark nose
    g.box((18, -1, 8), (19, 1, 10), "white", part="head")
    g.paint((19, 0, 10), (19, 0, 10), "dark")
    # the face mask: white cheeks and brows, a dark eye between them
    g.paint((17, -3, 8), (17, -2, 9), "white")
    g.paint((16, -3, 8), (16, -3, 9), "white")
    g.paint((16, -3, 12), (17, -2, 12), "white")
    g.set(17, -2, 11, "eye", part="head")
    g.set(16, -3, 11, "eye", part="head")
    # ears: white fronts, rusty backs
    g.box((14, -3, 14), (15, -2, 15), "fur", part="ears")
    g.paint((15, -3, 14), (15, -2, 15), "white")
    # long thick tail, ringed, darker tip
    g.box((-7, -1, 6), (1, 1, 9), "fur", part="tail")
    g.paint((-2, -1, 6), (-1, 1, 9), "ring")
    g.paint((-6, -1, 6), (-5, 1, 9), "ring")
    g.paint((-7, -1, 6), (-7, 1, 9), "dark")
    g.mirror("-Y")
