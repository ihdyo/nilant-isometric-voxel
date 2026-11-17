"""26-024 · Red-eyed Tree Frog (Agalychnis callidryas) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: green, red, blue, yellow, toe, belly, pupil. Size: 17 x 17 x 11 voxels posed.
Personality: a cheeky, bright-eyed show-off. Pose: sitting low and squat, as wide as it is long, the big hind thighs
on the back corners standing on flat orange feet that reach out behind (each leg an upper and a lower part), short
front arms with orange hands spread wide, the head tilted up to the camera. Expression: huge red eyes bulging on top
with a black pupil, and a wide grin across the front, painted flat."""


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
    g.joint("head", pivot=(9, 0.5, 4), rotate=(4, -6, -10), parent="body")
    # front legs: a short green upper arm on each side of the throat and the forearm with the orange hand spread wide
    g.box((10, -6, 2), (11, -5, 3), "green", part="leg_fl")
    g.joint("leg_fl", pivot=(11, -4.5, 3.5), parent="body")
    g.box((10, -6, 1), (11, -5, 1), "green", part="shin_fl")
    g.box((9, -7, 0), (12, -5, 0), "toe", part="shin_fl")
    g.joint("shin_fl", pivot=(11, -5.5, 2), parent="leg_fl")
    # hind legs: a big green thigh on each back corner, the blue inside showing at the front (the upper part), standing
    # on the flat orange webbed foot right under it, which reaches out behind and to the side (the lower part)
    g.box((0, -7, 1), (4, -5, 5), "green", part="leg_hl")
    g.paint((4, -7, 1), (4, -5, 2), "blue", of="leg_hl")
    g.joint("leg_hl", pivot=(2.5, -4.5, 4), parent="body")
    g.box((-2, -8, 0), (3, -5, 0), "toe", part="shin_hl")
    g.joint("shin_hl", pivot=(1.5, -6, 1), parent="leg_hl")
    g.mirror()
