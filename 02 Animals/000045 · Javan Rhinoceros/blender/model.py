"""000045 · Javan Rhinoceros (Rhinoceros sondaicus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: skin, fold, horn, nail, white, eye. Size: 42 x 16 x 23 voxels posed."""


def build(g):
    # barrel body with deep armor-like skin folds
    g.box((0, -6, 8), (23, 6, 20), "skin", part="body")
    g.paint((6, -6, 9), (6, 6, 20), "fold", of="body")
    g.paint((16, -6, 9), (16, 6, 20), "fold", of="body")
    g.paint((21, -6, 10), (21, 6, 19), "fold", of="body")
    # sturdy pillar legs
    for leg, x in (("leg_hl", 2), ("leg_fl", 17)):
        g.box((x, -5, 0), (x + 3, -2, 8), "skin", part=leg)
        for y in (-5, -3):
            g.box((x + 3, y, 0), (x + 3, y, 1), "nail", part=leg)
        g.joint(leg, pivot=(x + 2, -3.5, 8), parent="body")
    # short tail
    g.box((-2, 0, 11), (-1, 0, 17), "skin", part="tail")
    g.paint((-2, 0, 11), (-1, 0, 12), "fold", of="tail")
    g.joint("tail", pivot=(-1, 0, 17), rotate=(-10, 0, 0), parent="body")
    # head with pointed prehensile upper lip and single short horn
    g.box((22, -4, 9), (33, 4, 18), "skin", part="head")
    g.box((33, -2, 10), (34, 2, 13), "skin", part="head")
    g.set(28, -4, 15, "white", part="head")
    g.set(29, -4, 15, "eye", part="head")
    g.joint("head", pivot=(23, 0, 14), rotate=(4, 3, -8), parent="body")
    g.box((30, -1, 18), (32, 1, 22), "horn", part="horn")
    g.joint("horn", pivot=(31, 0, 18), rotate=(0, 12, 0), parent="head")
    g.box((23, -4, 18), (24, -3, 21), "skin", part="ear_l")
    g.joint("ear_l", pivot=(23.5, -3.5, 18), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(19, -3.5, 8), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(4, -3.5, 8), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(19, 3.5, 8), rotate=(0, 5, 0), parent="body")
