"""000027 · Cheetah (Acinonyx jubatus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, spot, belly, tear, white, eye. Size: 46 x 14 x 24 voxels posed."""


def build(g):
    # slender aerodynamic body
    g.box((1, -4, 11), (23, 4, 18), "coat", part="body")
    g.paint((3, -3, 11), (22, 3, 12), "belly", of="body")
    for x, y, z in ((4, -4, 15), (8, -4, 14), (12, -4, 16), (16, -4, 14), (20, -4, 15), (6, 4, 15), (11, 4, 14), (17, 4, 16)):
        g.set(x, y, z, "spot", part="body")
    # long runner legs
    for leg, shin, x in (("leg_hl", "shin_hl", 2), ("leg_fl", "shin_fl", 19)):
        g.box((x, -4, 6), (x + 2, -2, 11), "coat", part=leg)
        g.box((x, -4, 0), (x + 2, -2, 5), "coat", part=shin)
        g.joint(leg, pivot=(x + 1, -3, 11), parent="body")
        g.joint(shin, pivot=(x + 1, -3, 6), parent=leg)
    # long ringed tail with white tip
    g.box((-14, -1, 14), (0, 1, 16), "coat", part="tail")
    g.paint((-14, -1, 14), (-12, 1, 16), "white", of="tail")
    for x in (-10, -7, -4):
        g.paint((x, -1, 14), (x, 1, 16), "spot", of="tail")
    g.joint("tail", pivot=(1, 0, 15), rotate=(0, 8, -6), parent="body")
    # compact head with black tear streaks
    g.box((22, -4, 16), (29, 4, 23), "coat", part="head")
    g.paint((27, -2, 16), (29, 2, 18), "belly", of="head")
    g.box((29, -3, 17), (29, -3, 19), "tear", part="head")
    g.box((29, -3, 20), (29, -3, 20), "white", part="head")
    g.box((29, -2, 20), (29, -2, 20), "eye", part="head")
    g.joint("head", pivot=(23, 0, 18), rotate=(3, 2, -8), parent="body")
    g.box((23, -4, 24), (24, -3, 25), "coat", part="ear_l")
    g.joint("ear_l", pivot=(23.5, -3.5, 24), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(20, -3, 11), rotate=(0, -16, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -3, 11), rotate=(0, 12, 0), parent="body")
    g.joint("leg_fr", pivot=(20, 3, 11), rotate=(0, 8, 0), parent="body")
    g.joint("shin_fl", pivot=(20, -3, 6), rotate=(0, 18, 0), parent="leg_fl")
    g.joint("shin_hl", pivot=(3, -3, 6), rotate=(0, -14, 0), parent="leg_hl")
