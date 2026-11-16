"""Voxel Fauna · selftest creature: a generic bulky blocky-mob quadruped (not a species) that proves the engine end to
end: stacked boxes, sections turned at their joints with parents, a face painted flat, block ears, an asymmetric
step after the mirror.
Used only by `python _system/studio/scripts/vf.py selftest`; its renders go to _system/cache/selftest/.
Palette keys: fur, belly, dark (see SELFTEST_LOOK in scripts/vf.py). Same file as the worked example in key-prompt.md.
"""


def build(g):
    # body: one big bulky box, pale belly
    g.box((0, -4, 5), (14, 4, 12), "fur", part="body")
    g.paint((2, -4, 5), (12, 4, 5), "belly", of="body")
    # legs: 3 x 3 pillars hinged under the body, dark paws
    for name, x in (("leg_hl", 1), ("leg_fl", 10)):
        g.box((x, -4, 0), (x + 2, -2, 4), "fur", part=name)
        g.box((x, -4, 0), (x + 2, -2, 0), "dark", part=name)
        g.joint(name, pivot=(x + 1.5, -3, 5), parent="body")
    # head: a big box on the front of the body, tilted and turned towards the camera
    g.box((14, -5, 9), (21, 5, 17), "fur", part="head")
    g.joint("head", pivot=(15, 0.5, 12), rotate=(8, 0, -14), parent="body")
    # face, painted flat on the front of the head: a light eye with the dark pupil to the inside, a dark brow
    # stepping down towards the middle (a determined look)
    g.box((21, -4, 13), (21, -4, 14), "belly", part="head")
    g.box((21, -3, 13), (21, -3, 14), "dark", part="head")
    g.box((21, -5, 16), (21, -4, 16), "dark", part="head")
    g.box((21, -3, 15), (21, -2, 15), "dark", part="head")
    # snout: a box on the face, the dark nose on its top front edge, a small smile painted under it
    g.box((22, -2, 9), (24, 2, 12), "belly", part="snout")
    g.paint((24, -1, 12), (24, 1, 12), "dark", of="snout")
    g.set(24, -2, 10, "dark", part="snout")
    g.box((24, -1, 9), (24, 0, 9), "dark", part="snout")
    g.joint("snout", pivot=(22, 0.5, 10.5), parent="head")
    # ears: thin blocks on top of the head, tipped outwards
    g.box((17, -5, 18), (17, -3, 20), "fur", part="ear_l")
    g.joint("ear_l", pivot=(17, -4, 18), rotate=(18, 0, 0), parent="head")
    # tail: one block raised from its root
    g.box((-4, -1, 10), (-1, 1, 12), "fur", part="tail")
    g.box((-5, -1, 10), (-5, 1, 12), "belly", part="tail")
    g.joint("tail", pivot=(0, 0.5, 11), rotate=(0, 25, 0), parent="body")
    g.mirror()
    # an asymmetric step: the front-left leg forward, the hind-left back (set after the mirror)
    g.joint("leg_fl", pivot=(11.5, -3, 5), rotate=(0, -12, 0), parent="body")
    g.joint("leg_hl", pivot=(2.5, -3, 5), rotate=(0, 10, 0), parent="body")
