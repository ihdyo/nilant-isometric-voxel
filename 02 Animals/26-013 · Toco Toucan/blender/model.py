"""26-013 · Toco Toucan (Ramphastos toco) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: body, throat, bill, ring, eye, vent, feet. Size: 23 x 11 x 21 voxels posed.
Personality: cheerful, chatty and curious. Pose: hopping on the ground with the head cocked and the big bill tilted
up, the tail raised, one wing lifted a little. Expression: round blue eyes in their orange rings, wide and curious,
painted flat."""


def build(g):
    # legs: short blue-grey pillars on block feet, one voxel thick
    g.box((4, -2, 1), (4, -2, 4), "feet", part="leg_l")
    g.joint("leg_l", pivot=(4.5, -1.5, 5), parent="body")
    g.box((3, -2, 0), (6, -2, 0), "feet", part="foot_l")
    for x, y in ((6, -3), (6, -1), (3, -3), (3, -1)):              # two toes forward, two back
        g.set(x, y, 0, "feet", part="foot_l")
    g.joint("foot_l", pivot=(4.5, -1.5, 1), parent="leg_l")
    # body: one bulky black box, the white throat on the front, the red patch under the tail
    g.box((0, -3, 5), (7, 3, 13), "body", part="body")
    g.paint((5, -3, 9), (7, 3, 13), "throat", of="body")
    g.paint((0, -2, 5), (1, 2, 6), "vent", of="body")
    # wings: slabs along the flanks
    g.box((1, -4, 7), (6, -4, 13), "body", part="wing_l")
    g.joint("wing_l", pivot=(5, -3.5, 13), parent="body")
    # tail: one block raised at the back
    g.box((-5, -2, 9), (-1, 2, 11), "body", part="tail")
    g.joint("tail", pivot=(0, 0.5, 10), rotate=(0, 20, 0), parent="body")
    # head: a black box on top of the body, the white cheeks in front
    g.box((3, -3, 14), (9, 3, 19), "body", part="head")
    g.paint((7, -3, 14), (9, 3, 16), "throat", of="head")
    g.paint((5, -3, 14), (9, -3, 15), "throat", of="head")
    g.joint("head", pivot=(5, 0.5, 14), rotate=(14, -4, -12), parent="body")
    # eye painted flat on the side of the head: a ring of orange skin around a round blue eye with a black pupil
    g.box((5, -3, 15), (8, -3, 18), "ring", part="head")
    g.box((6, -3, 16), (7, -3, 17), "eye", part="head")
    g.set(7, -3, 16, "body", part="head")
    # the huge bill: a deep base and a narrower front, orange, a small black tip, tilted up
    g.box((10, -2, 14), (13, 2, 18), "bill", part="beak")
    g.box((14, -1, 15), (17, 1, 18), "bill", part="beak")
    g.paint((17, -1, 15), (17, 1, 18), "body", of="beak")
    g.joint("beak", pivot=(10, 0.5, 16), rotate=(0, -10, 0), parent="head")
    g.mirror()
    # one wing lifted a little (the left, the camera side)
    g.joint("wing_l", pivot=(5, -3.5, 13), rotate=(-16, 0, 0), parent="body")
