"""000002 · Giant Panda (Ailuropoda melanoleuca) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: white, black. Size: 31 x 16 x 27 voxels posed.
Personality: gentle and laid-back. Pose: an easy amble, the diagonal legs mid-stride, the head turned to the camera, a
little down, one ear forward."""


def build(g):
    # body: one big barrel box, the black band over the shoulders, a short white tail
    g.box((0, -6, 7), (18, 6, 17), "white", part="body")
    g.paint((12, -6, 7), (15, 6, 17), "black", of="body")
    g.box((-1, -1, 14), (-1, 1, 15), "white", part="body")
    # legs: thick 4 x 4 black pillars
    for name, x in (("leg_hl", 1), ("leg_fl", 13)):
        g.box((x, -6, 0), (x + 3, -3, 6), "black", part=name)
        g.joint(name, pivot=(x + 2, -4.5, 7), parent="body")
    # head: a big white box as wide as the body, stacked on its front
    g.box((18, -6, 12), (26, 6, 22), "white", part="head")
    g.joint("head", pivot=(19, 0.5, 15), rotate=(4, 6, -14), parent="body")
    # face, painted flat: solid black eye patches drooping at the outer side, a white glint in the top inner corner
    # of each (a hole in the middle of a patch reads as a letter)
    g.box((26, -5, 16), (26, -3, 18), "black", part="head")
    g.set(26, -5, 15, "black", part="head")
    g.set(26, -3, 18, "white", part="head")
    # muzzle with a black nose on top and a small U smile painted below it
    g.box((27, -2, 12), (29, 2, 16), "white", part="muzzle")
    g.paint((29, -1, 16), (29, 1, 16), "black", of="muzzle")
    g.set(29, -1, 14, "black", part="muzzle")
    g.set(29, 0, 13, "black", part="muzzle")
    g.joint("muzzle", pivot=(27, 0.5, 14), parent="head")
    # round black ears on the top corners, tipped out
    g.box((20, -6, 23), (21, -4, 25), "black", part="ear_l")
    g.joint("ear_l", pivot=(20.5, -5, 23), rotate=(10, 0, 0), parent="head")
    g.mirror()
    # an amble: front left forward, hind left back, the right side the other way
    g.joint("leg_fl", pivot=(15, -4.5, 7), rotate=(0, -18, 0), parent="body")
    g.joint("leg_fr", pivot=(15, 5.5, 7), rotate=(0, 12, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -4.5, 7), rotate=(0, 14, 0), parent="body")
    g.joint("leg_hr", pivot=(3, 5.5, 7), rotate=(0, -14, 0), parent="body")
