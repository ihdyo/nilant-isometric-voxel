"""26-005 · Capybara (Hydrochoerus hydrochaeris) · voxel model.
Built from docs/voxel-model.md. Palette keys: fur, dark, eye. Size: 24 x 9 x 15 voxels."""


def build(g):
    # legs: short 2 x 2, darker feet
    for x in (3, 13):
        g.box((x, -3, 0), (x + 1, -2, 3), "fur", part="legs")
        g.box((x, -3, 0), (x + 1, -2, 0), "dark", part="legs")
    # body: a big rounded barrel, the rump sloping down at the back, no tail
    g.box((2, -4, 4), (16, 4, 10), "fur", part="body")
    g.box((3, -3, 11), (15, 3, 12), "fur", part="body")
    g.carve((2, -4, 10), (16, -4, 10))
    g.carve((2, -4, 4), (2, -4, 10))
    g.carve((2, -3, 12), (3, 3, 12))
    g.box((1, -3, 5), (1, 3, 9), "fur", part="body")
    # head: big and blunt, flat on top, set high on a short neck
    g.box((17, -3, 6), (21, 3, 13), "fur", part="head")
    # the deep blunt muzzle, a step narrower and lower, the same brown; dark nostrils high on the front
    g.box((22, -2, 6), (23, 2, 11), "fur", part="head")
    g.carve((23, -2, 11), (23, 2, 11))
    g.paint((23, -1, 9), (23, -1, 10), "dark")
    # eyes high on the side of the head
    g.set(20, -3, 12, "eye", part="head")
    # small round ears on top, at the back of the head
    g.box((17, -3, 14), (18, -2, 14), "dark", part="ears")
    g.mirror("-Y")
