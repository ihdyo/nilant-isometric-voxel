"""000053 · American Bison (Bison bison) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: shag, coat, horn, hoof, white, eye. Size: 38 x 17 x 30 voxels.
Personality: mighty and grounded, thunder of the open prairie. Pose: a heavy forward stance, massive shaggy head lowered slightly, tail flicking. Expression: determined dark eyes peeking beneath a thick woolly brow."""


def build(g):
    # body: tan hindquarters and massive shaggy dark-brown shoulder hump
    g.box((2, -7, 11), (15, 7, 24), "coat", part="body")
    g.box((14, -8, 10), (28, 8, 29), "shag", part="body")
    # sturdy legs: woolly upper forelegs and sleeker lower legs
    for leg, shin, x, col in (("leg_hl", "shin_hl", 3, "coat"), ("leg_fl", "shin_fl", 21, "shag")):
        g.box((x, -7, 5), (x + 3, -4, 10), col, part=leg)
        g.box((x, -6, 1), (x + 2, -4, 4), "coat", part=shin)
        g.box((x, -6, 0), (x + 2, -4, 0), "hoof", part=shin)
        g.joint(leg, pivot=(x + 1.5, -5.5, 11), parent="body")
        g.joint(shin, pivot=(x + 1.5, -5.5, 5), parent=leg)
    # tufted tail
    g.box((0, -1, 14), (1, 1, 21), "coat", part="tail")
    g.box((0, -1, 12), (1, 1, 13), "shag", part="tail")
    g.joint("tail", pivot=(1, 0, 21), rotate=(-14, 0, 0), parent="body")
    # massive woolly head with chin beard and curved horns
    g.box((27, -6, 11), (36, 6, 24), "shag", part="head")
    g.box((30, -3, 7), (34, 3, 10), "shag", part="head")
    g.box((36, -3, 13), (37, 3, 16), "hoof", part="head")
    g.joint("head", pivot=(28, 0, 18), rotate=(4, 6, -8), parent="body")
    g.box((30, -8, 20), (32, -6, 25), "horn", part="horn_l")
    g.set(31, -8, 26, "hoof", part="horn_l")
    g.joint("horn_l", pivot=(31, -6.5, 20), rotate=(0, 0, 10), parent="head")
    g.box((33, -6, 18), (34, -6, 19), "white", part="head")
    g.box((34, -6, 18), (34, -6, 19), "eye", part="head")
    g.mirror()
    g.joint("leg_fl", pivot=(22.5, -5.5, 11), rotate=(0, -8, 0), parent="body")
    g.joint("leg_hl", pivot=(4.5, -5.5, 11), rotate=(0, 8, 0), parent="body")
