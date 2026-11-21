"""000074 · North Island Brown Kiwi (Apteryx mantelli) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: plumage, shade, beak, leg, eye. Size: 32 x 13 x 19 voxels.
Personality: curious and endearing, whisker-twitching midnight forager. Pose: a low bustling waddle, pear-shaped body pitched forward, long ivory beak probing downward. Expression: tiny bright black button eyes and cat-like bristles at the base of a long ivory bill."""


def build(g):
    # body: pear-shaped tailless streaked brown body
    g.box((0, -6, 4), (16, 6, 16), "plumage", part="body")
    g.box((1, -5, 15), (12, 5, 18), "shade", part="body")
    # short stout legs
    g.box((7, -5, 0), (10, -2, 4), "leg", part="leg_l")
    g.box((7, -5, 0), (12, -2, 1), "leg", part="leg_l")
    g.joint("leg_l", pivot=(8.5, -3.5, 4), parent="body")
    # rounded head and extremely long slender ivory bill
    g.box((14, -4, 11), (20, 4, 18), "plumage", part="head")
    g.box((20, -1, 12), (31, 1, 13), "beak", part="head")
    g.set(18, -4, 15, "eye", part="head")
    g.joint("head", pivot=(16, 0, 14), rotate=(4, 16, -8), parent="body")
    g.mirror()
    g.joint("leg_l", pivot=(8.5, -3.5, 4), rotate=(0, -8, 0), parent="body")
