"""000024 · Red-eyed Tree Frog (Agalychnis callidryas) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: green, red, blue, yellow, toe, belly, pupil. Size: 18 x 15 x 11 voxels posed.
Personality: a cheeky, bright-eyed show-off. Pose: sitting low and squat, ready to jump: each hind leg two flat
boards hinged at the knee like a clapperboard (the thigh on the flank, set into the body with one voxel showing on
its side and hinged inside; the lower leg with the long orange foot folded under it), short front arms in one piece
(no elbow, owner 2026-11-21) with the orange hands spread, the head turned to the camera and a little up. Expression: huge
red eyes bulging on top with a black pupil, and a wide grin across the front, painted flat."""


def build(g):
    # body: a wide, squat box, green on top, the white belly underneath, blue flanks with yellow stripes
    g.box((0, -4, 1), (8, 4, 6), "green", part="body")
    g.paint((1, -3, 1), (8, 3, 1), "belly", of="body")
    g.paint((5, -4, 1), (8, -4, 3), "blue", of="body")
    for x in (5, 7):
        g.paint((x, -4, 1), (x, -4, 4), "yellow", of="body")
    # head: the front of the frog, as wide as the body, the white chin and throat, a wide grin across the front
    g.box((9, -4, 2), (13, 4, 6), "green", part="head")
    g.paint((9, -4, 2), (13, 4, 2), "belly", of="head")
    g.paint((13, -3, 2), (13, 0, 3), "belly", of="head")
    g.paint((13, -3, 4), (13, 0, 4), "pupil", of="head")
    g.set(13, -4, 5, "pupil", part="head")
    # huge red eyes bulging on the top front corners, the black pupil on their front
    g.box((10, -4, 7), (12, -2, 9), "red", part="head")
    g.box((12, -3, 8), (12, -3, 9), "pupil", part="head")
    g.joint("head", pivot=(9, 0.5, 4), rotate=(3, -6, -14), parent="body")
    # front legs: one piece each (no elbow): a short green arm beside the throat down to the orange hand spread wide
    g.box((10, -6, 1), (11, -5, 3), "green", part="leg_fl")
    g.box((9, -7, 0), (12, -5, 0), "toe", part="leg_fl")
    g.joint("leg_fl", pivot=(10.5, -4.5, 3.5), parent="body")
    # hind legs, a clapperboard on each flank: the thigh a flat board two voxels wide, one voxel inside the body and
    # one showing on its side, hinged inside the body (the upper part); under it the lower leg, a second board folded
    # forward along the ground with the long webbed foot at its end (the lower part), hinged at the knee at the
    # thigh's front-bottom corner, so a jump opens the two boards like a clapper
    g.box((0, -5, 2), (5, -4, 5), "green", part="leg_hl")
    g.paint((0, -5, 2), (5, -5, 2), "blue", of="leg_hl")
    g.joint("leg_hl", pivot=(1.5, -3.5, 4.5), parent="body")
    g.box((-1, -5, 1), (5, -4, 1), "green", part="shin_hl")
    g.box((-3, -6, 0), (1, -4, 0), "toe", part="shin_hl")
    g.joint("shin_hl", pivot=(5.5, -4.5, 1.5), parent="leg_hl")
    g.mirror()
