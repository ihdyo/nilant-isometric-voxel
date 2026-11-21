"""000054 · Highland Cattle (Bos taurus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, fringe, horn, muzzle, white, eye. Size: 36 x 25 x 27 voxels.
Personality: gentle and cozy, unbothered by Scottish drizzle. Pose: a relaxed pasture stroll, head tilted slightly so one eye peeks out from under the fringe. Expression: a warm friendly eye peeking beneath a thick ginger fringe and a broad pale nose."""


def build(g):
    # body: shaggy ginger-red rectangular torso with wavy coat fringe
    g.box((2, -7, 8), (24, 7, 21), "coat", part="body")
    g.box((3, -8, 7), (23, 8, 12), "coat", part="body")
    # stocky legs
    for leg, shin, x in (("leg_hl", "shin_hl", 3), ("leg_fl", "shin_fl", 19)):
        g.box((x, -6, 4), (x + 3, -3, 8), "coat", part=leg)
        g.box((x, -6, 1), (x + 3, -3, 3), "coat", part=shin)
        g.box((x, -6, 0), (x + 3, -3, 0), "muzzle", part=shin)
        g.joint(leg, pivot=(x + 1.5, -4.5, 8), parent="body")
        g.joint(shin, pivot=(x + 1.5, -4.5, 4), parent=leg)
    # tufted tail
    g.box((0, -1, 10), (1, 1, 18), "coat", part="tail")
    g.box((0, -1, 8), (1, 1, 9), "fringe", part="tail")
    g.joint("tail", pivot=(1, 0, 18), rotate=(-10, 0, 0), parent="body")
    # head with thick ginger dossan fringe, broad pale muzzle, and sweeping horns
    g.box((24, -5, 11), (33, 5, 22), "coat", part="head")
    g.box((32, -4, 11), (35, 4, 15), "muzzle", part="head")
    g.box((31, -5, 17), (34, 5, 22), "fringe", part="head")
    g.joint("head", pivot=(25, 0, 16), rotate=(5, 4, -10), parent="body")
    g.box((27, -11, 19), (29, -5, 21), "horn", part="horn_l")
    g.box((28, -12, 22), (30, -10, 26), "horn", part="horn_l")
    g.joint("horn_l", pivot=(28, -5.5, 20), rotate=(0, -8, 12), parent="head")
    g.box((32, -5, 16), (33, -5, 16), "white", part="head")
    g.box((33, -5, 16), (33, -5, 16), "eye", part="head")
    g.mirror()
    g.joint("leg_fl", pivot=(20.5, -4.5, 8), rotate=(0, -8, 0), parent="body")
    g.joint("leg_hl", pivot=(4.5, -4.5, 8), rotate=(0, 6, 0), parent="body")
