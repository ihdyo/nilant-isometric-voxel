"""Voxel Fauna · what the render menu runs: every step on a chosen list of animals, with chosen options.

The menu (render_cli.py) decides WHICH animals and WHAT; this module does it, with the live progress line:

    build_many(rows, force)                              model.py -> .blend
    preview_many(rows, force, stills, rig_force, jobs)   LOW stills, then the rig, the rig check and the GIF loops
    final_many(rows, parts, low, force)                  the ULTRA (or LOW) export renders: masters "dyn", "block", the "loop"
    package_many(rows, parts, low, force)                the offline package, any mix of PACKAGE_PARTS
    rig_many(rows, force, no_preview, jobs, lineups)     the rig and loops again

`rows` are the menu's rows: (folder, animal, ...). Every function returns (done, skipped): lists of codes and of
"code (why)" strings, and never stops at one animal's failure: the others go on.
"""
import os
import time

import vflib as VL
import vf

ST = VL.ST

# ---- the offline package, piece by piece ------------------------------------------------------------------------------
# (id, label, what it is, seconds on this PC: the progress line's estimate)
PACKAGE_PARTS = (
    ("gif", "Loop GIF", "1080 px, 24 fps, plays forever", 15),
    ("card_en", "A5 card, English", "PDF, 3 mm bleed, 300 dpi, front and back", 8),
    ("card_id", "A5 card, Bahasa Indonesia", "PDF, the same card in Indonesian", 8),
    ("stock", "Stock JPEG", "the dynamic master as an sRGB JPEG for stock sites", 3),
    ("csv", "Stock upload CSVs", "Adobe Stock and Shutterstock sheets", 1),
    ("zip", "Gumroad zip", "the export package in one zip (needs the GIF and cards)", 3),
    ("registry", "Registry + overview", "the registry rows and overview.md", 2),
)
PART_IDS = tuple(p[0] for p in PACKAGE_PARTS)
LOW_PARTS = ("gif", "card_en", "card_id")                      # at LOW (layout tests, in the cache) only these exist
PACKAGE_PRESETS = (
    ("f", "Full package", PART_IDS),
    ("s", "Stock only", ("stock", "csv", "registry")),
    ("p", "PDF cards only", ("card_en", "card_id")),
    ("g", "GIF only", ("gif",)),
    ("z", "Gumroad bundle", ("gif", "card_en", "card_id", "zip", "registry")),
)
FINAL_PARTS = (
    ("dyn", "Master, dynamic pose", "4096 px square, crops to 1:1, 9:16 and 16:9", None),
    ("block", "Master, regular blocky pose", "4096 px square, the card's back", None),
    ("loop", "Loop frames", "the frames of the looped animation (the GIF is built by Package)", None),
)


def codes(rows):
    return [r[1]["code"] for r in rows]


def _label(an):
    return f"{an['code']} {an['common']}"


# ---- package state ----------------------------------------------------------------------------------------------------
def part_outputs(folder, animal, part, low=False):
    import package as PK
    import stock as SK
    code = animal["code"]
    if part == "gif":
        return [PK.export_file(folder, code, "LOOP", low)]
    if part in ("card_en", "card_id"):
        return [PK.export_file(folder, code, "CARD-" + part[-2:].upper(), low)]
    if part == "stock":
        return [SK.stock_file(folder, code)]
    if part == "csv":
        return [os.path.join(VL.PUBLISH, "Stock", f"{code} · {n}.csv") for n in ("Adobe Stock", "Shutterstock")]
    if part == "zip":
        return [SK.zip_file(folder, animal)]
    return []


def package_sources(folder, animal, low=False):
    import package as PK
    code = animal["code"]
    pl = PK.plates(code, low)
    return [PK.export_file(folder, code, "MASTER-DYN", low), PK.export_file(folder, code, "MASTER-BLOCK", low),
            os.path.join(pl, "cut-dyn.png")]


def rendered(folder, animal, low=False):
    import package as PK
    src = package_sources(folder, animal, low)
    return all(os.path.exists(p) for p in src) and os.path.isdir(os.path.join(PK.plates(animal["code"], low), "loop"))


def package_state(folder, animal, parts, low=False):
    """'not rendered' (the masters or loop frames are missing), 'todo' (a chosen output is missing or older than its
    source) or 'done', for the chosen parts of one animal."""
    if not rendered(folder, animal, low):
        return "not rendered"
    parts = [p for p in parts if not low or p in LOW_PARTS]
    src = package_sources(folder, animal, low) + [os.path.join(folder, "animal.json")]
    newest = max(os.path.getmtime(p) for p in src)
    for part in parts:
        outs = part_outputs(folder, animal, part, low)
        if part == "zip":                                     # the zip is only current after the package files in it
            newest_z = max([newest] + [os.path.getmtime(p) for q in ("gif", "card_en", "card_id")
                                       for p in part_outputs(folder, animal, q, low) if os.path.exists(p)])
        else:
            newest_z = newest
        if any(not os.path.exists(p) or os.path.getmtime(p) < newest_z for p in outs):
            return "todo"
    return "todo" if parts == ["registry"] else "done"


def package_seconds(parts):
    t = {p[0]: p[3] for p in PACKAGE_PARTS}
    return sum(t[p] for p in parts)


# ---- the runners ------------------------------------------------------------------------------------------------------
def _fail(skipped, an, e):
    skipped.append(f"{an['code']} ({e})")
    vf.out(f"  ! {an['code']} {an['common']}: {e}")


def _summary(what, done, skipped):
    vf.out(f"{what}: {len(done)} done ({', '.join(done) or '-'})" + (f", {len(skipped)} skipped" if skipped else ""))
    for s in skipped:
        vf.out(f"  skipped {s}")


def build_many(rows, force=False):
    done, skipped = [], []
    for i, (d, an, *_r) in enumerate(rows, 1):
        vf.out(f"[{i}/{len(rows)}] {_label(an)}")
        try:
            if not os.path.exists(os.path.join(d, "blender", "model.py")):
                raise SystemExit("no model.py yet")
            if vf.do_build(d, an, force=force):
                vf.advance(an, "Modelling")
                VL.save(d, an)
                vf.write_overview(d, an)
            done.append(an["code"])
        except SystemExit as e:
            _fail(skipped, an, e)
    _summary("build", done, skipped)
    vf.write_render_readme()
    return done, skipped


def preview_many(rows, force=False, stills=False, rig_force=False, jobs=3):
    """LOW previews of the chosen animals, then (unless `stills`) the rig, the rig check and the GIF loops."""
    done, skipped, plan = [], [], []
    for d, an, *_r in rows:
        if not os.path.exists(os.path.join(d, "blender", "model.py")):
            skipped.append(f"{an['code']} (no model.py)")
            continue
        try:
            ests = vf.todo_of(d, an, "LOW", force)[1]
        except OSError:                                        # not built yet: assume all six compositions
            ests = [ST.PROFILES["LOW"].get("estimate", {}).get(r, 0) for k in ST.KINDS for r in ST.RATIOS]
        plan.append((d, an, ests))
    VL.LIVE.start(sum(sum(e) for _, _, e in plan), sum(len(e) for _, _, e in plan), len(plan))
    try:
        for d, an, ests in plan:
            try:
                VL.LIVE.set_note("building")
                vf.preview(d, an, force=force)
                done.append(an["code"])
            except SystemExit as e:
                VL.LIVE.drop(sum(ests), len(ests))
                _fail(skipped, an, e)
    finally:
        VL.LIVE.stop()
    _summary("previews", done, skipped)
    vf.write_render_readme()
    if not stills and done:
        rig_many([r for r in rows if r[1]["code"] in done], force=rig_force, no_preview=False, jobs=jobs, lineups=False)
    return done, skipped


def rig_many(rows, force=False, no_preview=False, jobs=3, lineups=False):
    from concurrent.futures import ThreadPoolExecutor
    done, skipped = [], []
    todo = [r for r in rows if os.path.exists(os.path.join(r[0], "blender", "model.py"))]
    for d, an, *_r in todo:                                    # stills first, one at a time (cheap when current)
        try:
            vf.do_build(d, an)
        except SystemExit as e:
            _fail(skipped, an, e)

    def one(r):
        d, an = r[0], r[1]
        if any(s.startswith(an["code"]) for s in skipped):
            return
        try:
            vf.do_rig(d, an, force=force, preview=not no_preview)
            done.append(an["code"])
        except SystemExit as e:
            _fail(skipped, an, e)

    with ThreadPoolExecutor(max_workers=max(1, jobs)) as ex:
        list(ex.map(one, todo))
    if lineups:
        vf.out(f"-> {VL.rel(vf.check_lineup(vf.CHECK_LINEUP))}")
        if not no_preview and not skipped:
            vf.out(f"-> {VL.rel(vf.motion_lineup(vf.LINEUP_GIF))}")
    _summary("rig", done, skipped)
    return done, skipped


def final_many(rows, parts=("dyn", "block", "loop"), low=False, force=False):
    """The export renders of the chosen animals (masters and loop frames). Only preview-approved animals, unless `low`."""
    done, skipped, plan = [], [], []
    for d, an, *_r in rows:
        if not low and not (an.get("approvals") or {}).get("preview"):
            skipped.append(f"{an['code']} (no preview approval)")
            continue
        if not os.path.exists(os.path.join(d, "blender", "model.py")):
            skipped.append(f"{an['code']} (no model.py)")
            continue
        plan.append((d, an, [sec for _, sec in vf.final_plan(d, an, low=low, force=force, parts=parts)]))
    VL.LIVE.start(sum(sum(e) for _, _, e in plan), max(1, sum(len(e) for _, _, e in plan)), len(plan))
    try:
        for d, an, ests in plan:
            try:
                for e in vf.final(d, an, force=force, low=low, parts=parts):
                    vf.out("  ERROR", e)
                done.append(an["code"])
            except SystemExit as e:
                VL.LIVE.drop(sum(ests), len(ests))
                _fail(skipped, an, e)
    finally:
        VL.LIVE.stop()
    _summary("renders" + (" (LOW)" if low else ""), done, skipped)
    vf.write_render_readme()
    return done, skipped


def package_one(folder, animal, parts, low=False):
    """The chosen parts for one animal, in a fixed order (the zip after the files in it), ticking the progress line."""
    import package as PK
    import stock as SK
    import registry as RG
    code = animal["code"]
    parts = [p for p in PART_IDS if p in parts and (not low or p in LOW_PARTS)]
    pl = PK.plates(code, low)
    mblock = PK.export_file(folder, code, "MASTER-BLOCK", low)
    cut = os.path.join(pl, "cut-dyn.png")
    for part in parts:
        VL.LIVE.set_note(dict((p[0], p[1]) for p in PACKAGE_PARTS)[part].lower())
        if part == "gif":
            ld = os.path.join(pl, "loop")
            frames = sorted(os.path.join(ld, f) for f in os.listdir(ld) if f.endswith(".png"))
            if not frames:
                raise SystemExit(f"no loop frames in {VL.rel(ld)}")
            PK.loop_gif(frames, PK.export_file(folder, code, "LOOP", low), ST.MOTION["fps"])
        elif part in ("card_en", "card_id"):
            lang = part[-2:]
            PK.card_pdf(animal, folder, lang, cut, mblock, PK.export_file(folder, code, "CARD-" + lang.upper(), low), True)
        elif part in ("stock", "csv", "zip"):
            for line in SK.package(folder, animal, parts=({"stock": ("jpeg",)}.get(part) or (part,))):
                vf.out("    " + line)
        elif part == "registry":
            RG.upsert(folder, animal)
            vf.write_overview(folder, animal)
        VL.LIVE.item_done()
    return parts


def package_many(rows, parts=PART_IDS, low=False, force=False):
    """The offline package, the chosen parts, for the chosen animals. A part that is already current is skipped unless
    `force`; an animal that is not rendered yet is skipped with a note."""
    parts = [p for p in PART_IDS if p in parts and (not low or p in LOW_PARTS)]
    done, skipped, plan = [], [], []
    for d, an, *_r in rows:
        st = package_state(d, an, parts, low)
        if st == "not rendered":
            skipped.append(f"{an['code']} (not rendered yet)")
        elif st == "todo" or force:
            if force:
                todo = parts
            else:                                              # only the parts that are missing or out of date
                todo = [p for p in parts if package_state(d, an, [p], low) == "todo" or p == "registry"]
                if "zip" in parts and "zip" not in todo and any(p in todo for p in ("gif", "card_en", "card_id")):
                    todo.append("zip")
            plan.append((d, an, todo))
        else:
            done.append(an["code"] + " (already current)")
    if plan:
        total_steps = sum(len(t) for _, _, t in plan)
        VL.LIVE.start(sum(package_seconds(t) for _, _, t in plan), total_steps, len(plan), unit="steps")
        try:
            for d, an, todo in plan:
                ests = [dict((p[0], p[3]) for p in PACKAGE_PARTS)[p] for p in todo]
                VL.LIVE.begin_animal(_label(an), ests)
                try:
                    ran = package_one(d, an, todo, low)
                    done.append(an["code"])
                    vf.out(f"  {VL.TICK} {_label(an)}: {', '.join(ran)}")
                except (SystemExit, ValueError, OSError) as e:
                    VL.LIVE.drop(sum(ests), len(ests))
                    _fail(skipped, an, e)
        finally:
            VL.LIVE.stop()
    _summary("package", done, skipped)
    return done, skipped
