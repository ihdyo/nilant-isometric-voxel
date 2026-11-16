"""26-007 · Koala (Phascolarctos cinereus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, white, nose, eye, paw. Size: 14 x 24 x 25 voxels posed.
Personality: sleepy and cuddly. Pose: sitting, arms hanging from the sides of the body and swung forward so the
dark-palmed hands rest beside the knees, feet
forward with dark soles, the big head drowsily tilted, huge fluffy ears tipped out. Expression: eyes closed in a
sleepy curve and a tiny smile under the big nose, painted flat on the face."""


def build(g):
    # body: one upright box sitting on the ground, white chest
    g.box((0, -5, 0), (7, 5, 11), "fur", part="body")
    g.paint((7, -3, 2), (7, 3, 10), "white", of="body")
    # hind legs: thick blocks pointing forward, dark soles on the front, toes turned out
    g.box((5, -5, 0), (10, -3, 3), "fur", part="leg_l")
    g.box((10, -5, 0), (10, -3, 2), "paw", part="leg_l")
    g.joint("leg_l", pivot=(6, -4, 1.5), rotate=(0, 0, -10), parent="body")
    # arms: thick blocks on the sides of the body, hanging from the shoulders and swung forward so the dark-palmed
    # hands rest beside the knees
    g.box((3, -7, 4), (5, -6, 10), "fur", part="arm_l")
    g.box((3, -7, 4), (5, -6, 5), "paw", part="arm_l")
    g.joint("arm_l", pivot=(4.5, -5.5, 10.5), rotate=(8, -28, 0), parent="body")
    # head: a big box, wider than the body, drowsily tilted
    g.box((-1, -7, 12), (8, 7, 21), "fur", part="head")
    g.joint("head", pivot=(3.5, 0.5, 12), rotate=(12, 4, -8), parent="body")
    # sleepy closed eyes painted flat on the face: a dark curve, the ends higher than the middle
    g.set(8, -6, 18, "eye", part="head")
    g.box((8, -5, 17), (8, -4, 17), "eye", part="head")
    g.set(8, -3, 18, "eye", part="head")
    # a tiny smile painted under the nose
    g.box((8, -1, 12), (8, 0, 12), "nose", part="head")
    # the big dark nose block in the middle of the face
    g.box((9, -2, 13), (10, 2, 18), "nose", part="nose")
    g.joint("nose", pivot=(9, 0.5, 15.5), parent="head")
    # huge round ears sticking out on the sides, set into the head: grey rim, white fluffy front, tipped out
    g.box((2, -11, 16), (4, -6, 23), "fur", part="ear_l")
    g.paint((4, -10, 17), (4, -7, 22), "white", of="ear_l")
    g.paint((2, -11, 17), (4, -11, 22), "white", of="ear_l")
    g.joint("ear_l", pivot=(3, -6, 19.5), rotate=(14, 6, 0), parent="head")
    g.mirror()
