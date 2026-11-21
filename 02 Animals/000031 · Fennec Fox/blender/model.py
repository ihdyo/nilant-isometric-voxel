"""000031 · Fennec Fox (Vulpes zerda) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, ear_in, belly, tip, white, eye. Size: 28 x 14 x 24 voxels posed."""


def build(g):
    # petite desert body
    g.box((1, -3, 5), (14, 3, 10), "coat", part="body")
    g.paint((2, -2, 5), (13, 2, 6), "belly", of="body")
    # slender legs
    for leg, x in (("leg_hl", 2), ("leg_fl", 12)):
        g.box((x, -3, 0), (x + 1, -2, 5), "coat", part=leg)
        g.joint(leg, pivot=(x + 1, -2.5, 5), parent="body")
    # fluffy black-tipped tail
    g.box((-8, -1, 7), (0, 1, 10), "coat", part="tail")
    g.paint((-8, -1, 7), (-6, 1, 10), "tip", of="tail")
    g.joint("tail", pivot=(1, 0, 8.5), rotate=(0, -22, -10), parent="body")
    # head with cream mask and giant ears
    g.box((13, -4, 8), (19, 4, 15), "coat", part="head")
    g.paint((18, -3, 8), (19, 3, 11), "belly", of="head")
    g.box((19, -1, 9), (20, 1, 11), "belly", part="head")
    g.set(20, 0, 11, "tip", part="head")
    g.box((19, -3, 12), (19, -3, 13), "white", part="head")
    g.box((19, -2, 12), (19, -2, 13), "eye", part="head")
    g.joint("head", pivot=(14, 0, 11), rotate=(5, 2, -10), parent="body")
    # giant ears
    g.box((14, -6, 15), (16, -2, 23), "coat", part="ear_l")
    g.paint((16, -5, 16), (16, -3, 22), "ear_in", of="ear_l")
    g.joint("ear_l", pivot=(15, -3.5, 15), rotate=(0, 0, 14), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(13, -2.5, 5), rotate=(0, -12, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -2.5, 5), rotate=(0, 10, 0), parent="body")
    g.joint("leg_fr", pivot=(13, 2.5, 5), rotate=(0, 8, 0), parent="body")
