"""000007 · Koala (Phascolarctos cinereus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, white, nose, eye, paw. Size: 23 x 22 x 21 voxels posed.
Personality: sleepy and cuddly. Pose: A careful stride on all four feet, the big head turned to the camera, the ears
out. Expression: eyes closed in a sleepy curve and a tiny smile under the big nose, painted flat on the face."""


def build(g):
    # body: a stocky box on short legs, the white belly underneath and a white chest under the chin
    g.box((0, -5, 6), (12, 5, 14), "fur", part="body")
    g.paint((1, -4, 6), (11, 4, 6), "white", of="body")
    g.paint((12, -3, 6), (12, 3, 9), "white", of="body")
    # legs: four short, thick pillars, dark claws on the front of each paw
    for leg, x in (("leg_hl", 1), ("leg_fl", 9)):
        g.box((x, -5, 0), (x + 2, -3, 5), "fur", part=leg)
        g.box((x + 2, -5, 0), (x + 2, -3, 0), "paw", part=leg)
        g.joint(leg, pivot=(x + 1.5, -3.5, 6), parent="body")
    # head: a big box, wider than the body, held up on its front top, drowsily tilted
    g.box((12, -6, 10), (19, 6, 18), "fur", part="head")
    g.joint("head", pivot=(12, 0.5, 13), rotate=(4, 6, -14), parent="body")
    # sleepy closed eyes painted flat on the face: a dark curve, the ends higher than the middle
    g.set(19, -5, 15, "eye", part="head")
    g.box((19, -4, 14), (19, -3, 14), "eye", part="head")
    g.set(19, -2, 15, "eye", part="head")
    # a tiny smile painted under the nose
    g.box((19, -1, 10), (19, 0, 10), "nose", part="head")
    # the big dark nose block in the middle of the face
    g.box((20, -1, 11), (21, 1, 15), "nose", part="nose")
    g.joint("nose", pivot=(20, 0.5, 13), parent="head")
    # huge round ears sticking out on the sides, set into the head: grey rim, white fluffy front, tipped out
    g.box((14, -10, 14), (16, -6, 20), "fur", part="ear_l")
    g.paint((16, -9, 15), (16, -7, 19), "white", of="ear_l")
    g.paint((14, -10, 15), (16, -10, 19), "white", of="ear_l")
    g.joint("ear_l", pivot=(15, -5.5, 17), rotate=(12, 6, 0), parent="head")
    g.mirror()
    # a slow amble: the front left paw reaching forward, the hind left pushing back, the right side the other way
    g.joint("leg_fl", pivot=(10.5, -3.5, 6), rotate=(0, -18, 0), parent="body")
    g.joint("leg_fr", pivot=(10.5, 4.5, 6), rotate=(0, 12, 0), parent="body")
    g.joint("leg_hl", pivot=(2.5, -3.5, 6), rotate=(0, 14, 0), parent="body")
    g.joint("leg_hr", pivot=(2.5, 4.5, 6), rotate=(0, -12, 0), parent="body")
