"""26-003 · Red Panda (Ailurus fulgens) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, white, dark, ring, eye. Size: 32 x 15 x 20 voxels posed.
Personality: curious and playful. Pose: head cocked hard to one side and looking up, one front paw reaching forward,
the ringed tail curling up in two blocks. Expression: wide white eyes with the pupils to the inside, white brows
rising towards the middle, a small round mouth, all painted flat on the face."""


def build(g):
    # body: one box, rusty red, a dark belly
    g.box((0, -4, 5), (11, 4, 10), "fur", part="body")
    g.paint((1, -4, 5), (10, 4, 5), "dark", of="body")
    # legs: 3 x 3 dark pillars
    for name, x in (("leg_hl", 1), ("leg_fl", 8)):
        g.box((x, -4, 0), (x + 2, -2, 4), "dark", part=name)
        g.joint(name, pivot=(x + 1.5, -3, 5), parent="body")
    # head: a big box wider than the body; the white mask: cheeks and jaw, up the outer face
    g.box((11, -5, 8), (18, 5, 15), "fur", part="head")
    g.paint((16, -5, 8), (18, 5, 9), "white", of="head")
    g.paint((17, -5, 8), (18, -4, 10), "white", of="head")
    g.joint("head", pivot=(12, 0.5, 10), rotate=(18, -6, -12), parent="body")
    # face, painted flat: white eye with the pupil to the inside, a white brow rising towards the middle (curious)
    g.box((18, -3, 11), (18, -3, 12), "white", part="head")
    g.box((18, -2, 11), (18, -2, 12), "eye", part="head")
    g.box((18, -4, 14), (18, -3, 14), "white", part="head")
    g.set(18, -2, 15, "white", part="head")
    # short white muzzle, dark nose, a small round mouth painted on its front
    g.box((19, -2, 8), (20, 2, 10), "white", part="muzzle")
    g.paint((20, -1, 10), (20, 1, 10), "dark", of="muzzle")
    g.set(20, 0, 8, "dark", part="muzzle")
    g.joint("muzzle", pivot=(19, 0.5, 9), parent="head")
    # ears: rusty blocks with a white rim on the top and the outer edge, splayed and tipped forward
    g.box((13, -5, 16), (14, -3, 18), "fur", part="ear_l")
    g.paint((13, -5, 16), (14, -5, 18), "white", of="ear_l")
    g.paint((13, -5, 18), (14, -3, 18), "white", of="ear_l")
    g.joint("ear_l", pivot=(13.5, -4, 16), rotate=(16, 8, 0), parent="head")
    # the long ringed tail in two blocks curling up, dark tip
    g.box((-6, -2, 6), (-1, 2, 10), "fur", part="tail")
    g.paint((-3, -2, 6), (-2, 2, 10), "ring", of="tail")
    g.joint("tail", pivot=(0, 0.5, 8), rotate=(0, 18, 6), parent="body")
    g.box((-10, -2, 6), (-7, 2, 10), "fur", part="tail_tip")
    g.paint((-9, -2, 6), (-8, 2, 10), "ring", of="tail_tip")
    g.paint((-10, -2, 6), (-10, 2, 10), "dark", of="tail_tip")
    g.joint("tail_tip", pivot=(-6, 0.5, 8), rotate=(0, 20, 0), parent="tail")
    g.mirror()
    # one front paw reaching forward
    g.joint("leg_fl", pivot=(9.5, -3, 5), rotate=(0, -30, 0), parent="body")
    g.joint("leg_hl", pivot=(2.5, -3, 5), rotate=(0, 6, 0), parent="body")
    g.joint("leg_hr", pivot=(2.5, 4, 5), rotate=(0, -4, 0), parent="body")
