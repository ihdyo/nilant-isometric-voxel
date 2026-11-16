"""26-001 · Red Fox (Vulpes vulpes) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, white, dark, eye. Size: 32 x 14 x 23 voxels posed.
Personality: clever and sly. Pose: head turned to the camera and cocked, ears perked forward, tail raised, the front
left paw lifted mid-sneak. Expression: white eyes with the pupils to the inside, one brow slanting down to the
middle and the other raised, a crooked smirk, all painted flat on the face."""


def build(g):
    # body: one bulky box, white chest
    g.box((0, -4, 6), (13, 4, 12), "fur", part="body")
    g.paint((12, -3, 6), (13, 3, 9), "white", of="body")
    # legs: 3 x 3 pillars hinged under the body, black stockings
    for name, x in (("leg_hl", 1), ("leg_fl", 10)):
        g.box((x, -4, 0), (x + 2, -2, 5), "fur", part=name)
        g.box((x, -4, 0), (x + 2, -2, 2), "dark", part=name)
        g.joint(name, pivot=(x + 1.5, -3, 6), parent="body")
    # head: a big box stacked on the front of the body, white cheeks and jaw
    g.box((13, -5, 9), (20, 5, 17), "fur", part="head")
    g.paint((16, -5, 9), (20, 5, 11), "white", of="head")
    g.joint("head", pivot=(14, 0.5, 12), rotate=(8, -4, -16), parent="body")
    # face, painted flat on the front of the head: white eye with the pupil to the inside, a brow slanting down
    # towards the middle (sly)
    g.box((20, -4, 13), (20, -4, 14), "white", part="head")
    g.box((20, -3, 13), (20, -3, 14), "eye", part="head")
    g.box((20, -5, 16), (20, -4, 16), "dark", part="head")
    g.box((20, -3, 15), (20, -2, 15), "dark", part="head")
    # snout: orange bridge, white chin, black nose on its top front edge
    g.box((21, -2, 9), (23, 2, 12), "white", part="snout")
    g.paint((21, -2, 11), (23, 2, 12), "fur", of="snout")
    g.paint((23, -1, 12), (23, 1, 12), "dark", of="snout")
    g.joint("snout", pivot=(21, 0.5, 10.5), parent="head")
    # big ears with black tips, perked forward and splayed
    g.box((15, -5, 18), (16, -3, 20), "fur", part="ear_l")
    g.box((15, -5, 21), (16, -4, 21), "dark", part="ear_l")
    g.joint("ear_l", pivot=(15.5, -4, 18), rotate=(12, 10, 0), parent="head")
    # bushy tail in two blocks, raised, white tip
    g.box((-4, -2, 8), (-1, 2, 12), "fur", part="tail")
    g.joint("tail", pivot=(0, 0.5, 10), rotate=(0, 18, 8), parent="body")
    g.box((-7, -2, 8), (-5, 2, 12), "fur", part="tail_tip")
    g.box((-7, -2, 8), (-6, 2, 12), "white", part="tail_tip")
    g.joint("tail_tip", pivot=(-4, 0.5, 10), rotate=(0, 12, 0), parent="tail")
    g.mirror()
    # the sly look is lopsided: the right brow raised and level, a smirk rising on one side of the chin
    g.box((20, 2, 15), (20, 3, 15), "fur", part="head")
    g.box((20, 2, 16), (20, 5, 16), "dark", part="head")
    g.box((23, -1, 9), (23, 1, 9), "dark", part="snout")
    g.set(23, 2, 10, "dark", part="snout")
    # the front left paw lifted (sneaking); the other legs settle into the step
    g.joint("leg_fl", pivot=(11.5, -3, 6), rotate=(0, 24, 0), parent="body")
    g.joint("leg_fr", pivot=(11.5, 4, 6), rotate=(0, -6, 0), parent="body")
    g.joint("leg_hl", pivot=(2.5, -3, 6), rotate=(0, -8, 0), parent="body")
    g.joint("leg_hr", pivot=(2.5, 4, 6), rotate=(0, 6, 0), parent="body")
