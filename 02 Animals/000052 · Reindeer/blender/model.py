"""000052 · Reindeer (Rangifer tarandus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, ruff, antler, hoof, white, eye. Size: 36 x 19 x 42 voxels.
Personality: resilient and spirited, tireless traveller of the frozen north. Pose: a brisk trot, branching antlers swept back, white chest ruff puffed out. Expression: bright alert eyes and a fuzzy dark nose."""


def build(g):
    # body with fluffy white rump and chest ruff
    g.box((2, -6, 13), (23, 6, 24), "coat", part="body")
    g.box((1, -5, 14), (3, 5, 22), "ruff", part="body")
    g.box((18, -6, 12), (25, 6, 24), "ruff", part="body")
    # slender legs with broad crescent snowshoe hooves
    for leg, shin, x in (("leg_hl", "shin_hl", 3), ("leg_fl", "shin_fl", 19)):
        g.box((x, -5, 6), (x + 2, -3, 12), "coat", part=leg)
        g.box((x, -5, 1), (x + 2, -3, 5), "coat", part=shin)
        g.box((x - 1, -6, 0), (x + 3, -2, 0), "hoof", part=shin)
        g.joint(leg, pivot=(x + 1, -4, 13), parent="body")
        g.joint(shin, pivot=(x + 1, -4, 6), parent=leg)
    # short tail
    g.box((0, -1, 19), (1, 1, 22), "ruff", part="tail")
    g.joint("tail", pivot=(1, 0, 21), rotate=(-12, 0, 0), parent="body")
    # head and branching antlers
    g.box((23, -4, 21), (33, 4, 29), "coat", part="head")
    g.box((31, -3, 21), (35, 3, 25), "ruff", part="head")
    g.set(35, 0, 24, "hoof", part="head")
    g.joint("head", pivot=(24, 0, 24), rotate=(4, 4, -8), parent="body")
    g.box((24, -6, 29), (26, -4, 32), "coat", part="ear_l")
    g.joint("ear_l", pivot=(25, -4.5, 29), rotate=(0, 0, 16), parent="head")
    g.box((25, -8, 30), (27, -4, 40), "antler", part="antler_l")
    g.box((27, -9, 35), (32, -7, 39), "antler", part="antler_l")
    g.box((22, -9, 37), (25, -7, 41), "antler", part="antler_l")
    g.joint("antler_l", pivot=(26, -4, 30), rotate=(0, -8, 8), parent="head")
    g.box((30, -4, 26), (31, -4, 27), "white", part="head")
    g.box((31, -4, 26), (31, -4, 27), "eye", part="head")
    g.mirror()
    g.joint("leg_fl", pivot=(20, -4, 13), rotate=(0, -14, 0), parent="body")
    g.joint("leg_hl", pivot=(4, -4, 13), rotate=(0, 12, 0), parent="body")
