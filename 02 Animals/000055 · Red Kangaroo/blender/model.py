"""000055 · Red Kangaroo (Osphranter rufus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, belly, muzzle, claw, white, eye. Size: 24 x 14 x 40 voxels.
Personality: energetic and alert, spring-loaded sprinter of the red centre. Pose: upright poised stance balanced on long hind feet and heavy tail, ears perked forward. Expression: bright curious eyes and a twitching nose."""


def build(g):
    # body: upright pear-shaped torso with pale cream belly
    g.box((8, -5, 9), (18, 5, 25), "coat", part="body")
    g.box((15, -4, 10), (19, 4, 23), "belly", part="body")
    # thick muscular balancing tail
    g.box((0, -2, 2), (8, 2, 11), "coat", part="tail")
    g.joint("tail", pivot=(8, 0, 9), rotate=(0, 8, 0), parent="body")
    # powerful hind legs and long narrow feet
    g.box((9, -7, 4), (15, -4, 12), "coat", part="leg_hl")
    g.box((11, -7, 0), (21, -4, 2), "coat", part="foot_hl")
    g.box((21, -7, 0), (22, -4, 1), "claw", part="foot_hl")
    g.joint("leg_hl", pivot=(12, -5.5, 11), rotate=(0, -10, 0), parent="body")
    g.joint("foot_hl", pivot=(13, -5.5, 2), parent="leg_hl")
    # short forepaws held near the chest
    g.box((16, -6, 18), (21, -4, 22), "coat", part="arm_l")
    g.joint("arm_l", pivot=(17, -5, 22), rotate=(0, 18, 0), parent="body")
    # alert head with tall pointed ears
    g.box((12, -4, 25), (21, 4, 32), "coat", part="head")
    g.box((19, -3, 26), (23, 3, 29), "muzzle", part="head")
    g.set(23, 0, 28, "claw", part="head")
    g.joint("head", pivot=(15, 0, 26), rotate=(4, 4, -10), parent="body")
    g.box((13, -4, 32), (15, -2, 39), "coat", part="ear_l")
    g.paint((14, -3, 33), (15, -3, 38), "muzzle", of="ear_l")
    g.joint("ear_l", pivot=(14, -3, 32), rotate=(-8, 6, 8), parent="head")
    g.box((18, -4, 29), (19, -4, 30), "white", part="head")
    g.box((19, -4, 29), (19, -4, 30), "eye", part="head")
    g.mirror()
