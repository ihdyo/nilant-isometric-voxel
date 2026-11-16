"""Voxel Fauna · shared helpers for the command line (plain Python 3.10+, Pillow and openpyxl; no bpy).

Paths, the Tailwind palette and colour maths, animal folders and animal.json, image IDs, the Blender runner and the
standards fingerprint. Everything the look depends on is read from blender/vf_standards.py.
"""
import glob
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STUDIO = os.path.dirname(HERE)
BLENDER_DIR = os.path.join(STUDIO, "blender")
sys.path.insert(0, BLENDER_DIR)
import vf_standards as ST  # noqa: E402
import vf_voxel as VX  # noqa: E402
import vf_color as VC  # noqa: E402

ROOT = os.path.abspath(os.path.join(STUDIO, "..", ".."))
ANIMALS = os.path.join(ROOT, "02 Animals")
TEMPLATE = os.path.join(ANIMALS, "_Template")
DESIGN = os.path.join(ROOT, "03 Design")
FONTS = os.path.join(DESIGN, "Fonts")
PUBLISH = os.path.join(ROOT, "05 Publish")
REGISTRY = os.path.join(PUBLISH, "Voxel Fauna · Registry.xlsx")
DATA = os.path.join(ROOT, "_system", "data")
LOG = os.path.join(ROOT, "_system", "log")
CACHE = os.path.join(ROOT, "_system", "cache")
SKILL = os.path.join(ROOT, ".claude", "skills", "voxel-animal-production", "SKILL.md")
LOCK = os.path.join(DATA, "standards.lock.json")
PALETTE = json.load(open(os.path.join(DESIGN, "Color", "tailwind-v4-palette.json"), encoding="utf-8"))["colors"]
DEFAULT_BLENDER = r"C:\Users\ihdyo\AppData\Local\Programs\Blender 5.3.0\blender-5.3.0-windows-x64\blender.exe"

# the files whose content is the approved look: a change to any of them needs the owner's OK and a relock
LOCKED_FILES = ["_system/studio/blender/vf_standards.py", "_system/studio/blender/vf_voxel.py",
                "_system/studio/blender/vf_scene.py", "_system/studio/blender/vf_job.py",
                "_system/studio/blender/vf_color.py", "_system/studio/scripts/infographic.py"]


def rel(path):
    return os.path.relpath(path, ROOT).replace("\\", "/")


# ---- colour ---------------------------------------------------------------------------------------------------------
def hexcode(token):
    """A Tailwind token or "#RRGGBB" -> "RRGGBB"."""
    return VC.hex_of(token)


def is_colour(c):
    return VC.is_colour(c)


def background(look):
    """The rendered background colour: a vivid pastel of look.background (vf_standards.BACKGROUND_RULE)."""
    R = ST.BACKGROUND_RULE
    return VC.pastel(look["background"], R["max_chroma"], R["lightness"])


def background_factor(look):
    """The chroma factor the background gets; card colours drawn from its family get the same."""
    return VC.pastel_factor(look["background"], ST.BACKGROUND_RULE["max_chroma"])


def budget(animal):
    """(min, max, target) voxels on the posed longest side, from animal.json look.size.real_m (vf_standards.SIZE_RULE)."""
    real = ((animal.get("look") or {}).get("size") or {}).get("real_m")
    return ST.size_budget(real) if real else (ST.BUDGET[0], ST.BUDGET[1], None)


def rgb(token):
    h = hexcode(token)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _lin(c):
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(token):
    r, g, b = (_lin(c) for c in rgb(token))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def lab(token):
    r, g, b = (_lin(c) for c in rgb(token))
    x = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883

    def f(t):
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    fx, fy, fz = f(x), f(y), f(z)
    return 116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)


def delta_e(a, b):
    return sum((p - q) ** 2 for p, q in zip(lab(a), lab(b))) ** 0.5


def shade(token):
    try:
        return int(token.rsplit("-", 1)[1])
    except (IndexError, ValueError):
        return None


# ---- animals --------------------------------------------------------------------------------------------------------
def animal_dirs():
    return sorted(d for d in glob.glob(os.path.join(ANIMALS, "[0-9][0-9]-[0-9][0-9][0-9] · *")) if os.path.isdir(d))


def find(code):
    hits = [d for d in animal_dirs() if os.path.basename(d).startswith(code + " · ")]
    if not hits:
        raise SystemExit(f"no animal folder for {code} in 02 Animals/ (run: vf.py list)")
    return hits[0]


def load(folder):
    return json.load(open(os.path.join(folder, "animal.json"), encoding="utf-8"))


def save(folder, animal):
    with open(os.path.join(folder, "animal.json"), "w", encoding="utf-8") as f:
        json.dump(animal, f, indent=2, ensure_ascii=False)
        f.write("\n")


def image_id(code, kind, ratio):
    return ST.IMAGE_ID.format(code=code, kind=kind, ratio=ratio)


def export_path(folder, code, kind, ratio):
    return os.path.join(folder, "export", image_id(code, kind, ratio) + ".png")


def blend_path(folder, animal):
    return os.path.join(folder, "blender", f"{animal['code']} · {animal['common']}.blend")


def next_code():
    year = time.strftime("%y")
    used = [int(os.path.basename(d)[3:6]) for d in animal_dirs() if os.path.basename(d).startswith(year + "-")]
    return f"{year}-{(max(used) + 1 if used else 1):03d}"


# ---- Blender --------------------------------------------------------------------------------------------------------
def blender_exe():
    cands = [os.environ.get("BLENDER", "")]
    p = os.path.join(STUDIO, "blender_path.txt")
    if os.path.exists(p):
        cands.append(open(p, encoding="utf-8").read().strip())
    cands.append(DEFAULT_BLENDER)
    for c in cands:
        if c and os.path.isfile(c):
            return c
    raise SystemExit("Blender not found: set BLENDER or write its blender.exe path in _system/studio/blender_path.txt")


def run_blender(job, tag):
    """Write the job, run vf_job.py in a background Blender, stream its VF: lines, return the result dict."""
    work = os.path.join(CACHE, "jobs", tag)
    os.makedirs(work, exist_ok=True)
    job = dict(job, work=os.path.join(work, "passes"), result=os.path.join(work, "result.json"))
    if os.path.exists(job["result"]):
        os.remove(job["result"])
    jp = os.path.join(work, "job.json")
    json.dump(job, open(jp, "w", encoding="utf-8"), indent=1)
    cmd = [blender_exe(), "-b", "--factory-startup", "--python", os.path.join(BLENDER_DIR, "vf_job.py"), "--", jp]
    t = time.time()
    with open(os.path.join(work, "blender.log"), "w", encoding="utf-8", errors="replace") as logf:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8",
                             errors="replace")
        for line in p.stdout:
            logf.write(line)
            if line.startswith("VF:"):
                print("  " + line[3:].strip(), flush=True)
        p.wait()
    if not os.path.exists(job["result"]):
        raise SystemExit(f"Blender stopped without a result (exit {p.returncode}); see {rel(os.path.join(work, 'blender.log'))}")
    res = json.load(open(job["result"], encoding="utf-8"))
    res["wall_seconds"] = round(time.time() - t, 1)
    if not res.get("ok"):
        raise SystemExit(f"Blender job failed: {res.get('error')}\n{res.get('trace', '')}")
    return res


# ---- standards fingerprint ------------------------------------------------------------------------------------------
def fingerprint():
    out = {}
    for f in LOCKED_FILES:
        data = open(os.path.join(ROOT, f), "rb").read().replace(b"\r\n", b"\n")
        out[f] = hashlib.sha256(data).hexdigest()[:16]
    return out


def file_hash(path):
    return hashlib.sha256(open(path, "rb").read().replace(b"\r\n", b"\n")).hexdigest()[:16]
