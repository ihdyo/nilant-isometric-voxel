"""26-017 · Gray Wolf (Canis lupus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, back, light, nose. Size: 33 x 13 x 30 voxels posed.
Personality: loyal and a little dramatic, the pack's singer. Pose: standing four-square on long legs with knees, the
thick neck ruff raised and the head thrown back to howl at the sky, turned to the camera, the ears laid back, the
bushy tail hanging low. Expression: eyes shut tight and a round open mouth, mid-howl, painted flat."""


def build(g):
    # body: a long box on long legs, the dark saddle on top, the pale belly underneath
    g.box((0, -5, 9), (15, 5, 17), "fur", part="body")
    g.paint((2, -4, 17), (13, 4, 17), "back", of="body")
    g.paint((2, -3, 9), (14, 3, 9), "light", of="body")
    # legs: an upper leg and a shin each (long legs need knees), pale paws
    for leg, shin, x0, x1 in (("leg_hl", "shin_hl", 0, 3), ("leg_fl", "shin_fl", 12, 14)):
        g.box((x0, -5, 5), (x1, -3, 8), "fur", part=leg)
        g.box((x1 - 2, -5, 0), (x1, -3, 4), "fur", part=shin)
        g.box((x1 - 2, -5, 0), (x1, -3, 1), "light", part=shin)
        g.joint(leg, pivot=((x0 + x1 + 1) / 2, -3.5, 9), parent="body")
        g.joint(shin, pivot=(x1 - 0.5, -3.5, 5), parent=leg)
    # neck: the thick ruff rising from the front of the body, the pale throat in front, raised to howl
    g.box((14, -4, 14), (17, 4, 20), "fur", part="neck")
    g.paint((17, -3, 14), (17, 3, 18), "light", of="neck")
    g.joint("neck", pivot=(14.5, 0.5, 15), rotate=(0, -20, -6), parent="body")
    # head: on top of the neck, thrown back further to howl and turned to the camera; pale cheeks
    g.box((16, -5, 19), (22, 5, 25), "fur", part="head")
    g.paint((20, -5, 19), (22, 5, 20), "light", of="head")
    g.joint("head", pivot=(17, 0.5, 21), rotate=(6, -22, -10), parent="neck")
    # eyes shut tight, painted flat: dark lines on the front of the head
    g.box((22, -4, 23), (22, -2, 23), "nose", part="head")
    # snout: pale underneath, the black nose on its top front edge, the round open mouth painted on its front
    g.box((23, -2, 19), (26, 2, 22), "fur", part="snout")
    g.paint((23, -2, 19), (26, 2, 20), "light", of="snout")
    g.paint((26, -1, 22), (26, 1, 22), "nose", of="snout")
    g.box((26, -1, 19), (26, 1, 20), "nose", part="snout")
    g.joint("snout", pivot=(23, 0.5, 20.5), parent="head")
    # ears: pointed blocks with dark backs, laid back
    g.box((17, -5, 26), (18, -3, 28), "fur", part="ear_l")
    g.paint((17, -5, 26), (17, -3, 28), "back", of="ear_l")
    g.joint("ear_l", pivot=(17.5, -4, 26), rotate=(10, -14, 0), parent="head")
    # bushy tail hanging low behind, a dark tip
    g.box((-5, -2, 12), (-1, 2, 15), "fur", part="tail")
    g.joint("tail", pivot=(-0.5, 0.5, 14), rotate=(0, -28, 8), parent="body")
    g.box((-9, -2, 12), (-6, 2, 15), "fur", part="tail_tip")
    g.paint((-9, -2, 12), (-8, 2, 15), "back", of="tail_tip")
    g.joint("tail_tip", pivot=(-5.5, 0.5, 13.5), rotate=(0, -12, 6), parent="tail")
    g.mirror()
    # four-square, the front left paw a little forward
    g.joint("leg_fl", pivot=(13.5, -3.5, 9), rotate=(0, -6, 0), parent="body")
    g.joint("leg_hr", pivot=(2, 4.5, 9), rotate=(0, 5, 0), parent="body")
