"""000050 · Bactrian Camel (Camelus bactrianus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, shag, muzzle, white, eye. Size: 43 x 16 x 40 voxels.
Personality: steadfast and unhurried, a seasoned desert navigator. Pose: a measured desert stride, neck dipped and raised proudly, twin humps standing tall. Expression: calm half-lidded eyes with long lashes and a gentle closed-mouth smile."""


def build(g):
    # body: sturdy desert torso with twin dorsal humps
    g.box((2, -7, 16), (26, 7, 29), "coat", part="body")
    g.box((5, -5, 30), (11, 5, 37), "coat", part="body")
    g.box((16, -5, 30), (22, 5, 37), "coat", part="body")
    g.box((6, -4, 38), (10, 4, 39), "shag", part="body")
    g.box((17, -4, 38), (21, 4, 39), "shag", part="body")
    # legs: four long slender pillars with broad two-toed foot pads
    for leg, shin, x in (("leg_hl", "shin_hl", 3), ("leg_fl", "shin_fl", 21)):
        g.box((x, -7, 8), (x + 3, -4, 15), "coat", part=leg)
        g.box((x, -7, 1), (x + 3, -4, 7), "coat", part=shin)
        g.box((x, -8, 0), (x + 4, -3, 0), "muzzle", part=shin)
        g.joint(leg, pivot=(x + 1.5, -5.5, 16), parent="body")
        g.joint(shin, pivot=(x + 1.5, -5.5, 8), parent=leg)
    # tail: slender tail with dark tuft
    g.box((0, -1, 18), (1, 1, 26), "coat", part="tail")
    g.box((0, -1, 15), (1, 1, 17), "shag", part="tail")
    g.joint("tail", pivot=(1, 0, 26), rotate=(-10, 0, 0), parent="body")
    # neck and shaggy throat mane
    g.box((25, -4, 15), (32, 4, 29), "coat", part="neck")
    g.box((26, -5, 13), (31, 5, 22), "shag", part="neck")
    g.joint("neck", pivot=(26, 0, 22), rotate=(0, -14, 0), parent="body")
    # head: elongated camel head with split upper lip and small ears
    g.box((29, -4, 28), (40, 4, 35), "coat", part="head")
    g.box((38, -3, 28), (42, 3, 32), "muzzle", part="head")
    g.box((30, -5, 35), (32, -4, 37), "coat", part="ear_l")
    g.joint("ear_l", pivot=(31, -4.5, 35), rotate=(0, 0, 12), parent="head")
    g.joint("head", pivot=(30, 0, 29), rotate=(4, 6, -8), parent="neck")
    # face: calm eyes with long lashes and nostrils
    g.box((36, -4, 32), (37, -4, 33), "white", part="head")
    g.box((37, -4, 32), (37, -4, 33), "eye", part="head")
    g.box((36, -4, 34), (38, -4, 34), "eye", part="head")
    g.set(42, -2, 31, "eye", part="head")
    g.mirror()
    g.joint("leg_fl", pivot=(22.5, -5.5, 16), rotate=(0, -12, 0), parent="body")
    g.joint("leg_hl", pivot=(4.5, -5.5, 16), rotate=(0, 10, 0), parent="body")
    g.joint("shin_fl", pivot=(22.5, -5.5, 8), rotate=(0, 14, 0), parent="leg_fl")
