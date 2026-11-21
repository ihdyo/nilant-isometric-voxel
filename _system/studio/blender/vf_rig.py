"""Voxel Fauna · the rig and the motion library: one Blender run that turns an animal's built .blend into a rigged,
animated .blend and a .glb, and renders preview frames of its loops.

    blender -b --factory-startup --python vf_rig.py -- <job.json>

job.json (written by scripts/vf.py rig, never by hand):
    {"open": ".../<code> · <Name>.blend", "model": ".../blender/model.py", "motion": {...}, "readme": "...",
     "blend": ".../<code> · <Name> · Rig.blend", "glb": ".../<code> · <Name> · Rig.glb",
     "preview": {"dir": ".../anim", "step": 2, "actions": [...] (default: every action but "pose")},
     "work": "...", "result": "..."}
motion (animal.json -> motion): {"plan": "walker" | "sitter" | "bird" | "swimmer" | "sprawler" | "hopper",
     "actions": [...] (default: the plan's), "frames": {"swim": 48}, "base": {"walk": {"jaw": [0, 2, 0]}}}

APPROVED by the owner 2026-11-17 and in the standards lock: its numbers are vf_standards.MOTION. The stills pipeline
(vf_job, vf_scene) is untouched: the rig is built on a copy of the approved .blend and saved beside it.

The rig (PLAN.md, "Rig from the joints"):
  - one bone per jointed section, on its hinge (the vf_voxel joint pivot), parented like the joints; "body" carries
    every section without a joint; "root" sits on the ground under the body and carries the grounding and hops.
  - the skin: the sections joined into one mesh 'VF · animal', every vertex weighted 1.0 to its section's bone (a
    vertex group per bone) and deformed by an Armature modifier: rigid, so the blocks stay crisp.
  - the bind (rest) pose is the model as drawn, before any joint turns; the approved still is the action "pose".
Every action is the still pose plus offsets, so a loop starts and ends on the approved look; locomotion legs replace
their still angles. Each frame is grounded on the posed voxels (the lowest corner stands on z = 0), so planted feet
stay planted without foot targets; a hop adds its height on top.
"""
import json
import math
import os
import sys
import time
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

TAU = 2.0 * math.pi

# ---- the numbers of the motion: vf_standards.MOTION (APPROVED by the owner 2026-11-17, locked) ------------------------
import vf_standards as _ST  # noqa: E402
RIG = _ST.MOTION

# body plan -> the actions every animal of that plan gets (animal.json motion.actions adds or replaces)
PLANS = {
    "walker": ["pose", "idle", "walk"],
    "sitter": ["pose", "idle"],
    "bird": ["pose", "idle", "flap"],
    "swimmer": ["pose", "idle", "swim"],
    "sprawler": ["pose", "idle", "walk"],
    "hopper": ["pose", "idle", "hop"],
}


def log(line):
    print("VF:", line, flush=True)


def detect_plan(bones):
    b = set(bones)
    if {"leg_fl", "leg_hl"} <= b and not ("flukes" in b or "flipper_l" in b):
        return "walker"
    if "wing_l" in b or "beak" in b:
        return "bird"
    if "flukes" in b or "flipper_l" in b:
        return "swimmer"
    return "walker" if any(x.startswith("leg_") for x in b) else "sitter"


# ---- small curves -----------------------------------------------------------------------------------------------------
def smooth(x):
    x = min(1.0, max(0.0, x))
    return x * x * (3.0 - 2.0 * x)


def curve(t, pts):
    """Eased through (time, value) points; flat outside them."""
    if t <= pts[0][0]:
        return pts[0][1]
    for (t0, v0), (t1, v1) in zip(pts, pts[1:]):
        if t <= t1:
            return v0 + (v1 - v0) * smooth((t - t0) / max(1e-6, t1 - t0))
    return pts[-1][1]


def bump(t, c, w):
    return math.exp(-((t - c) / w) ** 2)


def sn(t, n, k=1.0, ph=0.0):
    return math.sin(TAU * (k * t / n + ph))


# ---- the motion library ---------------------------------------------------------------------------------------------
class Pose:
    """One frame: per bone ("add" | "abs", 3 x 3 rotation in the section's own rest axes), the body's turn about its
    hinge (bottom centre), and a hop in voxels."""

    def __init__(self, I3):
        self.rot, self.body, self.hop = {}, I3.copy(), 0.0


class Ctx:
    def __init__(self, info, plan, n, base):
        from mathutils import Euler, Matrix, Vector
        self.Euler, self.Matrix, self.Vector = Euler, Matrix, Vector
        self.I3 = Matrix.Identity(3)
        self.info, self.plan, self.N, self.base = info, plan, n, base
        self.cyc, self.length = 1, 0.0
        self.opt = {}                             # animal.json motion.options

    def has(self, b):
        return b in self.info

    def pair(self, stem):
        return [b for b in (f"{stem}_l", f"{stem}_r") if b in self.info]

    def hind(self, stem):
        return [b for b in (f"{stem}_hl", f"{stem}_hr") if b in self.info]

    def legs(self):
        return [b for b in ("leg_fl", "leg_fr", "leg_hl", "leg_hr") if b in self.info]

    def E(self, b, x, y, z):
        """Euler XYZ degrees as written for a left (-Y) section; a right section gets the mirror (-x, y, -z)."""
        if self.info[b]["side"] == "r":
            x, z = -x, -z
        return self.Euler((math.radians(x), math.radians(y), math.radians(z)), "XYZ").to_matrix()

    def Eb(self, x, y, z):
        return self.Euler((math.radians(x), math.radians(y), math.radians(z)), "XYZ").to_matrix()

    def toward(self, b, d, deg):
        """Turn a section about its hinge so its far end moves towards direction d (as written for a left section)."""
        d = self.Vector(d)
        if self.info[b]["side"] == "r":
            d.y = -d.y
        c = self.info[b]["c"]
        ax = c.cross(d)
        if ax.length < 1e-4 * max(1.0, c.length * d.length):
            return self.I3.copy()
        return self.Matrix.Rotation(math.radians(deg), 3, ax.normalized())

    def spread(self, b):
        c = self.info[b]["c"]
        return abs(c.y) > abs(c.x)

    def add(self, P, b, m):
        if b in self.info:
            mode, cur = P.rot.get(b, ("add", self.I3))
            P.rot[b] = (mode, cur @ m)

    def abs(self, P, b, m):
        if b in self.info:
            P.rot[b] = ("abs", m)

    def o(self, key, default):
        """A per-animal motion option (animal.json motion.options), else the default."""
        return float(self.opt.get(key, default))


def a_pose(C, t):
    return Pose(C.I3)


def _ears_idle(C, P, t):
    for b in C.pair("ear"):
        if C.info[b]["c"].length > 4.0:                  # big ears (elephant): a slow fan
            C.add(P, b, C.E(b, 0, 0, 10 * sn(t, C.N, 2)))
        else:                                            # a quick flick, one ear after the other
            when = 0.62 if C.info[b]["side"] == "l" else 0.75
            C.add(P, b, C.toward(b, (0, -1, 0.4), 26 * bump(t, when * C.N, 0.07 * C.N)))
            C.add(P, b, C.toward(b, (-1, 0, 0), 5 * sn(t, C.N, 2, 0.3)))


def _alive(C, P, t, amt=1.0, head=True, ears=True, wings=True, tail=True):
    """The life layer (v2, owner 2026-11-17: "tilt the head, ear, etc ... so the animation looks lively and not blindly
    look at camera"): over the whole loop the head looks around (yaw biased away from the camera's side, +Y), tilts and
    nods, shared with the neck; each ear perks and tips on its own beat; the tail wags; folded wings flutter with one
    fuller flap. Every term is a whole number of cycles a loop, so the loop stays seamless."""
    L, N = RIG["life"], C.N
    if head:
        yaw = L["look"] * (L["look_bias"] + 0.7 * sn(t, N, 1, 0.15) + 0.3 * sn(t, N, 2, 0.55))
        tilt = L["tilt"] * sn(t, N, 1, 0.4)
        nod = L["nod"] * sn(t, N, 2, 0.05)
        share = (("neck", 0.4), ("head", 0.6)) if C.has("neck") else (("head", 1.0),)
        for b, k in share:
            C.add(P, b, C.E(b, tilt * k * amt, nod * k * amt, yaw * k * amt))
        if C.has("mane"):
            C.add(P, "mane", C.E("mane", 0.4 * tilt * amt, 0, 0.3 * yaw * amt))
    if ears:
        for b in C.pair("ear"):
            ph = 0.0 if C.info[b]["side"] == "l" else 0.37
            if C.info[b]["c"].length > 4.0:                  # big ears (elephant): a slow fan, the two out of step
                C.add(P, b, C.E(b, 0, 0, 0.8 * L["ear"] * amt * sn(t, N, 2, ph)))
                continue
            C.add(P, b, C.toward(b, (-1, 0, 0), L["ear"] * amt * sn(t, N, 2, ph)))        # perk forward, tip back
            C.add(P, b, C.toward(b, (0, -1, 0), L["ear_tilt"] * amt * sn(t, N, 1, ph + 0.2)))   # tip outward
    if tail:
        for i, b in enumerate(b for b in ("tail", "tail_tip") if C.has(b)):
            C.add(P, b, C.toward(b, (0, 1, 0), (L["tail"] + 4 * i) * amt * sn(t, N, 2, -0.1 * i)))
    if wings:
        for b in C.pair("wing"):
            if C.spread(b):
                C.add(P, b, C.toward(b, (0, 0, 1), 0.5 * L["wing"] * amt * sn(t, N, 2)))
            else:
                ph = 0.0 if C.info[b]["side"] == "l" else 0.06
                flut = L["wing"] * (0.5 + 0.5 * sn(t, N, 4, ph)) + L["wing_flap"] * bump(t, 0.55 * N, 0.07 * N)
                C.add(P, b, C.toward(b, (0, -1, 0.6), flut * amt))
    for b in C.pair("gill"):
        C.add(P, b, C.E(b, 0.6 * L["ear"] * amt * sn(t, N, 4, 0.1), 0, 0))


TRUNK = ("trunk_1", "trunk_2", "trunk_3")


def _trunk(C, P, t, curl=1.0, sway=1.0, k=1.0):
    """A trunk that lives (owner 2026-11-21: "the elephant trunk should be animated dynamic"): a curl that rolls down
    the chain (the tip lags and goes furthest, forward and up), and a side sway that also travels down it, so the trunk
    reads as one soft limb, not three stiff blocks. Negative pitch lifts a hanging segment's tip forward."""
    N = C.N
    for i, b in enumerate(b for b in TRUNK if C.has(b)):
        lag = 0.11 * i
        c = curl * (10.0 + 9.0 * i) * (0.5 - 0.5 * math.cos(TAU * (k * t / N - lag)))
        w = sway * (5.0 + 5.0 * i) * math.sin(TAU * (k * t / N - lag - 0.2))
        C.add(P, b, C.E(b, w, -c, 0))


def _tail(C, P, t, amp, k=1.0, lag=0.12, d=(0, 1, 0)):
    for i, b in enumerate(b for b in ("tail", "tail_tip", "flukes") if C.has(b)):
        C.add(P, b, C.toward(b, d, (amp + 5 * i) * sn(t, C.N, k, -lag * i)))


def a_idle(C, t):
    P, N = Pose(C.I3), C.N
    if C.has("torso"):
        C.add(P, "torso", C.E("torso", 0, 1.2 * sn(t, N, 2), 0))
    _ears_idle(C, P, t)
    _tail(C, P, t, 10, d=(0, 0, 1) if C.plan == "swimmer" else (0, 1, 0))
    _trunk(C, P, t, curl=1.3, sway=1.0)
    if C.has("jaw"):
        C.add(P, "jaw", C.E("jaw", 0, -7 * (0.5 + 0.5 * sn(t, N, 2)), 0))
    if C.has("tongue"):
        C.add(P, "tongue", C.E("tongue", 0, 0, 12 * sn(t, N, 3)))
    for b in ("muzzle", "snout", "nose"):
        if C.has(b):
            C.add(P, b, C.E(b, 0, 2.0 * sn(t, N, 8) * bump(t, 0.25 * N, 0.08 * N), 0))
    for b in C.pair("wing"):
        if C.spread(b):
            C.add(P, b, C.toward(b, (0, 0, 1), 4 * sn(t, N)))
        else:
            C.add(P, b, C.toward(b, (0, -1, 0.6), 12 * bump(t, 0.38 * N, 0.05 * N)))
    for b in C.pair("flipper"):
        C.add(P, b, C.toward(b, (0, 0, 1), 5 * sn(t, N)))
    for b in C.hind("flipper"):
        C.add(P, b, C.toward(b, (0, 0, 1), 5 * sn(t, N, 1, 0.3)))
    for b in C.pair("arm"):
        C.add(P, b, C.toward(b, (0, 0, 1), 2 * sn(t, N, 2)))
    _alive(C, P, t, 1.0, wings=False)
    return P


def _sprawl(C, t):
    P, N = Pose(C.I3), C.N
    S = C.cyc
    ph = {"leg_fl": 0.0, "leg_hr": 0.0, "leg_fr": 0.5, "leg_hl": 0.5}
    for b in C.legs():
        th = TAU * (S * t / N + ph[b])
        C.add(P, b, C.E(b, 0, 0, 22 * math.sin(th)))
        C.add(P, b, C.toward(b, (0, 0, 1), 10 * max(0.0, math.cos(th))))
    th0 = TAU * S * t / N
    P.body = C.Eb(RIG["life"]["roll"] * math.sin(th0), 0, 6 * math.sin(th0))
    if C.has("head"):
        C.add(P, "head", C.E("head", 0, 0, -5 * math.sin(th0)))
    for i, b in enumerate(b for b in ("tail", "tail_tip", "flukes") if C.has(b)):
        C.add(P, b, C.toward(b, (0, 1, 0), (-12 - 5 * i) * math.sin(th0 - 0.6 * (i + 1))))
    _alive(C, P, t, 0.8, tail=False)
    return P


def _biped(C, t):
    """Two legs (a bird): the upper legs swing in turn, the lower leg folds back while its leg swings forward, the feet
    kept flat; the body sways onto the standing foot and the head bobs with each step."""
    P, N = Pose(C.I3), C.N
    S = C.cyc
    for side, ph in (("l", 0.0), ("r", 0.5)):
        th = TAU * (S * t / N + ph)
        a = RIG["leg_swing_biped"] * math.sin(th)                   # + forward
        fold = RIG["knee_fold_biped"] * max(0.0, math.cos(th)) ** 1.5
        leg, shin, foot = f"leg_{side}", f"shin_{side}", f"foot_{side}"
        if C.has(leg):
            C.abs(P, leg, C.E(leg, 0, -a, 0))
        if C.has(shin):
            C.abs(P, shin, C.E(shin, 0, fold, 0))
        if C.has(foot):
            C.abs(P, foot, C.E(foot, 0, a - fold, 0))            # flat: the leg's and the shin's pitch undone
    th0 = TAU * S * t / N
    P.body = C.Eb(4 * math.sin(th0), 0, 3 * math.sin(th0))
    if C.has("neck"):                                              # the bird's head bob: neck forward, head back
        C.add(P, "neck", C.E("neck", 0, 7 * math.sin(2 * th0), 0))
    if C.has("head"):
        C.add(P, "head", C.E("head", 0, -5 * math.sin(2 * th0), 0))
    for b in C.pair("wing"):                                       # the wings lift a little with every step
        lift = 0.5 + 0.5 * math.sin(2 * th0 + (0.0 if C.info[b]["side"] == "l" else 0.4))
        C.add(P, b, C.toward(b, (0, -1, 0.6), 10 * lift))
    if C.has("tail"):
        C.add(P, "tail", C.toward("tail", (0, 0, 1), 5 * math.sin(2 * th0)))
    _alive(C, P, t, 0.8)
    return P


def a_walk(C, t):
    if C.plan == "sprawler":
        return _sprawl(C, t)
    if not C.legs() and C.pair("leg"):
        return _biped(C, t)
    P, N = Pose(C.I3), C.N
    knees = any(C.has(f"shin_{k}") for k in ("fl", "fr", "hl", "hr"))
    A = RIG["leg_swing_knee"] if knees else RIG["leg_swing"]
    S = C.cyc
    ph = {"fl": 0.0, "hr": 0.0, "fr": 0.5, "hl": 0.5}          # diagonal pairs, like a block-game mob
    for k, p in ph.items():
        b = f"leg_{k}"
        if not C.has(b):
            continue
        th = TAU * (S * t / N + p)
        C.abs(P, b, C.E(b, 0, -A * math.sin(th), 0))           # + forward: -Y pitch brings the foot forward
        s = f"shin_{k}"
        if C.has(s):
            C.abs(P, s, C.E(s, 0, RIG["knee_fold"] * max(0.0, math.cos(th)) ** 1.5, 0))
    th0 = TAU * S * t / N
    Lf = RIG["life"]
    P.body = C.Eb(Lf["roll"] * math.sin(th0), 1.0 * math.sin(2 * th0), Lf["sway"] * math.sin(th0))
    if C.has("head"):
        C.add(P, "head", C.E("head", 0, 5 * math.sin(2 * th0 + 0.4), -3 * math.sin(th0)))
    if C.has("neck"):
        C.add(P, "neck", C.E("neck", 0, 3 * math.sin(2 * th0), 0))
    if C.has("mane"):
        C.add(P, "mane", C.E("mane", 0, 0, 2 * math.sin(th0)))
    if C.has("torso"):                                            # an upper body rolls with the stride (bear)
        C.add(P, "torso", C.E("torso", 0, 1.5 * math.sin(2 * th0), 3 * math.sin(th0)))
    for i, b in enumerate(b for b in ("tail", "tail_tip", "flukes") if C.has(b)):
        C.add(P, b, C.toward(b, (0, 1, 0), (9 + 5 * i) * math.sin(th0 - 0.5 * (i + 1))))
    for b in C.pair("ear"):                                        # ears bounce with each footfall
        C.add(P, b, C.toward(b, (-1, 0, 0), 6 * math.sin(2 * th0 + 0.8)))
    _trunk(C, P, t, curl=0.8, sway=1.4, k=S)
    if C.has("jaw"):
        yawn = C.o("walk_jaw", 0.0)              # a walking yawn (the hippo, owner 2026-11-21): the jaw opens wide
        if yawn > 0:                              # and closes once a loop, the head lifting as it opens
            x = (t % N) / N
            o = curve(x, [(0.0, 0.0), (0.12, 0.0), (0.36, 1.0), (0.58, 1.0), (0.82, 0.0), (1.0, 0.0)])
            C.abs(P, "jaw", C.E("jaw", 0, 2 + yawn * o, 0))
            if C.has("head"):
                C.add(P, "head", C.E("head", 0, -0.3 * yawn * o, 0))
        else:
            C.add(P, "jaw", C.E("jaw", 0, -5 * (0.5 + 0.5 * math.sin(2 * th0)), 0))
    _alive(C, P, t, 0.8, tail=False)
    return P


def a_flap(C, t):
    P, N = Pose(C.I3), C.N
    th = TAU * C.cyc * t / N
    lift = 0.5 - 0.5 * math.cos(th)
    for b in C.pair("wing"):
        if C.spread(b):
            C.add(P, b, C.toward(b, (0, 0, 1), 28 * math.sin(th)))
        else:
            C.add(P, b, C.toward(b, (0, -1, 0.6), 42 * lift))
    for b in C.pair("flipper"):
        C.add(P, b, C.toward(b, (0, -1, 0.3), 34 * (0.5 - 0.5 * math.cos(2 * th))))
    P.hop = 0.6 * lift
    for i, b in enumerate(C.pair("foot")):                        # the feet dangle and paddle while it lifts
        C.add(P, b, C.E(b, 0, 18 * lift + 6 * math.sin(2 * th + 0.5 * i) * lift, 0))
    for b in C.pair("leg"):
        C.add(P, b, C.E(b, 0, 8 * lift, 0))
    for b in ("tail", "tail_tip"):
        if C.has(b):
            C.add(P, b, C.toward(b, (0, 0, 1), 8 * math.sin(th - 0.6)))
    if C.has("head"):
        C.add(P, "head", C.E("head", 0, -4 * math.sin(th), 0))
    P.body = C.Eb(0, -3 * lift, 0)
    _alive(C, P, t, 0.7, wings=False, tail=False)
    return P


def a_hop(C, t):
    P, N = Pose(C.I3), C.N
    s = 24.0 / N
    t0 = t
    t = (t * C.cyc) % N                                             # the hop runs C.cyc times a loop
    u = (t * s - 6.0) / 12.0
    air = 4 * u * (1 - u) if 0.0 <= u <= 1.0 else 0.0
    push = curve(t * s, [(0, 0), (3, -0.25), (7, 1), (13, 0.5), (18, 0), (24, 0)])
    P.hop = RIG["hop_height"] * C.length * air
    for k in ("hl", "hr"):                                         # the hind legs push: the upper part swings back,
        if C.has(f"leg_{k}"):                                       # the lower part (foot) tips onto the toes
            C.add(P, f"leg_{k}", C.E(f"leg_{k}", 0, 36 * push, 0))
        if C.has(f"shin_{k}"):
            C.add(P, f"shin_{k}", C.E(f"shin_{k}", 0, 24 * push, 0))
    for k in ("fl", "fr"):                                         # the front legs reach forward in the air
        if C.has(f"leg_{k}"):
            C.add(P, f"leg_{k}", C.E(f"leg_{k}", 0, -26 * air + 6 * bump(t * s, 19, 1.6), 0))
        if C.has(f"shin_{k}"):
            C.add(P, f"shin_{k}", C.E(f"shin_{k}", 0, 14 * air, 0))
    for b in C.pair("leg"):                                       # a bird: legs tuck back in the air
        C.add(P, b, C.E(b, 0, 16 * air, 0))
    for b in C.pair("shin"):
        C.add(P, b, C.E(b, 0, 20 * air, 0))
    for i, b in enumerate(C.pair("foot")):                        # and the feet point their toes and paddle a little
        wig = 7.0 * math.sin(TAU * (2 * t * s / 24.0 + 0.25 * i)) * air          # (owner 2026-11-21: the toucan)
        land = 10.0 * bump(t * s, 19, 1.4)                         # toes flatten and spread as it lands
        C.add(P, b, C.E(b, 0, 30 * air + wig - land * 0.4, 0))
    P.body = C.Eb(0, -10 * curve(t * s, [(0, 0), (5, 0), (8, 1), (13, 0), (17, -0.6), (20, 0), (24, 0)]), 0)
    for b in C.pair("ear"):
        C.add(P, b, C.toward(b, (-1, 0, 0), 18 * air))
    for b in C.pair("wing"):
        C.add(P, b, C.toward(b, (0, -1, 0.6), 30 * air))
    if C.has("tail"):
        C.add(P, "tail", C.toward("tail", (0, 0, 1), 10 * air))
    if C.has("head"):
        C.add(P, "head", C.E("head", 0, 4 * air, 0))
    _alive(C, P, t0, 0.7)
    return P


def a_swim(C, t):
    P, N = Pose(C.I3), C.N
    th = TAU * t / N
    chain = [b for b in ("tail", "tail_tip", "flukes") if C.has(b)]
    if chain:                                                     # a dolphin: up-and-down strokes down the tail
        P.body = C.Eb(0, 3 * math.sin(th), 0)
        for i, b in enumerate(chain):
            C.add(P, b, C.toward(b, (0, 0, 1), (10 + 5 * i) * math.sin(th - 0.8 * (i + 1))))
        if C.has("head"):
            C.add(P, "head", C.E("head", 0, -3 * math.sin(th + 0.6), 0))
        for b in C.pair("flipper"):
            C.add(P, b, C.toward(b, (0, 0, 1), 8 * math.sin(th + 1.0)))
        P.hop = 0.8 * (0.5 + 0.5 * math.sin(th))
    else:                                                         # a turtle: front flippers row, the hind ones steer
        for b in C.pair("flipper"):
            C.add(P, b, C.toward(b, (-1, 0, 0), 26 * math.sin(th)))
            C.add(P, b, C.toward(b, (0, 0, 1), 10 * math.cos(th)))
        for b in C.hind("flipper"):
            C.add(P, b, C.toward(b, (-1, 0, 0), 10 * math.sin(th + math.pi)))
        if C.has("head"):
            C.add(P, "head", C.E("head", 0, 3 * math.sin(2 * th), 0))
        P.hop = 0.5 * (0.5 + 0.5 * math.sin(th - 0.5))
        P.body = C.Eb(RIG["life"]["roll"] * math.sin(th), 0, 0)
    _alive(C, P, t, 0.6, wings=False, tail=False)
    return P


def a_waddle(C, t):
    P, N = Pose(C.I3), C.N
    th = TAU * C.cyc * t / N
    P.body = C.Eb(8 * math.sin(th), 0, 5 * math.sin(th))
    for b in C.pair("foot"):
        up = max(0.0, math.sin(th) * (1 if C.info[b]["side"] == "r" else -1))
        C.add(P, b, C.E(b, 0, -14 * up, 0))
    for b in C.pair("flipper"):
        out = max(0.0, math.sin(th) * (1 if C.info[b]["side"] == "r" else -1))
        C.add(P, b, C.toward(b, (0, -1, 0.2), 14 * out))
    if C.has("head"):
        C.add(P, "head", C.E("head", -4 * math.sin(th), 0, 0))
    _alive(C, P, t, 0.8)
    return P


def a_howl(C, t):
    P, N = Pose(C.I3), C.N
    s = 48.0 / N
    H = C.o("howl_lift", 5.0)                    # how far the head lifts into the howl: a standing wolf (no howl in
    p = curve(t * s, [(0, 0), (12, 10), (20, -H), (40, -H), (48, 0)])   # its still) throws it right back
    band = curve(t * s, [(0, 0), (19, 0), (23, 1), (37, 1), (41, 0), (48, 0)])
    C.add(P, "head", C.E("head", 0, p + 1.5 * sn(t, 6) * band, 0))
    if C.has("neck"):                                             # the neck takes the breath and lifts into the howl
        C.add(P, "neck", C.E("neck", 0, 0.5 * p, 0))
    for b in C.pair("ear"):
        C.add(P, b, C.toward(b, (-1, 0, 0), 14 * curve(t * s, [(0, 0), (16, 0), (22, 1), (40, 1), (48, 0)])))
    if C.has("torso"):
        C.add(P, "torso", C.E("torso", 0, -2.5 * curve(t * s, [(0, 0), (10, 1), (20, 0), (48, 0)]), 0))
    _tail(C, P, t, 5)
    return P


def a_doze(C, t):
    P, N = Pose(C.I3), C.N
    s = 48.0 / N
    p = curve(t * s, [(0, 0), (28, 15), (32, 16), (35, -3), (40, 0), (48, 0)])
    C.add(P, "head", C.E("head", 0, p, 0))
    for b in C.pair("ear"):
        C.add(P, b, C.toward(b, (0, -1, -0.5), 0.5 * p))
    for b in C.pair("arm"):
        C.add(P, b, C.toward(b, (0, 0, -1), 0.15 * p))
    return P


def a_shake(C, t):
    P, N = Pose(C.I3), C.N
    env = math.sin(math.pi * t / N) ** 2
    s = 12 * sn(t, N, 3) * env
    if C.has("mane"):
        C.add(P, "mane", C.E("mane", s, 0, 0))
    C.add(P, "head", C.E("head", 0.6 * s, 0, 0))
    for b in C.pair("ear"):
        C.add(P, b, C.toward(b, (0, -1, 0), 12 * abs(sn(t, N, 3)) * env))
    _tail(C, P, t, 8)
    return P


def a_yawn(C, t):
    P, N = Pose(C.I3), C.N
    s = 48.0 / N
    o = curve(t * s, [(0, 0), (6, 0), (20, 1), (30, 1), (42, 0), (48, 0)])
    if C.has("jaw"):
        C.abs(P, "jaw", C.E("jaw", 0, 2 + 30 * o, 0))
    C.add(P, "head", C.E("head", 0, 14 * (1 - o), 0))
    for b in C.pair("ear"):
        C.add(P, b, C.toward(b, (0, -1, 0.4), 16 * bump(t * s, 40, 2.5)))
    return P


def a_fan(C, t):
    P, N = Pose(C.I3), C.N
    th = TAU * t / N
    for b in C.pair("ear"):
        C.add(P, b, C.E(b, 0, 0, 16 * sn(t, N, 2)))
    _trunk(C, P, t, curl=1.5, sway=1.2)
    C.add(P, "head", C.E("head", 0, 3 * math.sin(2 * th), -3 * math.sin(th)))
    _tail(C, P, t, 12, k=2)
    return P


def a_reach(C, t):
    P, N = Pose(C.I3), C.N
    s = 48.0 / N
    r = curve(t * s, [(0, 0), (8, 0), (22, 1), (32, 1), (44, 0), (48, 0)])
    if C.has("neck"):
        C.add(P, "neck", C.toward("neck", (1, 0, 0), 12 * r))
    C.add(P, "head", C.E("head", 0, -12 * r, 0))
    if C.has("tongue"):
        C.add(P, "tongue", C.E("tongue", 0, 0, 15 * sn(t, N, 4) * r))
    for b in C.pair("ear"):
        C.add(P, b, C.toward(b, (-1, 0, 0), 8 * r))
    return P


def a_sniff(C, t):
    P, N = Pose(C.I3), C.N
    s = 48.0 / N
    d = curve(t * s, [(0, 0), (10, 1), (38, 1), (48, 0)])
    C.add(P, "head", C.E("head", 0, 9 * d + 2.5 * sn(t, N, 8) * d, -4 * sn(t, N)))
    if C.has("neck"):
        C.add(P, "neck", C.E("neck", 0, 5 * d, 0))
    for b in ("snout", "muzzle", "nose"):
        if C.has(b):
            C.add(P, b, C.E(b, 0, 2 * sn(t, N, 16) * d, 0))
    _tail(C, P, t, 6, k=2)
    return P


ACTIONS = dict(pose=a_pose, idle=a_idle, walk=a_walk, flap=a_flap, hop=a_hop, swim=a_swim, waddle=a_waddle,
               howl=a_howl, doze=a_doze, shake=a_shake, yawn=a_yawn, fan=a_fan, reach=a_reach, sniff=a_sniff)


# ---- the rig ----------------------------------------------------------------------------------------------------------
def side_of(part):
    if "_" in part:
        suf = part.rsplit("_", 1)[1]
        if 1 <= len(suf) <= 2 and suf[-1] in "lr":
            return suf[-1]
    return None


def bone_info(grid):
    """Per bone: hinge (voxels), parent bone, still rotation, centroid offset from the hinge, side, sections."""
    from mathutils import Euler, Vector
    parts = grid.parts()
    jointed = {p for p in parts if p in grid.joints}
    body_vox = [pos for p, vs in parts.items() if p not in jointed for pos, _ in vs]
    cx = sum(x + 0.5 for x, _, _ in body_vox) / len(body_vox)
    zmin = min(z for _, _, z in body_vox)
    info = {}
    for p in sorted(jointed):
        j = grid.joints[p]
        par = j.get("parent")
        par = par if par in jointed else "body"
        vs = [pos for pos, _ in parts[p]]
        cen = Vector(tuple(sum(v[i] + 0.5 for v in vs) / len(vs) for i in range(3)))
        piv = Vector(j["pivot"])
        info[p] = dict(pivot=piv, parent=par, side=side_of(p), c=cen - piv, parts=[p],
                       still=Euler(tuple(math.radians(a) for a in j["rotate"]), "XYZ").to_matrix())
    body = dict(pivot=Vector((cx, 0.5, zmin)), parent="root", side=None, c=Vector((1.0, 0.0, 0.0)),
                parts=sorted(p for p in parts if p not in jointed))
    order, seen = [], set()

    def visit(b):
        if b in seen:
            return
        par = info[b]["parent"]
        if par in info:
            visit(par)
        seen.add(b)
        order.append(b)

    for b in sorted(info):
        visit(b)
    return info, body, order


class Solver:
    """Posed section matrices (voxels, rest grid -> posed grid) for one frame, with numpy, to ground and to frame."""

    def __init__(self, grid, info, body, order):
        import numpy as np
        from vf_voxel import CORNERS
        self.np, self.info, self.body, self.order = np, info, body, order
        self.pts = {}
        for part, vs in grid.parts().items():
            s = set()
            for (x, y, z), _ in vs:
                if grid.visible((x, y, z), part):
                    for dx, dy, dz in CORNERS:
                        s.add((x + dx, y + dy, z + dz))
            self.pts[part] = np.array(sorted(s), dtype=np.float64)
        self.owner = {p: b for b, d in info.items() for p in d["parts"]}
        for p in body["parts"]:
            self.owner[p] = "body"

    def mats(self, rots, body_rot):
        np = self.np

        def hinge(p, R):
            m = np.eye(4)
            Rn = np.array([list(r) for r in R])
            m[:3, :3] = Rn
            pv = np.array(tuple(p))
            m[:3, 3] = pv - Rn @ pv
            return m

        M = {"body": hinge(self.body["pivot"], body_rot)}
        for b in self.order:
            M[b] = M[self.info[b]["parent"]] @ hinge(self.info[b]["pivot"], rots[b])
        return M

    def points(self, M):
        np = self.np
        out = []
        for part, P in self.pts.items():
            m = M[self.owner[part]]
            out.append(P @ m[:3, :3].T + m[:3, 3])
        return np.concatenate(out)


def build_rig(grid, look_offset, motion):
    """Armature + the skinned mesh (rigid weights) + one action per entry of motion["actions"]. Returns a report."""
    import bpy
    import numpy as np
    from mathutils import Euler, Matrix, Vector
    import vf_standards as ST
    import vf_scene as V

    s = ST.VOXEL
    info, body, order = bone_info(grid)
    plan = motion.get("plan") or detect_plan(info)
    actions = list(motion.get("actions") or PLANS[plan])
    if "pose" not in actions:
        actions.insert(0, "pose")
    unknown = [a for a in actions if a not in ACTIONS]
    if unknown:
        raise ValueError(f"motion.actions: unknown {unknown} (library: {', '.join(ACTIONS)})")
    lift = look_offset                                        # the still's lift (voxels): the bind pose stands on it
    origin = Vector((body["pivot"].x, 0.5, 0.0))              # the armature (and the root) under the body's centre
    lo, hi = grid.posed_bounds()
    length = max(hi[i] - lo[i] for i in range(2))

    coll = bpy.data.collections["Animal"]
    ad = bpy.data.armatures.new("VF · armature")
    arm = bpy.data.objects.new("VF · armature", ad)
    coll.objects.link(arm)
    arm.location = origin * s
    ad.display_type = "OCTAHEDRAL"
    arm.show_in_front = True
    vl = bpy.context.view_layer
    for o in vl.objects:
        o.select_set(False)
    vl.objects.active = arm
    arm.select_set(True)
    bpy.ops.object.mode_set(mode="EDIT")

    def local(p):                                            # grid voxels (rest) -> armature space, metres
        return Vector((p[0] - origin.x, p[1] - origin.y, p[2] + lift - origin.z)) * s

    lo_b, hi_b = RIG["bone"]
    eb = ad.edit_bones.new("root")
    eb.head, eb.tail, eb.roll = Vector((0, 0, 0)), Vector((4 * s, 0, 0)), 0.0
    eb = ad.edit_bones.new("body")
    eb.head = local(body["pivot"])
    eb.tail = eb.head + Vector((max(lo_b, min(hi_b, 6.0)) * s, 0, 0))
    eb.roll, eb.parent, eb.use_connect = 0.0, ad.edit_bones["root"], False
    for b in order:
        d = info[b]
        e = ad.edit_bones.new(b)
        e.head = local(d["pivot"])
        c = d["c"]
        ln = max(lo_b, min(hi_b, c.length))
        dirn = c.normalized() if c.length > 1e-3 else Vector((0, 0, 1))
        e.tail = e.head + dirn * ln * s
        e.roll, e.parent, e.use_connect = 0.0, ad.edit_bones[d["parent"]], False
    bpy.ops.object.mode_set(mode="OBJECT")
    vl.update()

    Rb = {b.name: b.matrix_local.to_3x3() for b in ad.bones}
    Rbi = {k: m.inverted() for k, m in Rb.items()}

    # the skin: every section back in the bind pose (unturned, on the still's lift), all its vertices weighted 1.0 to
    # its bone (rigid: the blocks stay crisp), joined into one mesh deformed by an Armature modifier
    secs = []
    for p in sorted(grid.parts()):
        o = bpy.data.objects.get(f"VF · {p}")
        if o is None:
            raise KeyError(f"no object 'VF · {p}' in the built .blend")
        j = grid.joints.get(p)
        piv = j["pivot"] if j else (0.0, 0.0, 0.0)
        o.parent = None
        o.matrix_world = Matrix.Translation(Vector((piv[0], piv[1], piv[2] + lift)) * s)
        bone = p if p in info else "body"
        vg = o.vertex_groups.get(bone) or o.vertex_groups.new(name=bone)
        vg.add(list(range(len(o.data.vertices))), 1.0, "REPLACE")
        secs.append(o)
    vl.update()
    for o in vl.objects:
        o.select_set(o in secs)
    body_obj = bpy.data.objects["VF · body"]
    vl.objects.active = body_obj
    bpy.ops.object.join()
    mesh = body_obj
    mesh.name = mesh.data.name = "VF · animal"
    mw = mesh.matrix_world.copy()
    mesh.parent = arm
    mesh.parent_type = "OBJECT"
    mesh.matrix_parent_inverse = arm.matrix_world.inverted()
    mesh.matrix_world = mw
    mod = mesh.modifiers.new("VF armature", "ARMATURE")
    mod.object = arm
    mod.use_vertex_groups = True
    mod.use_bone_envelopes = False
    if V.DEPTH_ATTR in mesh.data.attributes:        # the stacking bias after the deform (vf_standards.STACK_LEVELS)
        V.add_depth_bias(mesh)
    for o in vl.objects:
        o.select_set(False)
    vl.update()
    unweighted = sum(1 for v in mesh.data.vertices if not v.groups)
    if unweighted:
        raise ValueError(f"{unweighted} vertices carry no bone weight")

    solver = Solver(grid, info, body, order)
    I3 = Matrix.Identity(3)
    still = {b: info[b]["still"] for b in order}
    z_still = float(solver.points(solver.mats(still, I3))[:, 2].min())
    log(f"rig: {len(order) + 2} bones ({plan}), still grounded at {-z_still:+.2f} voxels "
        f"(the built scene: {lift:+.2f})")

    q_view, right, up, back = V.view_axes()
    R_np = np.array([list(right), list(up), list(back)])
    extremes = []
    arm.animation_data_create()
    report = dict(plan=plan, bones=len(order) + 2, actions={})
    pbs = arm.pose.bones
    for pb in pbs:
        pb.rotation_mode = "QUATERNION"
    for name in actions:
        n = RIG["frames"][name]
        if name == "walk" and length >= RIG["large"]:
            n = RIG["frames"]["walk_large"]
        n = int((motion.get("frames") or {}).get(name, n))
        base = {b: still[b] for b in order}
        for b, e in ((motion.get("base") or {}).get(name) or {}).items():      # still angles replaced for this action
            if b in base:
                base[b] = Euler(tuple(math.radians(a) for a in e), "XYZ").to_matrix()
        C = Ctx(info, plan, n, base)
        C.length = length
        C.opt = dict(motion.get("options") or {})
        C.cyc = int(RIG.get("cycles", {}).get(name, 1))
        act = bpy.data.actions.new(name)
        act.use_fake_user = True
        arm.animation_data.action = act
        prev = {}
        frames = [0] if name == "pose" else list(range(n + 1))
        lows = []
        for f in frames:
            P = ACTIONS[name](C, f % n if n > 1 else 0)
            rots = {}
            for b in order:
                mode, off = P.rot.get(b, ("add", I3))
                rots[b] = off if mode == "abs" else base[b] @ off
            M = solver.mats(rots, P.body)
            pts = solver.points(M)
            z = float(pts[:, 2].min())
            lows.append(-z)
            dz = (-z - lift) + P.hop
            # extreme points for the camera (world metres)
            wp = (pts + np.array([0.0, 0.0, -z + P.hop])) * s
            proj = wp @ R_np.T
            for k in range(3):
                extremes.append(Vector(tuple(wp[int(proj[:, k].argmin())])))
                extremes.append(Vector(tuple(wp[int(proj[:, k].argmax())])))
            for b, R in list(rots.items()) + [("body", P.body)]:
                q = (Rbi[b] @ R @ Rb[b]).to_quaternion()
                if b in prev:
                    q.make_compatible(prev[b])
                prev[b] = q
                pbs[b].rotation_quaternion = q
                pbs[b].keyframe_insert("rotation_quaternion", frame=f, group=b)
            pbs["root"].location = Rbi["root"] @ Vector((0.0, 0.0, dz * s))
            pbs["root"].keyframe_insert("location", frame=f, group="root")
        act.use_frame_range = True
        act.frame_start, act.frame_end = 0, max(1, frames[-1])
        try:
            act.use_cyclic = name != "pose"
        except Exception:
            pass
        report["actions"][name] = dict(frames=n, keys=len(frames), lowest=[round(min(lows), 2), round(max(lows), 2)])
        log(f"action {name}: {n} frames at {RIG['fps']} fps")
    # rest the file on the still pose, idle active
    for pb in pbs:
        pb.rotation_quaternion = (1, 0, 0, 0)
        pb.location = (0, 0, 0)
        pb.scale = (1, 1, 1)
    arm.animation_data.action = bpy.data.actions.get("idle") or bpy.data.actions.get("pose")
    arm["vf_actions"] = actions
    arm["vf_plan"] = plan
    report["vertices"] = len(mesh.data.vertices)
    report["groups"] = sorted(g.name for g in mesh.vertex_groups)
    return arm, actions, extremes, report


def anim_scene(extremes, readme):
    """Keep one scene, "ANIM 1x1", framed on everything every action does; drop the six still compositions."""
    import bpy
    import vf_standards as ST
    import vf_scene as V
    cur = bpy.context.scene
    bg = cur.get("vf_background")
    for sc in list(bpy.data.scenes):
        for o in list(sc.collection.objects):
            if o.type == "CAMERA":
                bpy.data.objects.remove(o)
        if sc != cur:
            bpy.data.scenes.remove(sc)
    cur.name = "ANIM 1x1"
    w, h = ST.SIZES["1x1"]
    fr = V.frame("ILL", "1x1", extremes, w, h)
    V.camera(cur, "CAM · ANIM 1x1", fr)
    V.apply_profile(cur, "ULTRA", "1x1")
    cur["vf_background"] = bg
    cur["vf_profile"] = "ULTRA"
    cur.render.fps = RIG["fps"]
    cur.frame_start, cur.frame_end = 0, RIG["frames"]["idle"] - 1
    for t in list(bpy.data.texts):
        if t.name.startswith("README"):
            bpy.data.texts.remove(t)
    bpy.data.texts.new("README").write(readme)
    return cur, fr


def export_glb(arm, path):
    import bpy
    keep = arm.location.copy()
    arm.location = (0.0, 0.0, 0.0)
    bpy.context.view_layer.update()
    for o in bpy.context.view_layer.objects:
        o.select_set(o == arm or o.parent == arm)
    bpy.context.view_layer.objects.active = arm
    want = dict(filepath=path, export_format="GLB", use_selection=True, export_animations=True,
                export_animation_mode="ACTIONS", export_apply=False, export_yup=True, export_cameras=False,
                export_lights=False, export_force_sampling=True, export_frame_step=1, export_def_bones=False,
                export_materials="EXPORT")
    props = set(bpy.ops.export_scene.gltf.get_rna_type().properties.keys())
    skipped = [k for k in want if k not in props]
    bpy.ops.export_scene.gltf(**{k: v for k, v in want.items() if k in props})
    arm.location = keep
    bpy.context.view_layer.update()
    log(f"glb: {path}" + (f" (exporter has no {skipped})" if skipped else ""))


# ---- the rig check (owner, 2026-11-17: "check whether the animal is rigged properly ... at T posed render") ------------
CHECK = dict(size=768, bend=30.0, show_bend=24.0, moved=1e-5)


def _coords(mesh):
    """World positions of the deformed mesh's vertices (numpy, n x 3)."""
    import bpy
    import numpy as np
    dg = bpy.context.evaluated_depsgraph_get()
    ev = mesh.evaluated_get(dg)
    me = ev.to_mesh()
    co = np.empty(len(me.vertices) * 3, dtype=np.float64)
    me.vertices.foreach_get("co", co)
    ev.to_mesh_clear()
    M = np.array(mesh.matrix_world)
    return co.reshape(-1, 3) @ M[:3, :3].T + M[:3, 3]


def _hue(i):
    import colorsys
    return colorsys.hsv_to_rgb((0.07 + i * 0.618034) % 1.0, 0.68, 0.96)


def _gizmo(arm, name, coll):
    """An octahedral bone like Blender's, as a mesh riding the bone (background Blender draws no overlays)."""
    import bpy
    from mathutils import Matrix
    L = arm.data.bones[name].length
    w = 0.18 * L
    verts = [(0, 0, 0), (w, 0.15 * L, 0), (0, 0.15 * L, w), (-w, 0.15 * L, 0), (0, 0.15 * L, -w), (0, L, 0)]
    faces = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1), (5, 2, 1), (5, 3, 2), (5, 4, 3), (5, 1, 4)]
    j = 0.035                                                    # a joint marker on the hinge (3.5 cm)
    verts += [(x * j, y * j, z * j) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]
    faces += [(6, 7, 9, 8), (10, 12, 13, 11), (6, 10, 11, 7), (8, 9, 13, 12), (6, 8, 12, 10), (7, 11, 13, 9)]
    me = bpy.data.meshes.new(f"gizmo {name}")
    me.from_pydata(verts, [], faces)
    o = bpy.data.objects.new(f"gizmo {name}", me)
    coll.objects.link(o)
    o.parent, o.parent_type, o.parent_bone = arm, "BONE", name
    o.matrix_parent_inverse = Matrix.Translation((0.0, -L, 0.0))     # a bone child sits on the tail: back to the head
    o.color = (0.98, 0.80, 0.08, 1.0)                            # bone yellow, outlined black: reads on any colour
    return o


def rig_check(arm, mesh, out_dir):
    """Every vertex weighted to exactly one bone; every bone bent in turn moves its own section and everything below
    it, and nothing else; renders of the rest pose (the T-pose) and of every bone bent, sections coloured by bone,
    with the bones drawn on top."""
    import bpy
    import numpy as np
    from mathutils import Quaternion, Vector
    import vf_scene as V
    vl = bpy.context.view_layer
    ad = arm.data
    if arm.animation_data:
        arm.animation_data.action = None
    pbs = arm.pose.bones
    for pb in pbs:
        pb.rotation_mode = "QUATERNION"
        pb.rotation_quaternion = (1, 0, 0, 0)
        pb.location = (0, 0, 0)
        pb.scale = (1, 1, 1)
    vl.update()
    gname = {g.index: g.name for g in mesh.vertex_groups}
    gi = np.array([v.groups[0].group if len(v.groups) == 1 else -1 for v in mesh.data.vertices])
    weights_ok = all(len(v.groups) == 1 and abs(v.groups[0].weight - 1.0) < 1e-6 for v in mesh.data.vertices)
    counts = {gname[i]: int((gi == i).sum()) for i in gname}
    rest = _coords(mesh)
    bones = [b.name for b in ad.bones]
    rows, ok_all = [], weights_ok
    for b in ad.bones:
        if b.name == "root":
            rows.append(dict(bone="root", parent=None, verts=0, ok=True, note="carries grounding and hops"))
            continue
        expected = ({b.name} | {c.name for c in b.children_recursive}) & {n for n, k in counts.items() if k}
        pbs[b.name].rotation_quaternion = Quaternion((1.0, 0.0, 0.0), math.radians(CHECK["bend"]))
        vl.update()
        moved = np.linalg.norm(_coords(mesh) - rest, axis=1) > CHECK["moved"]
        pbs[b.name].rotation_quaternion = (1, 0, 0, 0)
        got = {gname[i] for i in np.unique(gi[moved]) if i >= 0}
        ok = got == expected and counts.get(b.name, 0) > 0
        ok_all &= ok
        rows.append(dict(bone=b.name, parent=b.parent.name if b.parent else None, verts=counts.get(b.name, 0), ok=ok,
                         moved=sorted(got), expected=sorted(expected)))
    vl.update()
    missing = [b for b in bones if b != "root" and not counts.get(b)]
    stray = [g for g in counts if g not in bones]
    ok_all &= not missing and not stray
    colour = {b: _hue(i) for i, b in enumerate(x for x in bones if x != "root")}

    # renders: Workbench, flat studio light, the sections coloured by bone; the bones in a second pass drawn on top
    ca = mesh.data.color_attributes.new("VF bone", "FLOAT_COLOR", "POINT")
    flat = np.zeros((len(mesh.data.vertices), 4), dtype=np.float32)
    flat[:, 3] = 1.0
    for i, n in gname.items():
        c = colour.get(n, (0.5, 0.5, 0.5))
        flat[gi == i, :3] = [x ** 2.2 for x in c]
    ca.data.foreach_set("color", flat.ravel())
    try:
        mesh.data.color_attributes.active_color = ca
        mesh.data.color_attributes.render_color_index = mesh.data.color_attributes.active_color_index
    except Exception:
        pass
    sc = bpy.data.scenes.new("RIG CHECK")
    sc.collection.children.link(bpy.data.collections["Animal"])
    gz = bpy.data.collections.new("Gizmos")
    sc.collection.children.link(gz)
    for b in bones:
        _gizmo(arm, b, gz)
    sc.render.engine = "BLENDER_WORKBENCH"
    sc.render.resolution_x = sc.render.resolution_y = CHECK["size"]
    sc.render.resolution_percentage = 100
    sc.render.film_transparent = True
    sc.render.image_settings.file_format = "PNG"
    sc.render.image_settings.color_mode = "RGBA"
    sc.view_settings.view_transform = "Standard"
    sh = sc.display.shading
    sh.light = "STUDIO"
    sh.show_object_outline = True
    sh.object_outline_color = (0.0, 0.0, 0.0)

    def pose_bent(on):
        for i, b in enumerate(bones):
            q = (1, 0, 0, 0)
            if on and b not in ("root", "body"):
                q = Quaternion((1.0, 0.0, 0.0), math.radians(CHECK["show_bend"] * (1 if i % 2 else -1)))
            pbs[b].rotation_quaternion = q
        vl.update()

    pose_bent(True)
    bent = _coords(mesh)
    pose_bent(False)
    q_view, right, up, back = V.view_axes()
    allp = np.concatenate([rest, bent])
    R = np.array([list(right), list(up), list(back)])
    pr = allp @ R.T
    ext = [Vector(tuple(allp[int(pr[:, k].argmin())])) for k in range(3)] + \
          [Vector(tuple(allp[int(pr[:, k].argmax())])) for k in range(3)]
    fr = V.frame("ILL", "1x1", ext, CHECK["size"], CHECK["size"])
    V.camera(sc, "CAM · RIG CHECK", fr)
    os.makedirs(out_dir, exist_ok=True)
    images = {}
    for state in ("rest", "bent"):
        pose_bent(state == "bent")
        for layer in ("animal", "bones"):
            mesh.hide_render = layer == "bones"
            gz.hide_render = layer == "animal"
            sh.color_type = "VERTEX" if layer == "animal" else "OBJECT"
            sc.render.filepath = os.path.join(out_dir, f"{state}-{layer}.png")
            bpy.ops.render.render(write_still=True, scene=sc.name)
            images[f"{state}-{layer}"] = sc.render.filepath
    mesh.hide_render = False
    pose_bent(False)
    for o in list(gz.objects):
        bpy.data.objects.remove(o)
    bpy.data.collections.remove(gz)
    bpy.data.scenes.remove(sc)
    mesh.data.color_attributes.remove(mesh.data.color_attributes["VF bone"])
    log(f"rig check: {'PASS' if ok_all else 'FAIL'} ({len(bones)} bones, {len(mesh.data.vertices)} vertices, "
        f"{sum(1 for r in rows if not r['ok'])} bones failing)")
    return dict(ok=bool(ok_all), weights_ok=bool(weights_ok), missing=missing, stray=stray, rows=rows,
                colours={b: "#%02X%02X%02X" % tuple(round(x * 255) for x in c) for b, c in colour.items()},
                images=images)


def _composite(pa, ps, bg_hex, out_png):
    """One preview frame: the animal pass over the exact background, darkened by the shadow pass. The same maths as
    vf_scene.render (its helpers, its SHADOW numbers), without the dither: previews are quantised to GIF anyway."""
    import bpy
    import numpy as np
    import vf_standards as ST
    import vf_scene as V
    A, S = V._load(pa), V._load(ps)
    La, sa = V._to_lin(S[..., :3]), S[..., 3]
    open_ = sa > 0.99
    g0 = np.percentile(La[open_], 90, axis=0) if open_.sum() >= 100 else np.ones(3, dtype=np.float32)
    s = np.ones_like(La)
    ok = sa > 0.01
    s[ok] = np.clip(La[ok] / g0, 0.0, 1.0)
    r = max(1, round(ST.SHADOW["smooth"] * min(s.shape[:2])))
    s = V._smooth_shadow(s, np.where(ok, sa, 0.0), r)        # no halo along the silhouette (vf_scene)
    t = ST.SHADOW["deadzone"]
    d = np.clip(((1.0 - s) - t) / (1.0 - t), 0.0, 1.0)
    s = 1.0 - ST.SHADOW["strength"] * d
    T = np.array([V._lin(c) for c in V.srgb(bg_hex)], dtype=np.float32)
    bg = V._to_srgb(T * s)
    alpha = A[..., 3:4]
    out = np.clip(np.round((A[..., :3] * alpha + bg * (1.0 - alpha)) * 255.0) / 255.0, 0.0, 1.0)
    h, w = out.shape[:2]
    img = bpy.data.images.new("vf anim frame", w, h, alpha=False, float_buffer=False)
    img.colorspace_settings.name = "Non-Color"
    img.pixels.foreach_set(np.concatenate([out, np.ones((h, w, 1), dtype=np.float32)], axis=-1).ravel())
    img.filepath_raw = out_png
    img.file_format = "PNG"
    img.save()
    bpy.data.images.remove(img)


def render_frames(arm, scene, action, out_dir, step, work):
    """Preview frames of one action: the animal pass and the shadow pass each rendered as one animation (a holdout
    switch per frame costs EEVEE a resync), then composited frame by frame like the stills."""
    import bpy
    import vf_standards as ST
    import vf_scene as V
    ST.PROFILES["ANIM"] = dict(ST.PROFILES["LOW"], scale=RIG["preview_scale"])
    P = ST.PROFILES["ANIM"]
    act = bpy.data.actions[action]
    arm.animation_data.action = act
    try:
        if arm.animation_data.action_slot is None and len(act.slots):
            arm.animation_data.action_slot = act.slots[0]
    except Exception:
        pass
    n = max(1, int(act.frame_end))
    os.makedirs(out_dir, exist_ok=True)
    for old in os.listdir(out_dir):
        if old.endswith(".png"):
            os.remove(os.path.join(out_dir, old))
    tmp = os.path.join(work, "anim", action)
    os.makedirs(tmp, exist_ok=True)
    V.apply_profile(scene, "ANIM", "1x1")
    scene.frame_start, scene.frame_end, scene.frame_step = 0, n - 1, step
    scene.render.film_transparent = True
    ground, animal = V._ground(), V._animal_objects()
    t0 = time.time()
    for kind in ("a", "s"):
        ground.is_holdout = kind == "a"
        for o in animal:
            o.is_holdout = kind == "s"
        if kind == "a":
            scene.view_settings.view_transform, scene.view_settings.look = ST.COLOR["view"], ST.COLOR["look"]
            scene.eevee.taa_render_samples = P["eevee"]["taa_render_samples"]
        else:
            scene.view_settings.view_transform, scene.view_settings.look = "Standard", "None"
            scene.eevee.taa_render_samples = P.get("shadow_samples", P["eevee"]["taa_render_samples"])
        scene.render.filepath = os.path.join(tmp, f"{kind}_####")
        V.depth_bias(kind == "a")                # stacked sections over their parents; the shadow pass exact
        try:
            bpy.ops.render.render(animation=True, scene=scene.name)
        finally:
            V.depth_bias(False)
    ground.is_holdout = False
    for o in animal:
        o.is_holdout = False
    scene.view_settings.view_transform, scene.view_settings.look = ST.COLOR["view"], ST.COLOR["look"]
    outs = []
    for f in range(0, n, step):
        p = os.path.join(out_dir, f"{f:03d}.png")
        _composite(os.path.join(tmp, f"a_{f:04d}.png"), os.path.join(tmp, f"s_{f:04d}.png"),
                   scene["vf_background"], p)
        outs.append(p)
    scene.frame_start, scene.frame_end, scene.frame_step = 0, RIG["frames"]["idle"] - 1, 1
    log(f"rendered {action}: {len(outs)} frames in {time.time() - t0:.0f} s")
    return outs


def main():
    job_path = sys.argv[sys.argv.index("--") + 1]
    job = json.load(open(job_path, encoding="utf-8"))
    result = dict(ok=False, started=time.strftime("%Y-%m-%d %H:%M:%S"))
    try:
        import bpy
        import vf_scene as V
        from vf_voxel import load_model
        result["blender"] = bpy.app.version_string
        if job.get("open_rig"):                       # check an existing rig only
            bpy.ops.wm.open_mainfile(filepath=job["open_rig"])
            log(f"opened {job['open_rig']}")
            arm, mesh = bpy.data.objects["VF · armature"], bpy.data.objects["VF · animal"]
            result["check"] = rig_check(arm, mesh, job["check"]["dir"])
            result["ok"] = True
            raise StopIteration
        bpy.ops.wm.open_mainfile(filepath=job["open"])
        log(f"opened {job['open']}")
        grid = load_model(job["model"])
        arm, actions, extremes, rep = build_rig(grid, V.ground_offset(grid), job.get("motion") or {})
        result["rig"] = rep
        scene, fr = anim_scene(extremes, job.get("readme", ""))
        result["frame"] = dict(ortho_scale=fr["ortho_scale"], box_size=fr["box_size"])
        os.makedirs(os.path.dirname(job["blend"]), exist_ok=True)
        bpy.ops.wm.save_as_mainfile(filepath=job["blend"], compress=True)
        log(f"saved {job['blend']}")
        if job.get("glb"):
            export_glb(arm, job["glb"])
        if job.get("check"):
            result["check"] = rig_check(arm, bpy.data.objects["VF · animal"], job["check"]["dir"])
        result["actions"] = actions
        result["fps"] = RIG["fps"]
        result["renders"] = {}
        pv = job.get("preview")
        if pv:
            step = int(pv.get("step", RIG["preview_step"]))
            result["step"] = step
            for name in pv.get("actions") or [a for a in actions if a != "pose"]:
                result["renders"][name] = render_frames(arm, scene, name, os.path.join(pv["dir"], name), step,
                                                        job["work"])
        result["ok"] = True
    except StopIteration:
        pass
    except Exception as e:
        result["error"] = f"{type(e).__name__}: {e}"
        result["trace"] = traceback.format_exc()
        print("VF: FAILED", result["error"], flush=True)
    result["finished"] = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(job["result"], "w", encoding="utf-8") as f:
        json.dump(result, f, indent=1, default=str)


if __name__ == "__main__":
    main()
