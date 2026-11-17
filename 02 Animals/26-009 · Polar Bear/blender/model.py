"""26-009 · Polar Bear (Ursus maritimus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, dark, shine. Size: 41 x 17 x 25 voxels posed.
Personality: a curious, patient wanderer of the ice. Pose: a long walking stride in two body sections, the heavy
hindquarters (the lower body, the highest point) and the shoulders (the upper body) turning at the waist towards the
camera, no neck: the long head carried low on the front of the shoulders, the nose lifted to sniff. Expression: round
white eyes with the dark pupils to the inside, a big black nose and a small open mouth, all painted flat."""


def build(g):
    # lower body: the heavy hindquarters (the highest point) and a stub of a tail
    g.box((0, -7, 9), (14, 7, 23), "fur", part="body")
    g.box((-1, -1, 19), (-1, 1, 20), "fur", part="body")
    # upper body: the slightly lower shoulders, their own section turning at the waist
    g.box((15, -6, 9), (27, 6, 21), "fur", part="torso")
    g.joint("torso", pivot=(15, 0.5, 15), rotate=(0, 3, -7), parent="body")
    # legs: thick 5 x 5 pillars with a knee, three dark claws on the front of each paw; the hind legs hang from the
    # lower body, the front legs from the upper body
    for leg, shin, x, y, parent in (("leg_hl", "shin_hl", 2, -7, "body"), ("leg_fl", "shin_fl", 20, -6, "torso")):
        g.box((x, y, 5), (x + 4, y + 4, 8), "fur", part=leg)
        g.box((x, y, 0), (x + 4, y + 4, 4), "fur", part=shin)
        for c in (y, y + 2, y + 4):
            g.set(x + 4, c, 0, "dark", part=shin)
        g.joint(leg, pivot=(x + 2.5, y + 2.5, 9), parent=parent)
        g.joint(shin, pivot=(x + 2.5, y + 2.5, 5), parent=leg)
    # head: a long box straight on the front of the shoulders, carried low, the nose lifted, turned to the camera
    g.box((28, -5, 9), (34, 5, 17), "fur", part="head")
    g.joint("head", pivot=(28, 0.5, 13), rotate=(5, -8, -12), parent="torso")
    # eyes painted flat: white with the dark pupil to the inside
    g.box((34, -4, 14), (34, -4, 15), "shine", part="head")
    g.box((34, -3, 14), (34, -3, 15), "dark", part="head")
    # long snout, the big black nose on its top front edge, a small open mouth painted below
    g.box((35, -3, 9), (38, 3, 13), "fur", part="snout")
    g.paint((38, -1, 12), (38, 1, 13), "dark", of="snout")
    g.set(38, 0, 10, "dark", part="snout")
    g.joint("snout", pivot=(35, 0.5, 11), parent="head")
    # small round ears
    g.box((29, -5, 18), (30, -4, 19), "fur", part="ear_l")
    g.joint("ear_l", pivot=(29.5, -4, 18), rotate=(12, 0, 0), parent="head")
    g.mirror()
    # a long stride: the front left forward and the hind left back, the right side the other way
    g.joint("leg_fl", pivot=(22.5, -3.5, 9), rotate=(0, -16, 0), parent="torso")
    g.joint("leg_fr", pivot=(22.5, 4.5, 9), rotate=(0, 12, 0), parent="torso")
    g.joint("leg_hl", pivot=(4.5, -4.5, 9), rotate=(0, 14, 0), parent="body")
    g.joint("leg_hr", pivot=(4.5, 5.5, 9), rotate=(0, -10, 0), parent="body")
    # the knees: the reaching front paw folds back, the pushing hind leg flexes at the hock
    g.joint("shin_fl", pivot=(22.5, -3.5, 5), rotate=(0, 22, 0), parent="leg_fl")
    g.joint("shin_hl", pivot=(4.5, -4.5, 5), rotate=(0, -14, 0), parent="leg_hl")
