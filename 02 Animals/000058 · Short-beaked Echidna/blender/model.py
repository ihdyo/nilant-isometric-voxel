"""000058 · Short-beaked Echidna (Tachyglossus aculeatus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, spine, snout, white, eye. Size: 30 x 14 x 17 voxels.
Personality: shy and tenacious, a walking pincushion with a curious nose. Pose: a low waddle, slender snout angled down toward an anthill, spines bristling neatly. Expression: tiny bright eyes tucked at the base of a long tubular snout."""


def build(g):
    # body: rounded dome covered in cream-and-black spines
    g.box((2, -6, 3), (19, 6, 13), "coat", part="body")
    for sx in range(3, 19, 3):
        for sy in (-5, -2, 2, 5):
            g.box((sx, sy, 13), (sx, sy, 16), "spine", part="body")
    for sz in (6, 10):
        for sx in range(4, 18, 3):
            g.box((sx, -7, sz), (sx, -7, sz + 1), "spine", part="body")
    # stout clawed digging feet
    for leg, x in (("leg_hl", 4), ("leg_fl", 14)):
        g.box((x, -6, 0), (x + 3, -3, 3), "snout", part=leg)
        g.joint(leg, pivot=(x + 1.5, -4.5, 3), parent="body")
    # compact head and long slender tubular snout
    g.box((19, -4, 4), (24, 4, 10), "coat", part="head")
    g.box((24, -1, 4), (31, 1, 6), "snout", part="head")
    g.joint("head", pivot=(19, 0, 7), rotate=(3, 8, -8), parent="body")
    g.box((22, -4, 7), (23, -4, 8), "white", part="head")
    g.box((23, -4, 7), (23, -4, 8), "eye", part="head")
    g.mirror()
    g.joint("leg_fl", pivot=(15.5, -4.5, 3), rotate=(0, -8, 0), parent="body")
