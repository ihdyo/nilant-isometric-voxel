"""000032 · Arctic Fox (Vulpes lagopus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, shade, nose, pad, white, eye. Size: 34 x 13 x 18 voxels posed."""


def build(g):
    # fluffy winter-white body
    g.box((1, -4, 5), (17, 4, 12), "coat", part="body")
    g.paint((2, -3, 5), (16, 3, 6), "shade", of="body")
    # short furred legs
    for leg, x in (("leg_hl", 2), ("leg_fl", 14)):
        g.box((x, -4, 0), (x + 2, -2, 5), "coat", part=leg)
        g.paint((x, -4, 0), (x + 2, -2, 0), "pad", of=leg)
        g.joint(leg, pivot=(x + 1, -3, 5), parent="body")
    # thick bottle-brush tail
    g.box((-10, -2, 7), (0, 2, 11), "coat", part="tail")
    g.paint((-10, -2, 7), (-1, 2, 8), "shade", of="tail")
    g.joint("tail", pivot=(1, 0, 9), rotate=(0, -12, -6), parent="body")
    # compact head and small rounded ears
    g.box((16, -4, 9), (23, 4, 16), "coat", part="head")
    g.box((23, -2, 9), (24, 2, 12), "coat", part="head")
    g.set(24, 0, 12, "nose", part="head")
    g.box((23, -3, 13), (23, -3, 14), "white", part="head")
    g.box((23, -2, 13), (23, -2, 14), "eye", part="head")
    g.joint("head", pivot=(17, 0, 12), rotate=(4, 2, -10), parent="body")
    g.box((17, -4, 16), (19, -2, 18), "coat", part="ear_l")
    g.paint((19, -3, 16), (19, -3, 17), "shade", of="ear_l")
    g.joint("ear_l", pivot=(18, -3, 16), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(15, -3, 5), rotate=(0, -12, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -3, 5), rotate=(0, 10, 0), parent="body")
    g.joint("leg_fr", pivot=(15, 3, 5), rotate=(0, 6, 0), parent="body")
