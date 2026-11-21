"""000057 · Platypus (Ornithorhynchus anatinus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, belly, bill, tail, white, eye. Size: 41 x 14 x 10 voxels.
Personality: quirky and inquisitive, nocturnal river detective. Pose: a sleek paddling glide, broad duck bill tilted up, paddle tail trailing. Expression: beady bright eyes just behind a wide slate-grey bill."""


def build(g):
    # body: streamlined low semi-aquatic torso with pale golden belly
    g.box((10, -5, 2), (26, 5, 9), "coat", part="body")
    g.box((11, -4, 1), (25, 4, 2), "belly", part="body")
    # broad flat beaver-like paddle tail
    g.box((0, -4, 3), (10, 4, 5), "tail", part="tail")
    g.joint("tail", pivot=(10, 0, 4), rotate=(0, 6, 0), parent="body")
    # webbed paddling feet
    for leg, x in (("leg_hl", 12), ("leg_fl", 22)):
        g.box((x, -8, 0), (x + 4, -5, 2), "bill", part=leg)
        g.joint(leg, pivot=(x + 2, -5.5, 2), parent="body")
    # head and wide flat rubbery duck bill
    g.box((26, -4, 3), (32, 4, 9), "coat", part="head")
    g.box((32, -4, 3), (40, 4, 5), "bill", part="head")
    g.joint("head", pivot=(26, 0, 6), rotate=(3, -5, -8), parent="body")
    g.box((29, -4, 6), (30, -4, 7), "white", part="head")
    g.box((30, -4, 6), (30, -4, 7), "eye", part="head")
    g.mirror()
    g.joint("leg_fl", pivot=(24, -5.5, 2), rotate=(0, 0, -16), parent="body")
    g.joint("leg_hl", pivot=(14, -5.5, 2), rotate=(0, 0, 14), parent="body")
