"""000070 · Secretarybird (Sagittarius serpentarius) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: plumage, legging, face, crest, leg. Size: 30 x 9 x 48 voxels.
Personality: poised and fearless, martial-arts aristocrat of the savanna. Pose: a high-stepping stride on stilt legs, quill crest fanned behind the head, wings tucked. Expression: keen eyes with long lashes set in vivid orange-red facial skin."""


def build(g):
    # body: silver-grey torso with long central tail feathers
    g.box((9, -4, 21), (21, 4, 30), "plumage", part="body")
    g.box((0, -2, 11), (10, 2, 23), "plumage", part="tail")
    g.joint("tail", pivot=(10, 0, 22), rotate=(0, 10, 0), parent="body")
    # long stilt legs with black feathered upper thighs
    for leg, shin, x in (("leg_l", "shin_l", 14),):
        g.box((x, -4, 14), (x + 2, -2, 21), "legging", part=leg)
        g.box((x, -3, 0), (x + 1, -2, 13), "leg", part=shin)
        g.joint(leg, pivot=(x + 1, -3, 21), parent="body")
        g.joint(shin, pivot=(x + 1, -3, 14), parent=leg)
    # tall neck, orange-faced head, and black-tipped quill crest
    g.box((18, -2, 29), (22, 2, 41), "plumage", part="neck")
    g.joint("neck", pivot=(20, 0, 29), parent="body")
    g.box((18, -3, 41), (25, 3, 46), "plumage", part="head")
    g.box((23, -3, 42), (26, 3, 44), "face", part="head")
    g.box((26, -1, 42), (29, 1, 43), "leg", part="head")
    g.box((13, -2, 43), (18, 2, 47), "crest", part="head")
    g.set(24, -3, 43, "crest", part="head")
    g.joint("head", pivot=(20, 0, 41), rotate=(4, 4, -10), parent="neck")
    g.mirror()
    g.joint("leg_l", pivot=(15, -3, 21), rotate=(0, -10, 0), parent="body")
