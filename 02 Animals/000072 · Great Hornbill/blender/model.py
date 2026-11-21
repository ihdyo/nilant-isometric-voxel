"""000072 · Great Hornbill (Buceros bicornis) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: plumage, neck, casque, trim, eye. Size: 31 x 11 x 33 voxels.
Personality: majestic and resonant, trumpet-voiced guardian of the rainforest canopy. Pose: perched on a high bough, huge yellow casque bill held proudly, banded tail hanging down. Expression: striking ruby-red eye set in a black facial mask behind an enormous golden bill."""


def build(g):
    # body: glossy black torso and white-banded tail
    g.box((7, -5, 11), (18, 5, 23), "plumage", part="body")
    g.box((0, -3, 2), (8, 3, 12), "neck", part="tail")
    g.box((2, -3, 5), (5, 3, 7), "trim", part="tail")
    g.joint("tail", pivot=(8, 0, 12), rotate=(0, 12, 0), parent="body")
    g.box((11, -4, 0), (13, -2, 11), "trim", part="leg_l")
    g.joint("leg_l", pivot=(12, -3, 11), parent="body")
    # golden-yellow neck, black-masked head, and huge yellow casque bill
    g.box((11, -4, 23), (18, 4, 31), "neck", part="head")
    g.box((15, -4, 26), (19, 4, 30), "plumage", part="head")
    g.box((19, -2, 25), (30, 2, 29), "casque", part="head")
    g.box((18, -2, 29), (26, 2, 32), "casque", part="head")
    g.box((25, -2, 29), (26, 2, 32), "trim", part="head")
    g.set(17, -4, 28, "eye", part="head")
    g.joint("head", pivot=(14, 0, 23), rotate=(4, 4, -10), parent="body")
    g.mirror()
