"""26-021 · Bottlenose Dolphin (Tursiops truncatus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: grey, back, belly, eye. Size: 42 x 16 x 12 voxels posed.
Personality: playful, smart and sociable. Pose: a happy U-curve: the belly on the ground, the head lifted and turned to
the camera, the tail and flukes curving up behind, the flippers spread. Expression: a bright eye with a glint and the
dolphin's built-in smile, painted flat."""


def build(g):
    # body: the thick middle of the arch, dark back, pale belly; the tall curved dorsal fin
    g.box((0, -4, 0), (15, 4, 7), "grey", part="body")
    g.paint((0, -3, 7), (15, 3, 7), "back", of="body")
    g.paint((0, -4, 0), (15, 4, 1), "belly", of="body")
    g.box((5, 0, 8), (9, 0, 8), "back", part="body")
    g.box((4, 0, 9), (7, 0, 9), "back", part="body")
    g.box((3, 0, 10), (5, 0, 10), "back", part="body")
    # flippers: paddles on the lower flanks, spread out
    g.box((12, -7, 1), (15, -5, 1), "grey", part="flipper_l")
    g.joint("flipper_l", pivot=(13.5, -4.5, 1.5), rotate=(10, 0, -14), parent="body")
    # head: the rounded melon, pale throat, lifted and turned to the camera
    g.box((16, -3, 1), (22, 3, 7), "grey", part="head")
    g.paint((16, -3, 1), (22, 3, 2), "belly", of="head")
    g.paint((16, -2, 7), (20, 2, 7), "back", of="head")
    g.joint("head", pivot=(16, 0.5, 4), rotate=(6, -16, -14), parent="body")
    # eye painted flat on the side of the head with a pale glint, and the smile line running back from the beak
    g.set(21, -3, 6, "eye", part="head")
    g.set(21, -3, 7, "belly", part="head")
    g.box((20, -3, 3), (22, -3, 3), "eye", part="head")
    # beak: long and rounded, pale below, the smile line along its side
    g.box((23, -1, 1), (27, 1, 3), "grey", part="beak")
    g.paint((23, -1, 1), (27, 1, 1), "belly", of="beak")
    g.box((23, -1, 2), (26, -1, 2), "eye", part="beak")
    g.joint("beak", pivot=(23, 0.5, 2), parent="head")
    # tail: the tail stock in two blocks curving up behind, ending in the wide flukes
    g.box((-7, -3, 1), (-1, 3, 6), "grey", part="tail")
    g.paint((-7, -2, 6), (-1, 2, 6), "back", of="tail")
    g.joint("tail", pivot=(-0.5, 0.5, 3.5), rotate=(0, 22, 0), parent="body")
    g.box((-13, -1, 2), (-8, 1, 5), "grey", part="tail_tip")
    g.joint("tail_tip", pivot=(-7.5, 0.5, 3.5), rotate=(0, 18, 0), parent="tail")
    g.box((-16, -6, 3), (-14, 6, 3), "back", part="flukes")
    g.box((-14, -2, 3), (-14, 2, 4), "grey", part="flukes")
    g.joint("flukes", pivot=(-13.5, 0.5, 3.5), rotate=(0, 10, 0), parent="tail_tip")
    g.mirror()
    # the smile line on the other side of the beak (the mirror copies y < 0 only)
    g.box((23, 1, 2), (26, 1, 2), "eye", part="beak")
