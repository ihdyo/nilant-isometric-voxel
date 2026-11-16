"""26-017 · Gray Wolf (Canis lupus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, back, light, nose. Size: 29 x 15 x 26 voxels posed.
Personality: loyal and a little dramatic, the pack's singer. Pose: sitting on its haunches, the back sloping up from
the hips to the shoulders, the front legs straight, the head thrown back to howl at the sky, the ears laid back, the
bushy tail curled round on the ground. Expression: eyes shut tight and a round open mouth, mid-howl, painted flat."""


def build(g):
    # body: the haunches sitting on the ground, the dark saddle on top
    g.box((0, -6, 0), (9, 6, 7), "fur", part="body")
    g.paint((1, -5, 7), (8, 5, 7), "back", of="body")
    # hind legs: a big thigh on each flank and a long foot forward on the ground
    g.box((1, -7, 0), (8, -7, 6), "fur", part="leg_hl")
    g.box((7, -7, 0), (11, -6, 1), "fur", part="leg_hl")
    g.joint("leg_hl", pivot=(4.5, -6.5, 4), parent="body")
    # torso: rising from the hips to the shoulders, the dark saddle on its back, the pale chest on its front
    g.box((3, -5, 3), (17, 5, 11), "fur", part="torso")
    g.paint((3, -4, 11), (14, 4, 11), "back", of="torso")
    g.paint((17, -3, 4), (17, 3, 10), "light", of="torso")
    g.joint("torso", pivot=(3, 0.5, 3), rotate=(0, -34, 0), parent="body")
    # front legs: straight pillars from the chest down to the ground, pale paws
    g.box((12, -5, 0), (14, -3, 12), "fur", part="leg_fl")
    g.box((12, -5, 0), (14, -3, 1), "light", part="leg_fl")
    g.joint("leg_fl", pivot=(13, -4, 12.5), parent="body")
    # head: on the front of the shoulders, thrown back further to howl and turned to the camera; pale cheeks
    g.box((15, -5, 9), (22, 5, 15), "fur", part="head")
    g.paint((20, -5, 9), (22, 5, 10), "light", of="head")
    g.joint("head", pivot=(16, 0.5, 10), rotate=(6, -12, -12), parent="torso")
    # eyes shut tight, painted flat: dark lines on the front of the head
    g.box((22, -4, 13), (22, -2, 13), "nose", part="head")
    # snout: pale underneath, the black nose on its top front edge, the round open mouth painted on its front
    g.box((23, -2, 9), (26, 2, 12), "fur", part="snout")
    g.paint((23, -2, 9), (26, 2, 10), "light", of="snout")
    g.paint((26, -1, 12), (26, 1, 12), "nose", of="snout")
    g.box((26, -1, 9), (26, 1, 10), "nose", part="snout")
    g.joint("snout", pivot=(23, 0.5, 10.5), parent="head")
    # ears: pointed blocks with dark backs, laid back
    g.box((16, -5, 16), (17, -3, 18), "fur", part="ear_l")
    g.paint((16, -5, 16), (16, -3, 18), "back", of="ear_l")
    g.joint("ear_l", pivot=(16.5, -4, 16), rotate=(10, -14, 0), parent="head")
    # bushy tail lying on the ground, curled round towards the camera, a dark tip
    g.box((-6, -2, 0), (-1, 2, 2), "fur", part="tail")
    g.joint("tail", pivot=(-0.5, 0.5, 1), rotate=(0, 0, 18), parent="body")
    g.box((-10, -2, 0), (-7, 2, 2), "fur", part="tail_tip")
    g.paint((-10, -2, 0), (-9, 2, 2), "back", of="tail_tip")
    g.joint("tail_tip", pivot=(-6.5, 0.5, 1), rotate=(0, 0, 30), parent="tail")
    g.mirror()
