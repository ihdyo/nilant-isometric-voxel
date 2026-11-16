"""Voxel Fauna · the command line. Run from the project root:

    python _system/studio/scripts/vf.py <command> [args]

  doctor                      Blender, Python packages, fonts, palette, standards lock
  list                        every animal with its status
  new "<Common name>" ["<Scientific name>"]
                              next YY-SEQ code, folder from 02 Animals/_Template, status Research
  check <code> [--strict]     everything the files can prove: animal.json, sources behind every fact, photo licence and
                              log, palette and background rules, the voxel brief, the voxel model, type fits, exports
  build <code>                model.py -> the editable .blend (+ blender/build.json); only when missing or stale
  preview <code>              LOW: builds if needed, renders all six compositions from the .blend into
                              _system/cache/preview/<code>/ with a contact sheet (Phase 3)
  approve <code> preview|final
                              records the OWNER's approval (only when the owner says so)
  final <code> [--force]      ULTRA from the approved .blend into export/ (Phase 4); resumes, skips finished images
  render-all LOW|ULTRA        every built animal (LOW) or every approved one (ULTRA): what render.bat runs
  info <code> [--profile LOW|ULTRA]
                              re-lays the cards of the three information artworks on their cached plates
  overview <code>             rewrites overview.md from animal.json and the files
  register <code>             adds or updates the animal and its six images in 05 Publish/Voxel Fauna · Registry.xlsx
  stock <code> [--only ILL-1x1,ILL-16x9]
                              stock JPEGs in export/stock/, upload CSVs in 05 Publish/Stock/ (illustrations only by
                              default: the information artworks carry a third-party photo), the Gumroad zip (all six)
  log <code|Image ID> <platform> <action> [--kinds ILL] [--link URL] [--note "..."]
                              records an upload event in the Publish Log (registry sheet + markdown), like Nilant's log
  selftest [--ultra] [--ratios 1x1] [--compare]
                              the engine end to end on a placeholder creature -> _system/cache/selftest/
  verify                      standards lock, the skill's standards table, every animal's check and build
  lock "<what and why>"       re-fingerprint the standards after the owner's OK (logs a DECISIONS row)
  standards [--write]         the standards table (--write puts it into the skill)
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vflib as VL  # noqa: E402

ST = VL.ST
TODAY = datetime.date.today().isoformat()
PHOTO_EXT = (".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff")


def out(*a):
    print(*a, flush=True)


# ---- the selftest creature (placeholder copy at the longest lengths the layouts allow) ------------------------------
SELFTEST = {
    "code": "00-000", "common": "Test Creature", "scientific": "Testus voxelis", "status": "Preview",
    "look": {"palette": {"fur": "orange-400", "belly": "orange-50", "dark": "stone-800"}, "background": "sky-200",
             "accent": None},
    "info": {
        "kicker": "Placeholder · Engine test",
        "conservation": {"status": "Least Concern", "code": "LC", "source": [1]},
        "stats": [{"label": "Length", "value": "00–00 cm", "source": [1]},
                  {"label": "Weight", "value": "0.0–0.0 kg", "source": [1]},
                  {"label": "Lifespan", "value": "0–0 yrs", "source": [1]},
                  {"label": "Top speed", "value": "00 km/h", "source": [1]}],
        "habitat": {"text": ("Placeholder copy at the longest length a habitat line may have, to prove it fits in."),
                    "source": [1]},
        "diet": {"text": "Placeholder copy at the longest length a diet line may have, to prove it fits.",
                 "source": [1]},
        "facts": [{"text": ("Placeholder fun fact at the longest length allowed. It only proves that the card holds "
                            "the type."), "source": [1]}],
        "photo": None,
    },
    "sources": [{"id": 1, "title": "Engine selftest (no real data)", "url": "", "accessed": TODAY}],
}


# ---- checks ---------------------------------------------------------------------------------------------------------
def _text(v):
    return v.get("text", "") if isinstance(v, dict) else (v or "")


def _srcs(v):
    s = v.get("source", []) if isinstance(v, dict) else []
    return s if isinstance(s, list) else [s]


def _photos(folder):
    d = os.path.join(folder, "assets", "photos")
    return sorted(p for p in os.listdir(d) if p.lower().endswith(PHOTO_EXT)) if os.path.isdir(d) else []


def brief_palette(folder):
    """The palette table of docs/voxel-model.md: {key: token}."""
    p = os.path.join(folder, "docs", "voxel-model.md")
    if not os.path.exists(p):
        return None
    pal = {}
    for line in open(p, encoding="utf-8"):
        m = re.match(r"\|\s*`([a-z_]+)`\s*\|\s*`([a-z]+-\d{2,3}|white|black|#[0-9A-Fa-f]{6})`\s*\|", line)
        if m:
            pal[m.group(1)] = m.group(2)
    return pal


def check_animal(folder, animal, strict=False):
    """Returns (errors, warnings). strict = the final gate (photos, docs, sources all required)."""
    E, W = [], []
    real = animal.get("code") != "00-000"
    for k in ("code", "common", "scientific", "status", "look", "info", "sources"):
        if k not in animal:
            E.append(f"animal.json: missing '{k}'")
    if E:
        return E, W
    lim = ST.INFO_LIMITS
    if len(animal["common"]) > lim["common"]:
        E.append(f"common name longer than {lim['common']} characters")
    sci = animal["scientific"].split()
    if len(sci) < 2 or not sci[0][:1].isupper() or not sci[1].islower():
        E.append(f"scientific name '{animal['scientific']}' is not 'Genus species'")
    if animal["status"] not in ST.STATUSES:
        E.append(f"status '{animal['status']}' is not one of {', '.join(ST.STATUSES)}")
    # look
    look = animal["look"]
    pal = look.get("palette") or {}
    for k, t in pal.items():
        if not VL.is_colour(t):
            E.append(f"look.palette.{k}: '{t}' is neither a Tailwind v4 token nor a #RRGGBB hex")
    bg = look.get("background", "")
    if not VL.is_colour(bg):
        E.append(f"look.background '{bg}' is neither a Tailwind v4 token nor a #RRGGBB hex")
    elif pal:
        lo, hi = ST.BACKGROUND_RULE["shades"]
        if bg in VL.PALETTE and not lo <= (VL.shade(bg) or 0) <= hi:
            E.append(f"background {bg}: shade outside the soft range {lo}-{hi}")
        if bg not in VL.PALETTE and VL.VC.oklch(bg)[0] < ST.BACKGROUND_RULE["min_lightness"]:
            E.append(f"background {bg}: OKLCH lightness {VL.VC.oklch(bg)[0]:.2f} is below "
                     f"{ST.BACKGROUND_RULE['min_lightness']} (backgrounds stay soft)")
        main = next(iter(pal.values()))
        if VL.is_colour(main):
            de = VL.delta_e(main, VL.background(look))
            if de < ST.BACKGROUND_RULE["min_delta_e"]:
                E.append(f"background {bg} (rendered {VL.background(look)}) is too close to the main colour {main} "
                         f"(delta E {de:.0f})")
    if real and not ((look.get("size") or {}).get("real_m")):
        has_model = bool(folder) and os.path.exists(os.path.join(folder, "blender", "model.py"))
        (E if has_model else W).append("look.size.real_m is missing (the real longest dimension in metres sets the "
                                       "voxel budget)")
    # no game or brand name in the stock metadata (the look is blocky-mob style, never a named game)
    import stock as SK
    hits = SK.trademark_hits(animal)
    if hits:
        E.append(f"animal.json stock title/keywords name a trademark ({', '.join(hits)}): remove it")
    # the voxel brief agrees with animal.json
    if real:
        bp = brief_palette(folder)
        if bp is None:
            (E if strict else W).append("docs/voxel-model.md is missing (the brief key-prompt.md needs)")
        elif bp != pal:
            E.append(f"docs/voxel-model.md palette {bp} differs from animal.json look.palette {pal}")
    # info and its sources
    info = animal["info"]
    ids = {s.get("id") for s in animal["sources"]}
    for s in animal["sources"]:
        if real and not s.get("url"):
            (E if strict else W).append(f"source {s.get('id')}: no URL")
    facts = info.get("facts", [])
    if len(facts) > lim["facts"]:
        E.append(f"more than {lim['facts']} facts")
    fields = [("kicker", info.get("kicker", ""), lim["kicker"], False),
              ("habitat", info.get("habitat"), lim["habitat"], True), ("diet", info.get("diet"), lim["diet"], True)]
    fields += [(f"facts[{i}]", f, lim["fact"], True) for i, f in enumerate(facts)]
    for name, v, n, needs_src in fields:
        t = _text(v)
        if needs_src and not t:
            (E if strict else W).append(f"info.{name} is empty")
        if len(t) > n:
            E.append(f"info.{name} is {len(t)} characters (limit {n})")
        if needs_src and t:
            s = _srcs(v)
            if not s:
                E.append(f"info.{name} has no source")
            E += [f"info.{name} cites source {i}, which is not in sources" for i in s if i not in ids]
    stats = info.get("stats", [])
    if len(stats) > lim["stats"]:
        E.append(f"more than {lim['stats']} stats")
    for s in stats:
        if not s.get("value"):
            (E if strict else W).append(f"stat '{s.get('label')}' has no value (fill or remove it)")
            continue
        if len(s.get("label", "")) > lim["stat_label"] or len(s.get("value", "")) > lim["stat_value"]:
            E.append(f"stat '{s.get('label')}: {s.get('value')}' is longer than {lim['stat_label']}/{lim['stat_value']}")
        if not _srcs(s):
            E.append(f"stat '{s.get('label')}' has no source")
        E += [f"stat '{s.get('label')}' cites source {i}, which is not in sources" for i in _srcs(s) if i not in ids]
    cons = info.get("conservation") or {}
    if not cons.get("code"):
        (E if strict else W).append("conservation status is empty")
    elif cons["code"] not in ST.INFO_STYLE["status"]:
        E.append(f"conservation code '{cons['code']}' is not an IUCN code ({', '.join(ST.INFO_STYLE['status'])})")
    elif not _srcs(cons):
        E.append("conservation status has no source")
    # model
    model = os.path.join(folder, "blender", "model.py") if folder else None
    if model and os.path.exists(model):
        try:
            g = VL.VX.load_model(model)
            e, notes = g.report(VL.budget(animal)[:2], ST.POSE["max_angle"], ST.POSE["plates"])
            E += [f"model: {x}" for x in e]
            W += [f"model: {x}" for x in notes if "not mirrored" in x]
            miss = [c for c in g.colors() if c not in pal]
            if miss:
                E.append(f"model uses colour keys missing from look.palette: {miss}")
        except Exception as ex:
            E.append(f"model.py: {type(ex).__name__}: {ex}")
    elif real:
        (E if animal["status"] != "Research" else W).append("blender/model.py is missing")
    # documents and photos
    if real:
        doc = os.path.join(folder, "docs", "animal-info.md")
        if not os.path.exists(doc) or "{{" in open(doc, encoding="utf-8").read():
            (E if strict else W).append("docs/animal-info.md is missing or still has template placeholders")
        refs = os.path.join(folder, "docs", "references.md")
        reft = open(refs, encoding="utf-8").read() if os.path.exists(refs) else ""
        photos = _photos(folder)
        if not photos:
            (E if strict else W).append("no reference photographs in assets/photos/")
        for p in photos:
            if p not in reft:
                (E if strict else W).append(f"photo {p} is not logged (author, licence, URL) in docs/references.md")
        ph = info.get("photo") or {}
        if not ph.get("file"):
            (E if strict else W).append("info.photo.file: no photograph chosen for the information artwork")
        elif not os.path.exists(os.path.join(folder, ph["file"])):
            E.append(f"info.photo.file {ph['file']} does not exist")
        elif not any((ph.get("licence") or "").startswith(ok) for ok in ST.INFO_STYLE["photo_licences"]):
            E.append(f"info.photo.licence '{ph.get('licence')}' cannot go on a sold image "
                     f"(allowed: {', '.join(ST.INFO_STYLE['photo_licences'])})")
    # the cards fit every layout
    try:
        import infographic as IG
        from PIL import Image
        tmp = os.path.join(VL.CACHE, "jobs", "measure")
        os.makedirs(tmp, exist_ok=True)
        for r in ST.RATIOS:
            w, h = ST.SIZES[r]
            p = os.path.join(tmp, f"blank-{r}.png")
            if not os.path.exists(p):
                Image.new("RGB", (w // 4, h // 4), "white").save(p)
            rep = IG.compose(p, None, animal, r, measure_only=True, strict=False, folder=folder)
            for e in rep["errors"]:
                (W if ("no photo" in e and not strict) else E).append(f"information {r}: {e}")
    except Exception as ex:
        E.append(f"information artwork: {ex}")
    # exports
    if folder and (strict or animal["status"] in ("Final", "Registered", "Approved")):
        from PIL import Image
        for kind in ST.KINDS:
            for r in ST.RATIOS:
                p = VL.export_path(folder, animal["code"], kind, r)
                if not os.path.exists(p):
                    E.append(f"export missing: {VL.rel(p)}")
                else:
                    with Image.open(p) as im:
                        if im.size != tuple(ST.SIZES[r]):
                            E.append(f"{os.path.basename(p)} is {im.size}, expected {ST.SIZES[r]}")
    return E, W


def cmd_check(a):
    folder = VL.find(a.code)
    E, W = check_animal(folder, VL.load(folder), strict=a.strict)
    for w in W:
        out("  warn ", w)
    for e in E:
        out("  ERROR", e)
    out(f"{a.code}: {len(E)} errors, {len(W)} warnings")
    return 1 if E else 0


# ---- build state ----------------------------------------------------------------------------------------------------
BUILD_FILES = ["_system/studio/blender/vf_standards.py", "_system/studio/blender/vf_voxel.py",
               "_system/studio/blender/vf_scene.py"]


def build_fingerprint():
    return {f: VL.file_hash(os.path.join(VL.ROOT, f)) for f in BUILD_FILES}


def look_hash(animal):
    look = animal["look"]
    s = json.dumps({"palette": look.get("palette"), "background": look.get("background")}, sort_keys=True)
    return hashlib.sha256(s.encode()).hexdigest()[:16]


def model_key(folder, animal):
    return VL.file_hash(os.path.join(folder, "blender", "model.py")) + "/" + look_hash(animal)


def build_state(folder, animal):
    """('missing' | 'stale' | 'current', reasons)."""
    if not os.path.exists(VL.blend_path(folder, animal)):
        return "missing", ["no .blend yet"]
    bj = os.path.join(folder, "blender", "build.json")
    if not os.path.exists(bj):
        return "stale", ["no build.json"]
    b = json.load(open(bj, encoding="utf-8"))
    why = []
    if b.get("model_hash") != VL.file_hash(os.path.join(folder, "blender", "model.py")):
        why.append("model.py changed")
    if b.get("look_hash") != look_hash(animal):
        why.append("palette or background changed")
    if b.get("build_standards") != build_fingerprint():
        why.append("the standards changed")
    return ("stale" if why else "current"), why


def readme_text(animal):
    return (f"{ST.COLLECTION} · {animal['code']} · {animal['common']} ({animal['scientific']})\n\n"
            "Built from blender/model.py by `python _system/studio/scripts/vf.py build <code>` (render.bat option 1).\n"
            "Do not edit this file by hand: change model.py or animal.json and build again.\n\n"
            "Scenes: ILL 1x1, ILL 9x16, ILL 16x9 (illustrations), INF 1x1, INF 9x16, INF 16x9 (plates for the\n"
            "information artworks). They share the collections Animal (one object per part), Stage (the ground) and\n"
            "Lights (key and rim suns). Each scene has its own framed orthographic camera and the ULTRA settings.\n"
            "A plain F12 render here shows the grey shadow-pass ground; the finished images are two passes laid over\n"
            "the exact background colour by vf.py / render.bat (see the skill voxel-animal-production).\n")


def do_build(folder, animal, force=False):
    state, why = build_state(folder, animal)
    if state == "current" and not force:
        return False
    out(f"  build {animal['code']} · {animal['common']}: {', '.join(why)}")
    E, _ = check_animal(folder, animal)
    model_errors = [e for e in E if e.startswith("model") or "palette" in e or "background" in e]
    if model_errors:
        raise SystemExit(f"{animal['code']}: cannot build: " + "; ".join(model_errors))
    res = VL.run_blender(dict(model=os.path.join(folder, "blender", "model.py"), look=animal["look"],
                              budget=list(VL.budget(animal)[:2]),
                              blend=VL.blend_path(folder, animal), readme=readme_text(animal), renders=[]),
                         f"{animal['code']}-build")
    data = dict(code=animal["code"], built=datetime.datetime.now().isoformat(timespec="seconds"),
                blender=res.get("blender"), model_hash=VL.file_hash(os.path.join(folder, "blender", "model.py")),
                look_hash=look_hash(animal), build_standards=build_fingerprint(),
                standards_version=ST.STANDARDS_VERSION, rig=ST.RIG, geometry=ST.GEOMETRY,
                model=res.get("model"), frames=res.get("frames"), renders={})
    old = os.path.join(folder, "blender", "build.json")
    json.dump(data, open(old, "w", encoding="utf-8"), indent=1, default=str)
    write_blender_readme(folder, animal)
    return True


def note_renders(folder, res, profile):
    p = os.path.join(folder, "blender", "build.json")
    b = json.load(open(p, encoding="utf-8"))
    b.setdefault("renders", {})[profile] = {r["scene"]: dict(seconds=r["seconds"], size=r["size"], at=TODAY)
                                           for r in res.get("renders", [])} | b.get("renders", {}).get(profile, {})
    json.dump(b, open(p, "w", encoding="utf-8"), indent=1, default=str)


# ---- rendering ------------------------------------------------------------------------------------------------------
def targets(animal, profile, folder):
    """(scene, output, kind, ratio) for the six compositions at a profile."""
    code = animal["code"]
    if profile == "ULTRA":
        dest = os.path.join(folder, "export")
    else:
        dest = os.path.join(VL.CACHE, "preview", code)
    plates = os.path.join(VL.CACHE, "plates", code, profile)
    t = []
    for kind in ST.KINDS:
        for r in ST.RATIOS:
            final = os.path.join(dest, VL.image_id(code, kind, r) + ".png")
            raw = final if kind == "ILL" else os.path.join(plates, f"INF-{r}.png")
            t.append(dict(scene=f"{kind} {r}", kind=kind, ratio=r, raw=raw, final=final))
    return t, dest, plates


def render_from_blend(folder, animal, profile, force=False):
    """Renders what is missing (or older than the .blend) from the built .blend; composes the information cards."""
    blend = VL.blend_path(folder, animal)
    bt = os.path.getmtime(blend)
    T, dest, plates = targets(animal, profile, folder)
    todo = [t for t in T if force or not os.path.exists(t["raw"]) or os.path.getmtime(t["raw"]) < bt]
    if todo:
        est = sum(ST.PROFILES[profile].get("estimate", {}).get(t["ratio"], 0) for t in todo)
        out(f"  render {animal['code']} · {animal['common']} {profile}: {len(todo)} of 6 compositions"
            + (f", about {est / 60:.0f} min" if est > 60 else ""))
        res = VL.run_blender(dict(open=blend, renders=[dict(scene=t["scene"], profile=profile, out=t["raw"]) for t in todo]),
                             f"{animal['code']}-{profile}")
        note_renders(folder, res, profile)
    from PIL import Image
    import infographic as IG
    for t in T:
        if t["kind"] == "ILL" and t in todo:
            with Image.open(t["raw"]) as im:
                im.convert("RGB").save(t["raw"], optimize=True, dpi=(300, 300))
        if t["kind"] == "INF" and (force or not os.path.exists(t["final"]) or
                                   os.path.getmtime(t["final"]) < os.path.getmtime(t["raw"]) or
                                   os.path.getmtime(t["final"]) < os.path.getmtime(os.path.join(folder, "animal.json"))):
            IG.compose(t["raw"], t["final"], animal, t["ratio"], folder=folder)
    return T, dest


def contact_sheet(paths_by_kind, target, title):
    from PIL import Image, ImageDraw, ImageFont
    cell_h, pad, head = 560, 24, 70
    rows = []
    for kind in ("ILL", "INF"):
        ims = [Image.open(p).convert("RGB") for p in paths_by_kind.get(kind, []) if os.path.exists(p)]
        rows.append([im.resize((round(im.width * cell_h / im.height), cell_h)) for im in ims])
    width = max(sum(i.width for i in r) + pad * (len(r) + 1) for r in rows if r)
    sheet = Image.new("RGB", (width, head + len(rows) * (cell_h + pad) + pad), "white")
    d = ImageDraw.Draw(sheet)
    d.text((pad, 18), title, font=ImageFont.truetype(os.path.join(VL.FONTS, "Poppins-SemiBold.ttf"), 30), fill="black")
    y = head
    for r in rows:
        x = pad
        for im in r:
            sheet.paste(im, (x, y))
            x += im.width + pad
        y += cell_h + pad
    sheet.save(target, optimize=True)
    return target


def advance(animal, status):
    if ST.STATUSES.index(status) > ST.STATUSES.index(animal["status"]):
        animal["status"] = status
        animal.setdefault("history", []).append(f"{TODAY} {status}")


def preview(folder, animal, force=False):
    do_build(folder, animal)
    T, dest = render_from_blend(folder, animal, "LOW", force)
    sheet = contact_sheet({k: [t["final"] for t in T if t["kind"] == k] for k in ST.KINDS},
                          os.path.join(dest, f"{animal['code']} · preview sheet.png"),
                          f"{animal['code']} · {animal['common']} · LOW preview · {TODAY}")
    advance(animal, "Preview")
    VL.save(folder, animal)
    write_overview(folder, animal)
    return sheet


def final(folder, animal, force=False):
    ap = animal.get("approvals") or {}
    if not ap.get("preview"):
        raise SystemExit(f"{animal['code']}: no preview approval yet (owner: vf.py approve {animal['code']} preview)")
    state, why = build_state(folder, animal)
    if state != "current":
        raise SystemExit(f"{animal['code']}: the .blend is {state} ({', '.join(why)}): run a new preview for the owner")
    if ap.get("preview_key") and ap["preview_key"] != model_key(folder, animal):
        raise SystemExit(f"{animal['code']}: the model or look changed after the owner approved the preview: "
                         "preview again and get a new approval")
    E, _ = check_animal(folder, animal)
    E = [e for e in E if not e.startswith("export missing")]
    if E:
        raise SystemExit(f"{animal['code']}: " + "; ".join(E))
    render_from_blend(folder, animal, "ULTRA", force)
    advance(animal, "Final")
    VL.save(folder, animal)
    write_overview(folder, animal)
    E, _ = check_animal(folder, animal, strict=True)
    return E


def cmd_build(a):
    folder = VL.find(a.code)
    animal = VL.load(folder)
    if not do_build(folder, animal, force=a.force):
        out(f"{a.code}: the .blend is current")
    else:
        advance(animal, "Modelling")
        VL.save(folder, animal)
        write_overview(folder, animal)
        out(f"{a.code}: built {VL.rel(VL.blend_path(folder, animal))}")
    return 0


def cmd_preview(a):
    folder = VL.find(a.code)
    animal = VL.load(folder)
    E, W = check_animal(folder, animal)
    for w in W:
        out("  warn ", w)
    if E:
        for e in E:
            out("  ERROR", e)
        return 1
    sheet = preview(folder, animal, force=a.force)
    out(f"-> {VL.rel(sheet)}")
    out(f"Review it with the owner; on their OK: vf.py approve {a.code} preview")
    return 0


def cmd_final(a):
    folder = VL.find(a.code)
    E = final(folder, VL.load(folder), force=a.force)
    for e in E:
        out("  ERROR", e)
    out(f"{a.code}: final {'complete' if not E else 'with problems'} -> {VL.rel(os.path.join(folder, 'export'))}")
    return 1 if E else 0


def cmd_render_all(a):
    done, skipped = [], []
    for d in VL.animal_dirs():
        an = VL.load(d)
        if not os.path.exists(os.path.join(d, "blender", "model.py")):
            continue
        try:
            if a.profile == "LOW":
                preview(d, an, force=a.force)
                done.append(an["code"])
            elif (an.get("approvals") or {}).get("preview"):
                final(d, an, force=a.force)
                done.append(an["code"])
            else:
                skipped.append(f"{an['code']} (no preview approval)")
        except SystemExit as e:
            skipped.append(f"{an['code']} ({e})")
    out(f"render-all {a.profile}: {len(done)} done ({', '.join(done) or '-'})")
    for s in skipped:
        out(f"  skipped {s}")
    write_render_readme()
    return 0


def cmd_approve(a):
    folder = VL.find(a.code)
    animal = VL.load(folder)
    ap = animal.setdefault("approvals", {})
    ap[a.stage] = TODAY
    if a.stage == "preview":
        ap["preview_key"] = model_key(folder, animal)
    advance(animal, "Preview approved" if a.stage == "preview" else "Approved")
    VL.save(folder, animal)
    write_overview(folder, animal)
    out(f"{a.code}: {a.stage} approved {TODAY} (status {animal['status']})")
    return 0


def cmd_info(a):
    folder = VL.find(a.code)
    animal = VL.load(folder)
    import infographic as IG
    T, dest, plates = targets(animal, a.profile, folder)
    for t in T:
        if t["kind"] == "INF":
            rep = IG.compose(t["raw"], t["final"], animal, t["ratio"], folder=folder)
            out(f"  {t['ratio']}: {VL.rel(t['final'])}")
    return 0


# ---- generated pages ------------------------------------------------------------------------------------------------
def write_blender_readme(folder, animal):
    state, why = build_state(folder, animal)
    b = json.load(open(os.path.join(folder, "blender", "build.json"), encoding="utf-8")) \
        if os.path.exists(os.path.join(folder, "blender", "build.json")) else {}
    model = (b.get("model") or {})
    lines = [f"# {animal['code']} · {animal['common']} · Blender", "",
             "> Written by `vf.py build`. The model is code: change `model.py` (or the palette in `animal.json`) and "
             "build again; never edit the .blend by hand.", "",
             "| File | What |", "|---|---|",
             "| `model.py` | the voxel model: `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (source of truth) |",
             f"| `{os.path.basename(VL.blend_path(folder, animal))}` | the editable project, built from `model.py`: "
             "collections Animal / Stage / Lights, six scenes (ILL and INF × 1x1, 9x16, 16x9) with framed orthographic cameras |",
             "| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |", "",
             f"- Build: **{state}**" + (f" ({', '.join(why)})" if why else "") + (f", built {b.get('built')}" if b else ""),
             f"- Model: {'; '.join(model.get('notes', [])) or '-'}",
             f"- Standards {b.get('standards_version', '?')}, rig `{b.get('rig', '?')}`, geometry `{b.get('geometry', '?')}`, "
             f"Blender {b.get('blender', '?')}", ""]
    open(os.path.join(folder, "blender", "README.md"), "w", encoding="utf-8").write("\n".join(lines))


def write_overview(folder, animal):
    code = animal["code"]
    ex = lambda k, r: VL.export_path(folder, code, k, r)  # noqa: E731
    model = os.path.join(folder, "blender", "model.py")
    blend = VL.blend_path(folder, animal)
    nphotos = len(_photos(folder))
    doc = os.path.join(folder, "docs", "animal-info.md")
    doc_ok = os.path.exists(doc) and "{{" not in open(doc, encoding="utf-8").read()
    preview_sheet = os.path.join(VL.CACHE, "preview", code, f"{code} · preview sheet.png")
    ap = animal.get("approvals") or {}
    n_ex = sum(os.path.exists(ex(k, r)) for k in ST.KINDS for r in ST.RATIOS)
    state, why = build_state(folder, animal) if os.path.exists(model) else ("missing", ["no model.py"])
    info = animal.get("info", {})
    look = animal.get("look", {})
    ph = info.get("photo") or {}

    def box(ok):
        return "x" if ok else " "
    lines = [
        f"# {code} · {animal['common']}", "",
        f"*{animal['scientific']}* · {ST.COLLECTION} · status **{animal['status']}**", "",
        "> Written by `python _system/studio/scripts/vf.py overview " + code + "` (also after build, preview, final, "
        "approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.", "",
        "## Progress", "",
        f"- [{box(doc_ok and nphotos > 0)}] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, "
        f"{nphotos} photo(s) in `assets/photos/`",
        f"- [{box(os.path.exists(model) and state == 'current')}] Phase 2 · Modelling: `docs/voxel-model.md`, "
        f"`blender/model.py`, .blend **{state}**" + (f" ({', '.join(why)})" if why and state != "missing" else ""),
        f"- [{box(bool(ap.get('preview')))}] Phase 3 · LOW preview approved by the owner"
        + (f" ({ap['preview']})" if ap.get("preview") else "")
        + (f" · sheet `{VL.rel(preview_sheet)}`" if os.path.exists(preview_sheet) else ""),
        f"- [{box(n_ex == 6)}] Phase 4 · ULTRA exports: {n_ex} of 6",
        f"- [{box(animal['status'] in ('Registered', 'Approved'))}] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`",
        f"- [{box(bool(ap.get('final')))}] Phase 6 · Approved by the owner" + (f" ({ap['final']})" if ap.get("final") else ""), "",
        "## At a glance", "",
        f"- {info.get('kicker', '')}" + (f" · IUCN {info['conservation'].get('status')}" if info.get("conservation") else ""),
    ]
    lines += [f"- {s['label']}: {s['value']}" for s in info.get("stats", []) if s.get("value")]
    for k, label in (("habitat", "Home turf"), ("diet", "On the menu")):
        if _text(info.get(k)):
            lines.append(f"- {label}: {_text(info[k])}")
    for f in info.get("facts", []):
        if _text(f):
            lines.append(f"- Fun fact: {_text(f)}")
    lines += ["", "## Deliverables", "", "| Image ID | Composition | File |", "|---|---|---|"]
    for k, kname in ST.KINDS.items():
        for r in ST.RATIOS:
            p = ex(k, r)
            w, h = ST.SIZES[r]
            lines.append(f"| `{VL.image_id(code, k, r)}` | {kname} {r.replace('x', ':')} ({w}×{h}) | "
                         + (f"`export/{os.path.basename(p)}`" if os.path.exists(p) else "not rendered") + " |")
    lines += ["", "## Look", "",
              f"- Background: `{look.get('background')}`" + (f": {look['why']}" if look.get("why") else ""),
              "- Palette: " + ", ".join(f"{k} `{v}`" for k, v in (look.get("palette") or {}).items()),
              f"- Photo on the information artwork: `{ph.get('file', '-')}` ({ph.get('author', '?')}, {ph.get('licence', '?')})",
              "", "## Files", "", "| Path | What |", "|---|---|",
              "| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |",
              "| `docs/animal-info.md` | the full biological documentation, every statement sourced |",
              "| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |",
              "| `docs/references.md` | every source and every photograph with author and licence |",
              "| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |",
              "| `blender/model.py` | the voxel model (source of truth for the .blend) |",
              f"| `blender/{os.path.basename(blend)}` | the editable Blender project, built from model.py |",
              "| `blender/build.json`, `blender/README.md` | the build stamp and its summary |",
              "| `export/` | the six final images (+ `stock/` JPEGs) |", ""]
    if animal.get("notes"):
        lines += ["## Notes", ""] + [f"- {n}" for n in animal["notes"]] + [""]
    open(os.path.join(folder, "overview.md"), "w", encoding="utf-8").write("\n".join(lines))


def write_render_readme():
    """_system/studio/render/README.md: every animal at a glance (as Nilant's footage library README)."""
    rows = []
    n_final = 0
    for d in VL.animal_dirs():
        an = VL.load(d)
        if not os.path.exists(os.path.join(d, "blender", "model.py")):
            state = "no model"
        else:
            state = build_state(d, an)[0]
        T, _, _ = targets(an, "LOW", d)
        low = sum(os.path.exists(t["final"]) for t in T)
        T, _, _ = targets(an, "ULTRA", d)
        ult = sum(os.path.exists(t["final"]) for t in T)
        n_final += ult == 6
        ap = an.get("approvals") or {}
        rows.append(f"| {an['code']} | {an['common']} | {state} | {low}/6 | {ap.get('preview') or '-'} | {ult}/6 | "
                    f"{ap.get('final') or '-'} |")
    lines = ["# Voxel Fauna · render status", "",
             "> Written by `render.bat` (and `vf.py render-all`). Double-click `render.bat` to build, preview and render.", "",
             f"- {len(rows)} animals · {n_final} with all six finals · checked {datetime.datetime.now():%Y-%m-%d %H:%M}", "",
             "| Code | Animal | .blend | LOW | Preview approved | ULTRA | Final approved |", "|---|---|---|---|---|---|---|"]
    lines += rows
    os.makedirs(os.path.join(VL.STUDIO, "render"), exist_ok=True)
    open(os.path.join(VL.STUDIO, "render", "README.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")


def cmd_overview(a):
    folder = VL.find(a.code)
    write_overview(folder, VL.load(folder))
    out(f"{a.code}: overview.md written")
    return 0


# ---- new, list ------------------------------------------------------------------------------------------------------
def cmd_new(a):
    for d in VL.animal_dirs():
        if VL.load(d).get("common", "").lower() == a.common.lower():
            out(f"{a.common} already exists: {os.path.basename(d)} (one folder per species)")
            return 1
    code = VL.next_code()
    folder = os.path.join(VL.ANIMALS, f"{code} · {a.common}")
    shutil.copytree(VL.TEMPLATE, folder)
    animal = VL.load(folder)
    animal.update(code=code, common=a.common, scientific=a.scientific or "Genus species", status="Research")
    animal["history"] = [f"{TODAY} Research (folder created)"]
    VL.save(folder, animal)
    for rel in ("docs/animal-info.md", "docs/references.md", "docs/voxel-model.md", "blender/model.py"):
        p = os.path.join(folder, rel)
        if os.path.exists(p):
            t = open(p, encoding="utf-8").read().replace("{{CODE}}", code).replace("{{COMMON}}", a.common)
            open(p, "w", encoding="utf-8").write(t.replace("{{SCIENTIFIC}}", a.scientific or "Genus species"))
    write_overview(folder, animal)
    out(f"created 02 Animals/{code} · {a.common} (status Research)")
    return 0


def cmd_list(a):
    for d in VL.animal_dirs():
        an = VL.load(d)
        st = build_state(d, an)[0] if os.path.exists(os.path.join(d, "blender", "model.py")) else "no model"
        out(f"{an['code']}  {an['status']:<17} .blend {st:<8} {an['common']} ({an['scientific']})")
    if not VL.animal_dirs():
        out("no animals yet: vf.py new \"<Common name>\" \"<Scientific name>\"")
    return 0


# ---- registry and stock ---------------------------------------------------------------------------------------------
def cmd_register(a):
    import registry
    folder = VL.find(a.code)
    animal = VL.load(folder)
    E, _ = check_animal(folder, animal, strict=True)
    if E:
        for e in E:
            out("  ERROR", e)
        out("register needs a complete animal (all six exports, docs, photos, sources)")
        return 1
    n = registry.upsert(folder, animal)
    advance(animal, "Registered")
    VL.save(folder, animal)
    write_overview(folder, animal)
    out(f"{a.code}: {n} rows written to {VL.rel(VL.REGISTRY)}")
    return 0


def cmd_stock(a):
    import stock
    folder = VL.find(a.code)
    animal = VL.load(folder)
    only = [s.strip() for s in a.only.split(",")] if a.only else None
    for line in stock.package(folder, animal, only):
        out("  " + line)
    return 0


def cmd_log(a):
    """Record an upload event: one dated row per image in the registry's Publish Log sheet and the markdown log."""
    import registry
    key = a.target
    code = key[3:9] if key.startswith("VF-") else key
    folder = VL.find(code)
    animal = VL.load(folder)
    if key.startswith("VF-"):
        ids = [key]
    else:
        kinds = [k.strip().upper() for k in (a.kinds or "ILL,INF").split(",")]
        ids = [VL.image_id(code, k, r) for k in kinds for r in ST.RATIOS]
    if a.action not in registry.LOG_ACTIONS:
        out(f"action must be one of {', '.join(registry.LOG_ACTIONS)}")
        return 1
    n = registry.log(ids, animal, a.platform, a.action, a.link or "", a.note or "")
    out(f"logged {n} image(s): {a.platform} {a.action} -> {VL.rel(registry.LOG_MD)} and the registry")
    return 0


# ---- selftest -------------------------------------------------------------------------------------------------------
def cmd_selftest(a):
    dest = os.path.join(VL.CACHE, "selftest")
    os.makedirs(dest, exist_ok=True)
    model = os.path.join(VL.BLENDER_DIR, "selftest_model.py")
    if a.compare:
        from PIL import Image, ImageDraw, ImageFont
        cells = []
        for rig in ST.RIGS:
            for geo in ST.GEOMETRIES:
                p = os.path.join(dest, f"cmp-{rig}-{geo}.png")
                out(f"compare: rig {rig}, geometry {geo}")
                VL.run_blender(dict(model=model, look=SELFTEST["look"], rig=rig, geometry=geo, blend=None,
                                    renders=[dict(scene="ILL 1x1", profile="LOW", out=p)]), f"compare-{rig}-{geo}")
                cells.append((rig, geo, p))
        f = ImageFont.truetype(os.path.join(VL.FONTS, "Poppins-SemiBold.ttf"), 34)
        cols = len(ST.GEOMETRIES)
        sheet = Image.new("RGB", (cols * 1024, ((len(cells) + cols - 1) // cols) * 1084), "white")
        d = ImageDraw.Draw(sheet)
        for i, (rig, geo, p) in enumerate(cells):
            x, y = (i % cols) * 1024, (i // cols) * 1084
            sheet.paste(Image.open(p).convert("RGB"), (x, y + 60))
            mark = "  (locked)" if rig == ST.RIG and geo == ST.GEOMETRY else ""
            d.text((x + 20, y + 10), f"rig {rig} · geometry {geo}{mark}", font=f, fill="black")
        sheet.save(os.path.join(dest, "compare-sheet.png"))
        out(f"-> {VL.rel(os.path.join(dest, 'compare-sheet.png'))}")
        return 0
    profile = "ULTRA" if a.ultra else "LOW"
    ratios = tuple(a.ratios.split(",")) if a.ratios else ST.RATIOS
    plates = os.path.join(VL.CACHE, "plates", "selftest", profile)
    renders = []
    for kind in ST.KINDS:
        for r in ratios:
            target = os.path.join(dest, VL.image_id("00-000", kind, r) + ".png") if kind == "ILL" \
                else os.path.join(plates, f"INF-{r}.png")
            renders.append(dict(scene=f"{kind} {r}", profile=profile, out=target))
    out(f"selftest: {profile}, {', '.join(ratios)}")
    res = VL.run_blender(dict(model=model, look=SELFTEST["look"], blend=os.path.join(dest, "selftest.blend"),
                              readme="selftest", renders=renders), f"selftest-{profile}")
    import infographic as IG
    from PIL import Image
    for r in ratios:
        rep = IG.compose(os.path.join(plates, f"INF-{r}.png"), os.path.join(dest, VL.image_id("00-000", "INF", r) + ".png"),
                         SELFTEST, r, strict=False)
        out(f"  cards {r}: " + ("fit" if not rep["errors"] else "; ".join(rep["errors"]))
            + (" (faux italic)" if rep["faux_italic"] else ""))
    for kind in ST.KINDS:
        for r in ratios:
            p = os.path.join(dest, VL.image_id("00-000", kind, r) + ".png")
            with Image.open(p) as im:
                if kind == "ILL":
                    im.convert("RGB").save(p, optimize=True, dpi=(300, 300))
                want = tuple(round(v * ST.PROFILES[profile]["scale"]) for v in ST.SIZES[r])
                corner = im.convert("RGB").getpixel((2, im.height - 3))
                bg = VL.rgb(VL.background(SELFTEST["look"]))
                out(f"  {os.path.basename(p)}: {im.size[0]}x{im.size[1]} {'ok' if im.size == want else 'WRONG SIZE'}, "
                    f"corner {'= background' if corner == bg else str(corner) + ' != ' + str(bg)}")
    sheet = contact_sheet({k: [os.path.join(dest, VL.image_id("00-000", k, r) + ".png") for r in ratios] for k in ST.KINDS},
                          os.path.join(dest, f"selftest sheet · {profile}.png"),
                          f"Selftest · {profile} · rig {ST.RIG} · geometry {ST.GEOMETRY} · {TODAY}")
    out("render times: " + ", ".join(f"{r['scene']} {r['seconds']} s" for r in res["renders"]))
    out(f"done in {res['wall_seconds']} s -> {VL.rel(sheet)}")
    return 0


# ---- standards, verify, lock ----------------------------------------------------------------------------------------
def standards_md():
    U, L = ST.PROFILES["ULTRA"], ST.PROFILES["LOW"]
    rig = ST.RIGS[ST.RIG]
    c = ST.CAMERA
    lines = [
        f"Standards version {ST.STANDARDS_VERSION} · rig `{ST.RIG}` · geometry `{ST.GEOMETRY}` "
        f"(generated from `vf_standards.py` by `vf.py standards --write`; do not edit by hand)", "",
        "| Area | Value |", "|---|---|",
        f"| Voxel | {ST.VOXEL} m; posed longest side {ST.BUDGET[0]}–{ST.BUDGET[1]} voxels: target "
        f"{ST.SIZE_RULE['base']:g} × (real longest dimension in m)^{ST.SIZE_RULE['exponent']} ± "
        f"{ST.SIZE_RULE['tolerance']:.0%}; smallest feature {ST.MIN_FEATURE} voxel |",
        f"| Pose | sections turn at their joints, at most {ST.POSE['max_angle']:g}° on any axis, ears, snout and jaw "
        f"follow their parent; plates (flat surfaces) {'allowed, ' + str(ST.POSE['plate']) + ' voxel thick' if ST.POSE['plates'] else 'switched off for now: whole voxels only'}; "
        f"the face is painted flat; the posed animal is set on z = 0 |",
        (f"| Bevel | {ST.BEVEL['width']} m, {ST.BEVEL['segments']} segments, profile {ST.BEVEL['profile']} (round); "
         f"`{ST.GEOMETRY}` geometry (bevel limit {ST.GEOMETRIES[ST.GEOMETRY]['limit']}, {ST.BEVEL_ANGLE}°) |"
         if ST.GEOMETRIES[ST.GEOMETRY]["bevel"] else
         f"| Geometry | `{ST.GEOMETRY}`: one part's faces merge into flat planes; sharp box edges (no bevel), flat "
         f"shading, flat solid colours; one voxel layer per part, so overlapping sections stack whole (no holes) |"),
        f"| Camera | {c['type']}, azimuth {c['azimuth']}°, elevation {c['elevation']}° (true isometric), "
        f"distance {c['distance']} m, clip {c['clip_start']}–{c['clip_end']} m, no depth of field |",
        f"| Facing | head towards {ST.FACING}, back up, left flank at −Y (head lower right in frame) |",
        f"| Colour | view {ST.COLOR['view']}, look {ST.COLOR['look']}, exposure {ST.COLOR['exposure']} |",
        f"| Key sun | {rig['key']['token']}, {rig['key']['energy']} W/m², rotation {rig['key']['rotation']} + "
        f"{ST.RIG_TURN}° turn, angle {ST.SUN_MIN_ANGLE} rad, shadow {rig['key']['shadow']} |",
        f"| Rim sun | {rig['rim']['token']}, {rig['rim']['energy']:.2f} W/m², rotation {rig['rim']['rotation']} + "
        f"{ST.RIG_TURN}° turn, angle {ST.SUN_MIN_ANGLE} rad, shadow {rig['rim']['shadow']} |",
        f"| Sky fill | {ST.SKY['token']} × {ST.SKY['strength']} |",
        f"| Material | {ST.GEOMETRIES[ST.GEOMETRY]['material']}: "
        + ", ".join(f"{k} {v}" for k, v in ST.MATERIALS[ST.GEOMETRIES[ST.GEOMETRY]['material']].items())
        + " (no texture) |",
        f"| Shadow | composited: strength {ST.SHADOW['strength']}, dead zone {ST.SHADOW['deadzone']}, "
        f"blur {ST.SHADOW['smooth']} of the short side (twice), pass ground grey {ST.SHADOW['ground_grey']} |",
        f"| Background | one colour per animal (Tailwind shade {ST.BACKGROUND_RULE['shades'][0]}–"
        f"{ST.BACKGROUND_RULE['shades'][1]} or hex, OKLCH L ≥ {ST.BACKGROUND_RULE['min_lightness']}), rendered as a "
        f"vivid pastel: OKLCH chroma ≤ {ST.BACKGROUND_RULE['max_chroma']}, lightness "
        f"{ST.BACKGROUND_RULE['lightness'][0]}–{ST.BACKGROUND_RULE['lightness'][1]} (card colours from its family get "
        f"the same chroma factor); ΔE ≥ {ST.BACKGROUND_RULE['min_delta_e']:.0f} from the main colour |",
        f"| Shared render base | {ST.RENDER_BASE['engine']}; " + ", ".join(f"{k} {v}" for k, v in ST.RENDER_BASE['eevee'].items())
        + f"; motion blur {ST.RENDER_BASE['motion_blur']}; bloom {ST.RENDER_BASE['bloom']} |",
        f"| ULTRA | scale {U['scale']}; " + ", ".join(f"{k} {v}" for k, v in U["eevee"].items())
        + f"; shadow pass samples {U['shadow_samples']}; ray tracing resolution 1/{U['rt_resolution']}, denoise {U['rt_denoise']} |",
        f"| LOW | scale {L['scale']}; " + ", ".join(f"{k} {v}" for k, v in L["eevee"].items())
        + f"; shadow pass samples {L['shadow_samples']}; ray tracing resolution 1/{L['rt_resolution']}, denoise {L['rt_denoise']} |",
        "| Sizes (ULTRA) | " + ", ".join(f"{r} {w}×{h}" for r, (w, h) in ST.SIZES.items()) + " |",
        "| Sizes (LOW) | " + ", ".join(f"{r} {round(w * L['scale'])}×{round(h * L['scale'])}" for r, (w, h) in ST.SIZES.items()) + " |",
        "| Framing | " + "; ".join(f"{k} {r}: zone {v['zone']}, fill {v['fill']}" for k in ST.FRAMING for r, v in ST.FRAMING[k].items()) + " |",
        f"| Card system | radius {ST.INFO_STYLE['radius']}u, lip {ST.INFO_STYLE['lip']}u (background + {ST.INFO_STYLE['lip_steps']}), "
        f"padding {ST.INFO_STYLE['pad']}u, white tiles and cards, fun fact on the background family at {ST.INFO_STYLE['fact_shade']}; "
        f"headings {', '.join(ST.INFO_STYLE['headings'].values())} |",
        "| Copy limits | " + ", ".join(f"{k} {v}" for k, v in ST.INFO_LIMITS.items()) + " |",
        f"| Photo licences | {', '.join(ST.INFO_STYLE['photo_licences'])} (credited on the artwork) |",
        f"| Image ID | `{ST.IMAGE_ID}` (e.g. `{VL.image_id('26-001', 'ILL', '1x1')}`) |",
    ]
    return "\n".join(lines)


def cmd_standards(a):
    md = standards_md()
    if a.write:
        t = open(VL.SKILL, encoding="utf-8").read()
        b, e = "<!-- standards:begin -->", "<!-- standards:end -->"
        i, j = t.index(b) + len(b), t.index(e)
        open(VL.SKILL, "w", encoding="utf-8").write(t[:i] + "\n" + md + "\n" + t[j:])
        out(f"standards table written into {VL.rel(VL.SKILL)}")
    else:
        out(md)
    return 0


def cmd_verify(a):
    fails, notes = [], []
    if not os.path.exists(VL.LOCK):
        fails.append("no standards lock yet (vf.py lock \"...\" after the owner's OK)")
    else:
        lock = json.load(open(VL.LOCK, encoding="utf-8"))
        for f, h in VL.fingerprint().items():
            if lock["files"].get(f) != h:
                fails.append(f"{f} changed since the lock of {lock['locked']} ({lock['reason'][:80]})")
    if standards_md() not in open(VL.SKILL, encoding="utf-8").read():
        fails.append("the skill's standards table is out of date (vf.py standards --write)")
    n = 0
    for d in VL.animal_dirs():
        an = VL.load(d)
        n += 1
        E, _ = check_animal(d, an, strict=an["status"] in ("Final", "Registered", "Approved"))
        fails += [f"{an['code']}: {e}" for e in E]
        if os.path.exists(os.path.join(d, "blender", "model.py")):
            state, why = build_state(d, an)
            if state != "current":
                (fails if an["status"] in ("Final", "Registered", "Approved") else notes).append(
                    f"{an['code']}: .blend {state} ({', '.join(why)})")
    for f in fails:
        out("  FAIL", f)
    for f in notes:
        out("  note", f)
    out(f"verify: {len(fails)} problems ({n} animals checked)")
    return 1 if fails else 0


def cmd_lock(a):
    data = dict(version=ST.STANDARDS_VERSION, locked=TODAY, reason=a.reason, rig=ST.RIG, geometry=ST.GEOMETRY,
                files=VL.fingerprint())
    json.dump(data, open(VL.LOCK, "w", encoding="utf-8"), indent=1)
    p = os.path.join(VL.LOG, "DECISIONS.md")
    with open(p, "a", encoding="utf-8") as f:
        f.write(f"| {TODAY} | Standards locked (v{ST.STANDARDS_VERSION}, rig {ST.RIG}, geometry {ST.GEOMETRY}) | "
                f"{a.reason} | `vf.py lock` |\n")
    out(f"locked: {VL.rel(VL.LOCK)}; logged in {VL.rel(p)}")
    return 0


def cmd_doctor(a):
    ok = True
    try:
        out("Blender:", VL.blender_exe())
    except SystemExit as e:
        out("Blender: MISSING", e)
        ok = False
    for mod in ("PIL", "openpyxl"):
        try:
            __import__(mod)
            out(f"python {mod}: ok")
        except ImportError:
            out(f"python {mod}: MISSING (pip install {'pillow' if mod == 'PIL' else mod})")
            ok = False
    for role in ("display", "heading", "body", "value", "label", "fact"):
        p = os.path.join(VL.FONTS, ST.TYPE[role])
        out(f"font {role}: {'ok' if os.path.exists(p) else 'MISSING ' + p}")
        ok &= os.path.exists(p)
    import infographic as IG
    out("font italic:", "Poppins italic found" if not IG.faux_italic()
        else "not installed: scientific names use a sheared Poppins Medium (see 03 Design/Fonts/README.md)")
    out("palette:", len(VL.PALETTE), "tokens")
    out("standards lock:", "present" if os.path.exists(VL.LOCK) else "missing")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("doctor")
    sub.add_parser("list")
    p = sub.add_parser("new")
    p.add_argument("common")
    p.add_argument("scientific", nargs="?")
    p = sub.add_parser("check")
    p.add_argument("code")
    p.add_argument("--strict", action="store_true")
    for name in ("build", "preview", "final"):
        p = sub.add_parser(name)
        p.add_argument("code")
        p.add_argument("--force", action="store_true")
    for name in ("overview", "register"):
        sub.add_parser(name).add_argument("code")
    p = sub.add_parser("render-all")
    p.add_argument("profile", choices=("LOW", "ULTRA"))
    p.add_argument("--force", action="store_true")
    p = sub.add_parser("approve")
    p.add_argument("code")
    p.add_argument("stage", choices=("preview", "final"))
    p = sub.add_parser("info")
    p.add_argument("code")
    p.add_argument("--profile", default="ULTRA", choices=("LOW", "ULTRA"))
    p = sub.add_parser("stock")
    p.add_argument("code")
    p.add_argument("--only")
    p = sub.add_parser("log")
    p.add_argument("target", help="an animal code (all its images) or one Image ID")
    p.add_argument("platform", help="Adobe Stock, Shutterstock, Gumroad, Freepik, ...")
    p.add_argument("action", help="Submitted, Accepted, Rejected, Live, Removed, Updated")
    p.add_argument("--kinds", help="ILL, INF or ILL,INF (with an animal code)")
    p.add_argument("--link")
    p.add_argument("--note")
    p = sub.add_parser("selftest")
    p.add_argument("--ultra", action="store_true")
    p.add_argument("--compare", action="store_true")
    p.add_argument("--ratios")
    sub.add_parser("verify")
    p = sub.add_parser("lock")
    p.add_argument("reason")
    p = sub.add_parser("standards")
    p.add_argument("--write", action="store_true")
    a = ap.parse_args()
    return globals()["cmd_" + a.cmd.replace("-", "_")](a)


if __name__ == "__main__":
    sys.exit(main())
