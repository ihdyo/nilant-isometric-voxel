"""26-023 · European Rabbit (Oryctolagus cuniculus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, belly, tail, ear, nose, eye. Size: 18 x 11 x 21 voxels posed.
Personality: alert, jumpy and sweet. Pose: standing on all four feet, the back rising from the low rump to the chest
held up on long, thin front legs, slanted thighs on the flanks over long hind feet flat on the ground (one voxel high),
the head on the front of the chest turned to the camera, the two tall ears side by side, one bent forward, the cotton
tail showing. Expression: big dark eyes with a glint on the front corners of the face, a pink nose over a pale muzzle
and a little split lip, painted flat."""


def build(g):
    # body: the low rump at the back and the chest held up in front, one part; the pale belly underneath
    g.box((0, -3, 4), (5, 3, 9), "fur", part="body")
    g.box((6, -3, 6), (10, 3, 10), "fur", part="body")
    g.paint((1, -2, 4), (5, 2, 4), "belly", of="body")
    g.paint((6, -2, 6), (10, 2, 6), "belly", of="body")
    # cotton tail at the back of the rump
    g.box((-1, -1, 7), (-1, 1, 9), "tail", part="body")
    # hind legs: a thigh block on each flank (the upper part), slanted, and the long foot flat on the ground, one voxel
    # high, running forward from the heel (the lower part)
    g.box((0, -5, 1), (4, -4, 7), "fur", part="leg_hl")
    g.joint("leg_hl", pivot=(2.5, -3.5, 6), rotate=(0, -14, 0), parent="body")
    g.box((0, -5, 0), (7, -4, 0), "fur", part="shin_hl")
    g.paint((7, -5, 0), (7, -4, 0), "belly", of="shin_hl")
    g.joint("shin_hl", pivot=(1, -4.5, 1), rotate=(0, 14, 0), parent="leg_hl")
    # front legs: long and thin under the chest, pale paws
    g.box((9, -3, 0), (10, -2, 5), "fur", part="leg_fl")
    g.paint((9, -3, 0), (10, -2, 0), "belly", of="leg_fl")
    g.joint("leg_fl", pivot=(10, -2, 6), parent="body")
    # head: a box on the front of the chest, turned to the camera
    g.box((11, -3, 8), (15, 3, 13), "fur", part="head")
    g.joint("head", pivot=(11, 0.5, 10), rotate=(4, -4, -14), parent="body")
    # face, painted flat on the front: big dark eyes on the corners with a white glint, a pale muzzle, the pink nose
    # and the little split lip
    g.box((15, -3, 11), (15, -2, 12), "eye", part="head")
    g.set(15, -3, 12, "tail", part="head")
    g.paint((15, -2, 8), (15, 0, 9), "belly", of="head")
    g.paint((15, -1, 10), (15, 0, 10), "nose", of="head")
    g.set(15, 0, 9, "eye", part="head")
    # ears: two tall ears side by side on top of the head, the pink inside on the front
    g.box((12, -2, 14), (13, -1, 20), "fur", part="ear_l")
    g.paint((13, -2, 15), (13, -1, 20), "ear", of="ear_l")
    g.joint("ear_l", pivot=(13, -1, 14), rotate=(6, -6, 0), parent="head")
    g.mirror()
    # one ear bent forward
    g.joint("ear_r", pivot=(13, 2, 14), rotate=(-6, 20, 0), parent="head")
