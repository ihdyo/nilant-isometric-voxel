"""000004 · Emperor Penguin (Aptenodytes forsteri) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: black, white, yellow, cream, bill. Size: 15 x 20 x 28 voxels posed.
Personality: proud and a little pompous. Pose: standing tall, chin up, turned to the camera, the left flipper held out wide, the right one lifted a little, the small feet turned out.
Expression: smug closed eyes, white lines dipping towards the middle, painted flat on the face."""


def build(g):
    # feet: black blocks one voxel tall on the ground, the toes poking out in front of the body, turned out
    g.box((7, -3, 0), (9, -1, 0), "black", part="foot_l")          # smaller feet (owner 2026-11-21), was 5 x 4
    g.joint("foot_l", pivot=(6, -2, 0.5), rotate=(0, 0, -12))
    # body: one tall bulky box: black back, white front and lower flanks, cream upper breast
    g.box((0, -5, 1), (9, 5, 17), "black", part="body")
    g.paint((8, -4, 1), (9, 4, 13), "white", of="body")
    g.paint((4, -5, 1), (9, -5, 10), "white", of="body")
    g.paint((8, -4, 14), (9, 4, 17), "cream", of="body")
    g.box((-1, -1, 1), (-1, 1, 3), "black", part="body")
    # flippers: slabs hanging from the shoulders, held out from the body
    g.box((3, -6, 6), (7, -6, 15), "black", part="flipper_l")
    g.joint("flipper_l", pivot=(5, -5.5, 15), rotate=(-32, 0, 0), parent="body")
    # head: a black box narrower than the body, the yellow ear patch low on its side
    g.box((1, -4, 18), (8, 4, 26), "black", part="head")
    g.paint((3, -4, 18), (6, -4, 20), "yellow", of="head")
    g.joint("head", pivot=(4.5, 0.5, 18), rotate=(3, -8, -14), parent="body")
    # smug closed eyes painted flat on the front of the head: a white line dipping towards the middle
    g.set(8, -3, 23, "white", part="head")
    g.set(8, -2, 22, "white", part="head")
    # long thin bill: black on top, the orange stripe underneath
    g.box((9, 0, 20), (13, 0, 21), "black", part="beak")
    g.paint((9, 0, 20), (12, 0, 20), "bill", of="beak")
    g.joint("beak", pivot=(9, 0.5, 21), rotate=(0, 4, 0), parent="head")
    g.mirror()
    # a livelier pose (owner 2026-11-21); the head turned to the camera
    g.joint("flipper_r", pivot=(5, 6.5, 15), rotate=(12, 0, 0), parent="body")
