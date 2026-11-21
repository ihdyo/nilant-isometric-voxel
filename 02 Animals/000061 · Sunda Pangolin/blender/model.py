"""000061 · Sunda Pangolin (Manis javanica) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: scale, shade, skin, claw, eye. Size: 35 x 11 x 19 voxels.
Personality: humble and armored, quiet guardian of the Sunda rainforest. Pose: a cautious bipedal-leaning amble, heavy scaly tail balanced behind, head angled down. Expression: gentle dark eyes on a narrow pale-tan conical snout."""


def build(g):
    # body: arched scaly back with pale tan underbelly
    g.box((10, -5, 6), (26, 5, 16), "scale", part="body")
    g.box((12, -4, 5), (25, 4, 7), "skin", part="body")
    g.box((13, -5, 16), (23, 5, 18), "shade", part="body")
    # long thick scaly prehensile tail
    g.box((0, -3, 4), (10, 3, 11), "scale", part="tail")
    g.joint("tail", pivot=(10, 0, 8), rotate=(0, 8, 0), parent="body")
    # sturdy hind legs and clawed forelimbs
    g.box((12, -5, 0), (15, -3, 6), "scale", part="leg_hl")
    g.box((21, -5, 2), (24, -3, 7), "skin", part="arm_l")
    g.box((24, -5, 2), (26, -3, 4), "claw", part="arm_l")
    g.joint("leg_hl", pivot=(13.5, -4, 6), parent="body")
    g.joint("arm_l", pivot=(22.5, -4, 7), rotate=(0, 14, 0), parent="body")
    # narrow tapered conical head
    g.box((26, -3, 8), (34, 3, 13), "skin", part="head")
    g.box((26, -3, 12), (31, 3, 14), "scale", part="head")
    g.set(30, -3, 11, "eye", part="head")
    g.set(34, 0, 10, "eye", part="head")
    g.joint("head", pivot=(26, 0, 11), rotate=(4, 12, -10), parent="body")
    g.mirror()
