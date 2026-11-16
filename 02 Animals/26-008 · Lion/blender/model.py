"""26-008 · Lion (Panthera leo) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, mane, muzzle, nose, eye. Size: 47 x 21 x 28 voxels posed.
Personality: proud and confident, the king who naps a lot. Pose: mid-stride, chest out, the head and its thick mane
turned to the camera and raised, the tail dropping and curling up to the dark tuft. Expression: steady pale eyes
with the pupils to the inside under heavy brows slanting down to the middle, a calm smile, all painted flat."""


def build(g):
    # body: one long bulky box
    g.box((0, -6, 9), (19, 6, 18), "coat", part="body")
    # legs: thick 4 x 4 pillars, an upper leg and a shin hinged at the knee
    for leg, shin, x in (("leg_hl", "shin_hl", 1), ("leg_fl", "shin_fl", 14)):
        g.box((x, -6, 4), (x + 3, -3, 8), "coat", part=leg)
        g.box((x, -6, 0), (x + 3, -3, 3), "coat", part=shin)
        g.joint(leg, pivot=(x + 2, -4.5, 9), parent="body")
        g.joint(shin, pivot=(x + 2, -4.5, 4), parent=leg)
    # the mane: a big heavy block around the neck and head, wider and taller than the body, reaching forward so only
    # the front two voxels of the head stick out of it
    g.box((18, -9, 8), (27, 9, 25), "mane", part="mane")
    g.joint("mane", pivot=(19, 0.5, 14), rotate=(4, -5, -10), parent="body")
    # head: a box set into the mane, its face two voxels proud of it, so the mane frames the face on every side
    g.box((24, -6, 11), (29, 6, 21), "coat", part="head")
    g.joint("head", pivot=(25, 0.5, 15), rotate=(4, 0, 0), parent="mane")
    # face, painted flat: pale eyes with the pupils to the inside, mane-coloured brows slanting down to the middle
    g.box((29, -4, 17), (29, -4, 18), "muzzle", part="head")
    g.box((29, -3, 17), (29, -3, 18), "eye", part="head")
    g.box((29, -5, 20), (29, -4, 20), "mane", part="head")
    g.box((29, -3, 19), (29, -2, 19), "mane", part="head")
    # pale muzzle, the T-shaped nose, a calm smile painted under it
    g.box((30, -3, 11), (32, 3, 15), "muzzle", part="muzzle")
    g.paint((32, -1, 15), (32, 1, 15), "nose", of="muzzle")
    g.set(32, 0, 14, "nose", part="muzzle")
    g.set(32, -2, 13, "nose", part="muzzle")
    g.box((32, -1, 12), (32, 0, 12), "nose", part="muzzle")
    g.joint("muzzle", pivot=(30, 0.5, 13), parent="head")
    # small round ears on top of the head, just in front of the mane
    g.box((28, -6, 22), (28, -5, 23), "coat", part="ear_l")
    g.joint("ear_l", pivot=(28.5, -5, 22), rotate=(10, 0, 0), parent="head")
    # tail: drops from the rump, then curls up to the dark tuft
    g.box((-6, -1, 15), (-1, 1, 16), "coat", part="tail")
    g.joint("tail", pivot=(0, 0.5, 16), rotate=(0, -24, 0), parent="body")
    g.box((-11, -1, 15), (-7, 1, 16), "coat", part="tail_tip")
    g.box((-14, -2, 14), (-11, 2, 17), "mane", part="tail_tip")
    g.joint("tail_tip", pivot=(-6, 0.5, 15.5), rotate=(0, 38, 0), parent="tail")
    g.mirror()
    # mid-stride: the front left paw forward, the hind left back, the right side the other way
    g.joint("leg_fl", pivot=(16, -4.5, 9), rotate=(0, -12, 0), parent="body")
    g.joint("leg_fr", pivot=(16, 5.5, 9), rotate=(0, 8, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -4.5, 9), rotate=(0, 10, 0), parent="body")
    g.joint("leg_hr", pivot=(3, 5.5, 9), rotate=(0, -8, 0), parent="body")
    # the knees: the front left paw folds back as it swings forward, the hind left hock flexes
    g.joint("shin_fl", pivot=(16, -4.5, 4), rotate=(0, 24, 0), parent="leg_fl")
    g.joint("shin_hl", pivot=(3, -4.5, 4), rotate=(0, -10, 0), parent="leg_hl")
