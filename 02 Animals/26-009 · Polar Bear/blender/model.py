"""26-009 · Polar Bear (Ursus maritimus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, dark, shine. Size: 42 x 15 x 24 voxels posed.
Personality: a curious, patient wanderer of the ice. Pose: a long walking stride, the hips higher than the shoulders,
the neck and long head carried low and swung towards the camera, the nose lifted to sniff. Expression: round white
eyes with the dark pupils to the inside, a big black nose and a small open mouth, all painted flat."""


def build(g):
    # body: the heavy hindquarters (the highest point) and the slightly lower shoulders, one part
    g.box((0, -7, 9), (14, 7, 23), "fur", part="body")
    g.box((15, -6, 9), (26, 6, 21), "fur", part="body")
    g.box((-1, -1, 19), (-1, 1, 20), "fur", part="body")
    # legs: thick 5 x 5 pillars, three dark claws on the front of each paw
    for leg, shin, x, y in (("leg_hl", "shin_hl", 2, -7), ("leg_fl", "shin_fl", 20, -6)):
        g.box((x, y, 5), (x + 4, y + 4, 8), "fur", part=leg)
        g.box((x, y, 0), (x + 4, y + 4, 4), "fur", part=shin)
        for c in (y, y + 2, y + 4):
            g.set(x + 4, c, 0, "dark", part=shin)
        g.joint(leg, pivot=(x + 2.5, y + 2.5, 9), parent="body")
        g.joint(shin, pivot=(x + 2.5, y + 2.5, 5), parent=leg)
    # neck: a block carried low and forward
    g.box((27, -4, 10), (29, 4, 17), "fur", part="neck")
    g.joint("neck", pivot=(26.5, 0.5, 14), rotate=(6, 8, -12), parent="body")
    # head: a long box, nose lifted
    g.box((30, -5, 7), (36, 5, 15), "fur", part="head")
    g.joint("head", pivot=(30, 0.5, 11), rotate=(4, -12, 0), parent="neck")
    # eyes painted flat: white with the dark pupil to the inside
    g.box((36, -4, 12), (36, -4, 13), "shine", part="head")
    g.box((36, -3, 12), (36, -3, 13), "dark", part="head")
    # long snout, the big black nose on its top front edge, a small open mouth painted below
    g.box((37, -3, 7), (40, 3, 11), "fur", part="snout")
    g.paint((40, -1, 10), (40, 1, 11), "dark", of="snout")
    g.set(40, 0, 8, "dark", part="snout")
    g.joint("snout", pivot=(37, 0.5, 9), parent="head")
    # small round ears
    g.box((31, -5, 16), (32, -4, 17), "fur", part="ear_l")
    g.joint("ear_l", pivot=(31.5, -4, 16), rotate=(12, 0, 0), parent="head")
    g.mirror()
    # a long stride: the front left forward and the hind left back, the right side the other way
    g.joint("leg_fl", pivot=(22.5, -3.5, 9), rotate=(0, -16, 0), parent="body")
    g.joint("leg_fr", pivot=(22.5, 4.5, 9), rotate=(0, 12, 0), parent="body")
    g.joint("leg_hl", pivot=(4.5, -4.5, 9), rotate=(0, 14, 0), parent="body")
    g.joint("leg_hr", pivot=(4.5, 5.5, 9), rotate=(0, -10, 0), parent="body")
    # the knees: the reaching front paw folds back, the pushing hind leg flexes at the hock
    g.joint("shin_fl", pivot=(22.5, -3.5, 5), rotate=(0, 22, 0), parent="leg_fl")
    g.joint("shin_hl", pivot=(4.5, -4.5, 5), rotate=(0, -14, 0), parent="leg_hl")
