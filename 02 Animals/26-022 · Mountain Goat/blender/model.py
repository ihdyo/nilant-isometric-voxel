"""26-022 · Mountain Goat (Oreamnos americanus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, shade, horn, nose. Size: 31 x 13 x 29 voxels posed.
Personality: brave, sure-footed and a bit stubborn. Pose: standing square with one front hoof raised as if stepping
up a ledge, the bearded chin lifted, the head turned to the camera. Expression: calm dark eyes under a level brow and a
small smile, painted flat."""


def build(g):
    # legs: thick pillars, shaggy shading at the top, black hooves
    for leg, shin, x in (("leg_hl", "shin_hl", 2), ("leg_fl", "shin_fl", 14)):
        g.box((x, -5, 6), (x + 3, -2, 10), "coat", part=leg)
        g.box((x, -5, 0), (x + 3, -2, 5), "coat", part=shin)
        g.box((x, -5, 0), (x + 3, -2, 1), "horn", part=shin)
        g.paint((x, -5, 2), (x + 3, -5, 4), "shade", of=shin)
        g.joint(leg, pivot=(x + 2, -3.5, 11), parent="body")
        g.joint(shin, pivot=(x + 2, -3.5, 6), parent=leg)
    # body: one shaggy box, the hump of thick fur over the shoulders, shaded underneath; a stub of a tail
    g.box((0, -6, 11), (19, 6, 20), "coat", part="body")
    g.box((12, -5, 21), (18, 5, 22), "coat", part="body")
    g.paint((1, -6, 11), (18, 6, 11), "shade", of="body")
    g.box((-1, -1, 18), (-1, 1, 19), "coat", part="body")
    # head: a long box, the chin lifted and turned to the camera; the white beard hanging under the jaw
    g.box((19, -3, 17), (25, 3, 23), "coat", part="head")
    g.box((22, -1, 13), (25, 1, 16), "shade", part="head")
    g.joint("head", pivot=(20, 0.5, 19), rotate=(6, -10, -18), parent="body")
    # face, painted flat: calm dark eyes under a level shaded brow
    g.set(25, -2, 21, "horn", part="head")
    g.box((25, -3, 22), (25, -1, 22), "shade", part="head")
    # muzzle: the dark nose on its top front edge, a small smile painted below it
    g.box((26, -2, 17), (28, 2, 20), "coat", part="muzzle")
    g.paint((28, -1, 20), (28, 1, 20), "nose", of="muzzle")
    g.set(28, -1, 18, "horn", part="muzzle")
    g.set(28, 0, 17, "horn", part="muzzle")
    g.joint("muzzle", pivot=(26, 0.5, 18.5), parent="head")
    # horns: short black daggers curving back
    g.box((20, -3, 24), (21, -2, 28), "horn", part="horn_l")
    g.joint("horn_l", pivot=(20.5, -2.5, 24), rotate=(6, -22, 0), parent="head")
    # ears sticking out sideways
    g.box((20, -5, 22), (21, -4, 23), "coat", part="ear_l")
    g.joint("ear_l", pivot=(20.5, -3.5, 22.5), rotate=(14, 0, 0), parent="head")
    g.mirror()
    # the smile's other corner (the mirror copies y < 0 only)
    g.set(28, 1, 18, "horn", part="muzzle")
    # one front hoof raised, as if stepping up a ledge
    g.joint("leg_fl", pivot=(16, -3.5, 11), rotate=(0, -30, 0), parent="body")
    g.joint("shin_fl", pivot=(16, -3.5, 6), rotate=(0, 34, 0), parent="leg_fl")
