"""26-019 · Nine-banded Armadillo (Dasypus novemcinctus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: shell, band, skin, eye. Size: 32 x 11 x 12 voxels posed.
Personality: curious and busy, a little shy. Pose: trundling forward with the nose down and turned to the camera to
sniff, the ears up, the long ringed tail curving behind, one front foot lifted. Expression: small beady eyes on the
head, painted flat, a dark nose tip."""


def build(g):
    # legs: short pillars under the shell
    for name, x in (("leg_hl", 2), ("leg_fl", 13)):
        g.box((x, -4, 0), (x + 2, -3, 2), "skin", part=name)
        g.joint(name, pivot=(x + 1.5, -3.5, 3), parent="body")
    # body: the armour shell, a box with a rounded top step; the bands across the middle
    g.box((0, -5, 3), (16, 5, 9), "shell", part="body")
    g.box((1, -4, 10), (15, 4, 10), "shell", part="body")
    for x in (5, 7, 9, 11):
        g.paint((x, -5, 3), (x, 5, 10), "band", of="body")
    g.paint((1, -5, 3), (15, 5, 3), "skin", of="body")
    # head: the armoured head shield, the pale cheeks, a long pointed snout with a dark tip
    g.box((17, -2, 4), (20, 2, 8), "shell", part="head")
    g.paint((17, -2, 4), (20, 2, 5), "skin", of="head")
    g.box((21, -1, 4), (23, 1, 6), "skin", part="head")
    g.set(23, 0, 6, "eye", part="head")
    g.joint("head", pivot=(17, 0.5, 6), rotate=(6, 12, -16), parent="body")
    # small beady eyes, painted flat on the front corners of the head
    g.set(20, -2, 7, "eye", part="head")
    # tall ears
    g.box((18, -2, 9), (18, -2, 11), "skin", part="ear_l")
    g.joint("ear_l", pivot=(18.5, -1.5, 9), rotate=(12, -8, 0), parent="head")
    # tail: long, in two ringed blocks curving down behind
    g.box((-5, -1, 5), (-1, 1, 6), "shell", part="tail")
    g.paint((-4, -1, 5), (-4, 1, 6), "band", of="tail")
    g.paint((-2, -1, 5), (-2, 1, 6), "band", of="tail")
    g.joint("tail", pivot=(-0.5, 0.5, 5.5), rotate=(0, -14, 10), parent="body")
    g.box((-8, 0, 5), (-6, 0, 5), "shell", part="tail_tip")
    g.set(-8, 0, 5, "band", part="tail_tip")
    g.joint("tail_tip", pivot=(-5.5, 0.5, 5.5), rotate=(0, -12, 14), parent="tail")
    g.mirror()
    # one front foot lifted mid-step
    g.joint("leg_fl", pivot=(14.5, -3.5, 3), rotate=(0, -24, 0), parent="body")
