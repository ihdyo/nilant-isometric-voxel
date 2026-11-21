"""000029 · Clouded Leopard (Neofelis nebulosa) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, cloud, belly, muzzle, white, eye. Size: 44 x 14 x 20 voxels posed."""


def build(g):
    # supple body with cloud blotches
    g.box((1, -4, 7), (21, 4, 14), "coat", part="body")
    g.paint((2, -3, 7), (20, 3, 8), "belly", of="body")
    g.box((4, -4, 9), (8, -4, 12), "cloud", part="body")
    g.box((12, -4, 9), (16, -4, 12), "cloud", part="body")
    g.box((5, 4, 9), (9, 4, 12), "cloud", part="body")
    g.box((13, 4, 9), (17, 4, 12), "cloud", part="body")
    # short stout climbing legs
    for leg, shin, x in (("leg_hl", "shin_hl", 2), ("leg_fl", "shin_fl", 17)):
        g.box((x, -4, 4), (x + 2, -2, 7), "coat", part=leg)
        g.box((x, -4, 0), (x + 2, -2, 3), "coat", part=shin)
        g.joint(leg, pivot=(x + 1, -3, 7), parent="body")
        g.joint(shin, pivot=(x + 1, -3, 4), parent=leg)
    # extra-long balancing tail
    g.box((-15, -1, 10), (0, 1, 12), "coat", part="tail")
    for x in (-13, -9, -5):
        g.paint((x, -1, 10), (x + 1, 1, 12), "cloud", of="tail")
    g.joint("tail", pivot=(1, 0, 11), rotate=(0, 6, -8), parent="body")
    # head
    g.box((20, -4, 11), (27, 4, 19), "coat", part="head")
    g.box((26, -2, 11), (28, 2, 14), "muzzle", part="head")
    g.box((27, -3, 15), (27, -3, 16), "white", part="head")
    g.box((27, -2, 15), (27, -2, 16), "eye", part="head")
    g.joint("head", pivot=(21, 0, 14), rotate=(4, 3, -10), parent="body")
    g.box((22, -4, 19), (23, -3, 20), "coat", part="ear_l")
    g.joint("ear_l", pivot=(22.5, -3.5, 19), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(18, -3, 7), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -3, 7), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(18, 3, 7), rotate=(0, 5, 0), parent="body")
    g.joint("shin_fl", pivot=(18, -3, 4), rotate=(0, 12, 0), parent="leg_fl")
    g.joint("shin_hl", pivot=(3, -3, 4), rotate=(0, -8, 0), parent="leg_hl")
