"""26-020 · Scarlet Macaw (Ara macao) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: red, yellow, blue, face, bill, dark, eye. Size: 26 x 20 x 24 voxels posed.
Personality: loud, cheeky and a show-off. Pose: standing tall with both wings half open to flash the yellow and
blue, the head cocked to the camera, the long tail sweeping down behind. Expression: a pale eye with the dark pupil
to the front in its white face patch, painted flat."""


def build(g):
    # legs: short dark pillars on block feet
    g.box((5, -2, 1), (5, -2, 3), "dark", part="leg_l")
    g.box((4, -3, 0), (7, -1, 0), "dark", part="leg_l")
    g.joint("leg_l", pivot=(5.5, -1.5, 4), parent="body")
    # body: one tall red box
    g.box((0, -3, 4), (8, 3, 15), "red", part="body")
    # wings: slabs on the flanks, red at the shoulder, the yellow band, blue flight feathers; held half open
    g.box((0, -4, 5), (7, -4, 15), "red", part="wing_l")
    g.paint((0, -4, 10), (7, -4, 12), "yellow", of="wing_l")
    g.paint((0, -4, 5), (7, -4, 9), "blue", of="wing_l")
    g.joint("wing_l", pivot=(5, -3.5, 15), rotate=(-30, 0, -10), parent="body")
    # tail: long red feathers with blue tips, sweeping down and back
    g.box((-7, -1, 7), (-1, 1, 8), "red", part="tail")
    g.joint("tail", pivot=(-0.5, 0.5, 8), rotate=(0, -24, 0), parent="body")
    g.box((-13, -1, 7), (-8, 1, 8), "red", part="tail_tip")
    g.paint((-13, -1, 7), (-11, 1, 8), "blue", of="tail_tip")
    g.joint("tail_tip", pivot=(-7.5, 0.5, 7.5), rotate=(0, -10, 0), parent="tail")
    # head: a red box on top of the body, the bare white face patch on its side, cocked to the camera
    g.box((2, -3, 16), (9, 3, 22), "red", part="head")
    g.paint((7, -3, 17), (9, -3, 20), "face", of="head")
    g.paint((9, -2, 17), (9, -2, 19), "face", of="head")
    g.joint("head", pivot=(5, 0.5, 16), rotate=(12, 0, -14), parent="body")
    # eye painted flat in the face patch: pale yellow with the dark pupil to the front
    g.set(8, -3, 19, "eye", part="head")
    g.set(9, -3, 19, "dark", part="head")
    # the big hooked bill: pale on top, black below, the tip hooked down
    g.box((10, -1, 17), (12, 1, 20), "bill", part="beak")
    g.box((13, -1, 16), (13, 1, 19), "bill", part="beak")
    g.box((10, -1, 16), (12, 1, 16), "dark", part="beak")
    g.joint("beak", pivot=(10, 0.5, 18), rotate=(0, 8, 0), parent="head")
    g.mirror()
