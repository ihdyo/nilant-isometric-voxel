"""000034 · Sea Otter (Enhydra lutris) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, head, paw, nose, white, eye. Size: 38 x 14 x 15 voxels posed."""


def build(g):
    # sleek dark-brown torpedo body
    g.box((2, -4, 3), (20, 4, 10), "coat", part="body")
    # short front paws & wide hind flippers
    g.box((17, -4, 0), (19, -2, 3), "paw", part="leg_fl")
    g.joint("leg_fl", pivot=(18, -3, 3), rotate=(0, -10, 0), parent="body")
    g.box((0, -5, 0), (4, -2, 2), "paw", part="flipper_hl")
    g.joint("flipper_hl", pivot=(3, -3.5, 2), rotate=(0, 8, 0), parent="body")
    # flattened rudder tail
    g.box((-10, -2, 4), (1, 2, 6), "coat", part="tail")
    g.joint("tail", pivot=(2, 0, 5), rotate=(0, 6, 0), parent="body")
    # pale creamy head with broad black nose
    g.box((19, -4, 6), (26, 4, 13), "head", part="head")
    g.box((26, -2, 6), (27, 2, 9), "head", part="head")
    g.box((27, -1, 8), (27, 1, 9), "nose", part="head")
    g.box((26, -3, 10), (26, -3, 11), "white", part="head")
    g.box((26, -2, 10), (26, -2, 11), "eye", part="head")
    g.joint("head", pivot=(20, 0, 9), rotate=(4, 3, -10), parent="body")
    g.box((20, -4, 13), (21, -3, 14), "coat", part="ear_l")
    g.joint("ear_l", pivot=(20.5, -3.5, 13), parent="head")
    g.mirror()
    g.joint("leg_fr", pivot=(18, 3, 3), rotate=(0, 6, 0), parent="body")
