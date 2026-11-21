"""000069 · Indian Peafowl (Pavo cristatus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: neck, train, eye_spot, face, eye. Size: 38 x 13 x 42 voxels.
Personality: regal and theatrical, proud showstopper of the forest clearing. Pose: a stately strut with cobalt chest held high, crown crest erect, long eyespot train sweeping behind. Expression: aristocratic dark eyes framed by crisp white cheek patches."""


def build(g):
    # body: royal-blue torso and long trailing emerald eyespot train
    g.box((18, -5, 11), (30, 5, 21), "neck", part="body")
    g.box((0, -6, 2), (19, 6, 13), "train", part="tail")
    for tx in (2, 7, 12):
        for ty in (-4, 0, 4):
            g.box((tx, ty, 8), (tx + 1, ty, 10), "eye_spot", part="tail")
    g.joint("tail", pivot=(18, 0, 13), rotate=(0, 8, 0), parent="body")
    # long legs
    g.box((22, -4, 0), (24, -2, 11), "eye", part="leg_l")
    g.joint("leg_l", pivot=(23, -3, 11), parent="body")
    # tall slender neck, head, and fan-shaped crest
    g.box((27, -2, 20), (31, 2, 32), "neck", part="neck")
    g.joint("neck", pivot=(28, 0, 20), parent="body")
    g.box((27, -3, 32), (34, 3, 37), "neck", part="head")
    g.box((34, -1, 33), (37, 1, 34), "face", part="head")
    g.box((28, -2, 37), (31, 2, 41), "neck", part="head")
    g.box((30, -3, 34), (32, -3, 35), "face", part="head")
    g.set(31, -3, 34, "eye", part="head")
    g.joint("head", pivot=(29, 0, 32), rotate=(4, 0, -10), parent="neck")
    g.mirror()
