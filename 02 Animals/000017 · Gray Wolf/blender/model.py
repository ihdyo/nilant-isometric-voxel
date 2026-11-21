"""000017 · Gray Wolf (Canis lupus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, back, light, nose. Size: 37 x 13 x 23 voxels posed.
Personality: loyal and a little dramatic, the pack's singer. Pose: standing on long legs with knees, mid-step, the
thick neck ruff part of the body and the head straight on it (no neck: owner 2026-11-21, "remove the neck from the
wolf so it showing the body section to head only"), turned to the camera and a little up, the ears perked, the bushy tail
hanging low and curving; the howl lifts the whole head. Expression: calm dark eyes with a pale glint, painted flat."""


def build(g):
    # body: a long box on long legs, the dark saddle on top, the pale belly underneath; the thick ruff around the
    # shoulders is part of the body, a voxel wider and taller than it all round
    g.box((0, -5, 9), (15, 5, 17), "fur", part="body")
    g.paint((2, -4, 17), (13, 4, 17), "back", of="body")
    g.paint((2, -3, 9), (14, 3, 9), "light", of="body")
    g.box((11, -6, 9), (16, 6, 18), "fur", part="body")
    g.paint((16, -4, 9), (16, 4, 15), "light", of="body")
    g.paint((11, -5, 18), (14, 5, 18), "back", of="body")
    # legs: an upper leg and a shin each (long legs need knees), pale paws
    for leg, shin, x0, x1 in (("leg_hl", "shin_hl", 0, 3), ("leg_fl", "shin_fl", 12, 14)):
        g.box((x0, -5, 5), (x1, -3, 8), "fur", part=leg)
        g.box((x1 - 2, -5, 0), (x1, -3, 4), "fur", part=shin)
        g.box((x1 - 2, -5, 0), (x1, -3, 1), "light", part=shin)
        g.joint(leg, pivot=((x0 + x1 + 1) / 2, -3.5, 9), parent="body")
        g.joint(shin, pivot=(x1 - 0.5, -3.5, 5), parent=leg)
    # head: straight on the front of the ruff (no neck), pale cheeks
    g.box((17, -4, 12), (22, 4, 18), "fur", part="head")
    g.paint((20, -4, 12), (22, 4, 13), "light", of="head")
    g.joint("head", pivot=(17, 0.5, 15), rotate=(3, -6, -14), parent="body")
    # eyes painted flat: dark, with a pale glint on the top inner corner
    g.box((22, -3, 15), (22, -2, 16), "nose", part="head")
    g.set(22, -2, 16, "light", part="head")
    # snout: pale underneath, the black nose on its top front edge, a dark mouth line
    g.box((23, -2, 12), (26, 2, 15), "fur", part="snout")
    g.paint((23, -2, 12), (26, 2, 13), "light", of="snout")
    g.paint((26, -1, 15), (26, 1, 15), "nose", of="snout")
    g.box((26, -1, 12), (26, 1, 12), "nose", part="snout")
    g.joint("snout", pivot=(23, 0.5, 13.5), parent="head")
    # ears: pointed blocks with dark backs, perked
    g.box((18, -4, 19), (19, -2, 21), "fur", part="ear_l")
    g.paint((18, -4, 19), (18, -2, 21), "back", of="ear_l")
    g.joint("ear_l", pivot=(18.5, -3, 19), rotate=(8, -4, 0), parent="head")
    # bushy tail hanging low behind, a dark tip
    g.box((-5, -2, 12), (-1, 2, 15), "fur", part="tail")
    g.joint("tail", pivot=(-0.5, 0.5, 14), rotate=(0, -22, 10), parent="body")
    g.box((-9, -2, 12), (-6, 2, 15), "fur", part="tail_tip")
    g.paint((-9, -2, 12), (-8, 2, 15), "back", of="tail_tip")
    g.joint("tail_tip", pivot=(-5.5, 0.5, 13.5), rotate=(0, -10, 6), parent="tail")
    g.mirror()
    # mid-step: the front left paw forward with its knee folding, the hind right reaching, the others pushing back
    g.joint("leg_fl", pivot=(13.5, -3.5, 9), rotate=(0, -16, 0), parent="body")
    g.joint("shin_fl", pivot=(13.5, -3.5, 5), rotate=(0, 22, 0), parent="leg_fl")
    g.joint("leg_fr", pivot=(13.5, 4.5, 9), rotate=(0, 10, 0), parent="body")
    g.joint("leg_hl", pivot=(2, -3.5, 9), rotate=(0, 12, 0), parent="body")
    g.joint("shin_hl", pivot=(2.5, -3.5, 5), rotate=(0, -10, 0), parent="leg_hl")
    g.joint("leg_hr", pivot=(2, 4.5, 9), rotate=(0, -10, 0), parent="body")
    g.joint("ear_r", pivot=(18.5, 4, 19), rotate=(-12, 4, 0), parent="head")
