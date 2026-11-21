"""000059 · Brown-throated Sloth (Bradypus variegatus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, face, stripe, claw, eye. Size: 22 x 15 x 26 voxels.
Personality: blissfully unhurried, smiling zen master of the treetops. Pose: a cozy seated hug pose with long arms reaching forward and hooked claws curved inward. Expression: a permanent gentle smile and dark bandit-mask eye stripes on a pale cream face."""


def build(g):
    # body: cozy rounded torso seated upright
    g.box((2, -6, 3), (14, 6, 18), "coat", part="body")
    g.box((0, -2, 4), (2, 2, 7), "coat", part="tail")
    # long hugging arms and hind legs with three curved hook claws
    g.box((8, -7, 13), (19, -5, 17), "coat", part="arm_l")
    g.box((19, -7, 11), (21, -5, 16), "claw", part="arm_l")
    g.joint("arm_l", pivot=(10, -6, 15), rotate=(0, -12, 16), parent="body")
    g.box((7, -7, 2), (17, -4, 6), "coat", part="leg_hl")
    g.box((17, -7, 1), (19, -4, 4), "claw", part="leg_hl")
    g.joint("leg_hl", pivot=(9, -5.5, 4), rotate=(0, 0, 12), parent="body")
    # round head with pale cream face mask, dark eye stripes, and gentle smile
    g.box((5, -5, 18), (15, 5, 26), "coat", part="head")
    g.box((13, -4, 19), (15, 4, 25), "face", part="head")
    g.box((15, -4, 22), (15, -2, 23), "stripe", part="head")
    g.set(15, -2, 22, "eye", part="head")
    g.set(15, 0, 21, "eye", part="head")
    g.set(15, -2, 20, "stripe", part="head")
    g.set(15, -1, 19, "stripe", part="head")
    g.joint("head", pivot=(10, 0, 18), rotate=(6, 4, -12), parent="body")
    g.mirror()
