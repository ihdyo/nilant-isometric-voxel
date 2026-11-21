"""000015 · European Hedgehog (Erinaceus europaeus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: spines, tips, face, nose, eye, feet. Size: 18 x 11 x 11 voxels posed.
Personality: shy, snuffly and curious. Pose: trotting, the head low and sniffing ahead, turned to the camera, one
front foot stepping out. Expression: beady black eyes and a little black nose on a soft furry face, painted flat; pale
one-voxel spines stand out of the dome."""


def build(g):
    # tiny feet under the body
    for name, x in (("leg_hl", 1), ("leg_fl", 8)):
        g.box((x, -3, 0), (x + 1, -2, 1), "feet", part=name)
        g.joint(name, pivot=(x + 1, -2.5, 2), parent="body")
    # body: the dome of spines, a bulky box with a narrower ridge on top, and a hood of spines reaching forward over
    # the face; a furry tan belly edge
    g.box((0, -4, 2), (11, 4, 8), "spines", part="body")
    g.box((1, -3, 9), (10, 3, 9), "spines", part="body")
    g.box((12, -3, 6), (13, 3, 8), "spines", part="body")
    g.paint((1, -4, 2), (11, 4, 2), "face", of="body")
    # spines: single pale voxels standing out of the dome in staggered rows, on the flank, the ridge and the hood
    for z, xs in ((3, (1, 4, 7, 10)), (5, (2, 5, 8, 11)), (7, (1, 4, 7, 10))):
        for x in xs:
            g.set(x, -5, z, "tips", part="body")
    for x in (3, 6, 9):
        g.set(x, -4, 9, "tips", part="body")
    for x, y in ((2, -2), (5, -2), (8, -2), (4, 0), (7, 0), (10, 0)):
        g.set(x, y, 10, "tips", part="body")
    g.set(12, -4, 7, "tips", part="body")
    g.set(13, -2, 9, "tips", part="body")
    # head: a soft furry face under the hood, a short snout in front
    g.box((12, -3, 2), (15, 3, 5), "face", part="head")
    g.box((16, -1, 2), (17, 1, 3), "face", part="head")
    g.joint("head", pivot=(12, 0.5, 4), rotate=(3, 8, -14), parent="body")
    # face, painted flat: beady black eyes above the snout, a little black nose on the snout's tip
    g.set(15, -2, 4, "eye", part="head")
    g.set(17, 0, 3, "nose", part="head")
    g.mirror()
    # one front foot stepping out
    g.joint("leg_fl", pivot=(9, -2.5, 2), rotate=(0, -18, 0), parent="body")
    # a livelier pose (owner 2026-11-21); the head turned to the camera
    g.joint("leg_fr", pivot=(9, 3.5, 2), rotate=(0, 10, 0), parent="body")
    g.joint("leg_hl", pivot=(2, -2.5, 2), rotate=(0, 12, 0), parent="body")
    g.joint("leg_hr", pivot=(2, 3.5, 2), rotate=(0, -12, 0), parent="body")
