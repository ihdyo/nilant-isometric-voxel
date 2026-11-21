"""000033 · Raccoon (Procyon lotor) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, mask, trim, dark, white, eye. Size: 34 x 14 x 18 voxels posed."""


def build(g):
    # rounded, slightly arched grizzled body
    g.box((1, -4, 5), (17, 4, 13), "coat", part="body")
    g.paint((3, -3, 12), (14, 3, 13), "dark", of="body")
    # legs with dark nimble paws
    for leg, x, h in (("leg_hl", 2, 6), ("leg_fl", 14, 5)):
        g.box((x, -4, 0), (x + 2, -2, h), "coat", part=leg)
        g.paint((x, -4, 0), (x + 2, -2, 1), "dark", of=leg)
        g.joint(leg, pivot=(x + 1, -3, h), parent="body")
    # ringed bushy tail
    g.box((-10, -2, 7), (0, 2, 10), "coat", part="tail")
    for x in (-10, -6, -2):
        g.paint((x, -2, 7), (x + 1, 2, 10), "mask", of="tail")
    g.joint("tail", pivot=(1, 0, 8.5), rotate=(0, -10, -6), parent="body")
    # masked head with white muzzle
    g.box((16, -4, 8), (23, 4, 15), "coat", part="head")
    g.box((22, -2, 8), (24, 2, 11), "trim", part="head")
    g.set(24, 0, 11, "mask", part="head")
    g.paint((23, -4, 11), (23, 4, 13), "mask", of="head")
    g.paint((23, -3, 14), (23, 3, 14), "trim", of="head")
    g.box((23, -3, 12), (23, -3, 12), "white", part="head")
    g.box((23, -2, 12), (23, -2, 12), "eye", part="head")
    g.joint("head", pivot=(17, 0, 11), rotate=(4, 3, -10), parent="body")
    g.box((17, -4, 15), (18, -2, 17), "coat", part="ear_l")
    g.paint((18, -4, 16), (18, -2, 17), "trim", of="ear_l")
    g.joint("ear_l", pivot=(17.5, -3, 15), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(15, -3, 5), rotate=(0, -12, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -3, 6), rotate=(0, 10, 0), parent="body")
    g.joint("leg_fr", pivot=(15, 3, 5), rotate=(0, 6, 0), parent="body")
