"""000073 · Southern Cassowary (Casuarius casuarius) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: plumage, neck, wattle, casque, leg. Size: 29 x 15 x 51 voxels.
Personality: bold and prehistoric, living dinosaur of the tropical rainforest. Pose: a powerful forest stride, helmet casque held high, twin crimson wattles swinging. Expression: fierce dark eyes above a vivid cobalt-blue neck and straight dark beak."""


def build(g):
    # body: shaggy drooping black plumage
    g.box((2, -6, 16), (22, 6, 30), "plumage", part="body")
    g.box((3, -7, 14), (21, 7, 17), "plumage", part="body")
    # thick dinosaur-like legs
    g.box((10, -5, 0), (13, -2, 16), "leg", part="leg_l")
    g.box((10, -5, 0), (16, -2, 1), "leg", part="leg_l")
    g.joint("leg_l", pivot=(11.5, -3.5, 16), parent="body")
    # vivid cobalt-blue neck, crimson wattles, and tall helmet casque
    g.box((19, -3, 28), (24, 3, 39), "neck", part="neck")
    g.box((23, -2, 26), (25, -1, 31), "wattle", part="wattle_l")
    g.joint("neck", pivot=(21, 0, 28), parent="body")
    g.joint("wattle_l", pivot=(24, -1.5, 31), rotate=(0, 0, 8), parent="neck")
    g.box((19, -3, 39), (26, 3, 44), "neck", part="head")
    g.box((26, -1, 39), (30, 1, 41), "plumage", part="head")
    g.box((20, -2, 44), (24, 2, 50), "casque", part="head")
    g.set(24, -3, 42, "plumage", part="head")
    g.joint("head", pivot=(22, 0, 39), rotate=(4, 4, -10), parent="neck")
    g.mirror()
    g.joint("leg_l", pivot=(11.5, -3.5, 16), rotate=(0, -10, 0), parent="body")
