"""000036 · Binturong (Arctictis binturong) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, frost, ear, muzzle, white, eye. Size: 44 x 14 x 17 voxels posed."""


def build(g):
    # shaggy charcoal body with silver frosting
    g.box((1, -4, 4), (21, 4, 11), "coat", part="body")
    for x, y in ((5, -4), (11, -4), (17, -4), (7, 4), (14, 4)):
        g.box((x, y, 8), (x + 1, y, 10), "frost", part="body")
    # short sturdy climbing legs
    for leg, x in (("leg_hl", 2), ("leg_fl", 16)):
        g.box((x, -4, 0), (x + 2, -2, 4), "coat", part=leg)
        g.joint(leg, pivot=(x + 1, -3, 4), parent="body")
    # thick prehensile tail in two segments
    g.box((-8, -2, 6), (0, 2, 9), "coat", part="tail_1")
    g.joint("tail_1", pivot=(1, 0, 7.5), rotate=(0, 10, 0), parent="body")
    g.box((-16, -1, 5), (-9, 1, 7), "coat", part="tail_2")
    g.joint("tail_2", pivot=(-8, 0, 6.5), rotate=(0, -28, -12), parent="tail_1")
    # grizzled head and white-trimmed tufted ears
    g.box((20, -4, 7), (27, 4, 14), "coat", part="head")
    g.paint((24, -4, 11), (27, 4, 14), "frost", of="head")
    g.box((27, -2, 7), (28, 2, 10), "muzzle", part="head")
    g.box((27, -3, 11), (27, -3, 12), "white", part="head")
    g.box((27, -2, 11), (27, -2, 12), "eye", part="head")
    g.joint("head", pivot=(21, 0, 10), rotate=(4, 3, -10), parent="body")
    g.box((21, -4, 14), (22, -3, 15), "ear", part="ear_l")
    g.set(21, -4, 16, "coat", part="ear_l")
    g.joint("ear_l", pivot=(21.5, -3.5, 14), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(17, -3, 4), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -3, 4), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(17, 3, 4), rotate=(0, 6, 0), parent="body")
