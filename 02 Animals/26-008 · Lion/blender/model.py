"""26-008 · Lion (Panthera leo), adult male · voxel model.
Built from docs/voxel-model.md. Palette keys: coat, mane, muzzle, nose, eye. Size: 32 x 11 x 19 voxels."""


def build(g):
    # legs: 2 x 2, long and strong
    for x in (4, 15):
        g.box((x, -3, 0), (x + 1, -2, 6), "coat", part="legs")
    # body: long, deep chest, a level back
    g.box((3, -3, 7), (17, 3, 12), "coat", part="body")
    g.box((5, -2, 13), (14, 2, 13), "coat", part="body")
    # the mane: a big rounded collar that frames the face on every side
    g.box((16, -5, 8), (23, 5, 17), "mane", part="mane")
    g.box((17, -4, 18), (22, 4, 18), "mane", part="mane")
    g.carve((16, -5, 17), (23, -5, 17))
    g.carve((16, -5, 8), (16, -5, 17))
    g.carve((23, -5, 8), (23, -5, 9))
    # the face set into the front of the mane, pale muzzle, dark nose
    g.box((23, -3, 10), (25, 3, 15), "coat", part="head")
    g.box((26, -2, 10), (27, 2, 12), "muzzle", part="head")
    g.box((27, -1, 12), (27, 0, 12), "nose", part="head")
    g.set(25, -2, 14, "eye", part="head")
    g.set(25, -3, 13, "coat", part="head")
    # small round ears poking out of the top of the mane
    g.box((22, -3, 18), (22, -2, 19), "coat", part="head")
    # long tail ending in a dark tuft
    g.box((0, 0, 11), (2, 0, 12), "coat", part="tail")
    g.box((-2, 0, 9), (-1, 0, 11), "coat", part="tail")
    g.box((-4, -1, 7), (-2, 1, 9), "mane", part="tail")
    g.mirror("-Y")
