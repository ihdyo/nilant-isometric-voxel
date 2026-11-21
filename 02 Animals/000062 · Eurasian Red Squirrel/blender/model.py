"""000062 · Eurasian Red Squirrel (Sciurus vulgaris) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, belly, tuft, paw, eye. Size: 18 x 10 x 27 voxels.
Personality: nimble and spirited, acrobat of the pine canopy. Pose: perched upright on hind paws holding an acorn, huge fluffy tail curled behind in an S-curve. Expression: big glossy black eyes, twitching whiskers and tall tufted ears."""


def build(g):
    # body: upright perching torso with crisp white belly
    g.box((6, -4, 3), (14, 4, 14), "coat", part="body")
    g.box((12, -3, 4), (15, 3, 13), "belly", part="body")
    # huge S-curved fluffy rufous tail
    g.box((0, -3, 2), (6, 3, 18), "coat", part="tail")
    g.box((1, -3, 16), (7, 3, 21), "tuft", part="tail")
    g.joint("tail", pivot=(6, 0, 5), rotate=(0, -8, 0), parent="body")
    # hind paws and front paws holding a nut
    g.box((8, -5, 0), (14, -3, 3), "coat", part="leg_hl")
    g.box((13, -4, 10), (17, -2, 13), "paw", part="arm_l")
    g.joint("leg_hl", pivot=(10, -4, 3), parent="body")
    g.joint("arm_l", pivot=(13, -3, 12), rotate=(0, 10, 14), parent="body")
    # rounded head with tall winter ear tufts
    g.box((8, -4, 14), (16, 4, 21), "coat", part="head")
    g.box((9, -4, 21), (11, -2, 23), "coat", part="ear_l")
    g.box((9, -3, 24), (10, -3, 26), "tuft", part="ear_l")
    g.joint("ear_l", pivot=(10, -3, 21), rotate=(-6, 0, 8), parent="head")
    g.box((14, -4, 17), (15, -4, 19), "eye", part="head")
    g.set(16, 0, 17, "eye", part="head")
    g.joint("head", pivot=(12, 0, 15), rotate=(4, 4, -10), parent="body")
    g.mirror()
