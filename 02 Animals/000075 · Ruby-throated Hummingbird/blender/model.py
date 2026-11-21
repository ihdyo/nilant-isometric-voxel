"""000075 · Ruby-throated Hummingbird (Archilochus colubris) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: back, throat, belly, beak, eye. Size: 25 x 25 x 17 voxels.
Personality: dazzling and fearless, a pocket-sized emerald rocket. Pose: hovering mid-air with swept-back wings and tail fanned slightly, needle bill poised forward. Expression: bright dark bead eyes above a shimmering ruby-red throat."""


def build(g):
    # body: compact metallic emerald back, ruby throat, white belly
    g.box((5, -3, 5), (13, 3, 13), "back", part="body")
    g.box((8, -3, 5), (14, 3, 10), "belly", part="body")
    g.box((10, -3, 10), (14, 3, 13), "throat", part="body")
    # forked tail and swept-back hovering wings
    g.box((0, -3, 2), (5, 3, 6), "beak", part="tail")
    g.joint("tail", pivot=(5, 0, 5), rotate=(0, 18, 0), parent="body")
    g.box((6, -12, 11), (11, -3, 13), "back", part="wing_l")
    g.joint("wing_l", pivot=(9, -3.5, 12), rotate=(18, -12, 14), parent="body")
    # tiny head and needle-thin black bill
    g.box((9, -3, 13), (15, 3, 18), "back", part="head")
    g.box((15, -1, 14), (24, 1, 15), "beak", part="head")
    g.set(13, -3, 16, "eye", part="head")
    g.joint("head", pivot=(12, 0, 13), rotate=(3, 4, -8), parent="body")
    g.mirror()
