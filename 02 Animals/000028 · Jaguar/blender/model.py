"""000028 · Jaguar (Panthera onca) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, rosette, belly, muzzle, white, eye. Size: 42 x 16 x 23 voxels posed."""


def build(g):
    # stocky muscular body
    g.box((1, -5, 9), (22, 5, 18), "coat", part="body")
    g.paint((2, -4, 9), (21, 4, 10), "belly", of="body")
    for x, y in ((4, -5), (10, -5), (16, -5), (6, 5), (12, 5), (18, 5)):
        g.box((x, y, 13), (x + 2, y, 15), "rosette", part="body")
        g.set(x + 1, y, 14, "coat", part="body")
    # thick pillar-like feline legs
    for leg, shin, x in (("leg_hl", "shin_hl", 2), ("leg_fl", "shin_fl", 17)):
        g.box((x, -5, 5), (x + 3, -2, 9), "coat", part=leg)
        g.box((x, -5, 0), (x + 3, -2, 4), "coat", part=shin)
        g.joint(leg, pivot=(x + 2, -3.5, 9), parent="body")
        g.joint(shin, pivot=(x + 2, -3.5, 5), parent=leg)
    # sturdy tail
    g.box((-11, -1, 12), (0, 1, 14), "coat", part="tail")
    g.paint((-11, -1, 12), (-9, 1, 14), "rosette", of="tail")
    g.joint("tail", pivot=(1, 0, 13), rotate=(0, 16, -8), parent="body")
    # broad powerful head
    g.box((21, -5, 13), (29, 5, 22), "coat", part="head")
    g.box((28, -3, 13), (30, 3, 16), "muzzle", part="head")
    g.paint((27, -3, 13), (29, 3, 14), "belly", of="head")
    g.box((29, -4, 18), (29, -4, 19), "white", part="head")
    g.box((29, -3, 18), (29, -3, 19), "eye", part="head")
    g.joint("head", pivot=(22, 0, 17), rotate=(4, 3, -10), parent="body")
    g.box((23, -5, 22), (24, -3, 23), "coat", part="ear_l")
    g.joint("ear_l", pivot=(23.5, -4, 22), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(19, -3.5, 9), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(4, -3.5, 9), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(19, 3.5, 9), rotate=(0, 5, 0), parent="body")
    g.joint("shin_fl", pivot=(19, -3.5, 5), rotate=(0, 12, 0), parent="leg_fl")
    g.joint("shin_hl", pivot=(4, -3.5, 5), rotate=(0, -8, 0), parent="leg_hl")
