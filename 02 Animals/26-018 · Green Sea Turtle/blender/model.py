"""26-018 · Green Sea Turtle (Chelonia mydas) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: shell, seam, skin, belly, eye. Size: 27 x 31 x 7 voxels posed.
Personality: calm, wise and unhurried. Pose: crawling up the beach: the front flippers raised mid-stroke, one higher
than the other, the head lifted and turned to the camera, the back flippers splayed. Expression: content, half-closed
eyes and a small smile, painted flat."""


def build(g):
    # body: the pale underside on the ground and the low domed shell in two steps, the plate seams on top
    g.box((1, -6, 0), (18, 6, 0), "belly", part="body")
    g.box((0, -7, 1), (19, 7, 5), "shell", part="body")
    g.box((2, -6, 6), (17, 6, 6), "shell", part="body")
    for x in (6, 10, 14):
        g.paint((x, -6, 6), (x, 6, 6), "seam", of="body")
    g.paint((2, -3, 6), (17, -3, 6), "seam", of="body")
    g.paint((0, -7, 1), (19, 7, 1), "seam", of="body")
    g.box((-1, 0, 1), (-1, 0, 2), "skin", part="body")
    # head: a rounded box on a short neck, the pale jaw, lifted and turned to the camera
    g.box((20, -2, 1), (24, 2, 5), "skin", part="head")
    g.paint((20, -2, 1), (24, 2, 1), "belly", of="head")
    g.joint("head", pivot=(20, 0.5, 3), rotate=(6, -14, -16), parent="body")
    # face, painted flat: content half-closed eyes along the sides of the head, a small smile on the front
    g.box((23, -2, 4), (24, -2, 4), "eye", part="head")
    g.set(24, -1, 2, "eye", part="head")
    g.set(24, 0, 2, "eye", part="head")
    # front flippers: long paddles, raised mid-stroke and swept forward
    g.box((11, -15, 2), (14, -8, 2), "skin", part="flipper_l")
    g.joint("flipper_l", pivot=(12.5, -7.5, 2.5), rotate=(-24, 0, 14), parent="body")
    # back flippers: short paddles splayed out behind
    g.box((1, -10, 1), (3, -8, 1), "skin", part="flipper_hl")
    g.joint("flipper_hl", pivot=(2, -7.5, 1.5), rotate=(0, 0, -20), parent="body")
    g.mirror()
    # one front flipper higher than the other
    g.joint("flipper_r", pivot=(12.5, 8.5, 2.5), rotate=(10, 0, -14), parent="body")
