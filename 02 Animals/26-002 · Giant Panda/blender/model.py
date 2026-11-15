"""26-002 · Giant Panda (Ailuropoda melanoleuca) · voxel model.
Built from docs/voxel-model.md. Palette keys: white, black, eye. Size: 22 x 9 x 19 voxels."""


def build(g):
    # legs: thick 3 x 3, all black
    for x in (3, 11):
        g.box((x, -4, 0), (x + 2, -2, 5), "black", part="legs")
    # body: a round white barrel, the black band over the shoulders down to the front legs
    g.box((2, -4, 6), (14, 4, 12), "white", part="body")
    g.box((4, -3, 13), (12, 3, 13), "white", part="body")
    g.paint((10, -4, 6), (13, 4, 13), "black")
    # head: big and round, white
    g.box((14, -4, 9), (20, 4, 16), "white", part="head")
    g.box((15, -3, 17), (19, 3, 17), "white", part="head")
    g.carve((20, -4, 16), (20, -4, 16))
    # short muzzle and black nose
    g.box((21, -2, 9), (22, 2, 11), "white", part="head")
    g.paint((22, -1, 11), (22, 0, 11), "black")
    # eye patches wrapping the corner of the face, a light eye inside
    g.paint((19, -4, 12), (20, -2, 14), "black")
    g.set(20, -3, 13, "eye", part="head")
    # round black ears
    g.box((15, -4, 17), (16, -3, 18), "black", part="ears")
    # little white tail
    g.box((1, -1, 9), (1, 0, 10), "white", part="tail")
    g.mirror("-Y")
