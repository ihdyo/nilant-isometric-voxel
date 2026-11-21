"""000064 · Bald Eagle (Haliaeetus leucocephalus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: plumage, head, beak, iris, eye. Size: 21 x 13 x 30 voxels.
Personality: commanding and keen-eyed, sovereign of the open sky. Pose: a proud perched stance with chest puffed, wings folded crisply, head turned sharply. Expression: fierce golden-yellow eyes under a prominent white brow ridge and heavy hooked beak."""


def build(g):
    # body: broad dark-chocolate chest and folded wings
    g.box((6, -5, 8), (16, 5, 22), "plumage", part="body")
    g.box((6, -6, 7), (14, -5, 21), "plumage", part="wing_l")
    g.joint("wing_l", pivot=(10, -5.5, 20), rotate=(0, 4, 6), parent="body")
    # snow-white wedge tail
    g.box((0, -3, 4), (7, 3, 10), "head", part="tail")
    g.joint("tail", pivot=(7, 0, 9), rotate=(0, 14, 0), parent="body")
    # yellow legs and curved talons
    g.box((10, -4, 2), (12, -2, 8), "beak", part="leg_l")
    g.box((10, -5, 0), (14, -1, 1), "beak", part="leg_l")
    g.set(14, -4, 0, "eye", part="leg_l")
    g.joint("leg_l", pivot=(11, -3, 8), parent="body")
    # snow-white head and heavy hooked golden beak
    g.box((8, -4, 22), (16, 4, 29), "head", part="head")
    g.box((16, -2, 23), (20, 2, 26), "beak", part="head")
    g.box((20, -1, 22), (20, 1, 25), "beak", part="head")
    g.box((13, -4, 26), (14, -4, 27), "iris", part="head")
    g.set(14, -4, 26, "eye", part="head")
    g.joint("head", pivot=(12, 0, 22), rotate=(4, 4, -14), parent="body")
    g.mirror()
