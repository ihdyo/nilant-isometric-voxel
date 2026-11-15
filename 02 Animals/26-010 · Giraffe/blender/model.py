"""26-010 · Giraffe (Giraffa camelopardalis) · voxel model.
Built from docs/voxel-model.md. Palette keys: patch, base, mane, dark, eye. Size: 20 x 5 x 32 voxels."""


def build(g):
    # long legs: 2 x 2 under a slim body, cream with dark hooves, patches on the upper legs
    for x in (3, 11):
        g.box((x, -2, 0), (x + 1, -1, 10), "base", part="legs")
        g.box((x, -2, 0), (x + 1, -1, 0), "dark", part="legs")
        g.paint((x, -2, 8), (x + 1, -1, 9), "patch")
    # body: short, sloping up to the high shoulders
    g.box((2, -2, 11), (13, 2, 15), "base", part="body")
    g.box((8, -2, 16), (13, 2, 16), "base", part="body")
    # the very long neck, rising almost straight up and a little forward, mane along the back
    g.box((11, -1, 17), (13, 1, 21), "base", part="neck")
    g.box((12, -1, 22), (14, 1, 25), "base", part="neck")
    g.box((13, -1, 26), (15, 1, 27), "base", part="neck")
    g.box((11, 0, 17), (11, 0, 21), "mane", part="neck")
    g.box((12, 0, 22), (12, 0, 25), "mane", part="neck")
    # head pointing forward, the muzzle, ears and ossicones with dark tufts
    g.box((14, -1, 27), (18, 1, 30), "base", part="head")
    g.box((19, -1, 27), (19, 1, 28), "base", part="head")
    g.set(19, 0, 28, "dark", part="head")
    g.set(17, -1, 29, "eye", part="head")
    g.box((15, -1, 31), (15, -1, 31), "dark", part="head")
    g.set(16, -2, 30, "base", part="head")
    # the patch network: brown blocks separated by cream lines
    for x0 in (2, 5, 8, 11):
        g.paint((x0, -2, 12), (x0 + 1, 2, 13), "patch")
    for x0 in (3, 6, 9, 12):
        g.paint((x0, -2, 15), (x0 + 1, 2, 15), "patch")
    g.paint((11, -1, 18), (13, 1, 19), "patch")
    g.paint((12, -1, 23), (14, 1, 24), "patch")
    g.paint((14, -1, 27), (15, 1, 27), "patch")
    # thin tail with a dark tuft
    g.box((1, 0, 11), (1, 0, 14), "base", part="tail")
    g.box((1, 0, 9), (1, 0, 10), "dark", part="tail")
    g.mirror("-Y")
