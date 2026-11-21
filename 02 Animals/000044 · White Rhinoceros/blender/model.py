"""000044 · White Rhinoceros (Ceratotherium simum) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: skin, shade, horn, nail, white, eye. Size: 48 x 18 x 26 voxels posed."""


def build(g):
    # massive barrel body with prominent shoulder/nuchal hump
    g.box((0, -7, 9), (26, 7, 21), "skin", part="body")
    g.box((18, -5, 21), (25, 5, 23), "skin", part="body")
    g.paint((8, -7, 10), (8, 7, 20), "shade", of="body")
    g.paint((19, -7, 10), (19, 7, 20), "shade", of="body")
    # thick pillar legs
    for leg, x in (("leg_hl", 2), ("leg_fl", 20)):
        g.box((x, -6, 0), (x + 4, -3, 9), "skin", part=leg)
        for y in (-6, -4):
            g.box((x + 4, y, 0), (x + 4, y, 1), "nail", part=leg)
        g.joint(leg, pivot=(x + 2, -4.5, 9), parent="body")
    # short tufted tail
    g.box((-2, 0, 13), (-1, 0, 19), "skin", part="tail")
    g.paint((-2, 0, 13), (-1, 0, 14), "shade", of="tail")
    g.joint("tail", pivot=(-1, 0, 19), rotate=(-10, 0, 0), parent="body")
    # long square-lipped grazing head
    g.box((25, -5, 8), (38, 5, 19), "skin", part="head")
    g.paint((37, -5, 8), (38, 5, 11), "shade", of="head")
    g.set(32, -5, 15, "white", part="head")
    g.set(33, -5, 15, "eye", part="head")
    g.joint("head", pivot=(26, 0, 15), rotate=(4, 5, -8), parent="body")
    # two keratin horns & tubular ears
    g.box((35, -1, 19), (37, 1, 26), "horn", part="horn_1")
    g.joint("horn_1", pivot=(36, 0, 19), rotate=(0, 10, 0), parent="head")
    g.box((31, -1, 19), (33, 1, 22), "horn", part="horn_2")
    g.joint("horn_2", pivot=(32, 0, 19), parent="head")
    g.box((26, -5, 19), (28, -4, 22), "skin", part="ear_l")
    g.paint((28, -5, 20), (28, -4, 21), "shade", of="ear_l")
    g.joint("ear_l", pivot=(27, -4.5, 19), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(22, -4.5, 9), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(4, -4.5, 9), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(22, 4.5, 9), rotate=(0, 5, 0), parent="body")
