"""Voxel Fauna · the render menu behind render.bat (the look of Nilant's footage_cli: cover, title bar, bars, boxes).

    RENDER   1 build every missing or stale .blend        2 LOW previews of every built animal (+ rigs and loops)
             3 ULTRA renders: the two masters and the loop     P package: GIF, cards, stock JPEG, zip, registry
    MOTION   R rig + GIF loops
    CHECK    5 status of every animal                     6 one animal's files
    MORE     4 one animal, any step                       Q quit

Every step opens the same job screen: WHICH animals (the ones that still need it, all of them, or a hand-picked list:
numbers, ranges, codes, names, filters) and WHAT (checkboxes: for Package the loop GIF, either card, the stock JPEG
and CSVs, the Gumroad zip, the registry; for the renders the masters and the loop; force, LOW, jobs, shut down when
finished). The choices are remembered in render_options.json beside render.bat (this PC's, git-ignored).

Without the menu (every option on the command line; `render.bat <command> --help`):
    render.bat status | files <code>
    render.bat build   [codes|ranges|all] [--force]
    render.bat preview [codes|ranges|all] [--stills] [--force] [--rig-force] [--jobs N]
    render.bat final   [codes|ranges|all] [--parts dyn,block,loop] [--low] [--force]
    render.bat package [codes|ranges|all] [--preset full|stock|pdf|gif|gumroad | --parts gif,card_en,card_id,stock,csv,zip,registry]
                       [--low] [--force]
    render.bat rig     [codes|ranges|all] [--force] [--no-preview] [--jobs N] [--lineups]
    render.bat <code> [preview|final|package]            (the older short form)
Without codes a command takes the animals that still need it; `all` takes every animal it can run on.

Blender renders (and Pillow lays the cards). No internet. Pause any time with Ctrl+C or by closing the window:
finished images are kept, and the next run skips them.
"""
import argparse
import json
import os
import re
import shutil
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vflib as VL  # noqa: E402
import vf  # noqa: E402
import render_art as ART  # noqa: E402
import render_jobs as RJ  # noqa: E402

ST = VL.ST
OPTIONS_FILE = os.path.join(VL.STUDIO, "render", "render_options.json")


def _width():
    return max(80, min(100, shutil.get_terminal_size((100, 40)).columns - 1))


W = _width()                                               # the width everything is laid out to


def _vt():
    """Turns on ANSI colours in the Windows console; False when the output cannot show them."""
    if os.name != "nt":
        return sys.stdout.isatty()
    try:
        import ctypes
        k = ctypes.windll.kernel32
        h = k.GetStdHandle(-11)
        mode = ctypes.c_ulong()
        if not k.GetConsoleMode(h, ctypes.byref(mode)):
            return False
        return bool(k.SetConsoleMode(h, mode.value | 0x0004))
    except Exception:
        return False


COLOR = _vt()
try:
    "█░●✓▶─╭╮╰╯│".encode(sys.stdout.encoding or "utf-8")
    BLOCK, SHADE, DOT, TICK, PLAY, LINE = "█", "░", "●", "✓", "▶", "─"
    BOX = dict(tl="╭", tr="╮", bl="╰", br="╯", h="─", v="│")
    ON, OFF, RADIO = "[x]", "[ ]", "◉"
except Exception:
    BLOCK, SHADE, DOT, TICK, PLAY, LINE = "#", ".", "o", "+", ">", "-"
    BOX = dict(tl="+", tr="+", bl="+", br="+", h="-", v="|")
    ON, OFF, RADIO = "[x]", "[ ]", "(o)"

_CODES = {"b": "1", "red": "31", "green": "32", "yellow": "33", "blue": "34", "magenta": "35", "cyan": "36",
          "white": "97", "grey": "90", "bgblue": "44"}


def c(text, *styles):
    if not COLOR or not styles:
        return text
    return "\x1b[" + ";".join(_CODES[s] for s in styles) + "m" + text + "\x1b[0m"


def _plain(s):
    return re.sub(r"\x1b\[[0-9;]*m", "", s)


def pad(s, width):
    """Pads coloured text to a visible width."""
    return s + " " * max(0, width - len(_plain(s)))


def clip(s, width):
    """Cuts plain text to a width with an ellipsis."""
    return s if len(s) <= width else s[:max(0, width - 1)] + "…"


def bar(frac, width=26, colour="green"):
    n = int(round(max(0.0, min(1.0, frac)) * width))
    return c(BLOCK * n, colour) + c(SHADE * (width - n), "grey")


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def rule():
    print("  " + c(LINE * (W - 2), "grey"))


def say(text, colour=None):
    print("  " + (c(text, colour) if colour else text))


def box(title, body, width, colour="cyan"):
    """A rounded box with a coloured title in its top edge: [lines]."""
    h, v = BOX["h"], BOX["v"]
    t = f" {title} " if title else ""
    top = c(BOX["tl"] + h, colour) + c(t, colour, "b") + c(h * max(0, width - 3 - len(t)) + BOX["tr"], colour)
    lines = [top]
    for ln in body:
        lines.append(c(v, colour) + " " + pad(ln, width - 4) + " " + c(v, colour))
    lines.append(c(BOX["bl"] + h * (width - 2) + BOX["br"], colour))
    return lines


def side_by_side(left, right, gap=2):
    """Two boxes (lists of lines) next to each other, the shorter one padded."""
    lw = max(len(_plain(x)) for x in left)
    out = []
    for i in range(max(len(left), len(right))):
        a = left[i] if i < len(left) else " " * lw
        b = right[i] if i < len(right) else ""
        out.append("  " + pad(a, lw) + " " * gap + b)
    return out


def blender_label():
    try:
        return os.path.basename(os.path.dirname(VL.blender_exe())).replace("blender-", "").split("-windows")[0]
    except Exception:
        return "Blender"


def header(title=""):
    cls()
    left = "  VOXEL FAUNA  RENDER" + (f"  {PLAY}  {title}" if title else "")
    right = f"{blender_label()}  offline  "
    left = left[:W - len(right) - 2]                       # a long title never runs into the right-hand label
    print(c(left.ljust(W - len(right)) + right, "b", "white", "bgblue"))
    print()


def ask(prompt, default=""):
    try:
        v = input("  " + c(prompt, "b") + " ").strip()
    except EOFError:
        print("\n  (no more input: quitting)")
        raise SystemExit(0)
    return v or default


def wait():
    ask(c("Enter to go back", "grey"))


def hm(sec):
    return f"{sec / 3600:.1f} h" if sec >= 5400 else f"{max(1, round(sec / 60))} min" if sec >= 45 else f"{max(1, round(sec))} s"


# ---- remembered choices ----------------------------------------------------------------------------------------------
def load_options():
    try:
        return json.load(open(OPTIONS_FILE, encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_options(job, values):
    data = load_options()
    data[job.key] = {k: v for k, v in values.items() if k in {o["id"] for o in job.options}}
    try:
        json.dump(data, open(OPTIONS_FILE, "w", encoding="utf-8"), indent=1)
    except OSError:
        pass


# ---- what every animal looks like right now ---------------------------------------------------------------------------
def n_items():
    import package as PK
    return len(PK.EXPORT["items"])


def state(d):
    an = VL.load(d)
    has_model = os.path.exists(os.path.join(d, "blender", "model.py"))
    bs = vf.build_state(d, an)[0] if has_model else "no model"
    low = sum(os.path.exists(t["final"]) for t in vf.targets(an, "LOW", d)[0])
    import package as PK
    ult = sum(os.path.exists(PK.export_file(d, an["code"], s)) for s, _, _ in PK.EXPORT["items"])
    ap = an.get("approvals") or {}                 # ult: the items of the export package (masters, GIF, cards)
    return an, bs, low, ult, ap


def colour_of(bs, low, ult, ap):
    if bs in ("missing", "no model"):
        return "grey"
    if bs == "stale":
        return "red"
    if ap.get("final") and ult == n_items():
        return "green"
    if ap.get("preview"):
        return "yellow" if ult < n_items() else "green"
    return "blue" if low == 6 else "cyan"


def collect(show=True, label="Reading animals"):
    """Every animal's state, with a 'reading' counter on one line (it takes a few seconds: it hashes the models)."""
    dirs, rows = VL.animal_dirs(), []
    for i, d in enumerate(dirs, 1):
        if show:
            sys.stdout.write(f"\r\x1b[2K  {c(VL.SPIN[i % len(VL.SPIN)], 'magenta')} {c(label, 'b')} "
                             f"{bar(i / len(dirs), 14)} {i}/{len(dirs)}")
            sys.stdout.flush()
        rows.append((d, *state(d)))
    if show:
        sys.stdout.write("\r\x1b[2K")
    return rows


def package_pending(rows):
    """(animals, seconds) the offline package still has to build: rendered, and an output missing or out of date."""
    n = sum(vf.package_state(d, an) == "todo" for d, an, *_ in rows)
    return n, n * sum(sec for _, sec in vf.PACKAGE_STEPS)


def pending(rows, profile):
    """(images, seconds) still to render at a profile, from the same rule the renderer uses."""
    n, secs = 0, 0.0
    for d, an, bs, low, ult, ap in rows:
        if bs != "current" or (profile == "ULTRA" and not ap.get("preview")):
            continue
        if profile == "ULTRA":                     # the two 4096 masters and the loop, by the rule `final` uses
            plan = vf.final_plan(d, an)
            n, secs = n + len(plan), secs + sum(sec for _, sec in plan)
            continue
        try:
            ests = vf.todo_of(d, an, profile)[1]
        except OSError:
            continue
        n, secs = n + len(ests), secs + sum(ests)
    return n, secs


def summary(rows):
    n = max(1, len(rows))
    built = sum(r[2] == "current" for r in rows)
    stale = sum(r[2] == "stale" for r in rows)
    prev = sum(r[3] == 6 for r in rows)
    appr = sum(bool(r[5].get("preview")) for r in rows)
    fin = sum(r[4] == n_items() for r in rows)
    print(f"  {c('Animals', 'b')}    {bar(built / n)}  {c(f'{built} of {len(rows)}', 'b')} built"
          + (c(f", {stale} stale: choose 1", "red", "b") if stale else ""))
    print(f"  {c('Previews', 'b')}   {bar(prev / n, colour='blue')}  {c(f'{prev} of {len(rows)}', 'b')} with six LOW images"
          f"  {c(f'({appr} approved)', 'grey')}")
    print(f"  {c('Finals', 'b')}     {bar(fin / n, colour='magenta')}  {c(f'{fin} of {len(rows)}', 'b')} with the whole export package"
          f"  {c('(masters 4096 px, loop, cards)', 'grey')}")
    ult_n, ult_s = pending(rows, "ULTRA")
    pkg_n, pkg_s = package_pending(rows)
    if ult_n:
        print(f"  {c('Next', 'b')}       {c(f'{ult_n} ULTRA render(s)', 'yellow')} waiting for approved animals, "
              f"{c('roughly ' + hm(ult_s * 1.0), 'yellow')}")
    elif appr and pkg_n == 0:
        print(f"  {c('Next', 'b')}       {c(TICK + ' every approved animal has its export package', 'green')}")
    elif appr:
        print(f"  {c('Next', 'b')}       {c(TICK + ' every approved animal is rendered', 'green')}")
    else:
        print(f"  {c('Next', 'b')}       {c('approve a preview (vf.py approve <code> preview) before an ULTRA render', 'grey')}")
    if pkg_n:
        print(f"  {c('Package', 'b')}    {c(f'{pkg_n} animal(s) rendered', 'yellow')}, ready for the loop GIF, cards and stock JPEG, "
              f"{c('roughly ' + hm(pkg_s) + ': press P', 'yellow')}")
    print()


def legend():
    items = (("done", "green"), ("approved, final to render", "yellow"), ("LOW preview", "blue"), ("built", "cyan"),
             ("stale: build again", "red"), ("not built", "grey"))
    print("  " + "   ".join(c(f"{DOT} {t}", col) for t, col in items))


def screen_status(rows=None):
    header("Animal status")
    rows = rows or collect()
    legend()
    rule()
    print(c(f"    {'code':<7} {'animal':<20} {'.blend':<8} {'LOW':<4} {'approved':<11} {'export'}", "grey"))
    for d, an, bs, low, ult, ap in rows:
        col = colour_of(bs, low, ult, ap)
        ub = c(BLOCK * ult, "green") + c(SHADE * (n_items() - ult), "grey")
        print(f"  {c(DOT, col)} {an['code']:<7} {an['common'][:20]:<20} {pad(c(bs, col), 8)} {low}/6  "
              f"{(ap.get('preview') or '-'):<11} {ub} {ult}/{n_items()}"
              + (c(f"  final {ap['final']}", "green") if ap.get("final") else ""))
    rule()
    say(c("Colours show each animal's state. Choose 'One animal's files' for its files.", "grey"))
    vf.write_render_readme()


def files_of(code=None):
    header("One animal's files")
    d = VL.find(code or ask("Animal code (e.g. 000001):"))
    an, bs, low, ult, ap = state(d)
    col = colour_of(bs, low, ult, ap)
    say(f"{c(an['code'] + ' · ' + an['common'], 'b')} {c('(' + an['scientific'] + ')', 'grey')}   "
        f"status {c(an['status'], col)}, .blend {c(bs, col)}")
    rule()
    import package as PK
    import stock as SK
    files = [(PK.export_file(d, an["code"], s), what) for s, _, what in PK.EXPORT["items"]]
    files.append((SK.stock_file(d, an["code"]), "stock JPEG: the dynamic master for stock sites"))
    files.append((SK.zip_file(d, an), "Gumroad zip"))
    for p, what in files:
        ok = os.path.exists(p)
        size = f", {os.path.getsize(p) // 1024:,} KB" if ok else ""
        say(f"{c(TICK if ok else DOT, 'green' if ok else 'grey')} {os.path.basename(p)}{c('  ' + what + size, 'grey')}")
    rule()
    say(c("LOW preview: " + VL.rel(os.path.join(VL.CACHE, "preview", an["code"])), "grey"))


# ---- running things ---------------------------------------------------------------------------------------------------
def run(label, fn):
    t = time.time()
    try:
        fn()
        say(f"{c(TICK, 'green')} {label}: done in {c(VL.hms(time.time() - t), 'b')}")
        return True
    except KeyboardInterrupt:
        VL.LIVE.stop()
        print()
        say(f"{label}: paused (finished images are kept; run it again to carry on)", "yellow")
    except SystemExit as e:
        VL.LIVE.stop()
        say(f"{label}: {e}", "red")
    return False


# ---- the jobs: what each step asks and does ---------------------------------------------------------------------------
def _has_model(d):
    return os.path.exists(os.path.join(d, "blender", "model.py"))


def _rig_current(d, an):
    try:
        return vf.rig_state(d, an)[0] == "current"
    except Exception:
        return False


def _opt(id_, label, hint="", default=False, kind="check", choices=None, group="Options"):
    return dict(id=id_, label=label, hint=hint, default=default, kind=kind, choices=choices or [], group=group)


def _parts_of(values, ids):
    return [i for i in ids if values.get(i)]


class Job:
    """One render step: its options, who can run it, who still needs it, how long it takes and what it runs."""

    def __init__(self, key, title, blurb, options, classify, estimate, runner, presets=()):
        self.key, self.title, self.blurb, self.options = key, title, blurb, options
        self.classify, self.estimate, self.runner, self.presets = classify, estimate, runner, presets

    def defaults(self):
        saved = load_options().get(self.key, {})
        vals = {}
        for o in self.options:
            v = saved.get(o["id"], o["default"])
            if o["kind"] == "choice" and v not in [x for x, _ in o["choices"]]:
                v = o["default"]
            vals[o["id"]] = v
        return vals


SHUTDOWN = _opt("shutdown", "Shut this PC down when it finishes", "60 seconds to cancel: shutdown /a", False,
                group="When it finishes")


def _build_job():
    def classify(r, v):
        d, an, bs = r[0], r[1], r[2]
        if not _has_model(d):
            return "blocked", "no model.py"
        return ("todo", bs) if bs in ("missing", "stale") or v["force"] else ("done", "built")

    def estimate(rows, v):
        return sum(30 for r in rows if classify(r, v)[0] == "todo") + 2 * len(rows)

    def runner(rows, v):
        return RJ.build_many(rows, force=v["force"])
    return Job("build", "Build .blend", "model.py to the editable .blend, with its six LOW-review scenes.",
               [_opt("force", "Rebuild even if current", "ignores the build stamp")], classify, estimate, runner)


def _preview_job():
    def classify(r, v):
        d, an, bs, low = r[0], r[1], r[2], r[3]
        if not _has_model(d):
            return "blocked", "no model.py"
        if v["force"] or bs != "current" or low < 6 or (not v["stills"] and not _rig_current(d, an)):
            return "todo", "needs it"
        return "done", "previewed"

    def estimate(rows, v):
        t = 0.0
        for r in rows:
            try:
                t += sum(vf.todo_of(r[0], r[1], "LOW", v["force"])[1])
            except OSError:
                t += 25
            if not v["stills"]:
                t += 90 / max(1, int(v["jobs"]))
        return t

    def runner(rows, v):
        return RJ.preview_many(rows, force=v["force"], stills=v["stills"], rig_force=v["rig_force"], jobs=int(v["jobs"]))
    return Job("preview", "LOW previews", "Six LOW review images and a contact sheet, then the rig, the rig check and the loops.",
               [_opt("stills", "Stills only", "skip the rig and the GIF loops"),
                _opt("force", "Render again even if current"),
                _opt("rig_force", "Rig again even if current", "rebuilds the rig and the GIF loops"),
                _opt("jobs", "Rigs at the same time", "more is faster, and heavier on the PC", 3, "choice",
                     [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (6, "6")])],
               classify, estimate, runner)


def _rig_job():
    def classify(r, v):
        d, an = r[0], r[1]
        if not _has_model(d):
            return "blocked", "no model.py"
        return ("done", "rig current") if _rig_current(d, an) and not v["force"] else ("todo", "needs it")

    def estimate(rows, v):
        n = sum(classify(r, v)[0] == "todo" for r in rows)
        return n * 90 / max(1, int(v["jobs"]))

    def runner(rows, v):
        return RJ.rig_many(rows, force=v["force"], no_preview=v["no_preview"], jobs=int(v["jobs"]), lineups=v["lineups"])
    return Job("rig", "Rig + GIF loops", "The armature, the rig check and the looping previews.",
               [_opt("force", "Rig again even if current"),
                _opt("no_preview", "No GIF loops", "the rig and its check only"),
                _opt("lineups", "Redraw the lineup sheets", "T-pose and motion sheets in 02 Animals"),
                _opt("jobs", "Rigs at the same time", "", 3, "choice", [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (6, "6")])],
               classify, estimate, runner)


def _final_job():
    ids = [p[0] for p in RJ.FINAL_PARTS]

    def parts(v):
        return _parts_of(v, ids)

    def classify(r, v):
        d, an = r[0], r[1]
        if not _has_model(d):
            return "blocked", "no model.py"
        if not v["low"] and not (an.get("approvals") or {}).get("preview"):
            return "blocked", "no preview approval"
        if not parts(v):
            return "done", "nothing chosen"
        plan = vf.final_plan(d, an, low=v["low"], force=v["force"], parts=parts(v))
        return ("todo", ", ".join(w for w, _ in plan)) if plan else ("done", "rendered")

    def estimate(rows, v):
        return sum(sec for r in rows if classify(r, v)[0] == "todo"
                   for _, sec in vf.final_plan(r[0], r[1], low=v["low"], force=v["force"], parts=parts(v)))

    def runner(rows, v):
        return RJ.final_many(rows, parts=parts(v), low=v["low"], force=v["force"])
    opts = [_opt(p[0], p[1], p[2], True, group="What to render") for p in RJ.FINAL_PARTS]
    opts += [_opt("force", "Render again even if current"),
             _opt("low", "LOW test render", "same set at LOW into the cache: layout tests, no approval needed")]
    presets = (("full", "all three", ids), ("masters", "the two masters", ("dyn", "block")), ("loop", "the loop frames", ("loop",)))
    return Job("final", "ULTRA renders", "The two 4096 masters and the frames of the loop (the GPU part: the RTX 3050).",
               opts, classify, estimate, runner, presets)


def _package_job():
    ids = list(RJ.PART_IDS)

    def parts(v):
        return _parts_of(v, ids)

    def classify(r, v):
        d, an = r[0], r[1]
        if not parts(v):
            return "done", "nothing chosen"
        st = RJ.package_state(d, an, parts(v), v["low"])
        if st == "not rendered":
            return "blocked", "not rendered yet"
        return ("todo", "needs it") if st == "todo" or v["force"] else ("done", "current")

    def estimate(rows, v):
        n = sum(classify(r, v)[0] == "todo" for r in rows)
        return n * RJ.package_seconds([p for p in parts(v) if not v["low"] or p in RJ.LOW_PARTS])

    def runner(rows, v):
        return RJ.package_many(rows, parts=parts(v), low=v["low"], force=v["force"])
    opts = [_opt(p[0], p[1], p[2], True, group="What to build") for p in RJ.PACKAGE_PARTS]
    opts += [_opt("force", "Build again even if current", "otherwise only what is missing or older than its source"),
             _opt("low", "LOW test set", "the GIF and cards from the LOW renders, in the cache (not exported)")]
    presets = tuple((name, label, parts_) for name, label, parts_ in
                    (("full", "full package", RJ.PART_IDS), ("stock", "stock only: JPEG + CSVs + registry", ("stock", "csv", "registry")),
                     ("pdf", "PDF cards only", ("card_en", "card_id")), ("gif", "GIF only", ("gif",)),
                     ("gumroad", "Gumroad bundle: GIF, cards, zip", ("gif", "card_en", "card_id", "zip", "registry"))))
    return Job("package", "Package", "Everything offline after the renders: choose the pieces.",
               opts, classify, estimate, runner, presets)


def make_jobs():
    jobs = {j.key: j for j in (_build_job(), _preview_job(), _final_job(), _package_job(), _rig_job())}
    for j in jobs.values():
        j.options.append(SHUTDOWN)
    return jobs


# ---- choosing animals -------------------------------------------------------------------------------------------------
def _matches(row, text):
    d, an = row[0], row[1]
    hay = f"{an['code']} {an['common']} {an.get('scientific', '')}".lower()
    return text.lower() in hay


def apply_selection(text, rows, sel, classes):
    """Applies a line such as '3 5-9 000012 all todo none invert /fox !wolf' to `sel` (a set of codes).
    `classes` is {code: (kind, why)}. Returns a one-line message ('' when nothing to say)."""
    msgs = []
    by_code = {r[1]["code"]: r for r in rows}
    elig = {code for code, (k, _) in classes.items() if k != "blocked"}
    todo = {code for code, (k, _) in classes.items() if k == "todo"}

    def toggle(code):
        if code not in by_code:
            msgs.append(f"no animal {code}")
        elif code not in elig:
            msgs.append(f"{code}: {classes[code][1]}")
        else:
            sel.symmetric_difference_update({code})

    for tok in re.split(r"[,\s]+", text.strip()):
        if not tok:
            continue
        low = tok.lower()
        if low == "all":
            sel |= elig
        elif low == "none":
            sel.clear()
        elif low == "todo":
            sel.clear()
            sel |= todo
        elif low in ("invert", "inv"):
            sel.symmetric_difference_update(elig)
            sel &= elig
        elif low in ("done",):
            sel.clear()
            sel |= {code for code, (k, _) in classes.items() if k == "done"}
        elif tok.startswith("/") and len(tok) > 1:
            sel |= {r[1]["code"] for r in rows if _matches(r, tok[1:]) and r[1]["code"] in elig}
        elif tok.startswith("!") and len(tok) > 1:
            sel -= {r[1]["code"] for r in rows if _matches(r, tok[1:])}
        elif re.fullmatch(r"\d{1,4}-\d{1,4}", tok):
            a, b = (int(x) for x in tok.split("-"))
            for i in range(min(a, b), max(a, b) + 1):
                if 1 <= i <= len(rows):
                    toggle(rows[i - 1][1]["code"])
        elif re.fullmatch(r"\d{5,}-\d{5,}", tok):                 # a range of codes
            a, b = (int(x) for x in tok.split("-"))
            for code in by_code:
                if code.isdigit() and min(a, b) <= int(code) <= max(a, b):
                    toggle(code)
        elif re.fullmatch(r"\d{1,4}", tok):
            i = int(tok)
            if 1 <= i <= len(rows):
                toggle(rows[i - 1][1]["code"])
            else:
                msgs.append(f"no number {i}")
        elif re.fullmatch(r"\d{5,}", tok):
            toggle(tok.zfill(6) if len(tok) < 6 else tok)
        else:
            hits = [r[1]["code"] for r in rows if _matches(r, tok)]
            if hits:
                sel |= {h for h in hits if h in elig}
            else:
                msgs.append(f"'{tok}' matches nothing")
    sel &= elig
    return "; ".join(msgs[:3])


def pick_animals(job, rows, sel, classes):
    """The animal chooser: a paged checklist with a command line under it. Returns the set of chosen codes (or the
    same set unchanged on q)."""
    page, msg = 0, ""
    size = max(8, min(40, shutil.get_terminal_size((100, 40)).lines - 17))
    pages = max(1, (len(rows) + size - 1) // size)
    work = set(sel)
    while True:
        header(f"Choose animals  ·  {job.title}")
        n_todo = sum(k == "todo" for k, _ in classes.values())
        say(f"{c(str(len(work)), 'b', 'green')} of {len(rows)} chosen   "
            + c(f"{n_todo} still need it · page {page + 1}/{pages}", "grey"))
        rule()
        for i in range(page * size, min(len(rows), (page + 1) * size)):
            d, an = rows[i][0], rows[i][1]
            kind, why = classes[an["code"]]
            colour = {"todo": "yellow", "done": "green", "blocked": "grey"}[kind]
            box_ = ON if an["code"] in work else OFF
            mark = c(box_, "green") if an["code"] in work else c(box_, "grey" if kind == "blocked" else "white")
            name = clip(an["common"], 26)
            print(f"  {mark} {c(f'{i + 1:>3}', 'grey')}  {an['code']}  {pad(c(name, 'grey' if kind == 'blocked' else 'white'), 26)}"
                  f" {c(DOT, colour)} {c(clip(why, 28), colour if kind != 'blocked' else 'grey')}")
        rule()
        say(c("numbers and ranges toggle (3 5-9)  ·  a code (000012) or a range of codes  ·  a name finds it", "grey"))
        say(c("all · none · todo · done · invert  ·  /fox adds matches  ·  !fox removes them  ·  n / p page  ·  g5 go to page", "grey"))
        say(c("Enter = done  ·  q = cancel", "grey"))
        if msg:
            say(c(msg, "yellow"))
            msg = ""
        line = ask("Choose:")
        low = line.lower()
        if not line:
            return work
        if low in ("q", "quit", "cancel"):
            return set(sel)
        if low in ("n", "next"):
            page = min(pages - 1, page + 1)
        elif low in ("p", "prev"):
            page = max(0, page - 1)
        elif re.fullmatch(r"g\d+", low):
            page = max(0, min(pages - 1, int(low[1:]) - 1))
        else:
            msg = apply_selection(line, rows, work, classes)


# ---- the job screen ---------------------------------------------------------------------------------------------------
def _numbered(job):
    return list(enumerate(job.options, 1))


def render_job_screen(job, rows, sel, values, classes, note=""):
    header(job.title)
    say(c(job.blurb, "grey"))
    print()
    elig = sum(k != "blocked" for k, _ in classes.values())
    todo = sum(k == "todo" for k, _ in classes.values())
    try:
        secs = job.estimate([r for r in rows if r[1]["code"] in sel and classes[r[1]["code"]][0] != "blocked"], values)
    except Exception:
        secs = 0
    say(f"{c('Animals', 'b')}   {c(str(len(sel)), 'b', 'green')} of {len(rows)} chosen"
        + c(f"  ({todo} still need it, {elig} can run)", "grey")
        + (f"   {c('about ' + hm(secs), 'yellow')}" if len(sel) and secs else ""))
    chosen = [r[1] for r in rows if r[1]["code"] in sel]
    if chosen:
        names = ", ".join(f"{a['code']} {a['common']}" for a in chosen[:3]) + (f" and {len(chosen) - 3} more" if len(chosen) > 3 else "")
        say(c("          " + clip(names, W - 14), "grey"))
    else:
        say(c("          nothing chosen: press A to choose, or type  todo  /  all", "red"))
    print()
    groups = []
    for n, o in _numbered(job):
        if not groups or groups[-1][0] != o["group"]:
            groups.append((o["group"], []))
        groups[-1][1].append((n, o))
    half = W - 2
    for gname, items in groups:
        body = []
        for n, o in items:
            if o["kind"] == "check":
                mark = c(ON, "green") if values[o["id"]] else c(OFF, "grey")
                txt = c(o["label"], "b" if values[o["id"]] else "white")
            else:
                cur = dict(o["choices"])[values[o["id"]]]
                mark = c(RADIO, "cyan")
                txt = f"{o['label']}: " + c(cur, "cyan", "b") + c("  (press again to change)", "grey")
            hint = c("  " + o["hint"], "grey") if o["hint"] else ""
            body.append(f"{c(f'[{n}]', 'cyan', 'b')} {mark} {txt}{hint}")
        for ln in box(gname, body, half, "cyan" if gname.startswith("What") else "magenta" if gname == "Options" else "yellow"):
            print("  " + ln)
    if job.presets:
        print("  " + c("presets:  ", "grey") + "   ".join(f"{c(n, 'cyan', 'b')} {c('= ' + lab, 'grey')}" for n, lab, _ in job.presets[:3]))
        if len(job.presets) > 3:
            print("            " + "   ".join(f"{c(n, 'cyan', 'b')} {c('= ' + lab, 'grey')}" for n, lab, _ in job.presets[3:]))
    print()
    say(f"{c('Enter', 'green', 'b')} run   {c('A', 'cyan', 'b')} choose animals   "
        f"{c('todo / all / none', 'cyan', 'b')} quick choice   {c('numbers', 'cyan', 'b')} change options   {c('Q', 'cyan', 'b')} back")
    if note:
        say(c(note, "yellow"))


def configure(job, rows, preset_codes=None):
    """The job screen: choose animals and options, then run. Returns True when something ran."""
    values = job.defaults()

    def classify_all():
        out = {}
        for r in rows:
            try:
                out[r[1]["code"]] = job.classify(r, values)
            except Exception as e:                              # an unreadable animal never stops the menu
                out[r[1]["code"]] = ("blocked", str(e)[:40])
        return out

    classes = classify_all()
    sel = set(preset_codes) if preset_codes is not None else {code for code, (k, _) in classes.items() if k == "todo"}
    sel = {code for code in sel if classes.get(code, ("blocked",))[0] != "blocked"}
    note = ""
    while True:
        render_job_screen(job, rows, sel, values, classes, note)
        note = ""
        line = ask("Option:")
        low = line.lower()
        if low in ("q", "quit", "back", "cancel"):
            return False
        if low in ("", "go", "run", "r"):
            chosen = [r for r in rows if r[1]["code"] in sel and classes[r[1]["code"]][0] != "blocked"]
            if not chosen:
                note = "Nothing chosen: press A, or type  todo  or  all."
                continue
            if job.key == "package" and not _parts_of(values, list(RJ.PART_IDS)):
                note = "No parts ticked: tick at least one (numbers), or type  full."
                continue
            if job.key == "final" and not _parts_of(values, [p[0] for p in RJ.FINAL_PARTS]):
                note = "Nothing ticked to render: tick at least one (numbers)."
                continue
            try:
                secs = job.estimate(chosen, values)
            except Exception:
                secs = 0
            if len(chosen) > 3 or secs >= 600:                      # a big batch: one more Enter before it starts
                what = f"{len(chosen)} animal(s)" + (f", about {hm(secs)}" if secs else "")
                if ask(f"Run {c(what, 'yellow', 'b')} now? [Y/n]").lower() in ("n", "no", "q"):
                    continue
            save_options(job, values)
            header(job.title)
            say(f"{len(chosen)} animal(s): " + c(clip(", ".join(r[1]["code"] for r in chosen), W - 30), "grey"))
            ok = run(job.title.lower(), lambda: job.runner(chosen, values))
            if values.get("shutdown") and ok:
                say("Shutting this PC down in 60 seconds (shutdown /a to cancel).", "yellow")
                os.system('shutdown /s /t 60 /c "Voxel Fauna render finished"')
            wait()
            return True
        if low in ("a", "animals", "choose", "pick"):
            sel = pick_animals(job, rows, sel, classes)
            continue
        if low in [n for n, _, _ in job.presets]:
            ids = next(p for n, _, p in job.presets if n == low)
            for o in job.options:
                if o["kind"] == "check" and o["group"].startswith("What"):
                    values[o["id"]] = o["id"] in ids
            classes = classify_all()
            continue
        # numbers toggle options; anything else is a selection command (all, none, todo, 3-5, /fox ...)
        toks = re.split(r"[,\s]+", line)
        if all(re.fullmatch(r"\d{1,2}", t) and 1 <= int(t) <= len(job.options) for t in toks if t):
            for t in toks:
                if not t:
                    continue
                o = job.options[int(t) - 1]
                if o["kind"] == "check":
                    values[o["id"]] = not values[o["id"]]
                else:
                    vs = [x for x, _ in o["choices"]]
                    values[o["id"]] = vs[(vs.index(values[o["id"]]) + 1) % len(vs)]
            classes = classify_all()
            continue
        note = apply_selection(line, rows, sel, classes) or note


# ---- the home screen --------------------------------------------------------------------------------------------------
def item(key, text, count=None, on=True, colour="cyan"):
    mark = c("[" + key + "]", colour if on else "grey", "b")
    tail = c(f"  {count}", "yellow") if count else ""
    return f"{mark} {text if on else c(text, 'grey')}{tail}"


def splash():
    cls()
    print()
    for ln in ART.cover(COLOR, BLOCK, W):
        print(ln)
    print()


def one_animal(rows, jobs):
    header("One animal")
    code = ask("Animal code or number (e.g. 000001 or 5):")
    if not code:
        return
    sel = set()
    classes = {r[1]["code"]: ("done", "") for r in rows}
    apply_selection(code, rows, sel, classes)
    if not sel:
        say(f"No animal for '{code}'.", "red")
        wait()
        return
    an = next(r[1] for r in rows if r[1]["code"] in sel)
    what = ask(f"{an['code']} {an['common']}: {c('b', 'b')}uild, {c('p', 'b')}review, {c('f', 'b')}inal, pac{c('k', 'b')}age, "
               f"{c('r', 'b')}ig?").lower()[:1]
    key = {"b": "build", "p": "preview", "f": "final", "k": "package", "r": "rig"}.get(what)
    if key:
        configure(jobs[key], rows, preset_codes=sel)


def menu():
    jobs = make_jobs()
    splash()
    rows = collect(label="Reading animals")
    while True:
        header()
        summary(rows)
        counts = {}
        for key, j in jobs.items():
            vals = j.defaults()
            n = 0
            for r in rows:
                try:
                    n += j.classify(r, vals)[0] == "todo"
                except Exception:
                    pass
            counts[key] = f"{n} todo" if n else ""
        left = box("RENDER", [
            item("1", "Build .blend files", counts["build"], colour="green"),
            item("2", "LOW previews, rigs, loops", counts["preview"], colour="green"),
            item("3", "ULTRA masters + loop", counts["final"], colour="green"),
            item("P", "Package: GIF, cards, stock", counts["package"], colour="green"),
            item("R", "Rig + GIF loops", counts["rig"], colour="green"),
        ], 48, "green")
        right = box("CHECK", [item("5", "Animal status"), item("6", "One animal's files")], W - 52, "cyan")
        more = box("MORE", [item("4", "One animal, any step"), item("Q", "Quit", colour="grey")], W - 52, "yellow")
        for ln in side_by_side(left, right + more):
            print(ln)
        print()
        say(c("Every step asks which animals (the ones that need it, all, or your own list) and what to build.", "grey"))
        say(c("Pause any time: Ctrl+C or close the window; finished work is kept. Animals: " + clip(VL.ANIMALS, W - 40), "grey"))
        print()
        k = ask("Choose:").lower()
        if k in ("1", "2", "3", "p", "r"):
            key = {"1": "build", "2": "preview", "3": "final", "p": "package", "r": "rig"}[k]
            if configure(jobs[key], rows):
                rows = collect(label="Reading animals")
        elif k == "4":
            one_animal(rows, jobs)
            rows = collect(label="Reading animals")
        elif k == "5":
            screen_status(rows)
            wait()
        elif k == "6":
            files_of()
            wait()
        elif k in ("q", "quit", "exit"):
            return


# ---- the command line -------------------------------------------------------------------------------------------------
def resolve(tokens, rows, classes, take_all):
    """Animals for a command line: codes, ranges, names; `all`; nothing = the ones that still need it."""
    sel = set()
    if take_all or any(t.lower() == "all" for t in tokens):
        sel |= {code for code, (k, _) in classes.items() if k != "blocked"}
    elif not tokens:
        sel |= {code for code, (k, _) in classes.items() if k == "todo"}
    else:
        msg = apply_selection(" ".join(t for t in tokens if t.lower() != "all"), rows, sel, classes)
        if msg:
            say(msg, "yellow")
    return sel


def cli(argv):
    ap = argparse.ArgumentParser(prog="render.bat", description="Voxel Fauna render. No arguments: the menu.")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("status")
    p = sub.add_parser("files")
    p.add_argument("code")
    for name, helptext in (("build", "build the .blend files"), ("preview", "LOW previews, rigs and loops"),
                           ("final", "ULTRA masters and the loop"), ("package", "GIF, cards, stock, zip, registry"),
                           ("rig", "rig and GIF loops")):
        p = sub.add_parser(name, help=helptext)
        p.add_argument("animals", nargs="*", help="codes, ranges (000001-000010), names, or all; none = those that need it")
        p.add_argument("--all", action="store_true", help="every animal this can run on")
        p.add_argument("--force", action="store_true")
        p.add_argument("--shutdown", action="store_true", help="shut the PC down when it finishes (60 s to cancel)")
        if name == "preview":
            p.add_argument("--stills", action="store_true")
            p.add_argument("--rig-force", action="store_true")
            p.add_argument("--jobs", type=int, default=3)
        if name == "final":
            p.add_argument("--parts", default="dyn,block,loop", help="dyn,block,loop")
            p.add_argument("--low", action="store_true")
        if name == "package":
            p.add_argument("--preset", choices=[x[0] for x in make_jobs()["package"].presets])
            p.add_argument("--parts", help=",".join(RJ.PART_IDS))
            p.add_argument("--low", action="store_true")
        if name == "rig":
            p.add_argument("--no-preview", action="store_true")
            p.add_argument("--jobs", type=int, default=3)
            p.add_argument("--lineups", action="store_true")
    known = {"status", "files", "build", "preview", "final", "package", "rig"}
    alias = {"low": "preview", "ultra": "final"}
    if argv and argv[0].lower() in alias:
        argv = [alias[argv[0].lower()]] + argv[1:]
    if argv and argv[0].lower() not in known and not argv[0].startswith("-"):   # render.bat <code> [preview|final|package]
        argv = [{"final": "final", "package": "package"}.get((argv[1] if len(argv) > 1 else "preview").lower(), "preview"),
                argv[0]]
    a = ap.parse_args(argv)
    if a.cmd == "status":
        return screen_status()
    if a.cmd == "files":
        return files_of(a.code)
    jobs = make_jobs()
    job = jobs[a.cmd]
    values = {o["id"]: o["default"] for o in job.options}        # the command line never reads the remembered choices
    values["force"] = a.force
    values["shutdown"] = a.shutdown
    for k in ("stills", "rig_force", "jobs", "low", "no_preview", "lineups"):
        if hasattr(a, k):
            values[k] = getattr(a, k)
    if a.cmd == "final":
        want = {x.strip() for x in a.parts.split(",") if x.strip()}
        for pid, *_ in RJ.FINAL_PARTS:
            values[pid] = pid in want
    if a.cmd == "package":
        if a.preset:
            want = set(next(p for n, _, p in job.presets if n == a.preset))
        elif a.parts:
            want = {x.strip() for x in a.parts.split(",") if x.strip()}
        else:
            want = set(RJ.PART_IDS)
        for pid in RJ.PART_IDS:
            values[pid] = pid in want
    rows = collect(show=True, label="Reading animals")
    classes = {r[1]["code"]: job.classify(r, values) for r in rows}
    sel = resolve(a.animals, rows, classes, a.all)
    chosen = [r for r in rows if r[1]["code"] in sel]
    if not chosen:
        say("Nothing to do: no animal needs this (use `all`, or name the animals).", "grey")
        return
    say(f"{job.title}: {len(chosen)} animal(s)")
    ok = run(job.title.lower(), lambda: job.runner(chosen, values))
    if values.get("shutdown") and ok:
        say("Shutting this PC down in 60 seconds (shutdown /a to cancel).", "yellow")
        os.system('shutdown /s /t 60 /c "Voxel Fauna render finished"')


def main(argv):
    if not argv:
        return menu()
    return cli(argv)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        VL.LIVE.stop()
        print(f"\n  {c('stopped', 'yellow')}")
