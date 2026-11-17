"""26-006 · American Flamingo (Phoenicopterus ruber) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: pink, light, black, bill, legs, feet, eye. Size: 16 x 11 x 34 voxels posed.
Personality: elegant and a little snooty. Pose: standing on one leg, the other (the camera side) lifted and bent at
the knee with the toes curled down, both legs built the same (an upper and a lower part on a webbed foot one voxel
thick) so it can walk on them, a long straight neck rising from the front of a bulky body, chin up, the big bill bent
down, wings lifted at the back. Expression: a half-lidded amber eye, the pink lid painted over its top half."""


def foot(g, part, cx, cy, z, d=1):
    """A small webbed flamingo foot, one voxel thick, 3 x 3: the heel at cx - d, the web under the leg and three short
    toes towards +X (d = 1) or, folded back, towards -X (d = -1). Both feet are this one shape (owner, 2026-11-17: the
    5-wide foot was too big)."""
    g.set(cx - d, cy, z, "feet", part=part)
    g.box((cx, cy - 1, z), (cx, cy + 1, z), "feet", part=part)
    for dy in (-1, 0, 1):
        g.set(cx + d, cy + dy, z, "feet", part=part)


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
    # legs, both the same: a thin pillar in two parts, the upper leg and the lower leg hinged at the knee (the joint
    # that bends backwards), on a webbed foot, so the flamingo can walk on them
    for side, y in (("l", -2), ("r", 2)):
        g.box((6, y, 6), (6, y, 11), "legs", part=f"leg_{side}")
        g.joint(f"leg_{side}", pivot=(6.5, y + 0.5, 12), parent="body")
        g.box((6, y, 1), (6, y, 5), "legs", part=f"shin_{side}")
        g.joint(f"shin_{side}", pivot=(6.5, y + 0.5, 6), parent=f"leg_{side}")
        foot(g, f"foot_{side}", 6, y, 0)
        g.joint(f"foot_{side}", pivot=(6.5, y + 0.5, 1), parent=f"shin_{side}")
    # standing on the right leg, its foot turned out a little; the left leg (the camera side) lifted and bent: the
    # knee swung forward, the lower leg folded back, the toes curled down
    g.joint("foot_r", pivot=(6.5, 2.5, 1), rotate=(0, 0, 8), parent="shin_r")
    g.joint("leg_l", pivot=(6.5, -1.5, 12), rotate=(0, -38, 0), parent="body")
    g.joint("shin_l", pivot=(6.5, -1.5, 6), rotate=(0, 40, 0), parent="leg_l")
    g.joint("foot_l", pivot=(6.5, -1.5, 1), rotate=(0, 34, 0), parent="shin_l")
