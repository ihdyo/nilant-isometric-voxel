"""000068 · Common Kingfisher (Alcedo atthis) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: back, belly, throat, beak, foot. Size: 20 x 7 x 18 voxels.
Personality: focused and vibrant, a living sapphire darting over the stream. Pose: perched intently on an overhanging twig, body compact, long dagger beak aimed slightly down. Expression: sharp dark eyes locked onto the water surface below."""


def build(g):
    # body: compact jewel-toned torso with vivid rufous belly
    g.box((3, -3, 3), (11, 3, 11), "back", part="body")
    g.box((7, -3, 3), (12, 3, 9), "belly", part="body")
    g.box((9, -3, 9), (12, 3, 11), "throat", part="body")
    g.box((1, -2, 2), (4, 2, 4), "back", part="tail")
    g.joint("tail", pivot=(4, 0, 4), rotate=(0, 16, 0), parent="body")
    g.box((6, -2, 0), (8, -1, 3), "foot", part="leg_l")
    g.joint("leg_l", pivot=(7, -1.5, 3), parent="body")
    # large head and long straight dagger bill
    g.box((5, -3, 11), (12, 3, 17), "back", part="head")
    g.box((8, -3, 12), (11, -3, 14), "belly", part="head")
    g.box((12, -1, 13), (20, 1, 14), "beak", part="head")
    g.set(10, -3, 15, "eye", part="head")
    g.joint("head", pivot=(8.5, 0, 11), rotate=(3, 12, -10), parent="body")
    g.mirror()
