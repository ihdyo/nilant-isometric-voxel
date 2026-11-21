"""000048 · Llama (Lama glama) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, patch, face, pad, white, eye. Size: 34 x 14 x 34 voxels posed."""


def build(g):
    # woolly body with chestnut saddle patch
    g.box((1, -4, 10), (18, 4, 18), "coat", part="body")
    g.paint((5, -4, 13), (13, 4, 18), "patch", of="body")
    # slender legs with short-haired lower shins and padded feet
    for leg, x in (("leg_hl", 2), ("leg_fl", 14)):
        g.box((x, -4, 0), (x + 2, -2, 10), "coat", part=leg)
        g.paint((x, -4, 0), (x + 2, -2, 3), "face", of=leg)
        g.paint((x, -4, 0), (x + 2, -2, 0), "pad", of=leg)
        g.joint(leg, pivot=(x + 1, -3, 10), parent="body")
    # tall upright woolly neck
    g.box((13, -3, 18), (18, 3, 28), "coat", part="neck")
    g.paint((13, -3, 21), (16, 3, 25), "patch", of="neck")
    g.joint("neck", pivot=(15.5, 0, 18), parent="body")
    # short fluffy tail
    g.box((-1, -1, 14), (0, 1, 17), "coat", part="tail")
    g.joint("tail", pivot=(0, 0, 17), rotate=(-12, 0, 0), parent="body")
    # head with clean dark muzzle & tall banana-shaped ears
    g.box((14, -3, 27), (20, 3, 31), "coat", part="head")
    g.box((20, -2, 27), (22, 2, 29), "face", part="head")
    g.set(20, -3, 29, "white", part="head")
    g.set(20, -2, 29, "eye", part="head")
    g.joint("head", pivot=(16, 0, 27), rotate=(3, 2, -10), parent="neck")
    g.box((15, -3, 31), (17, -2, 34), "coat", part="ear_l")
    g.set(16, -2, 35, "coat", part="ear_l")
    g.joint("ear_l", pivot=(16, -2.5, 31), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(15, -3, 10), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -3, 10), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(15, 3, 10), rotate=(0, 5, 0), parent="body")
