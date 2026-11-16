"""26-014 · Hippo (Hippopotamus amphibius) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: skin, pink, mouth, tusk, eye. Size: 45 x 21 x 28 voxels posed.
Personality: grumpy-looking but sleepy and lovable. Pose: standing in a slow, heavy stance, caught mid-yawn: the broad
muzzle tipped up and the lower jaw dropped open to show the pink mouth and the tusks, one ear flicked. Expression:
eyes squeezed into sleepy lines on top of the head by the yawn, painted flat."""


def build(g):
    # body: one huge barrel box, the pink belly; a stub of a tail
    g.box((0, -9, 7), (28, 9, 22), "skin", part="body")
    g.paint((2, -8, 7), (26, 8, 7), "pink", of="body")
    g.box((-1, -1, 17), (-1, 1, 20), "skin", part="body")
    # legs: short thick pillars
    for name, x in (("leg_hl", 2), ("leg_fl", 21)):
        g.box((x, -9, 0), (x + 5, -4, 6), "skin", part=name)
        g.joint(name, pivot=(x + 3, -6.5, 7), parent="body")
    # head: the skull on the front of the body, eye bumps and little ears on top, and the broad, square upper muzzle
    # (wider than the skull), its pink roof of the mouth underneath and two small upper tusks
    g.box((28, -7, 12), (33, 7, 22), "skin", part="head")
    g.box((34, -9, 14), (41, 9, 20), "skin", part="head")
    g.paint((35, -7, 14), (41, 7, 14), "mouth", of="head")
    g.box((40, -6, 13), (40, -5, 13), "tusk", part="head")
    g.box((38, -3, 20), (39, -2, 20), "eye", part="head")              # nostrils on top of the muzzle
    g.box((29, -7, 23), (31, -4, 24), "skin", part="head")             # the eye bump
    g.box((31, -7, 23), (31, -4, 23), "pink", part="head")
    g.box((31, -7, 24), (31, -4, 24), "eye", part="head")              # the sleepy eye, a line painted on its front
    g.joint("head", pivot=(28.5, 0.5, 15), rotate=(4, -14, -10), parent="body")
    # lower jaw: dropped open, the pink tongue and gums on top, two big tusks standing at its front corners
    g.box((34, -8, 9), (41, 8, 12), "skin", part="jaw")
    g.paint((35, -7, 12), (41, 7, 12), "mouth", of="jaw")
    g.box((40, -7, 13), (41, -6, 15), "tusk", part="jaw")
    g.joint("jaw", pivot=(34, 0.5, 13), rotate=(0, 28, 0), parent="head")
    # small round ears behind the eyes, pink inside
    g.box((28, -7, 25), (29, -6, 26), "skin", part="ear_l")
    g.set(29, -6, 25, "pink", part="ear_l")
    g.joint("ear_l", pivot=(28.5, -6.5, 25), rotate=(14, 0, 0), parent="head")
    g.mirror()
    # one ear flicked back; a slow, heavy stance
    g.joint("ear_r", pivot=(28.5, 7.5, 25), rotate=(-12, -26, 0), parent="head")
    g.joint("leg_fl", pivot=(24, -6.5, 7), rotate=(0, -6, 0), parent="body")
    g.joint("leg_hr", pivot=(5, 7.5, 7), rotate=(0, 5, 0), parent="body")
