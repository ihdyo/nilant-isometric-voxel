"""000041 · Japanese Macaque (Macaca fuscata) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, face, belly, shade, white, eye. Size: 24 x 15 x 20 voxels posed."""


def build(g):
    # stocky woolly torso
    g.box((1, -4, 5), (15, 4, 13), "coat", part="body")
    g.paint((3, -3, 5), (14, 3, 6), "belly", of="body")
    g.paint((2, -3, 12), (13, 3, 13), "shade", of="body")
    # sturdy winter limbs
    for leg, x in (("leg_hl", 2), ("leg_fl", 12)):
        g.box((x, -4, 0), (x + 2, -2, 5), "coat", part=leg)
        g.paint((x, -4, 0), (x + 2, -2, 0), "face", of=leg)
        g.joint(leg, pivot=(x + 1, -3, 5), parent="body")
    # short stubby tail
    g.box((-2, -1, 9), (0, 1, 11), "coat", part="tail")
    g.joint("tail", pivot=(1, 0, 10), rotate=(0, -15, 0), parent="body")
    # woolly head with bright rosy-red face
    g.box((14, -4, 10), (20, 4, 18), "coat", part="head")
    g.paint((20, -3, 11), (20, 3, 16), "face", of="head")
    g.box((20, -2, 11), (21, 2, 13), "face", part="head")
    g.set(20, -2, 15, "white", part="head")
    g.set(20, -1, 15, "eye", part="head")
    g.joint("head", pivot=(15, 0, 13), rotate=(4, 3, -10), parent="body")
    g.box((16, -5, 14), (17, -4, 16), "face", part="ear_l")
    g.joint("ear_l", pivot=(16.5, -4, 15), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(13, -3, 5), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -3, 5), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(13, 3, 5), rotate=(0, 6, 0), parent="body")
