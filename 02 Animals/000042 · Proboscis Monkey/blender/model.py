"""000042 · Proboscis Monkey (Nasalis larvatus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, face, pants, belly, white, eye. Size: 34 x 14 x 24 voxels posed."""


def build(g):
    # torso with cinnamon mantle and pale pot-belly
    g.box((1, -4, 7), (15, 4, 16), "coat", part="body")
    g.paint((4, -3, 7), (14, 3, 12), "belly", of="body")
    # pale grey limbs ("white pants")
    for leg, x in (("leg_hl", 2), ("leg_fl", 12)):
        g.box((x, -4, 0), (x + 2, -2, 7), "pants", part=leg)
        g.joint(leg, pivot=(x + 1, -3, 7), parent="body")
    # long white tail
    g.box((-12, -1, 11), (0, 1, 13), "pants", part="tail")
    g.joint("tail", pivot=(1, 0, 12), rotate=(0, 14, 0), parent="body")
    # head with cinnamon cap, pinkish face and famous pendulous nose
    g.box((13, -4, 15), (19, 4, 22), "coat", part="head")
    g.paint((19, -3, 15), (19, 3, 20), "face", of="head")
    g.set(19, -2, 19, "white", part="head")
    g.set(19, -1, 19, "eye", part="head")
    g.joint("head", pivot=(14, 0, 16), rotate=(4, 3, -10), parent="body")
    g.box((20, -1, 14), (22, 1, 19), "face", part="nose")
    g.joint("nose", pivot=(20, 0, 18), parent="head")
    g.mirror()
    g.joint("leg_fl", pivot=(13, -3, 7), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(3, -3, 7), rotate=(0, 8, 0), parent="body")
    g.joint("leg_fr", pivot=(13, 3, 7), rotate=(0, 6, 0), parent="body")
