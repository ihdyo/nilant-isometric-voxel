"""000035 · Meerkat (Suricata suricatta) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, stripe, mask, belly, white, eye. Size: 16 x 11 x 26 voxels posed."""


def build(g):
    # upright slender torso
    g.box((0, -3, 3), (6, 3, 18), "coat", part="body")
    g.paint((5, -2, 5), (6, 2, 15), "belly", of="body")
    for z in (6, 9, 12):
        g.paint((0, -3, z), (1, 3, z), "stripe", of="body")
    # hind feet & tripod tail
    g.box((1, -3, 0), (4, -1, 3), "coat", part="leg_hl")
    g.joint("leg_hl", pivot=(2.5, -2, 3), parent="body")
    g.box((-7, -1, 0), (0, 1, 2), "coat", part="tail")
    g.paint((-7, -1, 0), (-5, 1, 2), "mask", of="tail")
    g.joint("tail", pivot=(0, 0, 2), rotate=(0, 8, 0), parent="body")
    # tucked front arms
    g.box((5, -4, 11), (7, -3, 16), "coat", part="arm_l")
    g.joint("arm_l", pivot=(6, -3.5, 16), rotate=(10, 0, 0), parent="body")
    # alert sentry head with dark eye masks and pointed snout
    g.box((0, -3, 18), (7, 3, 25), "coat", part="head")
    g.box((7, -2, 19), (9, 2, 21), "coat", part="head")
    g.set(9, 0, 21, "mask", part="head")
    g.box((7, -3, 21), (7, -2, 23), "mask", part="head")
    g.set(7, -3, 22, "white", part="head")
    g.set(7, -2, 22, "eye", part="head")
    g.joint("head", pivot=(3.5, 0, 18), rotate=(4, -6, -12), parent="body")
    # low dark crescent ears
    g.box((2, -4, 21), (3, -3, 23), "mask", part="ear_l")
    g.joint("ear_l", pivot=(2.5, -3, 22), parent="head")
    g.mirror()
