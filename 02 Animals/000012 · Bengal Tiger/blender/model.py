"""000012 · Bengal Tiger (Panthera tigris tigris) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, stripe, white, nose, eye, pupil. Size: 43 x 16 x 25 voxels posed.
Personality: confident and playful, a proud hunter. Pose: A prowling stride, the front left paw reaching with its knee
folding, the head low and turned to the camera, the striped tail raised in a curve. Expression: amber eyes under black
brows slanting down to the middle, a cheeky grin, all painted flat."""


def build(g):
    # body: one long bulky box, white belly, black stripes down the flanks and over the back
    g.box((0, -5, 10), (21, 5, 18), "fur", part="body")
    g.paint((1, -4, 10), (20, 4, 10), "white", of="body")
    for x in (2, 5, 8, 11, 14, 17):
        g.paint((x, -5, 13), (x, -5, 18), "stripe", of="body")
        g.paint((x, -4, 18), (x, 4, 18), "stripe", of="body")
    # legs: thick 4 x 4 pillars, an upper leg and a shin hinged at the knee, a stripe on each
    for leg, shin, x in (("leg_hl", "shin_hl", 1), ("leg_fl", "shin_fl", 17)):
        g.box((x, -5, 5), (x + 3, -2, 9), "fur", part=leg)
        g.paint((x, -5, 7), (x + 3, -5, 7), "stripe", of=leg)
        g.box((x, -5, 0), (x + 3, -2, 4), "fur", part=shin)
        g.paint((x, -5, 2), (x + 3, -5, 2), "stripe", of=shin)
        g.joint(leg, pivot=(x + 2, -3.5, 10), parent="body")
        g.joint(shin, pivot=(x + 2, -3.5, 5), parent=leg)
    # head: a big box on the front of the body, white cheeks
    g.box((21, -6, 12), (29, 6, 22), "fur", part="head")
    g.paint((26, -6, 12), (29, -5, 15), "white", of="head")
    g.paint((23, -6, 17), (25, -6, 17), "stripe", of="head")
    g.paint((23, -6, 19), (24, -6, 19), "stripe", of="head")
    g.box((29, -1, 21), (29, -1, 22), "stripe", part="head")
    g.joint("head", pivot=(22, 0.5, 16), rotate=(3, 8, -14), parent="body")
    # face, painted flat: amber eyes with the pupils to the inside, a white spot over each, black brows slanting
    # down to the middle
    g.box((29, -4, 18), (29, -4, 19), "eye", part="head")
    g.box((29, -3, 18), (29, -3, 19), "pupil", part="head")
    g.set(29, -5, 20, "white", part="head")
    g.box((29, -5, 21), (29, -4, 21), "stripe", part="head")
    g.set(29, -3, 20, "stripe", part="head")
    # white muzzle, the pink nose, a cheeky grin painted under it
    g.box((30, -3, 11), (32, 3, 16), "white", part="muzzle")
    g.paint((32, -1, 16), (32, 1, 16), "nose", of="muzzle")
    g.set(32, 0, 15, "nose", part="muzzle")
    g.set(32, -2, 13, "stripe", part="muzzle")
    g.box((32, -1, 12), (32, 0, 12), "stripe", part="muzzle")
    g.joint("muzzle", pivot=(30, 0.5, 13.5), parent="head")
    # ears: small rounded blocks with a dark rim
    g.box((24, -6, 23), (25, -4, 24), "fur", part="ear_l")
    g.paint((24, -6, 24), (25, -4, 24), "stripe", of="ear_l")
    g.joint("ear_l", pivot=(24.5, -5, 23), rotate=(10, 6, 0), parent="head")
    # tail: two striped blocks raised in a curve, black tip
    g.box((-6, -1, 15), (-1, 1, 16), "fur", part="tail")
    g.paint((-3, -1, 15), (-3, 1, 16), "stripe", of="tail")
    g.joint("tail", pivot=(0, 0.5, 16), rotate=(0, 26, 10), parent="body")
    g.box((-11, -1, 15), (-7, 1, 16), "fur", part="tail_tip")
    g.paint((-9, -1, 15), (-9, 1, 16), "stripe", of="tail_tip")
    g.paint((-11, -1, 15), (-11, 1, 16), "stripe", of="tail_tip")
    g.joint("tail_tip", pivot=(-6, 0.5, 15.5), rotate=(0, 30, 0), parent="tail")
    g.mirror()
    # a prowling stride: the front left paw forward, the hind left back, the right side the other way
    g.joint("leg_fl", pivot=(19, -3.5, 10), rotate=(0, -20, 0), parent="body")
    g.joint("leg_fr", pivot=(19, 4.5, 10), rotate=(0, 12, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -3.5, 10), rotate=(0, 14, 0), parent="body")
    g.joint("leg_hr", pivot=(3, 4.5, 10), rotate=(0, -12, 0), parent="body")
    # the knees: the reaching front paw folds back, the hind hock flexes
    g.joint("shin_fl", pivot=(19, -3.5, 5), rotate=(0, 30, 0), parent="leg_fl")
    g.joint("shin_hl", pivot=(3, -3.5, 5), rotate=(0, -14, 0), parent="leg_hl")
