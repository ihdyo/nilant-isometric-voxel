"""Voxel Fauna · colour maths shared by the Blender engine and the command line (plain Python, no bpy).

A colour is a Tailwind v4 token ("teal-200", "white", "black") or a hex code ("#9FD8CC"). The owner lifted the
tokens-only rule on 2026-11-16 ("for this project, break from tailwind coloring token"); tokens remain the starting
point and are still used for every palette that has no reason to leave them.

    hex_of(c)      "RRGGBB" (no #)              srgb(c)   (r, g, b) in 0..1
    oklch(c)       (L 0..1, C, h degrees)        mute(c, k) the same lightness and hue, chroma x k, as "#RRGGBB"
    pastel(c, max_chroma, (lo, hi))   the hue kept, chroma capped, lightness held in the band: vivid but calm
"""
import json
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PALETTE = json.load(open(os.path.join(ROOT, "03 Design", "Color", "tailwind-v4-palette.json"), encoding="utf-8"))["colors"]
HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")


def is_colour(c):
    return isinstance(c, str) and (c in PALETTE or c in ("white", "black") or bool(HEX.match(c)))


def hex_of(c):
    if isinstance(c, str) and HEX.match(c):
        return c[1:].upper()
    return {"white": "FFFFFF", "black": "000000"}.get(c) or PALETTE[c]["hex"]


def srgb(c):
    h = hex_of(c)
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def _lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _gam(c):
    return c * 12.92 if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def _oklab_of_linear(r, g, b):
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = (math.copysign(abs(v) ** (1 / 3), v) for v in (l, m, s))
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)


def _linear_of_oklab(L, a, b):
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
            -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
            -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)


def oklch(c):
    L, a, b = _oklab_of_linear(*(_lin(v) for v in srgb(c)))
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


def from_oklch(L, C, h):
    """'#RRGGBB'; chroma is reduced until the colour fits sRGB."""
    for _ in range(40):
        a, b = C * math.cos(math.radians(h)), C * math.sin(math.radians(h))
        rgb = _linear_of_oklab(L, a, b)
        if all(-1e-4 <= v <= 1 + 1e-4 for v in rgb):
            break
        C *= 0.95
    return "#" + "".join(f"{round(max(0.0, min(1.0, _gam(max(0.0, min(1.0, v))))) * 255):02X}" for v in rgb)


def mute(c, k):
    """The colour with its OKLCH chroma multiplied by k (lightness and hue kept): a calmer version of it."""
    L, C, h = oklch(c)
    return from_oklch(L, C * k, h)


def pastel(c, max_chroma, lightness):
    """A vivid pastel of the colour: its hue, its chroma capped at max_chroma (soft colours stay as they are, neon
    ones calm down), its lightness held inside the (lo, hi) band."""
    L, C, h = oklch(c)
    lo, hi = lightness
    return from_oklch(min(hi, max(lo, L)), min(C, max_chroma), h)


def pastel_factor(c, max_chroma):
    """The chroma factor pastel() applies to this colour (1.0 when it is already soft enough)."""
    C = oklch(c)[1]
    return 1.0 if C <= max_chroma else max_chroma / C
