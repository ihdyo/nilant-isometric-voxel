"""000063 · North American Beaver (Castor canadensis) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, belly, tail, tooth, white, eye. Size: 32 x 13 x 15 voxels.
Personality: industrious and cheerful, tireless woodland architect. Pose: a sturdy waddle, broad flat paddle tail resting behind, holding a birch twig. Expression: cheerful dark eyes, chubby cheeks and two prominent orange front teeth."""


def build(g):
    # body: chunky waterproof chestnut torso
    g.box((9, -6, 3), (24, 6, 14), "coat", part="body")
    g.box((11, -5, 2), (23, 5, 4), "belly", part="body")
    # broad flat leathery paddle tail
    g.box((0, -4, 2), (9, 4, 3), "tail", part="tail")
    g.joint("tail", pivot=(9, 0, 3), rotate=(0, 6, 0), parent="body")
    # webbed hind feet and dexterous front paws
    g.box((11, -6, 0), (15, -3, 3), "tail", part="leg_hl")
    g.box((20, -6, 0), (23, -3, 4), "coat", part="leg_fl")
    g.joint("leg_hl", pivot=(13, -4.5, 3), parent="body")
    g.joint("leg_fl", pivot=(21.5, -4.5, 4), parent="body")
    # broad head with chubby cheeks and bright orange incisors
    g.box((23, -5, 5), (30, 5, 14), "coat", part="head")
    g.box((29, -4, 6), (31, 4, 9), "belly", part="head")
    g.box((31, -1, 4), (31, 1, 6), "tooth", part="head")
    g.set(31, 0, 9, "eye", part="head")
    g.box((27, -5, 10), (28, -5, 11), "white", part="head")
    g.box((28, -5, 10), (28, -5, 11), "eye", part="head")
    g.joint("head", pivot=(24, 0, 9), rotate=(4, -4, -8), parent="body")
    g.mirror()
