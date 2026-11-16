"""26-010 · Giraffe (Giraffa camelopardalis) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: patch, base, mane, dark, eye, tongue. Size: 28 x 11 x 55 voxels posed.
Personality: gentle, curious and a little goofy. Pose: the long neck leaning forward and turned to the camera, the
head cocked, ears out, the tail swishing, the long dark tongue poking out of the side of the mouth. Expression: big
friendly dark eyes with a cream glint under a row of long lashes, painted flat."""

PATCHED = ("body", "neck", "leg_fl", "leg_hl", "leg_fr", "leg_hr")


def build(g):
    # legs: tall 3 x 3 pillars, dark hooves
    for leg, shin, x in (("leg_hl", "shin_hl", 1), ("leg_fl", "shin_fl", 13)):
        g.box((x, -4, 10), (x + 2, -2, 19), "base", part=leg)
        g.box((x, -4, 0), (x + 2, -2, 9), "base", part=shin)
        g.box((x, -4, 0), (x + 2, -2, 1), "dark", part=shin)
        g.joint(leg, pivot=(x + 1.5, -3, 20), parent="body")
        g.joint(shin, pivot=(x + 1.5, -3, 10), parent=leg)
    # body: one box, a step higher at the shoulders
    g.box((0, -4, 20), (16, 4, 29), "base", part="body")
    g.box((9, -4, 30), (16, 4, 31), "base", part="body")
    # neck: a tall block rising from the shoulders (about as long as the legs), the mane strip down its back
    g.box((12, -2, 32), (16, 2, 45), "base", part="neck")
    g.box((11, 0, 33), (11, 0, 45), "mane", part="neck")
    g.joint("neck", pivot=(14.5, 0.5, 31.5), rotate=(0, 10, -8), parent="body")
    # tail: a thin column with a dark tuft, swishing towards the camera
    g.box((-1, 0, 21), (-1, 0, 28), "base", part="tail")
    g.box((-1, -1, 19), (-1, 1, 20), "dark", part="tail")
    g.joint("tail", pivot=(-0.5, 0.5, 28.5), rotate=(-16, 0, 0), parent="body")
    # head: a long box on top of the neck, a narrower, lower muzzle in front; cocked to one side
    g.box((12, -3, 46), (20, 3, 51), "base", part="head")
    g.box((21, -2, 46), (23, 2, 48), "base", part="head")
    g.joint("head", pivot=(14.5, 0.5, 46), rotate=(14, 6, 0), parent="neck")
    # face, painted flat above the muzzle: big dark eyes with a cream glint, a row of long dark lashes over them
    g.box((20, -3, 49), (20, -2, 50), "eye", part="head")
    g.set(20, -3, 50, "base", part="head")
    g.box((20, -3, 51), (20, -2, 51), "dark", part="head")
    # ossicones: thin cream horns with dark tufts
    g.box((14, -2, 52), (14, -2, 53), "base", part="head")
    g.set(14, -2, 54, "dark", part="head")
    # ears: small blocks sticking out sideways, drooping a little
    g.box((15, -4, 49), (17, -4, 50), "base", part="ear_l")
    g.joint("ear_l", pivot=(16, -3, 49.5), rotate=(20, 0, 0), parent="head")
    g.mirror()

    # square brown patches in a cream net, drawn on whichever face of the voxel shows: the flank (x, z), the
    # front or back (y, z), the top (x, y); on the body, the upper legs and the neck, not the head
    def net(a, b):
        return (a + 1) % 4 != 0 and (b + 1) % 4 != 0

    for p in PATCHED:
        for (x, y, z), c in list(g.parts()[p]):
            if c != "base" or z < 8:
                continue
            side = not g.has((x, y - 1, z), p) or not g.has((x, y + 1, z), p)
            front = not g.has((x + 1, y, z), p) or not g.has((x - 1, y, z), p)
            top = not g.has((x, y, z + 1), p)
            a, b = (x, z) if side else (y, z) if front else (x, y) if top else (x, z)
            if net(a, b):
                g.set(x, y, z, "patch", part=p)
    # the long dark tongue poking out of the left side of the mouth (one side only)
    g.box((22, -3, 46), (24, -3, 46), "tongue", part="tongue")
    g.joint("tongue", pivot=(22, -2.5, 46.5), rotate=(0, 18, -10), parent="head")
    g.joint("leg_fl", pivot=(14.5, -3, 20), rotate=(0, -8, 0), parent="body")
    g.joint("leg_hr", pivot=(2.5, 4, 20), rotate=(0, 6, 0), parent="body")
    # the knees: the stepping front foot folds back, the hind hock flexes
    g.joint("shin_fl", pivot=(14.5, -3, 10), rotate=(0, 18, 0), parent="leg_fl")
    g.joint("shin_hr", pivot=(2.5, 4, 10), rotate=(0, -10, 0), parent="leg_hr")
