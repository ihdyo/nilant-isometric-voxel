"""000065 · Snowy Owl (Bubo scandiacus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: plumage, bar, beak, iris, eye. Size: 16 x 13 x 26 voxels.
Personality: serene and watchful, silent ghost of the Arctic tundra. Pose: a poised upright perch, round head swivelled toward the camera, feathered toes gripping. Expression: huge glowing golden eyes framed by a fluffy white facial disc."""


def build(g):
    # body: compact upright owl torso and folded wings
    g.box((3, -5, 4), (13, 5, 17), "plumage", part="body")
    g.box((3, -6, 3), (11, -5, 16), "plumage", part="wing_l")
    g.paint((4, -6, 4), (10, -6, 14), "bar", of="wing_l")
    g.joint("wing_l", pivot=(7, -5.5, 15), parent="body")
    # tail and feathered feet
    g.box((0, -3, 2), (4, 3, 6), "plumage", part="tail")
    g.joint("tail", pivot=(4, 0, 5), rotate=(0, 12, 0), parent="body")
    g.box((7, -4, 0), (10, -2, 4), "plumage", part="leg_l")
    g.joint("leg_l", pivot=(8.5, -3, 4), parent="body")
    # round head with large expressive eyes and neat hooked beak
    g.box((4, -5, 17), (13, 5, 25), "plumage", part="head")
    g.box((13, -3, 20), (13, -2, 22), "iris", part="head")
    g.set(13, -2, 21, "eye", part="head")
    g.box((13, -1, 18), (15, 1, 20), "beak", part="head")
    g.joint("head", pivot=(8.5, 0, 17), rotate=(5, 0, -16), parent="body")
    g.mirror()
