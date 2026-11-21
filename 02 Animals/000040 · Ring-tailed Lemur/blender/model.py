"""000040 · Ring-tailed Lemur (Lemur catta) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, black, white, belly, muzzle, eye. Size: 28 x 12 x 30 voxels posed."""


def build(g):
    # slender grey torso with white underside
    g.box((1, -3, 6), (14, 3, 12), "coat", part="body")
    g.paint((2, -2, 6), (13, 2, 7), "belly", of="body")
    # agile limbs (longer hind legs)
    g.box((11, -3, 0), (13, -2, 6), "coat", part="leg_fl")
    g.joint("leg_fl", pivot=(12, -2.5, 6), rotate=(0, -12, 0), parent="body")
    g.box((2, -3, 0), (4, -2, 8), "coat", part="leg_hl")
    g.joint("leg_hl", pivot=(3, -2.5, 8), rotate=(0, 10, 0), parent="body")
    # iconic tall black-and-white ringed tail
    g.box((-2, -1, 11), (0, 1, 22), "white", part="tail_1")
    for z in (12, 15, 18, 21):
        g.paint((-2, -1, z), (0, 1, z + 1), "black", of="tail_1")
    g.joint("tail_1", pivot=(1, 0, 11), rotate=(0, -8, 0), parent="body")
    g.box((-6, -1, 22), (-1, 1, 29), "white", part="tail_2")
    for z in (23, 26, 28):
        g.paint((-6, -1, z), (-1, 1, z + 1), "black", of="tail_2")
    g.joint("tail_2", pivot=(-1, 0, 22), rotate=(0, -18, 0), parent="tail_1")
    # white face with black eye patches and pointed snout
    g.box((13, -3, 10), (19, 3, 16), "white", part="head")
    g.paint((13, -3, 15), (17, 3, 16), "coat", of="head")
    g.box((19, -2, 10), (21, 2, 12), "muzzle", part="head")
    g.box((19, -3, 13), (19, -2, 14), "black", part="head")
    g.set(19, -2, 13, "eye", part="head")
    g.joint("head", pivot=(14, 0, 12), rotate=(4, 3, -10), parent="body")
    g.box((14, -3, 16), (15, -2, 18), "white", part="ear_l")
    g.joint("ear_l", pivot=(14.5, -2.5, 16), parent="head")
    g.mirror()
    g.joint("leg_fr", pivot=(12, 2.5, 6), rotate=(0, 6, 0), parent="body")
