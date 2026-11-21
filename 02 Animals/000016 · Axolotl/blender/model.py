"""000016 · Axolotl (Ambystoma mexicanum) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: skin, gill, belly, eye. Size: 18 x 15 x 7 voxels posed.
Personality: happy-go-lucky and a little goofy. Pose: A sprawling stride, the legs swept forward and back, the tail
curving, the head turned to the camera, the gills fanned. Expression: a wide smile and small dark eyes set far apart,
painted flat."""


def build(g):
    # body: a low box lying on the ground, the pale belly underneath
    g.box((3, -2, 1), (10, 2, 3), "skin", part="body")
    g.paint((4, -2, 1), (9, 2, 1), "belly", of="body")
    # legs: little stubs sticking out sideways, splayed
    g.box((9, -4, 0), (9, -3, 1), "skin", part="leg_fl")
    g.joint("leg_fl", pivot=(9.5, -2, 1), rotate=(0, 0, 28), parent="body")
    g.box((4, -4, 0), (4, -3, 1), "skin", part="leg_hl")
    g.joint("leg_hl", pivot=(4.5, -2, 1), rotate=(0, 0, -26), parent="body")
    # head: a wide flat box, wider than the body, the pale chin underneath
    g.box((11, -3, 1), (14, 3, 5), "skin", part="head")
    g.paint((11, -3, 1), (14, 3, 1), "belly", of="head")
    g.joint("head", pivot=(11, 0.5, 2.5), rotate=(3, 6, -14), parent="body")
    # face, painted flat on the front of the head: small dark eyes on the outer corners, a wide smile
    g.set(14, -3, 4, "eye", part="head")
    g.box((14, -1, 2), (14, 0, 2), "gill", part="head")
    g.set(14, -2, 3, "gill", part="head")
    # gills: a column at the back of the head with three fingers fanning out sideways
    g.box((11, -4, 2), (11, -4, 6), "gill", part="gill_l")
    for z in (2, 4, 6):
        g.box((11, -6, z), (11, -5, z), "gill", part="gill_l")
    g.joint("gill_l", pivot=(11.5, -3, 3), rotate=(18, 0, -10), parent="head")
    # tail: two blocks curving to one side, a fin along the top
    g.box((0, -1, 1), (2, 1, 3), "skin", part="tail")
    g.box((0, 0, 4), (2, 0, 4), "gill", part="tail")
    g.joint("tail", pivot=(2.5, 0.5, 2), rotate=(0, 0, 20), parent="body")
    g.box((-2, -1, 1), (-1, 1, 2), "skin", part="tail_tip")
    g.box((-2, 0, 3), (-1, 0, 3), "gill", part="tail_tip")
    g.joint("tail_tip", pivot=(-0.5, 0.5, 2), rotate=(0, 0, 26), parent="tail")
    g.mirror()
    # the smile's other corner (the mirror copies y < 0 only)
    g.set(14, 1, 2, "gill", part="head")
    # a livelier pose (owner 2026-11-21); the head turned to the camera
    g.joint("leg_fr", pivot=(9.5, 3, 1), rotate=(0, 0, -14), parent="body")
    g.joint("leg_hr", pivot=(4.5, 3, 1), rotate=(0, 0, 14), parent="body")
