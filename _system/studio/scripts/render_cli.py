"""Voxel Fauna · the render menu behind render.bat (the look of Nilant's footage_cli: title bar, bars, coloured panels).

    RENDER   1 build every missing or stale .blend   2 LOW previews of every built animal (+ rigs and loops)
             3 ULTRA renders of every approved animal: the two masters and the loop (rendering only;
               package.bat then builds the stock image, the GIF and the cards)   4 one animal (build, preview or final)
    MOTION   R rig every animal + GIF loops
    CHECK    5 status of every animal                 6 one animal's files
    CONTROL  Q quit
Without the menu: render.bat status | build | preview | final | rig | <code> [preview|final]

Blender renders (and Pillow lays the LOW preview cards). No internet. Pause any time with Ctrl+C or by
closing the window: finished images are kept, and the next run skips them (it renders only what is missing or older
than its .blend).
"""
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vflib as VL  # noqa: E402
import vf  # noqa: E402

ST = VL.ST
W = 80                                                     # the width everything is laid out to


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
    "█░●✓▶─".encode(sys.stdout.encoding or "utf-8")
    BLOCK, SHADE, DOT, TICK, PLAY, LINE = "█", "░", "●", "✓", "▶", "─"
except Exception:
    BLOCK, SHADE, DOT, TICK, PLAY, LINE = "#", ".", "o", "+", ">", "-"

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


def bar(frac, width=26, colour="green"):
    n = int(round(max(0.0, min(1.0, frac)) * width))
    return c(BLOCK * n, colour) + c(SHADE * (width - n), "grey")


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def rule():
    print("  " + c(LINE * (W - 2), "grey"))


def say(text, colour=None):
    print("  " + (c(text, colour) if colour else text))


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


# ---- what every animal looks like right now ---------------------------------------------------------------------------
def state(d):
    an = VL.load(d)
    has_model = os.path.exists(os.path.join(d, "blender", "model.py"))
    bs = vf.build_state(d, an)[0] if has_model else "no model"
    low = sum(os.path.exists(t["final"]) for t in vf.targets(an, "LOW", d)[0])
    import package as PK
    ult = sum(os.path.exists(PK.export_file(d, an["code"], s)) for s, _, _ in PK.EXPORT["items"])
    ap = an.get("approvals") or {}                 # ult: the six items of the export package
    return an, bs, low, ult, ap


def colour_of(bs, low, ult, ap):
    if bs in ("missing", "no model"):
        return "grey"
    if bs == "stale":
        return "red"
    if ap.get("final") and ult == 6:
        return "green"
    if ap.get("preview"):
        return "yellow" if ult < 6 else "green"
    return "blue" if low == 6 else "cyan"


def collect():
    return [(d, *state(d)) for d in VL.animal_dirs()]


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


def hm(sec):
    return f"{sec / 3600:.1f} h" if sec >= 5400 else f"{max(1, round(sec / 60))} min"


def summary(rows):
    n = max(1, len(rows))
    built = sum(r[2] == "current" for r in rows)
    stale = sum(r[2] == "stale" for r in rows)
    prev = sum(r[3] == 6 for r in rows)
    appr = sum(bool(r[5].get("preview")) for r in rows)
    fin = sum(r[4] == 6 for r in rows)
    print(f"  {c('Animals', 'b')}    {bar(built / n)}  {c(f'{built} of {len(rows)}', 'b')} built"
          + (c(f", {stale} stale: choose 1", "red", "b") if stale else ""))
    print(f"  {c('Previews', 'b')}   {bar(prev / n, colour='blue')}  {c(f'{prev} of {len(rows)}', 'b')} with six LOW images"
          f"  {c(f'({appr} approved)', 'grey')}")
    print(f"  {c('Finals', 'b')}     {bar(fin / n, colour='magenta')}  {c(f'{fin} of {len(rows)}', 'b')} with the whole export package"
          f"  {c('(masters 4096 px, loop, cards)', 'grey')}")
    ult_n, ult_s = pending(rows, "ULTRA")
    if ult_n:
        print(f"  {c('Next', 'b')}       {c(f'{ult_n} ULTRA render(s)', 'yellow')} waiting for approved animals, "
              f"{c('roughly ' + hm(ult_s * 1.0), 'yellow')}")
    elif any(r[5].get("preview") and r[4] < 6 for r in rows):
        todo_pkg = sum(bool(r[5].get("preview")) and r[4] < 6 for r in rows)
        print(f"  {c('Next', 'b')}       {c(TICK + ' renders done', 'green')}; {c(f'{todo_pkg} animal(s) still need package.bat', 'yellow')}"
              f" {c('(stock crop, GIF, cards)', 'grey')}")
    elif appr:
        print(f"  {c('Next', 'b')}       {c(TICK + ' every approved animal has its export package', 'green')}")
    else:
        print(f"  {c('Next', 'b')}       {c('approve a preview (vf.py approve <code> preview) before an ULTRA render', 'grey')}")
    print()
    return ult_n, ult_s


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
        ub = c(BLOCK * ult, "green") + c(SHADE * (6 - ult), "grey")
        print(f"  {c(DOT, col)} {an['code']:<7} {an['common'][:20]:<20} {pad(c(bs, col), 8)} {low}/6  "
              f"{(ap.get('preview') or '-'):<11} {ub} {ult}/6"
              + (c(f"  final {ap['final']}", "green") if ap.get("final") else ""))
    rule()
    say(c("Colours show each animal's state. Choose 'One animal' for its files.", "grey"))
    vf.write_render_readme()


# ---- running things ---------------------------------------------------------------------------------------------------
def run(label, fn):
    t = time.time()
    try:
        fn()
        say(f"{c(TICK, 'green')} {label}: done in {c(vf_hms(time.time() - t), 'b')}")
    except KeyboardInterrupt:
        VL.LIVE.stop()
        print()
        say(f"{label}: paused (finished images are kept; run it again to carry on)", "yellow")
    except SystemExit as e:
        VL.LIVE.stop()
        say(f"{label}: {e}", "red")


def vf_hms(sec):
    return VL.hms(sec)


def do_build_all():
    todo = [d for d in VL.animal_dirs() if os.path.exists(os.path.join(d, "blender", "model.py"))]
    for i, d in enumerate(todo, 1):
        an = VL.load(d)
        say(c(f"[{i}/{len(todo)}]", "grey") + f" {an['code']} {an['common']}")
        if vf.do_build(d, an):
            vf.advance(an, "Modelling")
            VL.save(d, an)
            vf.write_overview(d, an)


def pick_animal():
    code = ask("Animal code (e.g. 26-001):")
    return VL.find(code) if code else None


def one_animal():
    header("One animal")
    rows = collect()
    for d, an, bs, low, ult, ap in rows:
        print(f"  {c(DOT, colour_of(bs, low, ult, ap))} {an['code']}  {an['common']}")
    print()
    d = pick_animal()
    if not d:
        return
    an = VL.load(d)
    what = ask(f"{c('b', 'b')}uild, {c('p', 'b')}review (LOW) or {c('f', 'b')}inal (ULTRA)?").lower()[:1]
    code = an["code"]
    if what == "b":
        run(f"build {code}", lambda: vf.do_build(d, an, force=True))
    elif what == "p":
        run(f"preview {code}", lambda: (print("  ->", VL.rel(vf.preview(d, an))), vf.do_rig(d, an)))
    elif what == "f":
        run(f"final {code}", lambda: [say(e, "red") for e in vf.final(d, an)])


def files_of():
    header("One animal's files")
    d = pick_animal()
    if not d:
        return
    an, bs, low, ult, ap = state(d)
    col = colour_of(bs, low, ult, ap)
    say(f"{c(an['code'] + ' · ' + an['common'], 'b')} {c('(' + an['scientific'] + ')', 'grey')}   "
        f"status {c(an['status'], col)}, .blend {c(bs, col)}")
    rule()
    import package as PK
    for s, _, what in PK.EXPORT["items"]:
        p = PK.export_file(d, an["code"], s)
        ok = os.path.exists(p)
        size = f", {os.path.getsize(p) // 1024:,} KB" if ok else ""
        say(f"{c(TICK if ok else DOT, 'green' if ok else 'grey')} {os.path.basename(p)}{c('  ' + what + size, 'grey')}")
    rule()
    say(c("LOW preview: " + VL.rel(os.path.join(VL.CACHE, "preview", an["code"])), "grey"))


def rig_all():
    vf.cmd_rig_all(type("A", (), dict(force=False, no_preview=False, jobs=3))())


def render_all(profile):
    return lambda: vf.cmd_render_all(type("A", (), dict(profile=profile, force=False))())


# ---- the home screen --------------------------------------------------------------------------------------------------
def item(key, text, on=True, colour="cyan"):
    return f"{c('[' + key + ']', colour if on else 'grey', 'b')} {text if on else c(text, 'grey')}"


def menu():
    while True:
        header()
        rows = collect()
        ult_n, ult_s = summary(rows)
        low_n, low_s = pending(rows, "LOW")
        stale = any(r[2] in ("stale", "missing") for r in rows)
        panels = [
            ([c(PLAY + " RENDER", "b", "green"),
              item("1", "Build missing or stale .blend", stale, "green"),
              item("2", "LOW previews + rigs and loops" + c(f"  ~{hm(low_s)}" if low_n else "", "grey")),
              item("3", "ULTRA masters + loop (approved)" + c(f"  ~{hm(ult_s)}" if ult_n else "", "grey"), bool(ult_n), "green"),
              item("4", "One animal"),
              item("R", "Rig every animal + GIF loops")],
             [c(PLAY + " CHECK", "b", "cyan"),
              item("5", "Animal status"),
              item("6", "One animal's files")]),
            ([c(PLAY + " CONTROL", "b", "yellow"),
              item("Q", "Quit", True, "grey")],
             [c("Pause any time", "grey"),
              c("Ctrl+C or close the window:", "grey"),
              c("finished images are kept; run it again", "grey"),
              c("after 3: package.bat builds the rest", "grey")]),
        ]
        for left_col, right_col in panels:
            for i in range(max(len(left_col), len(right_col))):
                a = left_col[i] if i < len(left_col) else ""
                b = right_col[i] if i < len(right_col) else ""
                print("  " + pad(a, 44) + b)
            print()
        k = ask("Choose:").lower()
        if k == "1":
            header("Build")
            run("build", do_build_all)
            wait()
        elif k == "2":
            header("LOW previews")
            run("LOW previews", render_all("LOW"))
            wait()
        elif k == "3":
            header("ULTRA finals")
            if not ult_n:
                say("Nothing to render: every approved animal is finished, or no preview is approved yet.", "grey")
            else:
                run("ULTRA finals", render_all("ULTRA"))
            wait()
        elif k == "4":
            one_animal()
            wait()
        elif k == "r":
            header("Rig")
            run("rig", rig_all)
            wait()
        elif k == "5":
            screen_status(rows)
            wait()
        elif k == "6":
            files_of()
            wait()
        elif k in ("q", "quit", "exit"):
            return


def main(argv):
    if not argv:
        return menu()
    a = argv[0].lower()
    if a == "status":
        screen_status()
    elif a == "build":
        run("build", do_build_all)
    elif a in ("preview", "low"):
        run("LOW previews", render_all("LOW"))
    elif a in ("final", "ultra"):
        run("ULTRA finals", render_all("ULTRA"))
    elif a == "rig":
        run("rig", rig_all)
    else:
        d = VL.find(argv[0])
        an = VL.load(d)
        what = (argv[1] if len(argv) > 1 else "preview").lower()
        if what == "final":
            run(f"final {argv[0]}", lambda: [say(e, "red") for e in vf.final(d, an)])
        else:
            run(f"preview {argv[0]}", lambda: (print("  ->", VL.rel(vf.preview(d, an))), vf.do_rig(d, an)))


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        VL.LIVE.stop()
        print(f"\n  {c('stopped', 'yellow')}")
