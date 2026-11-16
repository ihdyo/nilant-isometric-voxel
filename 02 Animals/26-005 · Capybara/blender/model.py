"""26-005 · Capybara (Hydrochoerus hydrochaeris) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: fur, dark, eye. Size: 29 x 13 x 19 voxels posed.
Personality: calm, unbothered, everyone's friend. Pose: standing at ease, the big head lowered and turned a little to
the camera, one ear flicked back. Expression: sleepy half-closed eyes (flat lines) and a small easy smile, painted
flat."""


def build(g):
    # body: one big barrel box
    g.box((0, -6, 4), (17, 6, 14), "fur", part="body")
    # legs: short 3 x 3 pillars
    for name, x in (("leg_hl", 1), ("leg_fl", 13)):
        g.box((x, -6, 0), (x + 2, -4, 3), "fur", part=name)
        g.joint(name, pivot=(x + 1.5, -5, 4), parent="body")
    # head: a long box, a little narrower than the body
    g.box((17, -5, 8), (24, 5, 16), "fur", part="head")
    g.joint("head", pivot=(18, 0.5, 12), rotate=(6, 10, -8), parent="body")
    # sleepy eyes painted high on the face: flat dark lines
    g.box((24, -4, 14), (24, -3, 14), "eye", part="head")
    # deep square snout, nearly as wide as the head; dark nostrils and a small easy smile painted on its front
    g.box((25, -4, 8), (27, 4, 13), "fur", part="snout")
    g.set(27, -2, 12, "dark", part="snout")
    g.box((27, -1, 9), (27, 0, 9), "dark", part="snout")
    g.joint("snout", pivot=(25, 0.5, 10.5), parent="head")
    # small dark ears on top, one flicked back
    g.box((19, -5, 17), (20, -4, 17), "dark", part="ear_l")
    g.joint("ear_l", pivot=(19.5, -4.5, 17), rotate=(20, 0, 0), parent="head")
    g.mirror()
    g.joint("ear_r", pivot=(19.5, 5.5, 17), rotate=(-10, -24, 0), parent="head")
    g.joint("leg_fl", pivot=(14.5, -5, 4), rotate=(0, -6, 0), parent="body")
    g.joint("leg_hr", pivot=(2.5, 6, 4), rotate=(0, 6, 0), parent="body")
