"""Voxel Fauna · the command line. Run from the project root:

    python _system/studio/scripts/vf.py <command> [args]

  doctor                      Blender, Python packages, fonts, palette, standards lock
  list                        every animal with its status
  new "<Common name>" ["<Scientific name>"]
                              next YY-SEQ code, folder from 02 Animals/_Template, status Research
  check <code> [--strict]     everything the files can prove: animal.json, sources behind every fact, photo licence and
                              log, palette and background rules, the voxel brief, the voxel model, type fits, exports
  build <code>                model.py -> the editable .blend (+ blender/build.json); only when missing or stale
  preview <code> [--stills]   LOW: builds if needed, renders all six compositions from the .blend into
                              _system/cache/preview/<code>/ with a contact sheet, then rigs, checks and animates the
                              animal (vf.py rig); --stills for the six stills only while iterating (Phase 3)
  approve <code> preview|final
                              records the OWNER's approval (only when the owner says so)
  final <code> [--force]      ULTRA from the approved .blend into export/ (Phase 4); resumes, skips finished images
  render-all LOW|ULTRA [--stills]
                              every built animal (LOW, then every rig and loop) or every approved one (ULTRA): what
                              render.bat runs
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
  rig <code> [--force] [--no-preview]
                              the still .blend -> "<code> · <Name> · Rig.blend" (armature from the joints, one action
                              per motion.actions) + "· Rig.glb", and GIF loops in _system/cache/preview/<code>/anim/
                              (the motion APPROVED by the owner 2026-11-17, vf_rig.py in the standards lock)
  rig-all [--force] [--no-preview] [--jobs 3]
                              every animal, then the rig-check sheet and the motion lineup GIF in 02 Animals/
  rig-check [<code>]          the rig check again on built rigs: every vertex fully weighted to one bone, each bone
                              bent in turn moves its section and everything below it and nothing else; T-pose and
                              bent renders, sections coloured by bone, bones on top -> anim/VF-<code>-RIG-check.png
  verify                      standards lock, the skill's standards table, every animal's check and build
  lock "<what and why>"       re-fingerprint the standards after the owner's OK (logs a DECISIONS row)
  standards [--write]         the standards table (--write puts it into the skill)
"""
import argparse
import datetime
import hashlib
import json
import math
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
    # motion (the animation rig): every animal with a model is rigged and animated (owner, 2026-11-17: "for future
    # generation of animals, ensure it have everything until it rigged and animated"), so the plan and the actions
    # are required once model.py exists; a known plan and actions from the library
    mo = animal.get("motion")
    if folder and os.path.exists(os.path.join(folder, "blender", "model.py")) and \
            not ((mo or {}).get("plan") and (mo or {}).get("actions")):
        E.append("motion: choose motion.plan (walker, sitter, bird, swimmer, sprawler, hopper) and motion.actions "
                 "(pose, idle, the gait, the species specials) in animal.json")
    if mo is not None:
        import vf_rig as VR
        if mo.get("plan") and mo["plan"] not in VR.PLANS:
            E.append(f"motion.plan '{mo['plan']}' is not one of {', '.join(VR.PLANS)}")
        bad = [x for x in (mo.get("actions") or []) + list(mo.get("frames") or {}) + list(mo.get("base") or {})
               if x not in VR.ACTIONS]
        if bad:
            E.append(f"motion: unknown actions {bad} (library: {', '.join(VR.ACTIONS)})")
    # the Indonesian card copy (owner, 2026-11-17: "provide the english and bahasa indonesia for animal info"): needed
    # for the ID card once the owner approved the preview
    if (animal.get("approvals") or {}).get("preview"):
        tid = ((animal.get("i18n") or {}).get("id")) or {}
        miss = [k for k in ("common", "kicker", "stats", "habitat", "diet", "facts") if not tid.get(k)]
        if miss:
            E.append(f"i18n.id: missing {', '.join(miss)} (the Indonesian card copy, the same facts as info)")
        elif len(tid["stats"]) != len(info.get("stats", [])) or len(tid["facts"]) != len(info.get("facts", [])):
            E.append("i18n.id: stats and facts must match info one for one")
    # the export package (PROPOSED 2026-11-17): the two masters once Final; everything once Registered or Approved
    if folder and (strict or animal["status"] in ("Final", "Registered", "Approved")):
        from PIL import Image
        import package as PK
        full = animal["status"] in ("Registered", "Approved")
        for suffix, ext, _ in PK.EXPORT["items"]:
            if not (full or suffix.startswith("MASTER")):
                continue
            p = PK.export_file(folder, animal["code"], suffix)
            if not os.path.exists(p):
                E.append(f"export missing: {VL.rel(p)}")
            elif suffix.startswith("MASTER"):
                with Image.open(p) as im:
                    if im.size != (PK.EXPORT["master"],) * 2:
                        E.append(f"{os.path.basename(p)} is {im.size}, expected {PK.EXPORT['master']} square")
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


def final(folder, animal, force=False, low=False):
    """The ULTRA renders of the export package (PROPOSED 2026-11-17, blender/vf_export.py): the two masters (dynamic
    and regular blocky, 4096 square, the animal in the centre safe square) into export/, their cut-outs and the frames
    of the looped animation into the cache. Rendering only: scripts/package.py builds the rest offline (package.bat).
    Renders what is missing or older than the rig; low=True renders the same set at LOW into the cache (layouts)."""
    import package as PK
    code = animal["code"]
    ap = animal.get("approvals") or {}
    if not low:
        if not ap.get("preview"):
            raise SystemExit(f"{code}: no preview approval yet (owner: vf.py approve {code} preview)")
        if ap.get("preview_key") and ap["preview_key"] != model_key(folder, animal):
            raise SystemExit(f"{code}: the model or look changed after the owner approved the preview: "
                             "preview again and get a new approval")
    E, _ = check_animal(folder, animal)
    E = [e for e in E if not e.startswith("export missing")]
    if E:
        raise SystemExit(f"{code}: " + "; ".join(E))
    do_build(folder, animal)
    if rig_state(folder, animal)[0] != "current":
        do_rig(folder, animal, preview=False)
    rig_blend = rig_paths(folder, animal)[0]
    rt = os.path.getmtime(rig_blend)
    pl = PK.plates(code, low)
    masters = {w: PK.export_file(folder, code, f"MASTER-{w.upper()}", low) for w in ("dyn", "block")}
    cutouts = {w: os.path.join(pl, f"cut-{w}.png") for w in masters}
    todo = {w: p for w, p in masters.items()
            if force or not os.path.exists(p) or not os.path.exists(cutouts[w]) or os.path.getmtime(p) < rt}
    r = json.load(open(os.path.join(folder, "blender", "rig.json"), encoding="utf-8"))
    action = signature(animal, list(r.get("actions", {})))
    n = int((r.get("actions") or {}).get(action) or 0)
    ld = os.path.join(pl, "loop")
    frames = sorted(f for f in os.listdir(ld) if f.endswith(".png")) if os.path.isdir(ld) else []
    loop_ok = (not force and len(frames) == n and
               min(os.path.getmtime(os.path.join(ld, f)) for f in frames) >= rt)
    stamp = os.path.join(pl, "export.json")
    if loop_ok and os.path.exists(stamp) and json.load(open(stamp, encoding="utf-8")).get("action") != action:
        loop_ok = False
    if todo or not loop_ok:
        prof = "LOW" if low else "ULTRA"
        out(f"  render {code} · {animal['common']} {prof}: "
            + ", ".join([f"master {w}" for w in todo] + ([f"loop ({action}, {n} frames)"] if not loop_ok else [])))
        job = dict(open=rig_blend, profile=prof, masters=todo, cutouts=cutouts)
        if not loop_ok:
            job["loop"] = dict(action=action, dir=ld, profile="LOOP_LOW" if low else "LOOP")
        res = VL.run_blender(job, f"{code}-export-{prof}", script="vf_export.py")
        os.makedirs(pl, exist_ok=True)
        json.dump(dict(code=code, profile=prof, action=action, rendered=datetime.datetime.now().isoformat(
            timespec="seconds"), masters=res.get("masters"), loop=dict((res.get("loop") or {}), frames=n)),
            open(stamp, "w", encoding="utf-8"), indent=1, default=str)
    if not low:
        advance(animal, "Final")
        VL.save(folder, animal)
        write_overview(folder, animal)
        E, _ = check_animal(folder, animal, strict=True)
        return E
    return []


def package_one(folder, animal, low=False):
    """The offline half of the export (scripts/package.py): stock crop, loop GIF, the English and Indonesian cards."""
    import package as PK
    res = PK.package(folder, animal, low=low)
    out(f"  package {animal['code']} · {animal['common']}{' (LOW)' if low else ''}: "
        + ", ".join(VL.rel(p) for p in [res["stock"], res["loop"]] + [c["pdf"] for c in res["cards"].values()]))
    return res


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
    if not getattr(a, "stills", False):              # every animal goes all the way: rigged, checked and animated
        do_rig(folder, animal)
        r = json.load(open(os.path.join(folder, "blender", "rig.json"), encoding="utf-8"))
        out(f"-> rig: {VL.rel(rig_paths(folder, animal)[0])} ({r.get('bones')} bones, rig check "
            f"{'PASS' if (r.get('check') or {}).get('ok') else 'FAIL'}), loops in {VL.rel(anim_dir(a.code))}")
    out(f"Review it with the owner; on their OK: vf.py approve {a.code} preview")
    return 0


def cmd_final(a):
    folder = VL.find(a.code)
    low = getattr(a, "low", False)
    E = final(folder, VL.load(folder), force=a.force, low=low)
    for e in E:
        out("  ERROR", e)
    dest = os.path.join(VL.CACHE, "export-low", a.code) if low else os.path.join(folder, "export")
    out(f"{a.code}: renders {'complete' if not E else 'with problems'} -> {VL.rel(dest)}; "
        f"then vf.py package {a.code}{' --low' if low else ''} (or package.bat)")
    return 1 if E else 0


def cmd_package(a):
    folder = VL.find(a.code)
    an = VL.load(folder)
    package_one(folder, an, low=a.low)
    if not a.low:                              # the stock JPEG and CSVs, the Gumroad zip, the registry rows
        import stock as SK
        import registry as RG
        for line in SK.package(folder, an):
            out("    " + line)
        RG.upsert(folder, an)
        write_overview(folder, an)
    return 0


def cmd_package_all(a):
    """Every animal with its renders: package it, then the stock files and the registry rows (package.bat)."""
    import package as PK
    done, skipped = [], []
    for d in VL.animal_dirs():
        an = VL.load(d)
        if not os.path.exists(PK.export_file(d, an["code"], "MASTER-DYN", a.low)):
            skipped.append(f"{an['code']} (not rendered yet)")
            continue
        try:
            package_one(d, an, low=a.low)
            if not a.low:                      # the stock JPEG and CSVs, the Gumroad zip, the registry rows
                import stock as SK
                import registry as RG
                for line in SK.package(d, an):
                    out("    " + line)
                RG.upsert(d, an)
                write_overview(d, an)
            done.append(an["code"])
        except (SystemExit, ValueError) as e:
            skipped.append(f"{an['code']} ({e})")
    out(f"package-all: {len(done)} packaged ({', '.join(done) or '-'})")
    for s in skipped:
        out(f"  skipped {s}")
    return 1 if any("not rendered" not in s for s in skipped) else 0


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
    if a.profile == "LOW" and not getattr(a, "stills", False):     # previews include the rig and the loops
        return cmd_rig_all(type("A", (), dict(force=False, no_preview=False, jobs=getattr(a, "jobs", 3)))())
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


# ---- rig and motion -------------------------------------------------------------------------------------------------
# APPROVED by the owner 2026-11-17. blender/vf_rig.py turns the built still .blend into a rigged copy with looping
# actions and a .glb; the stills and their .blend are untouched. vf_rig.py is in the standards lock and its numbers
# are vf_standards.MOTION.
RIG_ENGINE = "_system/studio/blender/vf_rig.py"


def rig_paths(folder, animal):
    base = os.path.splitext(VL.blend_path(folder, animal))[0]
    return base + " · Rig.blend", base + " · Rig.glb"


def motion_hash(animal):
    return hashlib.sha256(json.dumps(animal.get("motion") or {}, sort_keys=True).encode()).hexdigest()[:16]


def rig_state(folder, animal):
    """('missing' | 'stale' | 'current', reasons)."""
    blend, glb = rig_paths(folder, animal)
    rj = os.path.join(folder, "blender", "rig.json")
    if not os.path.exists(blend) or not os.path.exists(rj):
        return "missing", ["no rig yet"]
    r = json.load(open(rj, encoding="utf-8"))
    why = []
    if build_state(folder, animal)[0] != "current":
        why.append("the still .blend is not current")
    elif r.get("still_built") != json.load(open(os.path.join(folder, "blender", "build.json"),
                                                encoding="utf-8")).get("built"):
        why.append("the still .blend was rebuilt")
    if r.get("motion_hash") != motion_hash(animal):
        why.append("motion changed")
    if r.get("rig_engine") != VL.file_hash(os.path.join(VL.ROOT, RIG_ENGINE)):
        why.append("vf_rig.py changed")
    if not os.path.exists(glb):
        why.append("no .glb")
    return ("stale" if why else "current"), why


def anim_dir(code):
    return os.path.join(VL.CACHE, "preview", code, "anim")


def gif_path(code, action):
    return os.path.join(anim_dir(code), f"VF-{code}-ANIM-{action}.gif")


def write_gif(frames, target, fps):
    from PIL import Image
    ims = [Image.open(p).convert("RGB").quantize(colors=255, method=Image.Quantize.MEDIANCUT,
                                                 dither=Image.Dither.NONE) for p in frames]
    os.makedirs(os.path.dirname(target), exist_ok=True)
    ims[0].save(target, save_all=True, append_images=ims[1:], duration=round(1000 / fps), loop=0, disposal=1)
    return target


def rig_readme(animal):
    return (f"{ST.COLLECTION} · {animal['code']} · {animal['common']} ({animal['scientific']}) · rig\n\n"
            "Built by `python _system/studio/scripts/vf.py rig <code>` from the still .blend beside it (never edit by\n"
            "hand: change model.py or animal.json -> motion and rig again). The motion is approved (owner, 2026-11-17).\n\n"
            "Armature 'VF · armature': root (on the ground, carries grounding and hops) -> body -> one bone per jointed\n"
            "section on its hinge, parented like the joints in model.py. Mesh 'VF · animal': every section, each\n"
            "vertex weighted 1.0 to its bone (vertex groups), Armature modifier. Rest pose = the model as drawn\n"
            "(T-pose); the action 'pose' is the approved still.\n"
            "Actions (24 fps, looping): see the armature's custom property vf_actions. Pick one in the Action\n"
            "editor and play; the scene 'ANIM 1x1' is framed on everything every action does.\n")


def do_rig(folder, animal, force=False, preview=True):
    """Still .blend (if stale) -> rig .blend + .glb -> GIF loops of every action. Returns {action: gif} or None."""
    code = animal["code"]
    do_build(folder, animal)
    state, why = rig_state(folder, animal)
    rj = os.path.join(folder, "blender", "rig.json")
    have = json.load(open(rj, encoding="utf-8")).get("actions", {}) if os.path.exists(rj) else {}
    gifs_ok = bool(have) and all(os.path.exists(gif_path(code, n)) for n in have if n != "pose")
    if state == "current" and not force and (gifs_ok or not preview):
        out(f"  rig {code} · {animal['common']}: current")
        return None
    out(f"  rig {code} · {animal['common']}: {', '.join(why) if state != 'current' else 'previews'}")
    blend, glb = rig_paths(folder, animal)
    job = dict(open=VL.blend_path(folder, animal), model=os.path.join(folder, "blender", "model.py"),
               motion=animal.get("motion") or {}, readme=rig_readme(animal), blend=blend, glb=glb,
               check=dict(dir=check_dir(code)))
    if preview:
        job["preview"] = dict(dir=os.path.join(anim_dir(code), "frames"), step=2)
    res = VL.run_blender(job, f"{code}-rig", script="vf_rig.py")
    chk = res.get("check") or {}
    sheet = check_sheet(animal, chk)
    out(f"  rig check {code}: {'PASS' if chk.get('ok') else 'FAIL'} -> {VL.rel(sheet)}")
    b = json.load(open(os.path.join(folder, "blender", "build.json"), encoding="utf-8"))
    rig = res.get("rig") or {}
    data = dict(code=code, rigged=datetime.datetime.now().isoformat(timespec="seconds"), blender=res.get("blender"),
                still_built=b.get("built"), motion_hash=motion_hash(animal),
                rig_engine=VL.file_hash(os.path.join(VL.ROOT, RIG_ENGINE)), plan=rig.get("plan"),
                bones=rig.get("bones"), fps=res.get("fps"),
                actions={n: v.get("frames") for n, v in (rig.get("actions") or {}).items()},
                blend=os.path.basename(blend), glb=os.path.basename(glb), frame=res.get("frame"),
                vertices=rig.get("vertices"), groups=rig.get("groups"),
                check=dict(ok=chk.get("ok"), weights_ok=chk.get("weights_ok"), missing=chk.get("missing"),
                           failing=[r["bone"] for r in chk.get("rows", []) if not r.get("ok")]),
                status="APPROVED motion (owner, 2026-11-17); vf_rig.py and vf_standards.MOTION are locked")
    json.dump(data, open(rj, "w", encoding="utf-8"), indent=1, default=str)
    gifs = {}
    step = res.get("step") or 2
    for name, frames in (res.get("renders") or {}).items():
        gifs[name] = write_gif(frames, gif_path(code, name), (res.get("fps") or 24) / step)
    write_blender_readme(folder, animal)
    return gifs


def signature(animal, actions):
    """The action that shows an animal best in a lineup: motion.signature, else the first after pose and idle."""
    m = animal.get("motion") or {}
    if m.get("signature") in actions:
        return m["signature"]
    rest = [a for a in actions if a not in ("pose", "idle")]
    return rest[0] if rest else "idle"


def motion_lineup(target, cell=216, cols=5):
    """Every rigged animal's signature loop in one GIF grid (each cell loops on its own length)."""
    from PIL import Image, ImageDraw, ImageFont
    cells = []
    for d in VL.animal_dirs():
        an = VL.load(d)
        rj = os.path.join(d, "blender", "rig.json")
        if not os.path.exists(rj):
            continue
        acts = list(json.load(open(rj, encoding="utf-8")).get("actions", {}))
        act = signature(an, acts)
        fd = os.path.join(anim_dir(an["code"]), "frames", act)
        fs = sorted(os.path.join(fd, f) for f in os.listdir(fd) if f.endswith(".png")) if os.path.isdir(fd) else []
        if fs:
            cells.append((f"{an['code']} · {an['common']} · {act}", fs))
    if not cells:
        raise SystemExit("no rigged animal with previews yet (vf.py rig-all)")
    n = 1
    for _, fs in cells:
        n = n * len(fs) // math.gcd(n, len(fs))
    n = min(n, 96)
    head = 30
    rows = (len(cells) + cols - 1) // cols
    font = ImageFont.truetype(os.path.join(VL.FONTS, "Poppins-SemiBold.ttf"), 14)
    cache = {}

    def tile(p):
        if p not in cache:
            im = Image.open(p).convert("RGB")
            m = round(im.width * 0.06)
            cache[p] = im.crop((m, m, im.width - m, im.height - m)).resize((cell, cell), Image.LANCZOS)
        return cache[p]

    frames = []
    for i in range(n):
        sheet = Image.new("RGB", (cols * cell, rows * (cell + head)), "white")
        dr = ImageDraw.Draw(sheet)
        for k, (label, fs) in enumerate(cells):
            x, y = (k % cols) * cell, (k // cols) * (cell + head)
            dr.text((x + 8, y + 7), label, font=font, fill="black")
            sheet.paste(tile(fs[i % len(fs)]), (x, y + head))
        frames.append(sheet.quantize(colors=255, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE))
    frames[0].save(target, save_all=True, append_images=frames[1:], duration=round(1000 / 12), loop=0, disposal=1)
    return target


LINEUP_GIF = os.path.join(VL.ANIMALS, "Voxel Fauna · Twenty-five examples · motion (LOW preview).gif")
CHECK_LINEUP = os.path.join(VL.ANIMALS, "Voxel Fauna · Twenty-five examples · rig check (T-pose).jpg")


def check_dir(code):
    return os.path.join(anim_dir(code), "check")


def check_sheet_path(code):
    return os.path.join(anim_dir(code), f"VF-{code}-RIG-check.png")


def _check_tile(d, state):
    """The section pass (coloured by bone) with the bone pass laid over it at 80 %."""
    from PIL import Image
    a = Image.open(os.path.join(d, f"{state}-animal.png")).convert("RGBA")
    b = Image.open(os.path.join(d, f"{state}-bones.png")).convert("RGBA")
    bg = Image.new("RGBA", a.size, (255, 255, 255, 255))
    bg.alpha_composite(a)
    b.putalpha(b.getchannel("A").point(lambda v: int(v * 0.92)))
    bg.alpha_composite(b)
    return bg.convert("RGB")


def check_sheet(animal, chk):
    """One animal's rig check: the T-pose (rest) and every bone bent, side by side, and the bone legend."""
    from PIL import Image, ImageDraw, ImageFont
    code = animal["code"]
    d = check_dir(code)
    rest, bent = _check_tile(d, "rest"), _check_tile(d, "bent")
    w, h = rest.size
    rows = chk.get("rows", [])
    fb = ImageFont.truetype(os.path.join(VL.FONTS, "Poppins-SemiBold.ttf"), 26)
    f = ImageFont.truetype(os.path.join(VL.FONTS, "Poppins-Medium.ttf"), 19)
    head, leg_w, line = 96, 470, 30
    H = max(h, 70 + line * (len(rows) + 2)) + head
    sheet = Image.new("RGB", (2 * w + leg_w, H), "white")
    dr = ImageDraw.Draw(sheet)
    verdict = "PASS" if chk.get("ok") else "FAIL"
    dr.text((24, 16), f"{code} · {animal['common']} · rig check: {verdict}", font=fb,
            fill=(21, 128, 61) if chk.get("ok") else (185, 28, 28))
    dr.text((24, 54), "left: rest pose (T-pose), each section coloured by its bone, bones drawn on top · right: every "
            "bone bent ±24° at once", font=f, fill=(71, 85, 105))
    sheet.paste(rest, (0, head))
    sheet.paste(bent, (w, head))
    x0, y = 2 * w + 10, head + 10
    dr.text((x0, y), "bone (parent) · vertices · bend test", font=f, fill=(71, 85, 105))
    y += line + 6
    for r in rows:
        c = chk.get("colours", {}).get(r["bone"])
        if c:
            dr.rectangle((x0, y + 5, x0 + 20, y + 25), fill=c, outline="black")
        mark = "ok" if r.get("ok") else "FAIL"
        dr.text((x0 + 30, y), f"{r['bone']} ({r.get('parent') or '-'}) · {r.get('verts', 0)} · {mark}", font=f,
                fill="black" if r.get("ok") else (185, 28, 28))
        y += line
    if not chk.get("weights_ok", True):
        dr.text((x0, y + 10), "vertices without exactly one full weight", font=f, fill=(185, 28, 28))
    target = check_sheet_path(code)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    sheet.save(target)
    return target


def check_lineup(target, cell=360, cols=5):
    """Every rigged animal's T-pose with its bones, PASS or FAIL, in one sheet."""
    from PIL import Image, ImageDraw, ImageFont
    cells = []
    for d in VL.animal_dirs():
        an = VL.load(d)
        rj = os.path.join(d, "blender", "rig.json")
        cd = check_dir(an["code"])
        if os.path.exists(rj) and os.path.exists(os.path.join(cd, "rest-animal.png")):
            r = json.load(open(rj, encoding="utf-8"))
            cells.append((an, (r.get("check") or {}), r.get("bones"), _check_tile(cd, "rest")))
    if not cells:
        raise SystemExit("no rig checks yet (vf.py rig-all)")
    head = 34
    rows = (len(cells) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cell, rows * (cell + head)), "white")
    dr = ImageDraw.Draw(sheet)
    f = ImageFont.truetype(os.path.join(VL.FONTS, "Poppins-SemiBold.ttf"), 16)
    for k, (an, chk, nb, im) in enumerate(cells):
        x, y = (k % cols) * cell, (k // cols) * (cell + head)
        ok = chk.get("ok")
        dr.text((x + 8, y + 8), f"{an['code']} · {an['common']} · {nb} bones · {'PASS' if ok else 'FAIL'}", font=f,
                fill=(21, 128, 61) if ok else (185, 28, 28))
        m = round(im.width * 0.08)
        sheet.paste(im.crop((m, m, im.width - m, im.height - m)).resize((cell, cell), Image.LANCZOS), (x, y + head))
    sheet.save(target, quality=90)
    return target


def cmd_rig_check(a):
    """Re-checks built rigs without rebuilding them (one code, or every rigged animal)."""
    dirs = [VL.find(a.code)] if a.code else VL.animal_dirs()
    bad = []
    for d in dirs:
        an = VL.load(d)
        blend, _ = rig_paths(d, an)
        if not os.path.exists(blend):
            continue
        res = VL.run_blender(dict(open_rig=blend, check=dict(dir=check_dir(an["code"]))), f"{an['code']}-rigcheck",
                             script="vf_rig.py")
        chk = res.get("check") or {}
        rj = os.path.join(d, "blender", "rig.json")
        if os.path.exists(rj):
            r = json.load(open(rj, encoding="utf-8"))
            r["check"] = dict(ok=chk.get("ok"), weights_ok=chk.get("weights_ok"), missing=chk.get("missing"),
                              failing=[x["bone"] for x in chk.get("rows", []) if not x.get("ok")])
            json.dump(r, open(rj, "w", encoding="utf-8"), indent=1, default=str)
        out(f"  {an['code']} · {an['common']}: {'PASS' if chk.get('ok') else 'FAIL'} -> "
            f"{VL.rel(check_sheet(an, chk))}")
        if not chk.get("ok"):
            bad.append(an["code"])
    if not a.code:
        out(f"-> {VL.rel(check_lineup(CHECK_LINEUP))}")
    out(f"rig-check: {len(bad)} failing" + (f" ({', '.join(bad)})" if bad else ""))
    return 1 if bad else 0


def cmd_rig(a):
    folder = VL.find(a.code)
    animal = VL.load(folder)
    gifs = do_rig(folder, animal, force=a.force, preview=not a.no_preview)
    blend, glb = rig_paths(folder, animal)
    out(f"{a.code}: {VL.rel(blend)}, {VL.rel(glb)}")
    for name, g in (gifs or {}).items():
        out(f"  {name}: {VL.rel(g)}")
    return 0


def cmd_rig_all(a):
    from concurrent.futures import ThreadPoolExecutor
    todo = [d for d in VL.animal_dirs() if os.path.exists(os.path.join(d, "blender", "model.py"))]
    for d in todo:                               # stills first, one at a time (cheap when current)
        do_build(d, VL.load(d))
    errors = []

    def one(d):
        an = VL.load(d)
        try:
            do_rig(d, an, force=a.force, preview=not a.no_preview)
        except SystemExit as e:
            errors.append(f"{an['code']}: {e}")

    with ThreadPoolExecutor(max_workers=max(1, a.jobs)) as ex:
        list(ex.map(one, todo))
    for e in errors:
        out("  ERROR", e)
    out(f"-> {VL.rel(check_lineup(CHECK_LINEUP))}")
    if not a.no_preview and not errors:
        out(f"-> {VL.rel(motion_lineup(LINEUP_GIF))}")
    out(f"rig-all: {len(todo) - len(errors)} rigged, {len(errors)} failed")
    return 1 if errors else 0


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
             "| `build.json` | the stamp: when, which Blender, the model, look and standards hashes, framing, render times |"]
    rblend, rglb = rig_paths(folder, animal)
    rj = os.path.join(folder, "blender", "rig.json")
    r = json.load(open(rj, encoding="utf-8")) if os.path.exists(rj) else None
    rig_line = []
    if r:
        rs, rwhy = rig_state(folder, animal)
        acts = ", ".join(f"{k} ({v} f)" for k, v in r.get("actions", {}).items())
        lines += [f"| `{os.path.basename(rblend)}` | the animation rig (`vf.py rig`, approved motion): armature "
                  f"`VF · armature` from the joints, mesh `VF · animal` skinned with rigid weights, actions {acts} at {r.get('fps')} fps, "
                  "scene `ANIM 1x1` |",
                  f"| `{os.path.basename(rglb)}` | the same rig and actions as glTF binary (Y up, one animation per action) |",
                  "| `rig.json` | the rig's stamp: plan, bones, actions, the still and motion hashes |"]
        rig_line = [f"- Animation rig: **{rs}**" + (f" ({', '.join(rwhy)})" if rwhy else "")
                    + f", {r.get('plan')} plan, {r.get('bones')} bones, rigged {r.get('rigged')}"]
    lines += ["",
             f"- Build: **{state}**" + (f" ({', '.join(why)})" if why else "") + (f", built {b.get('built')}" if b else ""),
             *rig_line,
             f"- Model: {'; '.join(model.get('notes', [])) or '-'}",
             f"- Standards {b.get('standards_version', '?')}, rig `{b.get('rig', '?')}`, geometry `{b.get('geometry', '?')}`, "
             f"Blender {b.get('blender', '?')}", ""]
    open(os.path.join(folder, "blender", "README.md"), "w", encoding="utf-8").write("\n".join(lines))


def write_overview(folder, animal):
    code = animal["code"]
    import package as PK
    items = PK.EXPORT["items"]
    model = os.path.join(folder, "blender", "model.py")
    blend = VL.blend_path(folder, animal)
    nphotos = len(_photos(folder))
    doc = os.path.join(folder, "docs", "animal-info.md")
    doc_ok = os.path.exists(doc) and "{{" not in open(doc, encoding="utf-8").read()
    preview_sheet = os.path.join(VL.CACHE, "preview", code, f"{code} · preview sheet.png")
    ap = animal.get("approvals") or {}
    n_ex = sum(os.path.exists(PK.export_file(folder, code, s)) for s, _, _ in items)
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
        f"- [{box(n_ex == len(items))}] Phase 4 · Export package: {n_ex} of {len(items)} (render.bat renders the "
        "masters and the loop; package.bat builds the stock image, the GIF and the cards)",
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
    lines += ["", "## Deliverables (the export package)", "", "| ID | What | File |", "|---|---|---|"]
    for suffix, _, what in items:
        p = PK.export_file(folder, code, suffix)
        lines.append(f"| `{PK.export_id(code, suffix)}` | {what} | "
                     + (f"`export/{os.path.basename(p)}`" if os.path.exists(p) else "not built yet") + " |")
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
              "| `export/` | the export package (+ the `stock/` JPEG) |", ""]
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
        f"| Motion | armature from the joints, sections skinned with rigid weights, rest pose = the model as drawn, "
        f"action `pose` = the still; {ST.MOTION['fps']} fps; idle {ST.MOTION['frames']['idle']} frames, walk "
        f"{ST.MOTION['frames']['walk']} ({ST.MOTION['frames']['walk_large']} from {ST.MOTION['large']} voxels long); "
        f"legs swing {ST.MOTION['leg_swing']:g}° stiff, {ST.MOTION['leg_swing_knee']:g}° over a knee folding "
        f"{ST.MOTION['knee_fold']:g}°, two legs {ST.MOTION['leg_swing_biped']:g}° folding "
        f"{ST.MOTION['knee_fold_biped']:g}°; hops {ST.MOTION['hop_height']:g} of the length; every frame grounded |",
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
            # every animal with a model is rigged, passes the rig check and has a loop of every action (owner,
            # 2026-11-17); a missing or stale rig is a problem
            rs, rwhy = rig_state(d, an)
            if rs != "current":
                fails.append(f"{an['code']}: animation rig {rs} ({', '.join(rwhy)}): vf.py rig {an['code']}")
            else:
                r = json.load(open(os.path.join(d, "blender", "rig.json"), encoding="utf-8"))
                if not (r.get("check") or {}).get("ok"):
                    fails.append(f"{an['code']}: rig check FAIL ({', '.join((r.get('check') or {}).get('failing') or [])}):"
                                 f" see {VL.rel(check_sheet_path(an['code']))}")
                if len(r.get("actions", {})) < 2:
                    fails.append(f"{an['code']}: the rig has no actions besides the still pose")
                missing = [n for n in r.get("actions", {}) if n != "pose" and not os.path.exists(gif_path(an["code"], n))]
                if missing:                      # the GIF loops live in the git-ignored cache: a note, they rebuild
                    notes.append(f"{an['code']}: no preview loop for {', '.join(missing)} on this PC: "
                                 f"vf.py rig {an['code']} --force")
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
        if name == "preview":
            p.add_argument("--stills", action="store_true", help="the six stills only (quick model iteration); "
                           "without it the preview also rigs, checks and animates the animal")
        if name == "final":
            p.add_argument("--low", action="store_true", help="the same renders at LOW into the cache (layouts)")
    p = sub.add_parser("package")
    p.add_argument("code")
    p.add_argument("--low", action="store_true")
    p = sub.add_parser("package-all")
    p.add_argument("--low", action="store_true")
    for name in ("overview", "register"):
        sub.add_parser(name).add_argument("code")
    p = sub.add_parser("render-all")
    p.add_argument("profile", choices=("LOW", "ULTRA"))
    p.add_argument("--force", action="store_true")
    p.add_argument("--stills", action="store_true", help="LOW: the stills only, no rigs and loops")
    p.add_argument("--jobs", type=int, default=3)
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
    p = sub.add_parser("rig")
    p.add_argument("code")
    p.add_argument("--force", action="store_true")
    p.add_argument("--no-preview", action="store_true")
    p = sub.add_parser("rig-all")
    p.add_argument("--force", action="store_true")
    p.add_argument("--no-preview", action="store_true")
    p.add_argument("--jobs", type=int, default=3, help="Blender runs at once (default 3)")
    p = sub.add_parser("rig-check")
    p.add_argument("code", nargs="?")
    sub.add_parser("verify")
    p = sub.add_parser("lock")
    p.add_argument("reason")
    p = sub.add_parser("standards")
    p.add_argument("--write", action="store_true")
    a = ap.parse_args()
    return globals()["cmd_" + a.cmd.replace("-", "_")](a)


if __name__ == "__main__":
    sys.exit(main())
