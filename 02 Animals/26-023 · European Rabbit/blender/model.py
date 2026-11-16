"""26-023 · European Rabbit (Oryctolagus cuniculus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, belly, tail, ear, nose, eye. Size: 17 x 11 x 17 voxels posed.
Personality: alert, jumpy and sweet. Pose: crouched in a round loaf on all four feet, the long hind feet flat on the
ground, the big head turned to the camera, the ears standing tall with one bent forward, the cotton tail showing.
Expression: a big round eye with a glint, a pink nose and a little split lip, painted flat."""


def build(g):
    # body: a round loaf, higher over the haunches at the back, a step down to the shoulders; the pale belly
    g.box((0, -4, 1), (9, 4, 7), "fur", part="body")
    g.box((1, -3, 8), (6, 3, 8), "fur", part="body")
    g.paint((1, -3, 1), (9, 3, 1), "belly", of="body")
    g.paint((9, -2, 2), (9, 2, 5), "belly", of="body")
    # cotton tail at the back
    g.box((-1, -1, 4), (-1, 1, 6), "tail", part="body")
    # hind legs: a round thigh on each flank and a long foot flat on the ground beside the body
    g.box((1, -5, 1), (5, -5, 5), "fur", part="leg_hl")
    g.box((1, -5, 0), (7, -4, 0), "fur", part="leg_hl")
    g.joint("leg_hl", pivot=(3, -4.5, 3), parent="body")
    # front paws: short, under the chest
    g.box((8, -3, 0), (9, -2, 1), "fur", part="leg_fl")
    g.joint("leg_fl", pivot=(8.5, -2.5, 1.5), parent="body")
    # head: a big box on the front of the body, turned to the camera
    g.box((9, -3, 5), (14, 3, 10), "fur", part="head")
    g.joint("head", pivot=(9.5, 0.5, 6), rotate=(6, -4, -16), parent="body")
    # face, painted flat: big round eyes on the front corners with a white glint
    g.box((14, -3, 7), (14, -2, 8), "eye", part="head")
    g.set(14, -3, 8, "tail", part="head")
    # muzzle: pale, the pink nose on top, the little split lip below
    g.box((15, -1, 5), (15, 1, 7), "belly", part="muzzle")
    g.set(15, 0, 7, "nose", part="muzzle")
    g.set(15, 0, 6, "eye", part="muzzle")
    g.joint("muzzle", pivot=(15, 0.5, 6), parent="head")
    # ears: tall, standing up from the back of the head, the pink inside on the front
    g.box((10, -3, 11), (11, -2, 16), "fur", part="ear_l")
    g.paint((11, -3, 12), (11, -2, 16), "ear", of="ear_l")
    g.joint("ear_l", pivot=(10.5, -2.5, 11), rotate=(8, -6, 0), parent="head")
    g.mirror()
    # one ear bent forward
    g.joint("ear_r", pivot=(10.5, 3.5, 11), rotate=(-8, 26, 0), parent="head")
