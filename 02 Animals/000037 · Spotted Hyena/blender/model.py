"""000037 · Spotted Hyena (Crocuta crocuta) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, spot, muzzle, mane, white, eye. Size: 38 x 15 x 24 voxels posed."""


def build(g):
    # sloping muscular torso (higher at shoulders than rump)
    g.box((1, -4, 7), (11, 4, 15), "coat", part="body")
    g.box((12, -4, 9), (21, 4, 17), "coat", part="body")
    g.paint((12, -1, 17), (20, 1, 17), "mane", of="body")
    for x, y, z in ((4, -4, 12), (8, -4, 11), (14, -4, 13), (18, -4, 12), (5, 4, 12), (13, 4, 13)):
        g.set(x, y, z, "spot", part="body")
    # taller front legs, shorter hind legs
    g.box((17, -4, 0), (19, -2, 9), "coat", part="leg_fl")
    g.paint((17, -4, 0), (19, -2, 2), "muzzle", of="leg_fl")
    g.joint("leg_fl", pivot=(18, -3, 9), rotate=(0, -12, 0), parent="body")
    g.box((2, -4, 0), (4, -2, 7), "coat", part="leg_hl")
    g.paint((2, -4, 0), (4, -2, 2), "muzzle", of="leg_hl")
    g.joint("leg_hl", pivot=(3, -3, 7), rotate=(0, 10, 0), parent="body")
    # short bushy dark-tipped tail
    g.box((-7, -1, 11), (0, 1, 13), "coat", part="tail")
    g.paint((-7, -1, 11), (-4, 1, 13), "muzzle", of="tail")
    g.joint("tail", pivot=(1, 0, 12), rotate=(0, 25, 0), parent="body")
    # heavy-jawed head & rounded ears
    g.box((20, -4, 14), (27, 4, 21), "coat", part="head")
    g.box((27, -2, 14), (29, 2, 17), "muzzle", part="head")
    g.box((27, -3, 18), (27, -3, 19), "white", part="head")
    g.box((27, -2, 18), (27, -2, 19), "eye", part="head")
    g.joint("head", pivot=(21, 0, 17), rotate=(4, 3, -10), parent="body")
    g.box((21, -4, 21), (23, -2, 23), "coat", part="ear_l")
    g.joint("ear_l", pivot=(22, -3, 21), parent="head")
    g.mirror()
    g.joint("leg_fr", pivot=(18, 3, 9), rotate=(0, 6, 0), parent="body")
