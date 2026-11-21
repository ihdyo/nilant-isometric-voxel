"""000049 · Alpaca (Vicugna pacos) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fleece, shade, face, nose, white, eye. Size: 30 x 14 x 30 voxels posed."""


def build(g):
    # extra-fluffy cloud-like body
    g.box((1, -5, 8), (16, 5, 16), "fleece", part="body")
    g.paint((2, -4, 8), (15, 4, 9), "shade", of="body")
    # woolly legs
    for leg, x in (("leg_hl", 2), ("leg_fl", 12)):
        g.box((x, -4, 0), (x + 2, -2, 8), "fleece", part=leg)
        g.paint((x, -4, 0), (x + 2, -2, 0), "nose", of=leg)
        g.joint(leg, pivot=(x + 1, -3, 8), parent="body")
    # thick woolly neck
    g.box((11, -3, 16), (16, 3, 24), "fleece", part="neck")
    g.joint("neck", pivot=(13.5, 0, 16), parent="body")
    # fluffy stub tail
    g.box((-1, -1, 12), (0, 1, 15), "fleece", part="tail")
    g.joint("tail", pivot=(0, 0, 15), rotate=(-12, 0, 0), parent="body")
    # fluffy head with topknot & straight spear-shaped ears
    g.box((12, -3, 23), (18, 3, 28), "fleece", part="head")
    g.box((18, -2, 23), (20, 2, 25), "face", part="head")
    g.set(20, 0, 25, "nose", part="head")
    g.set(18, -3, 25, "white", part="head")
    g.set(18, -2, 25, "eye", part="head")
    g.joint("head", pivot=(14, 0, 23), rotate=(3, 2, -10), parent="neck")
    g.box((13, -3, 28), (15, -2, 30), "face", part="ear_l")
    g.joint("ear_l", pivot=(14, -2.5, 28), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(13, -3, 8), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -3, 8), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(13, 3, 8), rotate=(0, 5, 0), parent="body")
