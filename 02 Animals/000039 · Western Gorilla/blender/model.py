"""000039 · Western Gorilla (Gorilla gorilla) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, silver, skin, chest, white, eye. Size: 26 x 24 x 30 voxels posed."""


def build(g):
    # massive muscular torso with silverback saddle
    g.box((0, -8, 7), (14, 8, 22), "coat", part="body")
    g.paint((0, -7, 9), (4, 7, 20), "silver", of="body")
    g.paint((13, -5, 10), (14, 5, 20), "chest", of="body")
    # short thick legs
    g.box((2, -7, 0), (7, -3, 7), "coat", part="leg_l")
    g.paint((5, -7, 0), (8, -3, 1), "skin", of="leg_l")
    g.joint("leg_l", pivot=(4.5, -5, 7), parent="body")
    # massive knuckle-walking arms
    g.box((10, -11, 0), (15, -8, 21), "coat", part="arm_l")
    g.paint((10, -11, 0), (15, -8, 2), "skin", of="arm_l")
    g.joint("arm_l", pivot=(12.5, -9.5, 21), rotate=(6, -10, 0), parent="body")
    # domed head with heavy brow ridge
    g.box((8, -6, 22), (17, 6, 30), "coat", part="head")
    g.paint((16, -5, 22), (17, 5, 28), "skin", of="head")
    g.box((17, -5, 27), (18, 5, 28), "skin", part="head")
    g.box((17, -3, 25), (17, -3, 26), "white", part="head")
    g.box((17, -2, 25), (17, -2, 26), "eye", part="head")
    g.joint("head", pivot=(12, 0, 22), rotate=(3, 3, -10), parent="body")
    g.mirror()
    g.joint("arm_r", pivot=(12.5, 9.5, 21), rotate=(-6, 5, 0), parent="body")
