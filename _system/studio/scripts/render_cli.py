"""Voxel Fauna · the render menu behind render.bat (the same idea as Nilant's footage_cli: one window, offline).

    RENDER   1 build every missing or stale .blend   2 LOW previews of every built animal
             3 ULTRA finals of every approved animal  4 one animal (build, preview or final)
    CHECK    5 status of every animal                 6 one animal's files
    CONTROL  Q quit
Without the menu: render.bat status | build | preview | final | <code> [preview|final]

Blender renders, this Python lays the information cards (Pillow). No internet. Pause any time with Ctrl+C or by
closing the window: finished images are kept, and the next run skips them (it renders only what is missing or older
than its .blend).
"""
import datetime
import json
import os
import sys
import time

os.system("")                                    # enable ANSI colours in the Windows console
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vflib as VL  # noqa: E402
import vf  # noqa: E402

ST = VL.ST
G, R, Y, B, M, C, D, W, END = ("\033[92m", "\033[91m", "\033[93m", "\033[94m", "\033[95m", "\033[96m", "\033[90m",
                               "\033[97m", "\033[0m")


def state(d):
    an = VL.load(d)
    has_model = os.path.exists(os.path.join(d, "blender", "model.py"))
    bs = vf.build_state(d, an)[0] if has_model else "no model"
    low = sum(os.path.exists(t["final"]) for t in vf.targets(an, "LOW", d)[0])
    ult = sum(os.path.exists(t["final"]) for t in vf.targets(an, "ULTRA", d)[0])
    ap = an.get("approvals") or {}
    return an, bs, low, ult, ap


def colour_of(bs, low, ult, ap):
    if bs in ("missing", "no model"):
        return D
    if bs == "stale":
        return R
    if ap.get("final") and ult == 6:
        return G
    if ap.get("preview"):
        return Y if ult < 6 else G
    return B if low == 6 else C


def status(verbose=True):
    rows = [(d, *state(d)) for d in VL.animal_dirs()]
    n = len(rows)
    built = sum(r[2] == "current" for r in rows)
    stale = sum(r[2] == "stale" for r in rows)
    prev = sum(r[3] == 6 for r in rows)
    appr = sum(bool(r[5].get("preview")) for r in rows)
    fin = sum(r[4] == 6 for r in rows)
    print(f" {W}{n}{END} animals · {G}{built}{END} built · {R}{stale}{END} stale · {B}{prev}{END} previewed · "
          f"{Y}{appr}{END} preview-approved · {G}{fin}{END} with all six finals")
    if verbose:
        print(f" {D}code    animal              .blend    LOW   approved     ULTRA  final{END}")
        for d, an, bs, low, ult, ap in rows:
            c = colour_of(bs, low, ult, ap)
            print(f" {c}{an['code']}  {an['common'][:18]:<18}  {bs:<8}  {low}/6   {(ap.get('preview') or '-'):<11}  {ult}/6    "
                  f"{ap.get('final') or '-'}{END}")
        print(f" {D}colours: {G}done {B}LOW preview {Y}approved, final to render {R}stale (build again) "
              f"{C}built {D}not built{END}")
    vf.write_render_readme()
    return rows


def eta(rows, profile):
    secs = 0
    for d, an, bs, low, ult, ap in rows:
        if profile == "ULTRA" and not ap.get("preview"):
            continue
        done = ult if profile == "ULTRA" else low
        if done < 6:
            secs += sum(ST.PROFILES[profile]["estimate"].values()) * 2 * (6 - done) / 6
    return secs


def run(label, fn):
    t = time.time()
    try:
        fn()
        print(f" {G}{label}: done in {time.time() - t:.0f} s{END}")
    except KeyboardInterrupt:
        print(f"\n {Y}{label}: paused (finished images are kept; run it again to carry on){END}")
    except SystemExit as e:
        print(f" {R}{label}: {e}{END}")


def do_build_all():
    for d in VL.animal_dirs():
        an = VL.load(d)
        if os.path.exists(os.path.join(d, "blender", "model.py")):
            if vf.do_build(d, an):
                vf.advance(an, "Modelling")
                VL.save(d, an)
                vf.write_overview(d, an)


def one_animal():
    rows = status(verbose=True)
    code = input(f" {W}code (e.g. 26-001):{END} ").strip()
    d = VL.find(code)
    an = VL.load(d)
    what = input(f" {W}b{END}uild, {W}p{END}review (LOW) or {W}f{END}inal (ULTRA)? ").strip().lower()[:1]
    if what == "b":
        run(f"build {code}", lambda: vf.do_build(d, an, force=True))
    elif what == "p":
        run(f"preview {code}", lambda: print("  ->", VL.rel(vf.preview(d, an))))
    elif what == "f":
        run(f"final {code}", lambda: [print(f"  {R}{e}{END}") for e in vf.final(d, an)])


def files_of():
    code = input(f" {W}code:{END} ").strip()
    d = VL.find(code)
    an, bs, low, ult, ap = state(d)
    print(f" {W}{an['code']} · {an['common']}{END} ({an['scientific']}), status {an['status']}, .blend {bs}")
    for t in vf.targets(an, "ULTRA", d)[0]:
        ok = os.path.exists(t["final"])
        print(f"  {G if ok else D}{os.path.basename(t['final'])}{END}" + (f"  {D}{os.path.getsize(t['final']) // 1024} KB{END}" if ok else ""))
    print(f"  {D}preview: {VL.rel(os.path.join(VL.CACHE, 'preview', an['code']))}{END}")


def menu():
    while True:
        print(f"\n {W}Voxel Fauna · render{END}  {D}{datetime.datetime.now():%Y-%m-%d %H:%M} · Blender {os.path.basename(os.path.dirname(VL.blender_exe()))}{END}")
        rows = status(verbose=False)
        low_eta, ult_eta = eta(rows, "LOW"), eta(rows, "ULTRA")
        print(f"\n {C}RENDER{END}   1 Build every missing or stale .blend")
        print(f"          2 LOW previews of every built animal {D}(~{low_eta / 60:.0f} min){END}")
        print(f"          3 ULTRA finals of every preview-approved animal {D}(~{ult_eta / 60:.0f} min; skips finished images){END}")
        print("          4 One animal (build, preview or final)")
        print(f" {C}CHECK{END}    5 Status of every animal     6 One animal's files")
        print(f" {C}CONTROL{END}  Q Quit   {D}(Ctrl+C pauses a render; run it again to carry on){END}")
        k = input(f"\n {W}choose:{END} ").strip().lower()
        if k == "1":
            run("build", do_build_all)
        elif k == "2":
            run("LOW previews", lambda: vf.cmd_render_all(type("A", (), dict(profile="LOW", force=False))()))
        elif k == "3":
            run("ULTRA finals", lambda: vf.cmd_render_all(type("A", (), dict(profile="ULTRA", force=False))()))
        elif k == "4":
            run("one animal", one_animal)
        elif k == "5":
            status(verbose=True)
        elif k == "6":
            run("files", files_of)
        elif k in ("q", ""):
            return


def main(argv):
    if not argv:
        return menu()
    a = argv[0].lower()
    if a == "status":
        status(verbose=True)
    elif a == "build":
        run("build", do_build_all)
    elif a in ("preview", "low"):
        run("LOW previews", lambda: vf.cmd_render_all(type("A", (), dict(profile="LOW", force=False))()))
    elif a in ("final", "ultra"):
        run("ULTRA finals", lambda: vf.cmd_render_all(type("A", (), dict(profile="ULTRA", force=False))()))
    else:
        d = VL.find(argv[0])
        an = VL.load(d)
        what = (argv[1] if len(argv) > 1 else "preview").lower()
        if what == "final":
            run(f"final {argv[0]}", lambda: [print(f"  {R}{e}{END}") for e in vf.final(d, an)])
        else:
            run(f"preview {argv[0]}", lambda: print("  ->", VL.rel(vf.preview(d, an))))


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print(f"\n {Y}stopped{END}")
