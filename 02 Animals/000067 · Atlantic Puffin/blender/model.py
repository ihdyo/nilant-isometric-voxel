"""000067 · Atlantic Puffin (Fratercula arctica) · voxel model, bulky blocky-mob style.
Built from docs/voxel-model.md. Palette keys: back, belly, face, beak, eye. Size: 15 x 11 x 22 voxels.
Personality: plucky and dapper, charming clown of the North Atlantic cliffs. Pose: standing upright on bright orange webbed feet, chest puffed, head cocked inquisitively. Expression: soulful dark eyes framed by triangular red-orange eye rings and pale grey cheeks."""


def build(g):
    # body: tuxedo black back and crisp white belly
    g.box((2, -4, 4), (11, 4, 15), "back", part="body")
    g.box((7, -4, 4), (12, 4, 13), "belly", part="body")
    g.box((2, -5, 4), (9, -4, 14), "back", part="wing_l")
    g.joint("wing_l", pivot=(6, -4.5, 13), parent="body")
    # bright orange webbed feet
    g.box((6, -4, 1), (8, -2, 4), "beak", part="leg_l")
    g.box((6, -4, 0), (10, -1, 0), "beak", part="leg_l")
    g.joint("leg_l", pivot=(7, -3, 4), parent="body")
    # head with pale grey cheeks and huge striped triangular beak
    g.box((3, -4, 15), (11, 4, 21), "back", part="head")
    g.box((7, -4, 16), (11, -3, 19), "face", part="head")
    g.box((11, -2, 15), (16, 2, 20), "beak", part="head")
    g.box((8, -4, 18), (9, -4, 19), "eye", part="head")
    g.joint("head", pivot=(7, 0, 15), rotate=(4, 4, -12), parent="body")
    g.mirror()
