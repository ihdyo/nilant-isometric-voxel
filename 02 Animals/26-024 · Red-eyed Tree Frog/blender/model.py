"""26-024 · Red-eyed Tree Frog (Agalychnis callidryas) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: green, red, blue, yellow, toe, belly, pupil. Size: 18 x 15 x 12 voxels posed.
Personality: a cheeky, bright-eyed show-off. Pose: sitting tall on folded back legs with the front feet planted wide
and the orange toes spread, the head tilted up to the camera. Expression: huge red eyes with a black pupil and a wide
grin, painted flat."""


def build(g):
    # body: one box, green on top, the white belly underneath, blue flanks with yellow stripes
    g.box((0, -4, 2), (10, 4, 6), "green", part="body")
    g.paint((1, -3, 2), (9, 3, 2), "belly", of="body")
    g.paint((1, -4, 2), (9, -4, 3), "blue", of="body")
    for x in (3, 6):
        g.paint((x, -4, 2), (x, -4, 4), "yellow", of="body")
    # back legs folded beside the body: a green thigh with a blue inside, a long orange foot on the ground
    g.box((1, -6, 1), (6, -5, 3), "green", part="leg_hl")
    g.paint((1, -5, 1), (6, -5, 1), "blue", of="leg_hl")
    g.box((4, -7, 0), (8, -5, 0), "toe", part="leg_hl")
    g.joint("leg_hl", pivot=(3.5, -4.5, 3), parent="body")
    # front legs: green arms planted wide, orange hands with spread toes
    g.box((10, -5, 1), (11, -5, 3), "green", part="leg_fl")
    g.box((11, -7, 0), (13, -5, 0), "toe", part="leg_fl")
    g.joint("leg_fl", pivot=(10.5, -4.5, 3), parent="body")
    # head: a wide box tilted up to the camera, the white chin
    g.box((11, -4, 3), (16, 4, 7), "green", part="head")
    g.paint((11, -4, 3), (16, 4, 3), "belly", of="head")
    g.joint("head", pivot=(11, 0.5, 5), rotate=(8, -12, -14), parent="body")
    # huge bulging red eyes on the top corners, a black pupil painted on the front
    g.box((14, -5, 7), (16, -3, 9), "red", part="head")
    g.set(16, -4, 8, "pupil", part="head")
    # a wide grin painted flat on the front of the head
    g.box((16, -2, 4), (16, 0, 4), "pupil", part="head")
    g.set(16, -3, 5, "pupil", part="head")
    g.mirror()
    # the grin's other end (the mirror copies y < 0 only)
    g.box((16, 1, 4), (16, 2, 4), "pupil", part="head")
    g.set(16, 3, 5, "pupil", part="head")
