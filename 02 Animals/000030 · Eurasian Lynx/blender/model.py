"""000030 · Eurasian Lynx (Lynx lynx) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, tuft, ruff, spot, white, eye. Size: 34 x 15 x 26 voxels posed."""


def build(g):
    # tall compact torso
    g.box((2, -4, 10), (20, 4, 18), "coat", part="body")
    g.paint((3, -3, 10), (19, 3, 11), "ruff", of="body")
    for x, y in ((5, -4), (10, -4), (15, -4), (7, 4), (13, 4)):
        g.set(x, y, 14, "spot", part="body")
    # long forest legs
    for leg, shin, x in (("leg_hl", "shin_hl", 3), ("leg_fl", "shin_fl", 17)):
        g.box((x, -4, 6), (x + 2, -2, 10), "coat", part=leg)
        g.box((x, -4, 0), (x + 2, -2, 5), "coat", part=shin)
        g.joint(leg, pivot=(x + 1, -3, 10), parent="body")
        g.joint(shin, pivot=(x + 1, -3, 6), parent=leg)
    # short black-tipped bobtail
    g.box((-2, -1, 15), (1, 1, 18), "coat", part="tail")
    g.paint((-2, -1, 15), (-1, 1, 18), "tuft", of="tail")
    g.joint("tail", pivot=(2, 0, 16), rotate=(0, -20, 0), parent="body")
    # head with cheek ruffs and tall tufted ears
    g.box((19, -5, 14), (26, 5, 22), "coat", part="head")
    g.paint((20, -5, 14), (24, -5, 17), "ruff", of="head")
    g.paint((25, -3, 14), (26, 3, 16), "ruff", of="head")
    g.box((26, -3, 18), (26, -3, 19), "white", part="head")
    g.box((26, -2, 18), (26, -2, 19), "eye", part="head")
    g.joint("head", pivot=(20, 0, 18), rotate=(4, 3, -10), parent="body")
    g.box((21, -4, 22), (23, -3, 24), "coat", part="ear_l")
    g.box((22, -4, 25), (22, -3, 26), "tuft", part="ear_l")
    g.joint("ear_l", pivot=(22, -3.5, 22), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(18, -3, 10), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(4, -3, 10), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(18, 3, 10), rotate=(0, 5, 0), parent="body")
    g.joint("shin_fl", pivot=(18, -3, 6), rotate=(0, 12, 0), parent="leg_fl")
    g.joint("shin_hl", pivot=(4, -3, 6), rotate=(0, -8, 0), parent="leg_hl")
