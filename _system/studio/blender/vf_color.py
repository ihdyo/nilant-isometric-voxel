"""Voxel Fauna · colour maths shared by the Blender engine and the command line (plain Python, no bpy).

Every colour is a hex code "#RRGGBB" (owner 2026-11-21: "remove the tailwind color palette completely"; the tokens
were converted to their exact hex values, so nothing renders differently). A card colour drawn from an animal's
background is written "#RRGGBB-700": the background's hue at a shade of the collection's own OKLCH ramp (RAMP below),
the way a Tailwind family was used before.

    hex_of(c)      "RRGGBB" (no #)              srgb(c)   (r, g, b) in 0..1
    oklch(c)       (L 0..1, C, h degrees)        mute(c, k) the same lightness and hue, chroma x k, as "#RRGGBB"
    pastel(c, max_chroma, (lo, hi))   the hue kept, chroma capped, lightness held in the band: vivid but calm
    background(hue, lightness, chroma)  an animal's background: the collection's one chroma at its own hue
    ramp(base, shade)  the base colour's hue at a shade 50..950 of RAMP ("#RRGGBB-700" resolves through it)
"""
import math
import re

HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")
SHADED = re.compile(r"^(#[0-9A-Fa-f]{6})-([0-9]{2,3})$")

# The collection's own shade ramp (replaces the Tailwind families, 2026-11-21): per shade, the OKLCH lightness and
# chroma of a colour drawn from a background's hue. Lightness steps like Tailwind v4's; chroma calm (the old family
# colours were muted by the background's chroma factor, about x 0.6), peaking at 500-700 for the inks and lips.
RAMP = {50: (0.975, 0.018), 100: (0.95, 0.03), 200: (0.91, 0.045), 300: (0.87, 0.06), 400: (0.78, 0.08),
        500: (0.68, 0.095), 600: (0.585, 0.1), 700: (0.5, 0.095), 800: (0.42, 0.085), 900: (0.345, 0.07),
        950: (0.265, 0.055)}
SHADES = tuple(sorted(RAMP))
NAMED = {"white": "FFFFFF", "black": "000000"}     # the card system's plain white and black (not animal colours)


def is_colour(c):
    return isinstance(c, str) and bool(HEX.match(c) or SHADED.match(c))


def hex_of(c):
    if isinstance(c, str) and HEX.match(c):
        return c[1:].upper()
    if c in NAMED:
        return NAMED[c]
    m = SHADED.match(c) if isinstance(c, str) else None
    if m:
        return ramp(m.group(1), int(m.group(2)))[1:]
    raise ValueError(f"not a colour: {c!r} (a colour is '#RRGGBB')")


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


def tone(c, knee, slope, scale):
    """The animal colour as it renders (vf_standards.ANIMAL_TONE): lightness and hue kept, chroma above `knee`
    compressed to `slope` of its excess, then x `scale`. Greys, black and white are untouched in effect."""
    L, C, h = oklch(c)
    C2 = (C if C <= knee else knee + (C - knee) * slope) * scale
    return from_oklch(L, C2, h)


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


def background(hue, lightness, chroma):
    """An animal's background: OKLCH (lightness, chroma, hue) as '#RRGGBB' (vf_standards.BACKGROUND_RULE)."""
    return from_oklch(lightness, chroma, hue)


def ramp(base, shade):
    """The base colour's hue at one shade of RAMP: '#RRGGBB'. A grey base (chroma under 0.01) keeps a grey ramp."""
    shade = min(SHADES, key=lambda s: abs(s - int(shade)))
    L, C, h = oklch(base)
    Lr, Cr = RAMP[shade]
    return from_oklch(Lr, Cr if C >= 0.01 else C, h)


def nearest_shade(c):
    """The RAMP shade whose lightness is closest to the colour's."""
    L = oklch(c)[0]
    return min(SHADES, key=lambda s: abs(RAMP[s][0] - L))
