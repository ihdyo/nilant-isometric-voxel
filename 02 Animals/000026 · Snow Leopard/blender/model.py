"""000026 · Snow Leopard (Panthera uncia) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, spot, belly, nose, white, eye. Size: 46 x 16 x 23 voxels posed."""


def build(g):
    # body: muscular torso with white underbelly
    g.box((1, -5, 9), (22, 5, 17), "coat", part="body")
    g.paint((2, -4, 9), (21, 4, 10), "belly", of="body")
    for x, y in ((4, -5), (9, -5), (14, -5), (18, -5), (6, 5), (12, 5), (17, 5)):
        g.box((x, y, 13), (x + 1, y, 15), "spot", part="body")
    # legs: thick snow-ready paws
    for leg, shin, x in (("leg_hl", "shin_hl", 2), ("leg_fl", "shin_fl", 17)):
        g.box((x, -5, 5), (x + 3, -2, 9), "coat", part=leg)
        g.box((x, -5, 0), (x + 3, -2, 4), "coat", part=shin)
        g.paint((x, -5, 0), (x + 3, -2, 1), "belly", of=shin)
        g.joint(leg, pivot=(x + 2, -3.5, 9), parent="body")
        g.joint(shin, pivot=(x + 2, -3.5, 5), parent=leg)
    # long thick tail in two segments
    g.box((-8, -2, 12), (0, 2, 15), "coat", part="tail_1")
    g.paint((-6, -2, 13), (-5, 2, 15), "spot", of="tail_1")
    g.joint("tail_1", pivot=(1, 0, 14), rotate=(0, 12, -8), parent="body")
    g.box((-17, -2, 11), (-9, 2, 14), "coat", part="tail_2")
    g.paint((-15, -2, 11), (-13, 2, 14), "spot", of="tail_2")
    g.joint("tail_2", pivot=(-8, 0, 13), rotate=(0, -18, -12), parent="tail_1")
    # head & rounded ears
    g.box((21, -5, 13), (29, 5, 22), "coat", part="head")
    g.paint((27, -3, 13), (29, 3, 16), "belly", of="head")
    g.box((29, -1, 16), (29, 1, 17), "nose", part="head")
    g.box((29, -4, 18), (29, -4, 19), "white", part="head")
    g.box((29, -3, 18), (29, -3, 19), "eye", part="head")
    g.joint("head", pivot=(22, 0, 17), rotate=(4, 3, -10), parent="body")
    g.box((23, -5, 22), (25, -3, 24), "coat", part="ear_l")
    g.joint("ear_l", pivot=(24, -4, 22), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(19, -3.5, 9), rotate=(0, -12, 0), parent="body")
    g.joint("leg_hl", pivot=(4, -3.5, 9), rotate=(0, 10, 0), parent="body")
    g.joint("leg_fr", pivot=(19, 3.5, 9), rotate=(0, 6, 0), parent="body")
    g.joint("shin_fl", pivot=(19, -3.5, 5), rotate=(0, 14, 0), parent="leg_fl")
    g.joint("shin_hl", pivot=(4, -3.5, 5), rotate=(0, -10, 0), parent="leg_hl")
