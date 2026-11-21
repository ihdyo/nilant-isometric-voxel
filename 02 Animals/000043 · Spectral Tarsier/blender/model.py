"""000043 · Spectral Tarsier (Tarsius tarsier) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, ear, belly, finger, white, eye. Size: 22 x 13 x 22 voxels posed."""


def build(g):
    # compact upright body
    g.box((0, -3, 4), (7, 3, 13), "coat", part="body")
    g.paint((6, -2, 5), (7, 2, 11), "belly", of="body")
    # long leaping hind legs
    g.box((1, -4, 0), (5, -2, 6), "coat", part="leg_hl")
    g.paint((4, -4, 0), (6, -2, 0), "finger", of="leg_hl")
    g.joint("leg_hl", pivot=(3, -3, 6), parent="body")
    # slender grasping arms
    g.box((5, -4, 8), (8, -3, 12), "coat", part="arm_l")
    g.paint((7, -4, 8), (8, -3, 8), "finger", of="arm_l")
    g.joint("arm_l", pivot=(6.5, -3.5, 12), rotate=(12, 0, 0), parent="body")
    # long naked tail with furry tip
    g.box((-12, 0, 4), (0, 0, 4), "finger", part="tail")
    g.box((-12, -1, 3), (-9, 1, 5), "coat", part="tail")
    g.joint("tail", pivot=(0, 0, 4), rotate=(0, 12, 0), parent="body")
    # oversized head with huge golden eyes and bat-like ears
    g.box((0, -4, 13), (8, 4, 20), "coat", part="head")
    g.box((8, -3, 15), (8, -1, 18), "eye", part="head")
    g.set(8, -3, 18, "white", part="head")
    g.set(8, 0, 14, "finger", part="head")
    g.joint("head", pivot=(4, 0, 13), rotate=(4, -4, -16), parent="body")
    g.box((3, -6, 17), (5, -4, 21), "ear", part="ear_l")
    g.joint("ear_l", pivot=(4, -4, 18), rotate=(0, 0, 15), parent="head")
    g.mirror()
