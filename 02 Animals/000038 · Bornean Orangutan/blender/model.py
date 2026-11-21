"""000038 · Bornean Orangutan (Pongo pygmaeus) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: coat, skin, beard, shade, white, eye. Size: 22 x 22 x 28 voxels posed."""


def build(g):
    # stocky barrel-shaped torso with shaggy orange coat
    g.box((1, -7, 6), (11, 7, 20), "coat", part="body")
    g.paint((10, -4, 9), (11, 4, 17), "skin", of="body")
    g.paint((1, -6, 6), (3, 6, 11), "shade", of="body")
    # short grasping legs
    g.box((3, -6, 0), (7, -3, 6), "coat", part="leg_l")
    g.paint((4, -6, 0), (8, -3, 1), "skin", of="leg_l")
    g.joint("leg_l", pivot=(5, -4.5, 6), parent="body")
    # extra-long shaggy arms reaching nearly to the ground
    g.box((7, -10, 1), (11, -7, 19), "coat", part="arm_l")
    g.paint((7, -10, 1), (11, -7, 3), "skin", of="arm_l")
    g.paint((7, -10, 14), (10, -10, 19), "beard", of="arm_l")
    g.joint("arm_l", pivot=(9, -8.5, 19), rotate=(8, -12, 0), parent="body")
    # flanged head with dark face and orange beard
    g.box((5, -6, 20), (13, 6, 28), "coat", part="head")
    g.paint((12, -5, 20), (13, 5, 26), "skin", of="head")
    g.paint((12, -3, 20), (13, 3, 21), "beard", of="head")
    g.box((13, -3, 24), (13, -3, 25), "white", part="head")
    g.box((13, -2, 24), (13, -2, 25), "eye", part="head")
    g.joint("head", pivot=(9, 0, 20), rotate=(4, 3, -10), parent="body")
    g.mirror()
    g.joint("arm_r", pivot=(9, 8.5, 19), rotate=(-8, 6, 0), parent="body")
