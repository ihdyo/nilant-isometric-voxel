"""Voxel Fauna · the voxel grid every animal model is written in (plain Python, no bpy).

An animal's `blender/model.py` defines `build(g)` and fills a Grid with voxels. A voxel is an integer cell (x, y, z):
it occupies [x, x+1] x [y, y+1] x [z, z+1] voxels of VOXEL metres. Conventions (vf_standards.FACING):
  +X  the head end          -X  the tail end
  -Y  the animal's left     +Y  its right       (y = 0 is the centre line: odd widths are symmetric about it)
  +Z  up; the feet stand on z = 0 (nothing below it)
Every voxel carries a colour key (a key of animal.json -> look.palette, never a raw colour) and a part name (the
Blender object it lands in: body, head, legs, tail, ...).

Typical model:
    def build(g):
        g.box((0, -3, 4), (13, 3, 9), "fur", part="body")          # inclusive corners
        g.box((14, -3, 7), (19, 3, 12), "fur", part="head")
        g.paint((19, -1, 8), (19, 1, 9), "nose")                    # recolour what is there
        g.set(17, -3, 11, "eye", part="head"); g.mirror()           # mirror copies the left side (-Y) to the right
"""

FACES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


class Grid:
    def __init__(self):
        self.v = {}                       # (x, y, z) -> (colour key, part)

    # ---- filling --------------------------------------------------------------------------------------------------
    def set(self, x, y, z, color, part="body"):
        self.v[(int(x), int(y), int(z))] = (color, part)

    def box(self, a, b, color, part="body"):
        """Fill the inclusive box between corners a and b."""
        (x0, x1), (y0, y1), (z0, z1) = (sorted((a[i], b[i])) for i in range(3))
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                for z in range(z0, z1 + 1):
                    self.v[(x, y, z)] = (color, part)

    def ellipsoid(self, center, radii, color, part="body"):
        """Fill voxels whose centres fall inside the ellipsoid (centre and radii in voxels; half-integers allowed).
        Keep radii >= 2: a smaller ellipsoid is just noise at this voxel scale."""
        cx, cy, cz = center
        rx, ry, rz = radii
        for x in range(int(cx - rx) - 1, int(cx + rx) + 2):
            for y in range(int(cy - ry) - 1, int(cy + ry) + 2):
                for z in range(int(cz - rz) - 1, int(cz + rz) + 2):
                    px, py, pz = x + 0.5 - cx, y + 0.5 - cy, z + 0.5 - cz
                    if (px / rx) ** 2 + (py / ry) ** 2 + (pz / rz) ** 2 <= 1.0:
                        self.v[(x, y, z)] = (color, part)

    def paint(self, a, b, color, part=None, only=None):
        """Recolour (and optionally re-part) voxels already in the box; `only` limits it to one colour key."""
        (x0, x1), (y0, y1), (z0, z1) = (sorted((a[i], b[i])) for i in range(3))
        for k, (c, p) in list(self.v.items()):
            if x0 <= k[0] <= x1 and y0 <= k[1] <= y1 and z0 <= k[2] <= z1 and (only is None or c == only):
                self.v[k] = (color, part or p)

    def carve(self, a, b):
        """Remove every voxel in the box."""
        (x0, x1), (y0, y1), (z0, z1) = (sorted((a[i], b[i])) for i in range(3))
        for k in [k for k in self.v if x0 <= k[0] <= x1 and y0 <= k[1] <= y1 and z0 <= k[2] <= z1]:
            del self.v[k]

    def mirror(self, source="-Y"):
        """Copy one side to the other across y = 0 (y -> -y). `source` is the side that was modelled."""
        sign = -1 if source == "-Y" else 1
        for (x, y, z), val in list(self.v.items()):
            if y * sign > 0:
                self.v[(x, -y, z)] = val

    # ---- reading --------------------------------------------------------------------------------------------------
    def bounds(self):
        if not self.v:
            return (0, 0, 0), (0, 0, 0)
        xs, ys, zs = zip(*self.v)
        return (min(xs), min(ys), min(zs)), (max(xs), max(ys), max(zs))

    def size(self):
        lo, hi = self.bounds()
        return tuple(hi[i] - lo[i] + 1 for i in range(3))

    def visible(self, key):
        """True when at least one face of the voxel is open."""
        x, y, z = key
        return any((x + dx, y + dy, z + dz) not in self.v for dx, dy, dz in FACES)

    def parts(self):
        out = {}
        for k, (c, p) in self.v.items():
            out.setdefault(p, []).append((k, c))
        return out

    def colors(self):
        return sorted({c for c, _ in self.v.values()})

    def islands(self):
        """Groups of face-connected voxels (a floating eye or ear is its own island)."""
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

    def report(self, budget=(16, 32)):
        """Checks every model must pass before Blender builds it. Returns (errors, notes)."""
        errors, notes = [], []
        if not self.v:
            return ["the model is empty"], notes
        lo, hi = self.bounds()
        size = self.size()
        longest = max(size)
        if lo[2] < 0:
            errors.append(f"voxels below the ground (lowest z = {lo[2]}); the feet stand on z = 0")
        if lo[2] > 0:
            errors.append(f"the model floats: lowest z = {lo[2]}, the feet must touch z = 0")
        if not budget[0] <= longest <= budget[1]:
            errors.append(f"longest side {longest} voxels is outside the collection's budget {budget[0]}-{budget[1]}")
        isl = self.islands()
        if len(isl) > 1:
            small = sorted(len(g) for g in isl)[:-1]
            errors.append(f"{len(isl)} separate pieces (sizes {small} besides the main body): every voxel must touch the body")
        asym = sum(1 for (x, y, z), (c, _) in self.v.items() if self.v.get((x, -y, z), (None,))[0] != c)
        if asym:
            notes.append(f"{asym} voxels are not mirrored across y = 0 (fine for a pose or a marking; check it is meant)")
        notes.append(f"size {size[0]} x {size[1]} x {size[2]} voxels (L x W x H), {len(self.v)} voxels, "
                     f"{sum(1 for k in self.v if self.visible(k))} visible, colours {', '.join(self.colors())}, "
                     f"parts {', '.join(sorted(self.parts()))}")
        return errors, notes


def load_model(path):
    """Run an animal's model.py and return its Grid."""
    import runpy
    ns = runpy.run_path(path)
    if "build" not in ns:
        raise ValueError(f"{path}: no build(g) function")
    g = Grid()
    ns["build"](g)
    return g
