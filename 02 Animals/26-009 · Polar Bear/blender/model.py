"""26-009 · Polar Bear (Ursus maritimus) · voxel model.
Built from docs/voxel-model.md. Palette keys: fur, dark. Size: 26 x 9 x 15 voxels."""


def build(g):
    # legs: thick 3 x 3 pillars, big paws (dark claws at the front edge)
    for x in (3, 14):
        g.box((x, -4, 0), (x + 2, -2, 6), "fur", part="legs")
        g.box((x + 2, -4, 0), (x + 2, -2, 0), "dark", part="legs")
    # body: long and heavy, high at the hips, sloping to the shoulders
    g.box((2, -4, 7), (17, 4, 13), "fur", part="body")
    g.box((3, -3, 14), (12, 3, 14), "fur", part="body")
    # long neck and the long narrow head, typical of polar bears
    g.box((17, -3, 9), (19, -2, 12), "fur", part="head")
    g.box((17, -3, 9), (19, 0, 12), "fur", part="head")
    g.box((20, -3, 9), (23, 0, 12), "fur", part="head")
    # the tapering snout, black nose
    g.box((24, -2, 9), (25, 0, 11), "fur", part="head")
    g.box((25, -1, 11), (25, 0, 11), "dark", part="head")
    # small eye, small round ears
    g.set(22, -3, 11, "dark", part="head")
    g.box((20, -3, 13), (20, -2, 13), "fur", part="head")
    # stubby tail
    g.box((1, -1, 11), (1, 0, 12), "fur", part="tail")
    g.mirror("-Y")
