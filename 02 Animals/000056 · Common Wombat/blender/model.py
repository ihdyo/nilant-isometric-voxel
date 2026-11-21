"""000056 · Common Wombat (Vombatus ursinus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, shade, nose, ear, white, eye. Size: 30 x 15 x 17 voxels.
Personality: sturdy and stubborn, the cuddly tank of the bush. Pose: a low waddling stride, chunky head held up, broad black nose sniffing the air. Expression: round dark eyes and a tiny tucked smile beneath a big black nose."""


def build(g):
    # body: chunky barrel torso low to the ground with darker rump shield
    g.box((1, -7, 4), (21, 7, 15), "coat", part="body")
    g.box((0, -6, 5), (3, 6, 14), "shade", part="body")
    # four short stout legs with digging claws
    for leg, x in (("leg_hl", 3), ("leg_fl", 16)):
        g.box((x, -7, 0), (x + 3, -4, 4), "coat", part=leg)
        g.box((x + 3, -7, 0), (x + 4, -4, 1), "nose", part=leg)
        g.joint(leg, pivot=(x + 1.5, -5.5, 4), parent="body")
    # broad rounded head with big bare black nose and small rounded ears
    g.box((20, -6, 5), (28, 6, 14), "coat", part="head")
    g.box((28, -3, 7), (29, 3, 10), "nose", part="head")
    g.joint("head", pivot=(21, 0, 9), rotate=(4, -4, -8), parent="body")
    g.box((21, -6, 14), (23, -4, 16), "coat", part="ear_l")
    g.paint((22, -5, 14), (23, -5, 15), "ear", of="ear_l")
    g.joint("ear_l", pivot=(22, -5, 14), rotate=(0, 0, 12), parent="head")
    g.box((25, -6, 11), (26, -6, 12), "white", part="head")
    g.box((26, -6, 11), (26, -6, 12), "eye", part="head")
    g.mirror()
    g.joint("leg_fl", pivot=(17.5, -5.5, 4), rotate=(0, -10, 0), parent="body")
    g.joint("leg_hl", pivot=(4.5, -5.5, 4), rotate=(0, 10, 0), parent="body")
