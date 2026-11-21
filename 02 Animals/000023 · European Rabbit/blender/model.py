"""000023 · European Rabbit (Oryctolagus cuniculus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, belly, tail, ear, nose, eye. Size: 17 x 9 x 19 voxels posed.
Personality: alert, jumpy and sweet. Pose: crouched on all four feet, ready to hop: one block of a body (owner
2026-11-21: "1 block body instead of squiggly body"), a small slab thigh on each flank set into the body with one voxel
showing on the side and its hinge inside (the block-game rabbit's haunch, owner: "inside and side"), the long hind
foot flat on the ground under it (the lower part, hinged at the heel), thin front legs starting beside the chest, the
head on the front of the body turned to the camera, the two tall ears side by side, one tipped back, the cotton tail
showing. Expression: big dark eyes with a glint on the front corners of the face, a pink nose over a pale muzzle and
a little split lip, painted flat."""


def build(g):
    # body: one block, the pale belly underneath, the cotton tail at the back
    g.box((0, -3, 3), (10, 3, 8), "fur", part="body")
    g.paint((1, -2, 3), (9, 2, 3), "belly", of="body")
    g.box((-1, -1, 6), (-1, 1, 8), "tail", part="body")
    # hind legs: the thigh a slab two voxels wide on each flank, one voxel inside the body and one showing on its
    # side, hinged inside (the upper part); the long foot flat on the ground under it, one voxel high, running
    # forward from the heel (the lower part)
    g.box((0, -4, 2), (4, -3, 6), "fur", part="leg_hl")
    g.joint("leg_hl", pivot=(2.5, -2.5, 5), parent="body")
    g.box((-1, -4, 0), (5, -3, 0), "fur", part="shin_hl")
    g.box((-1, -4, 1), (0, -3, 1), "fur", part="shin_hl")
    g.paint((5, -4, 0), (5, -3, 0), "belly", of="shin_hl")
    g.joint("shin_hl", pivot=(0, -3.5, 1.5), parent="leg_hl")
    # front legs: thin, starting beside the chest (on the flank, not under it), pale paws
    g.box((8, -4, 0), (9, -4, 6), "fur", part="leg_fl")
    g.paint((8, -4, 0), (9, -4, 0), "belly", of="leg_fl")
    g.joint("leg_fl", pivot=(8.5, -3.5, 6), parent="body")
    # head: a box on the front of the body, above the chest
    g.box((10, -3, 6), (14, 3, 11), "fur", part="head")
    g.joint("head", pivot=(10.5, 0.5, 8), rotate=(3, 4, -14), parent="body")
    # face, painted flat on the front: big dark eyes on the corners with a white glint, a pale muzzle, the pink nose
    # and the little split lip
    g.box((14, -3, 9), (14, -2, 10), "eye", part="head")
    g.set(14, -3, 10, "tail", part="head")
    g.paint((14, -2, 6), (14, 0, 7), "belly", of="head")
    g.paint((14, -1, 8), (14, 0, 8), "nose", of="head")
    g.set(14, 0, 7, "eye", part="head")
    # ears: two tall ears side by side on top of the head, the pink inside on the front
    g.box((11, -2, 12), (12, -1, 18), "fur", part="ear_l")
    g.paint((12, -2, 13), (12, -1, 18), "ear", of="ear_l")
    g.joint("ear_l", pivot=(12, -1, 12), rotate=(6, -4, 0), parent="head")
    g.mirror()
    # one ear tipped back; a crouch with the front paws a little apart
    g.joint("ear_r", pivot=(12, 2, 12), rotate=(-8, -16, 0), parent="head")
    g.joint("leg_fl", pivot=(8.5, -3.5, 6), rotate=(0, -8, 0), parent="body")
    g.joint("leg_fr", pivot=(8.5, 4.5, 6), rotate=(0, 6, 0), parent="body")
