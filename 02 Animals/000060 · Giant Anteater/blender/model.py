"""000060 · Giant Anteater (Myrmecophaga tridactyla) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, stripe, trim, tail, eye. Size: 49 x 11 x 21 voxels.
Personality: focused and eccentric, methodical termite-mound inspector. Pose: a knuckle-walking stride, long tubular snout sweeping low, huge bushy tail streaming behind. Expression: small earnest eyes set high on a remarkably long slender snout."""


def build(g):
    # body: long torso with bold black-and-white diagonal shoulder wedge
    g.box((12, -5, 9), (32, 5, 20), "coat", part="body")
    g.box((20, -5, 9), (29, 5, 17), "stripe", part="body")
    g.box((19, -5, 16), (30, 5, 18), "trim", part="body")
    # enormous bushy plumed tail
    g.box((0, -4, 4), (12, 4, 18), "tail", part="tail")
    g.joint("tail", pivot=(12, 0, 13), rotate=(0, -6, 0), parent="body")
    # knuckle-walking white front legs and grey hind legs
    g.box((14, -5, 0), (17, -3, 9), "coat", part="leg_hl")
    g.box((27, -5, 0), (30, -3, 9), "trim", part="leg_fl")
    g.joint("leg_hl", pivot=(15.5, -4, 9), parent="body")
    g.joint("leg_fl", pivot=(28.5, -4, 9), parent="body")
    # narrow head tapering into an extremely long tubular snout
    g.box((32, -3, 12), (38, 3, 18), "coat", part="head")
    g.box((38, -2, 11), (48, 2, 15), "coat", part="head")
    g.set(48, 0, 13, "eye", part="head")
    g.set(35, -3, 16, "eye", part="head")
    g.joint("head", pivot=(32, 0, 15), rotate=(3, 10, -8), parent="body")
    g.mirror()
    g.joint("leg_fl", pivot=(28.5, -4, 9), rotate=(0, -12, 0), parent="body")
