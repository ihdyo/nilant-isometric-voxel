"""000046 · Malayan Tapir (Tapirus indicus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: dark, saddle, ear, nail, white, eye. Size: 42 x 16 x 22 voxels posed."""


def build(g):
    # plump rounded torso with iconic white saddle
    g.box((0, -6, 7), (23, 6, 19), "dark", part="body")
    g.paint((6, -6, 7), (16, 6, 19), "saddle", of="body")
    # sturdy black legs with pale hooves
    for leg, x in (("leg_hl", 2), ("leg_fl", 18)):
        g.box((x, -5, 0), (x + 2, -2, 7), "dark", part=leg)
        for y in (-5, -3):
            g.box((x + 2, y, 0), (x + 2, y, 0), "nail", part=leg)
        g.joint(leg, pivot=(x + 1, -3.5, 7), parent="body")
    # tiny stubby tail
    g.box((-1, -1, 12), (0, 1, 14), "dark", part="tail")
    g.joint("tail", pivot=(0, 0, 13), parent="body")
    # tapering head, flexible proboscis snout & white-tipped ears
    g.box((22, -4, 10), (31, 4, 18), "dark", part="head")
    g.set(28, -4, 15, "white", part="head")
    g.set(29, -4, 15, "eye", part="head")
    g.joint("head", pivot=(23, 0, 14), rotate=(4, 4, -10), parent="body")
    g.box((31, -2, 10), (34, 2, 13), "dark", part="snout")
    g.joint("snout", pivot=(31, 0, 12.5), rotate=(0, 16, 0), parent="head")
    g.box((23, -4, 18), (24, -3, 20), "dark", part="ear_l")
    g.paint((23, -4, 20), (24, -3, 20), "ear", of="ear_l")
    g.joint("ear_l", pivot=(23.5, -3.5, 18), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(19, -3.5, 7), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -3.5, 7), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(19, 3.5, 7), rotate=(0, 5, 0), parent="body")
