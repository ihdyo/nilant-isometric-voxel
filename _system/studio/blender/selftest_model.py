"""Voxel Fauna · selftest creature: a generic blocky quadruped (not a species) that proves the engine end to end.
Used only by `python _system/studio/scripts/vf.py selftest`; its renders go to _system/cache/selftest/.
Palette keys: fur, belly, dark (see SELFTEST_LOOK in scripts/vf.py).
"""


def build(g):
    # legs (2 x 2 voxels, the left side; mirrored at the end)
    for x in (2, 11):
        g.box((x, -3, 0), (x + 1, -2, 5), "fur", part="legs")
        g.box((x, -3, 0), (x + 1, -2, 0), "dark", part="legs")          # paws
    # body
    g.box((1, -3, 6), (14, 3, 11), "fur", part="body")
    g.paint((3, -2, 6), (12, 2, 6), "belly")
    # head, snout, nose, eyes, ears
    g.box((14, -3, 9), (19, 3, 15), "fur", part="head")
    g.box((20, -2, 9), (22, 2, 12), "belly", part="head")
    g.box((22, -1, 11), (22, 1, 12), "dark", part="head")
    g.paint((19, -2, 13), (19, -2, 13), "dark")
    g.box((15, -3, 16), (16, -2, 17), "fur", part="head")
    # tail, rising
    g.box((-1, -1, 10), (0, 1, 11), "fur", part="tail")
    g.box((-3, -1, 11), (-2, 1, 13), "belly", part="tail")
    g.mirror("-Y")
