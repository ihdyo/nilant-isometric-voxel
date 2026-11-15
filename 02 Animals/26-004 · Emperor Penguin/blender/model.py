"""26-004 · Emperor Penguin (Aptenodytes forsteri) · voxel model.
Built from docs/voxel-model.md. Palette keys: black, white, yellow, cream, bill. Size: 12 x 11 x 26 voxels."""


def build(g):
    # feet: black, flat on the ice, toes forward
    g.box((4, -3, 0), (7, -2, 0), "black", part="legs")
    # body: a tall column, black back and flanks, white front, corners stepped round
    g.box((0, -4, 1), (7, 4, 17), "black", part="body")
    g.carve((0, -4, 1), (0, -4, 17))
    g.carve((7, -4, 1), (7, -4, 17))
    g.carve((0, -4, 15), (7, -3, 17))
    g.paint((4, -3, 1), (7, 3, 15), "white")
    g.paint((6, -3, 13), (7, 3, 15), "cream")
    # neck and head: narrower, black
    g.box((1, -3, 18), (6, 3, 19), "black", part="head")
    g.box((2, -3, 20), (7, 3, 25), "black", part="head")
    # the yellow ear patch on the side of the head, fading to the pale breast
    g.paint((3, -3, 19), (5, -3, 22), "yellow")
    g.paint((6, -3, 18), (6, -3, 19), "yellow")
    # long slightly down-curved beak with the orange stripe below
    g.box((8, 0, 22), (9, 0, 23), "black", part="beak")
    g.set(10, 0, 22, "black", part="beak")
    g.paint((8, 0, 22), (9, 0, 22), "bill")
    # flippers along the flanks
    g.box((2, -5, 7), (4, -5, 15), "black", part="wings")
    # short tail
    g.box((-1, -1, 1), (-1, 0, 2), "black", part="tail")
    g.mirror("-Y")
