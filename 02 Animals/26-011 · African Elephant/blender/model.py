"""26-011 · African Elephant (Loxodonta africana) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: skin, shade, tusk, nail, white, eye. Size: 53 x 35 x 39 voxels posed.
Personality: wise and gentle, the herd's calm leader. Pose: a slow, heavy step, the big ears spread wide, the trunk
lifted and curling up at the tip, the head turned a little to the camera. Expression: kind white eyes with the pupils
to the inside under soft level brows, a small smile, all painted flat."""


def build(g):
    # body: one huge bulky box
    g.box((0, -9, 14), (29, 9, 31), "skin", part="body")
    # legs: thick 6 x 6 pillars, an upper leg and a shin hinged at the knee, pale toenails on the front
    for leg, shin, x in (("leg_hl", "shin_hl", 1), ("leg_fl", "shin_fl", 23)):
        g.box((x, -9, 7), (x + 5, -4, 13), "skin", part=leg)
        g.box((x, -9, 0), (x + 5, -4, 6), "skin", part=shin)
        for y in (-8, -6):
            g.box((x + 5, y, 0), (x + 5, y, 1), "nail", part=shin)
        g.joint(leg, pivot=(x + 3, -6.5, 14), parent="body")
        g.joint(shin, pivot=(x + 3, -6.5, 7), parent=leg)
    # tail: a thin column with a dark tuft
    g.box((-1, 0, 21), (-1, 0, 29), "skin", part="tail")
    g.box((-1, 0, 19), (-1, 0, 20), "shade", part="tail")
    g.joint("tail", pivot=(-0.5, 0.5, 29.5), rotate=(-12, 0, 0), parent="body")
    # head: a big box stacked on the front of the body, a little lower than the back
    g.box((29, -7, 20), (39, 7, 36), "skin", part="head")
    g.joint("head", pivot=(30, 0.5, 26), rotate=(6, 4, -10), parent="body")
    # face, painted flat: white eyes with the pupils to the inside, soft level brows, a smile at the corners
    g.box((39, -5, 29), (39, -5, 30), "white", part="head")
    g.box((39, -4, 29), (39, -4, 30), "eye", part="head")
    g.box((39, -6, 32), (39, -3, 32), "shade", part="head")
    g.set(39, -4, 22, "eye", part="head")
    g.set(39, -3, 21, "eye", part="head")
    # ears: huge flat slabs on the sides of the head, the inner face darker, spread forward
    g.box((30, -17, 18), (31, -8, 36), "skin", part="ear_l")
    g.paint((31, -16, 20), (31, -9, 34), "shade", of="ear_l")
    g.joint("ear_l", pivot=(30.5, -7.5, 30), rotate=(0, 0, 28), parent="head")
    # tusks: pale blocks from the sides of the trunk, curving up
    g.box((40, -4, 21), (44, -3, 22), "tusk", part="tusk_l")
    g.joint("tusk_l", pivot=(40, -3.5, 21.5), rotate=(0, -22, -6), parent="head")
    # trunk: three blocks hanging from the face, each turned forward a little more, so it curls up in front of it
    g.box((40, -2, 20), (42, 2, 26), "skin", part="trunk_1")
    g.joint("trunk_1", pivot=(41, 0.5, 26), rotate=(0, -30, 0), parent="head")
    g.box((40, -1, 15), (41, 1, 19), "skin", part="trunk_2")
    g.joint("trunk_2", pivot=(41, 0.5, 19.5), rotate=(0, -40, 0), parent="trunk_1")
    g.box((40, -1, 11), (41, 1, 14), "skin", part="trunk_3")
    g.paint((40, -1, 11), (41, 1, 11), "shade", of="trunk_3")
    g.joint("trunk_3", pivot=(41, 0.5, 14.5), rotate=(0, -40, 0), parent="trunk_2")
    g.mirror()
    # a slow, heavy step: the front left foot forward, the hind left back
    g.joint("leg_fl", pivot=(26, -6.5, 14), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(4, -6.5, 14), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(26, 7.5, 14), rotate=(0, 5, 0), parent="body")
    # the knees: the stepping front foot folds back a little, the hind knee flexes
    g.joint("shin_fl", pivot=(26, -6.5, 7), rotate=(0, 16, 0), parent="leg_fl")
    g.joint("shin_hl", pivot=(4, -6.5, 7), rotate=(0, -8, 0), parent="leg_hl")
