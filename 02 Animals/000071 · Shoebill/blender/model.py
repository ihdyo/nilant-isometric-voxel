"""000071 · Shoebill (Balaeniceps rex) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: plumage, bill, leg, iris, eye. Size: 26 x 11 x 40 voxels.
Personality: stoic and prehistoric, an ancient swamp statue with a secret grin. Pose: standing motionless with head tucked slightly into the shoulders, massive clog bill resting downward. Expression: intense forward-facing pale-gold eyes and a subtle hooked grin on its huge clog bill."""


def build(g):
    # body: slate-blue torso and broad folded wings
    g.box((4, -5, 16), (16, 5, 29), "plumage", part="body")
    g.box((1, -3, 12), (5, 3, 18), "plumage", part="tail")
    g.joint("tail", pivot=(5, 0, 17), rotate=(0, 12, 0), parent="body")
    # long black stilt legs
    g.box((9, -4, 0), (11, -2, 16), "leg", part="leg_l")
    g.box((9, -5, 0), (13, -1, 0), "leg", part="leg_l")
    g.joint("leg_l", pivot=(10, -3, 16), parent="body")
    # big head with wispy crest and enormous clog-shaped bill
    g.box((8, -5, 29), (17, 5, 37), "plumage", part="head")
    g.box((6, -1, 36), (8, 1, 39), "plumage", part="head")
    g.box((17, -4, 27), (26, 4, 34), "bill", part="head")
    g.set(26, 0, 26, "eye", part="head")
    g.box((15, -5, 33), (16, -5, 34), "iris", part="head")
    g.set(16, -5, 33, "eye", part="head")
    g.joint("head", pivot=(12, 0, 29), rotate=(3, 8, -10), parent="body")
    g.mirror()
