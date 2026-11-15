"""26-001 · Red Fox (Vulpes vulpes) · voxel model.
Built from docs/voxel-model.md. Palette keys: fur, white, dark, eye. Size: 31 x 7 x 18 voxels."""


def build(g):
    # legs: 2 x 2, black stockings up to the knee
    for x in (5, 14):
        g.box((x, -3, 0), (x + 1, -2, 5), "fur", part="legs")
        g.box((x, -3, 0), (x + 1, -2, 2), "dark", part="legs")
    # body: long and low, a rounded back, a white bib at the chest
    g.box((4, -3, 6), (16, 3, 10), "fur", part="body")
    g.box((6, -2, 11), (14, 2, 11), "fur", part="body")
    g.paint((15, -2, 6), (16, 2, 9), "white")
    # neck and head: narrower than the body, white cheeks and jaw
    g.box((16, -2, 9), (17, 2, 12), "fur", part="head")
    g.box((17, -2, 10), (21, 2, 14), "fur", part="head")
    g.paint((19, -2, 10), (21, 2, 11), "white")
    # long pointed snout, white underneath, black nose
    g.box((22, -1, 10), (24, 1, 11), "white", part="head")
    g.box((22, -1, 12), (23, 1, 12), "fur", part="head")
    g.paint((24, 0, 11), (24, 0, 11), "dark")
    # eye on the corner of the face (seen from the front and the flank)
    g.set(21, -2, 13, "eye", part="head")
    # big pointed ears with black tips
    g.box((18, -2, 15), (19, -1, 16), "fur", part="ears")
    g.set(18, -2, 17, "dark", part="ears")
    # bushy tail with the white tip
    g.box((2, -1, 8), (3, 1, 10), "fur", part="tail")
    g.box((-4, -2, 6), (1, 2, 10), "fur", part="tail")
    g.box((-6, -1, 6), (-5, 1, 9), "white", part="tail")
    g.mirror("-Y")
