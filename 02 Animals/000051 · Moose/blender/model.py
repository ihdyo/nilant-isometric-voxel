"""000051 · Moose (Alces alces) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, antler, leg, muzzle, white, eye. Size: 43 x 31 x 43 voxels.
Personality: dignified and tranquil, lord of the misty northern marsh. Pose: a high-stepping wade, broad palmate antlers tilted slightly forward, throat bell swaying. Expression: steady dark eyes under thick brow ridges and a long overhanging muzzle."""


def build(g):
    # body: tall humped shoulders and deep chest
    g.box((2, -7, 17), (26, 7, 30), "coat", part="body")
    g.box((17, -7, 30), (26, 7, 33), "coat", part="body")
    # long stilt legs with pale lower shins
    for leg, shin, x in (("leg_hl", "shin_hl", 3), ("leg_fl", "shin_fl", 21)):
        g.box((x, -6, 9), (x + 3, -3, 16), "coat", part=leg)
        g.box((x, -6, 0), (x + 3, -3, 8), "leg", part=shin)
        g.joint(leg, pivot=(x + 1.5, -4.5, 17), parent="body")
        g.joint(shin, pivot=(x + 1.5, -4.5, 9), parent=leg)
    # stubby tail
    g.box((0, -1, 25), (1, 1, 28), "coat", part="tail")
    g.joint("tail", pivot=(1, 0, 27), rotate=(-8, 0, 0), parent="body")
    # head with overhanging bulbous muzzle and dangling throat bell
    g.box((26, -5, 23), (38, 5, 33), "coat", part="head")
    g.box((36, -4, 22), (42, 4, 29), "muzzle", part="head")
    g.box((29, -2, 17), (32, 2, 22), "muzzle", part="head")
    g.joint("head", pivot=(27, 0, 28), rotate=(4, 5, -8), parent="body")
    # ears and broad palmate antlers
    g.box((27, -7, 33), (29, -5, 37), "coat", part="ear_l")
    g.joint("ear_l", pivot=(28, -5.5, 33), rotate=(0, 0, 18), parent="head")
    g.box((28, -14, 34), (34, -4, 41), "antler", part="antler_l")
    g.box((33, -15, 36), (36, -12, 42), "antler", part="antler_l")
    g.joint("antler_l", pivot=(29, -4, 34), rotate=(0, -6, 10), parent="head")
    # eyes and nostrils
    g.box((34, -5, 29), (35, -5, 30), "white", part="head")
    g.box((35, -5, 29), (35, -5, 30), "eye", part="head")
    g.set(42, -2, 26, "eye", part="head")
    g.mirror()
    g.joint("leg_fl", pivot=(22.5, -4.5, 17), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(4.5, -4.5, 17), rotate=(0, 8, 0), parent="body")
