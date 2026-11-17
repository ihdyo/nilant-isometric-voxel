"""26-025 · Plains Zebra (Equus quagga) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: white, stripe, muzzle. Size: 33 x 12 x 39 voxels posed.
Personality: lively, sociable and a little cheeky. Pose: trotting with one front leg lifted, the head held high and
turned to the camera, the short mane bristling along the top and down the back of the neck, the tail swishing.
Expression: a big dark eye with a white glint and a cheeky smirk, painted flat."""


def build(g):
    # legs: tall pillars with horizontal stripes down to black hooves
    for leg, shin, x in (("leg_hl", "shin_hl", 2), ("leg_fl", "shin_fl", 18)):
        g.box((x, -5, 8), (x + 2, -3, 14), "white", part=leg)
        g.box((x, -5, 0), (x + 2, -3, 7), "white", part=shin)
        g.box((x, -5, 0), (x + 2, -3, 1), "stripe", part=shin)
        for z in (10, 13):
            g.paint((x, -5, z), (x + 2, -3, z), "stripe", of=leg)
        for z in (4, 7):
            g.paint((x, -5, z), (x + 2, -3, z), "stripe", of=shin)
        g.joint(leg, pivot=(x + 1.5, -4, 15), parent="body")
        g.joint(shin, pivot=(x + 1.5, -4, 8), parent=leg)
    # body: one long box; stripes vertical over the shoulders and middle, horizontal on the rump
    g.box((0, -5, 15), (21, 5, 24), "white", part="body")
    for x in (7, 10, 13, 16, 19):
        g.paint((x, -5, 15), (x, 5, 24), "stripe", of="body")
    for z in (16, 19, 22):
        g.paint((0, -5, z), (4, 5, z), "stripe", of="body")
    # tail: a striped column swishing towards the camera, a black tuft at the end
    g.box((-1, 0, 17), (-1, 0, 23), "white", part="tail")
    g.box((-1, -1, 13), (-1, 1, 16), "stripe", part="tail")
    g.joint("tail", pivot=(-0.5, 0.5, 23.5), rotate=(-20, 0, 0), parent="body")
    # neck: raised, a little narrower than the head, vertical stripes; the short upright striped mane, a brush three
    # voxels wide, runs along its top and down the back of the neck to the withers
    g.box((18, -2, 25), (22, 2, 32), "white", part="neck")
    for x in (19, 21):
        g.paint((x, -2, 25), (x, 2, 32), "stripe", of="neck")
    for x in range(17, 23):
        g.box((x, -1, 33), (x, 1, 34), "stripe" if x % 2 else "white", part="neck")
    for z in range(25, 35):
        g.box((15, -1, z), (17, 1, z), "stripe" if z % 2 else "white", part="neck")
    g.joint("neck", pivot=(20, 0.5, 24.5), rotate=(0, -6, -10), parent="body")
    # head: a long box held high, stripes across the forehead, the dark muzzle
    g.box((22, -3, 30), (29, 3, 35), "white", part="head")
    for x in (23, 25):
        g.paint((x, -3, 33), (x, 3, 35), "stripe", of="head")
    g.joint("head", pivot=(22, 0.5, 32), rotate=(6, 8, -8), parent="neck")
    # face, painted flat: a big dark eye on the front corner with a white glint above
    g.box((29, -3, 32), (29, -3, 33), "stripe", part="head")
    g.set(28, -3, 33, "stripe", part="head")
    # muzzle: dark, a cheeky smirk painted white on one side
    g.box((30, -2, 30), (32, 2, 33), "muzzle", part="muzzle")
    g.box((32, -1, 31), (32, 0, 31), "white", part="muzzle")
    g.joint("muzzle", pivot=(30, 0.5, 31.5), parent="head")
    # ears: upright, white with a black tip
    g.box((24, -3, 36), (25, -2, 38), "white", part="ear_l")
    g.paint((24, -3, 38), (25, -2, 38), "stripe", of="ear_l")
    g.joint("ear_l", pivot=(24.5, -2.5, 36), rotate=(10, 0, 0), parent="head")
    g.mirror()
    # the smirk rises on one side only
    g.set(32, -2, 32, "white", part="muzzle")
    # a trot: the front left leg lifted, the hind right swinging back
    g.joint("leg_fl", pivot=(19.5, -4, 15), rotate=(0, -28, 0), parent="body")
    g.joint("leg_hr", pivot=(3.5, 5, 15), rotate=(0, 14, 0), parent="body")
    # the knees: the lifted front hoof tucks back (the trot), the swinging hind hock flexes
    g.joint("shin_fl", pivot=(19.5, -4, 8), rotate=(0, 40, 0), parent="leg_fl")
    g.joint("shin_hr", pivot=(3.5, 5, 8), rotate=(0, -12, 0), parent="leg_hr")
