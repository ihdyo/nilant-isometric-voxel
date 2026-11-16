"""26-006 · American Flamingo (Phoenicopterus ruber) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: pink, light, black, bill, legs, feet, eye. Size: 18 x 11 x 34 voxels posed.
Personality: elegant and a little snooty. Pose: standing on one leg, the other folded up and tucked back under the
body on the camera side, a long straight neck rising from the front of a bulky body, chin up, the big bill bent down,
wings lifted at the back, a webbed foot one voxel thick on the ground. Expression: a half-lidded amber eye, the pink lid painted
over its top half."""


def foot(g, part, cx, cy, z):
    """A webbed flamingo foot, one voxel thick: the heel under the leg, the web spreading forward to three toes."""
    g.set(cx - 1, cy, z, "feet", part=part)
    g.box((cx, cy - 1, z), (cx, cy + 1, z), "feet", part=part)
    g.box((cx + 1, cy - 2, z), (cx + 1, cy + 2, z), "feet", part=part)
    for dy in (-2, 0, 2):
        g.set(cx + 2, cy + dy, z, "feet", part=part)


def build(g):
    # body: one bulky box
    g.box((0, -4, 12), (10, 4, 18), "pink", part="body")
    # wings: slabs along the flanks, black flight feathers at the back, the rear lifted
    g.box((0, -5, 13), (8, -5, 18), "pink", part="wing_l")
    g.paint((0, -5, 13), (2, -5, 18), "black", of="wing_l")
    g.joint("wing_l", pivot=(8, -4.5, 18), rotate=(0, 14, 0), parent="body")
    # neck: a long straight column rising from the front of the body, leaning back a little
    g.box((8, -1, 19), (9, 1, 28), "light", part="neck")
    g.joint("neck", pivot=(8.5, 0.5, 18.5), rotate=(0, -6, 0), parent="body")
    # head: a box on the neck, chin up and cocked
    g.box((7, -2, 29), (12, 2, 32), "light", part="head")
    g.joint("head", pivot=(9, 0.5, 29), rotate=(10, -10, -6), parent="neck")
    # eye painted flat on the side of the head: amber with a black pupil at the front, the pink lid over its top half
    g.box((10, -2, 30), (11, -2, 31), "eye", part="head")
    g.set(11, -2, 30, "black", part="head")
    g.box((10, -2, 31), (11, -2, 31), "pink", part="head")
    g.set(9, -2, 31, "pink", part="head")
    # the big bill: pale base, the black tip hooked down
    g.box((13, -1, 29), (15, 1, 31), "bill", part="beak")
    g.box((15, -1, 27), (16, 1, 29), "black", part="beak")
    g.joint("beak", pivot=(13, 0.5, 30.5), rotate=(0, 24, 0), parent="head")
    g.mirror()
    # standing leg (right): a thin straight pillar on a webbed foot
    g.box((6, 2, 1), (6, 2, 11), "legs", part="leg_r")
    g.joint("leg_r", pivot=(6.5, 2.5, 12), parent="body")
    foot(g, "foot_r", 6, 2, 0)
    g.joint("foot_r", pivot=(6.5, 2.5, 1), rotate=(0, 0, 8), parent="leg_r")
    # folded leg (left, the camera side): the shin hangs from the body, the foot runs back from the ankle, the
    # whole leg swung back so the foot tucks up under the tail; the webbed foot folded flat at its end
    g.box((6, -2, 7), (6, -2, 11), "legs", part="leg_l")
    g.box((1, -2, 7), (5, -2, 7), "legs", part="leg_l")
    g.joint("leg_l", pivot=(6.5, -1.5, 12), rotate=(0, 28, 0), parent="body")
    g.box((-1, -3, 7), (0, -1, 7), "feet", part="foot_l")
    g.joint("foot_l", pivot=(0.5, -1.5, 7.5), parent="leg_l")
