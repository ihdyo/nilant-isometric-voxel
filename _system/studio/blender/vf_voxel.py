"""Voxel Fauna · the voxel grid every animal model is written in (plain Python, no bpy).

An animal's `blender/model.py` defines `build(g)` and fills a Grid with voxels. A voxel is an integer cell (x, y, z):
it occupies [x, x+1] x [y, y+1] x [z, z+1] voxels of VOXEL metres. Conventions (vf_standards.FACING):
  +X  the head end          -X  the tail end
  -Y  the animal's left     +Y  its right       (the column y = 0 is the centre line: odd widths are symmetric
                                                 about it; as a coordinate the centre plane is y = 0.5, the middle of
                                                 that column, so a centred hinge has pivot y = 0.5)
  +Z  up; the feet stand on z = 0 (nothing below it in the rest pose)
Every voxel carries a colour key (a key of animal.json -> look.palette, never a raw colour) and a part name (the
Blender object it lands in: body, head, leg_fl, ear_l, tail, ...).

Sections (owner, 2026-11-16: "on assembling them, they can rotate the section so it looks more dynamic"): every part
is modelled in place in the rest pose, then `joint` turns it about a pivot (its hinge: the top of a leg, the base of
an ear, the neck) and may hang it on a parent part so it follows the parent's turn (ears and brows on the head).
`plate` makes a flat surface: a one-voxel-thick box squashed to a thin plate (feet, brows, wing tips).

Left and right: model the left side (y < 0) and the centre, then `mirror()`. A part whose name ends in "_l" or a
two-letter "_?l" (ear_l, leg_fl, leg_hl) is copied to the matching "_r" part (ear_r, leg_fr, leg_hr) with its joint
mirrored; parts on the centre line (body, head) are mirrored into themselves. Joints set after `mirror()` override the
mirrored ones (an asymmetric pose: one leg forward, one ear down).

Typical model:
    def build(g):
        g.box((0, -3, 4), (13, 3, 9), "fur", part="body")          # inclusive corners
        g.box((2, -3, 0), (3, -2, 3), "fur", part="leg_fl")
        g.joint("leg_fl", pivot=(3, -2, 4), rotate=(0, 12, 0))      # swing the front leg forward 12 degrees
        g.box((14, -3, 7), (19, 3, 12), "fur", part="head")
        g.joint("head", pivot=(14, 0.5, 9), rotate=(8, 0, -12))     # tilt and turn the head towards the camera
        g.plate((16, -3, 13), (17, -2, 13), "fur", part="ear_l")   # a flat ear
        g.joint("ear_l", pivot=(16.5, -2, 13), rotate=(-20, 0, 0), parent="head")
        g.mirror()
"""
import math

LIMB_STEMS = ("leg", "shin", "foot", "flipper", "arm", "wing")   # hinged on their parent's face by design
ANCHOR_REACH = 2.5         # voxels from a section's hinge within which Grid.anchor() sinks it into its parent
FACES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
CORNERS = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1))


def side_twin(part):
    """'ear_l' -> 'ear_r', 'leg_fl' -> 'leg_fr', 'ear_r' -> 'ear_l'; anything else -> itself."""
    if "_" in part:
        head, suf = part.rsplit("_", 1)
        if 1 <= len(suf) <= 2 and suf[-1] in "lr":
            return f"{head}_{suf[:-1]}{'r' if suf[-1] == 'l' else 'l'}"
    return part


# ---- 4 x 4 affine matrices (row-major lists), voxel units --------------------------------------------------------------
def _mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def _translate(t):
    return [[1, 0, 0, t[0]], [0, 1, 0, t[1]], [0, 0, 1, t[2]], [0, 0, 0, 1]]


def _rotate(deg):
    """Euler XYZ in degrees, as Blender's rotation_euler (X applied first): R = Rz . Ry . Rx."""
    x, y, z = (math.radians(d) for d in deg)
    cx, sx, cy, sy, cz, sz = math.cos(x), math.sin(x), math.cos(y), math.sin(y), math.cos(z), math.sin(z)
    rx = [[1, 0, 0, 0], [0, cx, -sx, 0], [0, sx, cx, 0], [0, 0, 0, 1]]
    ry = [[cy, 0, sy, 0], [0, 1, 0, 0], [-sy, 0, cy, 0], [0, 0, 0, 1]]
    rz = [[cz, -sz, 0, 0], [sz, cz, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    return _mul(rz, _mul(ry, rx))


def apply(m, p):
    return tuple(m[i][0] * p[0] + m[i][1] * p[1] + m[i][2] * p[2] + m[i][3] for i in range(3))


IDENTITY = _translate((0, 0, 0))


class Grid:
    """Each part is its own layer of voxels: a box drawn for one part never removes another part's voxels, so where
    sections overlap (an ear set into the head, the head set into the mane) both stay whole and the sections stack
    like assembled blocks; a section that turns never leaves a hole in its neighbour (owner, 2026-11-16: "stack the
    block, dont make a hole of it")."""

    def __init__(self):
        self.layers = {}                  # part -> {(x, y, z): colour key}, in the order the parts were started
        self.joints = {}                  # part -> dict(pivot, rotate, parent, scale, scale_pivot)
        self.anchored = {}                # part -> cells sunk into its parent by anchor()
        self._merged = None

    def _put(self, pos, color, part):
        self.layers.setdefault(part, {})[pos] = color
        self._merged = None

    @property
    def v(self):
        """Every occupied cell -> (colour key, part); where parts overlap, the part started last is listed."""
        if self._merged is None:
            m = {}
            for part, layer in self.layers.items():
                for pos, c in layer.items():
                    m[pos] = (c, part)
            self._merged = m
        return self._merged

    def has(self, pos, part=None):
        """Is the cell filled (by `part`, or by any part)?"""
        return pos in self.layers.get(part, {}) if part else pos in self.v

    # ---- filling --------------------------------------------------------------------------------------------------
    def set(self, x, y, z, color, part="body"):
        self._put((int(x), int(y), int(z)), color, part)

    def box(self, a, b, color, part="body"):
        """Fill the inclusive box between corners a and b (in that part's own layer)."""
        (x0, x1), (y0, y1), (z0, z1) = (sorted((a[i], b[i])) for i in range(3))
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                for z in range(z0, z1 + 1):
                    self._put((x, y, z), color, part)

    def ellipsoid(self, center, radii, color, part="body"):
        """Fill voxels whose centres fall inside the ellipsoid (not used in the blocky-mob style)."""
        cx, cy, cz = center
        rx, ry, rz = radii
        for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
            for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
                for z in range(int(cz - rz) - 1, int(cz + rz) + 2):
                    px, py, pz = x + 0.5 - cx, y + 0.5 - cy, z + 0.5 - cz
                    if (px / rx) ** 2 + (py / ry) ** 2 + (pz / rz) ** 2 <= 1.0:
                        self._put((x, y, z), color, part)

    def paint(self, a, b, color, part=None, only=None, of=None):
        """Recolour voxels already in the box: `only` limits it to one colour key, `of` to one part; `part` moves the
        painted voxels into another part."""
        (x0, x1), (y0, y1), (z0, z1) = (sorted((a[i], b[i])) for i in range(3))
        for p, layer in list(self.layers.items()):
            if of and p != of:
                continue
            for k, c in list(layer.items()):
                if x0 <= k[0] <= x1 and y0 <= k[1] <= y1 and z0 <= k[2] <= z1 and (only is None or c == only):
                    if part and part != p:
                        del layer[k]
                        self._put(k, color, part)
                    else:
                        layer[k] = color
        self._merged = None

    def carve(self, a, b, of=None):
        """Remove every voxel in the box (of one part, or of every part)."""
        (x0, x1), (y0, y1), (z0, z1) = (sorted((a[i], b[i])) for i in range(3))
        for p, layer in self.layers.items():
            if of and p != of:
                continue
            for k in [k for k in layer if x0 <= k[0] <= x1 and y0 <= k[1] <= y1 and z0 <= k[2] <= z1]:
                del layer[k]
        self._merged = None

    def plate(self, a, b, color, part, thickness=0.2, keep=None):
        """A flat surface: the box (one voxel thick on one axis) squashed to `thickness` voxel on that axis. `keep` is
        the face that stays where it is ("-z", "+x", ...); by default the bottom of a lying plate (feet on the
        ground), the back of a plate facing +X or -X (brows on a face), and the inner side of a plate facing the flank."""
        self.box(a, b, color, part)
        lo = [min(a[i], b[i]) for i in range(3)]
        hi = [max(a[i], b[i]) + 1 for i in range(3)]
        thin = [i for i in range(3) if hi[i] - lo[i] == 1]
        if not thin:
            raise ValueError(f"plate {part}: the box must be one voxel thick on one axis")
        ax = 2 if 2 in thin else thin[0]
        if keep is None:
            keep = {2: "-z", 0: "-x"}.get(ax) or ("+y" if hi[1] <= 0 else "-y")
        ax = "xyz".index(keep[1])
        sp = [(lo[i] + hi[i]) / 2 for i in range(3)]
        sp[ax] = lo[ax] if keep[0] == "-" else hi[ax]
        sc = [1.0, 1.0, 1.0]
        sc[ax] = float(thickness)
        j = self.joints.setdefault(part, dict(pivot=tuple(sp), rotate=(0.0, 0.0, 0.0), parent=None))
        j["scale"], j["scale_pivot"] = tuple(sc), tuple(sp)

    def joint(self, part, pivot, rotate=(0, 0, 0), parent=None):
        """Turn a part about `pivot` (voxel coordinates; halves allowed: a hinge sits on a face or an edge) by Euler
        XYZ degrees, after its `parent` part's own turn (so ears follow the head):
          X  roll: + tips the top towards -Y (the camera side); a hanging part's lower end swings towards +Y
          Y  pitch: + puts a +X end down (nose down) and a -X end up (tail up); a hanging leg's foot goes back
          Z  yaw: + turns +X towards +Y (away from the camera); - turns the face towards the camera"""
        j = self.joints.setdefault(part, dict(pivot=tuple(pivot), rotate=(0.0, 0.0, 0.0), parent=None))
        j["pivot"] = tuple(float(c) for c in pivot)
        j["rotate"] = tuple(float(c) for c in rotate)
        j["parent"] = parent

    def mirror(self, source="-Y"):
        """Copy one side to the other across y = 0 (y -> -y), with "_l" parts renamed "_r" and their joints mirrored."""
        sign = -1 if source == "-Y" else 1
        for p, layer in list(self.layers.items()):
            for (x, y, z), c in list(layer.items()):
                if y * sign > 0:
                    self._put((x, -y, z), c, side_twin(p))
        for part, j in list(self.joints.items()):
            twin = side_twin(part)
            if twin == part:
                continue
            m = dict(j)
            m["pivot"] = (j["pivot"][0], 1.0 - j["pivot"][1], j["pivot"][2])        # the mirror plane is y = 0.5
            m["rotate"] = (-j["rotate"][0], j["rotate"][1], -j["rotate"][2])
            m["parent"] = side_twin(j["parent"]) if j.get("parent") else None
            if "scale_pivot" in j:
                m["scale_pivot"] = (j["scale_pivot"][0], 1.0 - j["scale_pivot"][1], j["scale_pivot"][2])
            self.joints[twin] = m

    def anchor(self):
        """Sink every turning section that only touches its parent one voxel into it (owner 2026-11-21: the
        flamingo's and zebra's necks "floating", the giraffe's and zebra's tails): the parent's cells against the
        section join the section's own layer, in the parent's colours, so they are hidden inside the parent (or flush
        with it, the same colour) while still, and fill the gap when the section turns. Limbs hang from the body's
        face by design. Called by load_model() after build(), for every animal."""
        added = {}
        for part, j in list(self.joints.items()):
            par = j.get("parent")
            if (par is None or part not in self.layers or par not in self.layers
                    or part.split("_")[0] in LIMB_STEMS):
                continue
            mine, theirs = self.layers[part], self.layers[par]
            if set(mine) & set(theirs):
                continue
            new = {}
            pv = j["pivot"]
            for (x, y, z) in mine:
                for dx, dy, dz in FACES:
                    n = (x + dx, y + dy, z + dz)
                    if n in theirs and n not in mine:
                        # only near the hinge: the contact face's centre within ANCHOR_REACH of the pivot, so a long
                        # tail lying against the rump is held at its root, not doubled along its whole length
                        fc = (x + 0.5 + dx / 2.0, y + 0.5 + dy / 2.0, z + 0.5 + dz / 2.0)
                        if sum((fc[i] - pv[i]) ** 2 for i in range(3)) <= ANCHOR_REACH ** 2:
                            new[n] = theirs[n]
            mine.update(new)
            if new:
                added[part] = len(new)
        self._merged = None
        self.anchored = added
        return added

    # ---- reading --------------------------------------------------------------------------------------------------
    def bounds(self):
        if not self.v:
            return (0, 0, 0), (0, 0, 0)
        xs, ys, zs = zip(*self.v)
        return (min(xs), min(ys), min(zs)), (max(xs), max(ys), max(zs))

    def size(self):
        lo, hi = self.bounds()
        return tuple(hi[i] - lo[i] + 1 for i in range(3))

    def visible(self, key, part=None):
        """True when at least one face of the voxel is open to the outside of its own part (faces against another
        part are kept: that part may turn away)."""
        x, y, z = key
        layer = self.layers.get(part) if part else None
        if layer is None:
            part = self.v[key][1]
            layer = self.layers[part]
        return any((x + dx, y + dy, z + dz) not in layer for dx, dy, dz in FACES)

    def parts(self):
        return {p: list(layer.items()) for p, layer in self.layers.items() if layer}

    def colors(self):
        return sorted({c for layer in self.layers.values() for c in layer.values()})

    def matrix(self, part, _seen=None):
        """The part's pose: rest-pose voxel coordinates -> posed coordinates (scale not included)."""
        j = self.joints.get(part)
        if not j:
            return IDENTITY
        seen = (_seen or set()) | {part}
        parent = j.get("parent")
        if parent in seen:
            raise ValueError(f"joint loop through {part} and {parent}")
        p = j["pivot"]
        local = _mul(_translate(p), _mul(_rotate(j["rotate"]), _translate((-p[0], -p[1], -p[2]))))
        return _mul(self.matrix(parent, seen), local) if parent else local

    def scaled(self, part, p):
        """A rest-pose point squashed by the part's plate scale (if any)."""
        j = self.joints.get(part)
        if not j or "scale" not in j:
            return p
        sp, sc = j["scale_pivot"], j["scale"]
        return tuple(sp[i] + (p[i] - sp[i]) * sc[i] for i in range(3))

    def posed_points(self):
        """Every visible voxel corner in the posed animal (voxel units), before grounding."""
        out = []
        for part, vs in self.parts().items():
            m = self.matrix(part)
            for (x, y, z), _ in vs:
                if not self.visible((x, y, z), part):
                    continue
                for dx, dy, dz in CORNERS:
                    out.append(apply(m, self.scaled(part, (x + dx, y + dy, z + dz))))
        return out

    def posed_bounds(self):
        pts = self.posed_points()
        lo = tuple(min(p[i] for p in pts) for i in range(3))
        hi = tuple(max(p[i] for p in pts) for i in range(3))
        return lo, hi

    def islands(self):
        """Groups of face-connected cells in the rest pose, all parts together (a floating eye or ear is its own
        island; overlapping parts are connected)."""
        left, groups = set(self.v), []
        while left:
            seed = left.pop()
            stack, group = [seed], [seed]
            while stack:
                x, y, z = stack.pop()
                for dx, dy, dz in FACES:
                    n = (x + dx, y + dy, z + dz)
                    if n in left:
                        left.remove(n)
                        stack.append(n)
                        group.append(n)
            groups.append(group)
        return groups

    def report(self, budget=(16, 32), max_angle=40.0, plates=True):
        """Checks every model must pass before Blender builds it. Returns (errors, notes)."""
        errors, notes = [], []
        if not self.v:
            return ["the model is empty"], notes
        lo, hi = self.bounds()
        if lo[2] < 0:
            errors.append(f"voxels below the ground (lowest z = {lo[2]}); the feet stand on z = 0")
        if lo[2] > 0:
            errors.append(f"the model floats: lowest z = {lo[2]}, the feet must touch z = 0")
        isl = self.islands()
        if len(isl) > 1:
            small = sorted(len(g) for g in isl)[:-1]
            errors.append(f"{len(isl)} separate pieces (sizes {small} besides the main body): every voxel must touch the body")
        parts = self.parts()
        flat = sorted(p for p, j in self.joints.items() if "scale" in j)
        if flat and not plates:
            errors.append(f"plates are switched off for now (vf_standards.POSE): {', '.join(flat)} must be whole voxels")
        for part, j in self.joints.items():
            if part not in parts:
                errors.append(f"joint for '{part}', which has no voxels")
                continue
            if j.get("parent") and j["parent"] not in parts:
                errors.append(f"joint '{part}': parent '{j['parent']}' has no voxels")
            big = [a for a in j["rotate"] if abs(a) > max_angle]
            if big:
                errors.append(f"joint '{part}' turns {max(abs(a) for a in big):.0f} degrees (limit {max_angle:.0f}: subtle poses)")
            xs, ys, zs = zip(*[k for k, _ in parts[part]])
            box = ((min(xs), max(xs) + 1), (min(ys), max(ys) + 1), (min(zs), max(zs) + 1))
            if any(not box[i][0] - 1.5 <= j["pivot"][i] <= box[i][1] + 1.5 for i in range(3)):
                errors.append(f"joint '{part}': pivot {j['pivot']} is not on the part (its hinge must touch it)")
        # a turning section must be sunk into its parent (owner 2026-11-21: the flamingo's and the zebra's necks
        # "floating", the giraffe's and zebra's tails): a section that only touches its parent's face opens a gap as
        # soon as it turns. Limbs hang from the body's face by design (block-game legs)
        loose = []
        for part, j in self.joints.items():
            par = j.get("parent")
            stem = part.split("_")[0]
            if par is None or part not in parts or par not in parts or stem in LIMB_STEMS:
                continue
            if not set(self.layers[part]) & set(self.layers[par]):
                loose.append(f"{part} on {par}")
        if loose:
            errors.append(f"section(s) only touching their parent, sink each one voxel into it so it stays attached "
                          f"when it turns: {', '.join(sorted(loose))}")
        try:
            plo, phi = self.posed_bounds()
        except ValueError as e:
            return errors + [str(e)], notes
        size = tuple(phi[i] - plo[i] for i in range(3))
        longest = max(size)
        if not budget[0] <= round(longest) <= budget[1]:
            errors.append(f"longest side {longest:.1f} voxels (posed) is outside this animal's budget {budget[0]}-{budget[1]}")
        if abs(plo[2]) > 0.01:
            (errors if abs(plo[2]) > 1.5 else notes).append(
                f"the pose moves the lowest point to z = {plo[2]:+.2f}: the engine sets the animal back on the ground")
        asym = sum(1 for (x, y, z), (c, _) in self.v.items() if self.v.get((x, -y, z), (None,))[0] != c)
        if asym:
            notes.append(f"{asym} voxels are not mirrored across y = 0 (fine for a pose or a marking; check it is meant)")
        turned = sorted(p for p, j in self.joints.items() if any(abs(a) > 0.01 for a in j["rotate"]))
        plates = sorted(p for p, j in self.joints.items() if "scale" in j)
        notes.append(f"posed size {size[0]:.1f} x {size[1]:.1f} x {size[2]:.1f} voxels (L x W x H), {len(self.v)} voxels, "
                     f"colours {', '.join(self.colors())}, parts {', '.join(sorted(parts))}"
                     + (f"; turned {', '.join(turned)}" if turned else "") + (f"; plates {', '.join(plates)}" if plates else ""))
        return errors, notes


def load_model(path):
    """Run an animal's model.py and return its Grid."""
    import runpy
    ns = runpy.run_path(path)
    if "build" not in ns:
        raise ValueError(f"{path}: no build(g) function")
    g = Grid()
    ns["build"](g)
    g.anchor()
    return g
