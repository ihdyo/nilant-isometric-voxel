"""000047 · Okapi (Okapia johnstoni) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, stripe, sock, face, horn, eye. Size: 40 x 15 x 30 voxels posed."""


def build(g):
    # sloping chestnut-chocolate torso with zebra-striped rump
    g.box((1, -5, 10), (21, 5, 19), "coat", part="body")
    g.box((12, -5, 19), (21, 5, 20), "coat", part="body")
    for z in (12, 14, 16):
        g.paint((1, -5, z), (5, 5, z), "stripe", of="body")
    # slender legs with white stockings and striped upper thighs
    for leg, x in (("leg_hl", 2), ("leg_fl", 17)):
        g.box((x, -4, 0), (x + 2, -2, 10), "sock", part=leg)
        g.paint((x, -4, 0), (x + 2, -2, 0), "horn", of=leg)
        g.paint((x, -4, 7), (x + 2, -2, 7), "coat", of=leg)
        g.paint((x, -4, 9), (x + 2, -2, 9), "coat", of=leg)
        g.joint(leg, pivot=(x + 1, -3, 10), parent="body")
    # tall giraffe-like neck
    g.box((17, -3, 18), (22, 3, 26), "coat", part="neck")
    g.paint((22, -2, 19), (22, 2, 25), "face", of="neck")
    g.joint("neck", pivot=(19.5, 0, 19), rotate=(0, 10, 0), parent="body")
    # tufted tail
    g.box((-1, 0, 12), (0, 0, 18), "coat", part="tail")
    g.paint((-1, 0, 12), (0, 0, 13), "horn", of="tail")
    g.joint("tail", pivot=(0, 0, 18), rotate=(-8, 0, 0), parent="body")
    # pale-cheeked head, ossicones & large ears
    g.box((19, -3, 24), (27, 3, 29), "face", part="head")
    g.paint((19, -3, 28), (25, 3, 29), "coat", of="head")
    g.set(25, -3, 27, "sock", part="head")
    g.set(26, -3, 27, "eye", part="head")
    g.box((20, -2, 29), (21, -2, 30), "horn", part="head")
    g.joint("head", pivot=(20, 0, 25), rotate=(3, 3, -10), parent="neck")
    g.box((19, -5, 28), (21, -3, 31), "coat", part="ear_l")
    g.paint((21, -5, 29), (21, -4, 30), "face", of="ear_l")
    g.joint("ear_l", pivot=(20, -3.5, 28), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(18, -3, 10), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -3, 10), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(18, 3, 10), rotate=(0, 5, 0), parent="body")
