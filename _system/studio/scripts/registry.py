"""Voxel Fauna · the registry workbooks, styled like Nilant's Schedule & Metrics workbook: Arial, a dark header row,
amber cells for typing, every other cell written by vf.py.

Owner, 2026-11-21: "the registry excel should list the animal info. the platform target should listed in different
excel files." So:

    05 Publish/Voxel Fauna · Registry.xlsx                 Read Me + Animals: one row per species with its information
                                                           (names, classification, IUCN, size, stats, habitat, diet,
                                                           facts, colours, photo, motion, status, approvals)
    05 Publish/Platforms/Voxel Fauna · <Platform>.xlsx     one workbook per platform: Read Me (its rules), Items (what
                                                           goes there, per animal, with the upload state) and its
                                                           Publish Log

    upsert(folder, a)     the animal's registry row and its rows in every platform workbook (typed cells kept)
    log(ids, a, platform, action, link, note)   one dated row per item in that platform's Publish Log, the item's
                                                state set, and a row in 05 Publish/Voxel Fauna · Publish Log.md
"""
import datetime
import os

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

import vflib as VL

ST = VL.ST
DARK, AMBER, WHITE = "262626", "FEF3C6", "FFFFFF"
STATES = "Not submitted,Submitted,Accepted,Rejected,Live,Removed"
LOG_ACTIONS = ("Submitted", "Accepted", "Rejected", "Live", "Removed", "Updated")
PLATFORM_DIR = os.path.join(VL.PUBLISH, "Platforms")

# (header, width, typed by the owner)
ANIMALS = [("Code", 9, False), ("Common name", 22, False), ("Common name (ID)", 22, False),
           ("Scientific name", 28, False), ("Kicker", 26, False), ("Class", 12, False), ("Order", 16, False),
           ("Family", 16, False), ("IUCN", 6, False), ("IUCN status", 20, False), ("Assessed", 9, False),
           ("Trend", 11, False), ("Real size (m)", 11, False), ("Size measured", 40, False), ("Stat 1", 22, False),
           ("Stat 2", 22, False), ("Stat 3", 22, False), ("Stat 4", 22, False), ("Habitat", 50, False),
           ("Diet", 50, False), ("Fun fact", 60, False), ("Second fact", 60, False), ("Background", 10, False),
           ("Background name", 20, False), ("Main colour", 10, False), ("Palette", 40, False), ("Motion", 30, False),
           ("Photo credit", 34, False), ("Sources", 8, False), ("Folder", 34, False), ("Status", 16, False),
           ("Preview approved", 15, False), ("Final approved", 14, False), ("Notes", 40, True)]
ITEMS = [("Image ID", 24, False), ("Animal code", 11, False), ("Common name", 22, False),
         ("Scientific name", 26, False), ("Item", 16, False), ("Size", 13, False), ("File", 60, False),
         ("File status", 11, False), ("State", 14, True), ("Link or platform ID", 40, True), ("Notes", 36, True)]
LOG = [("Date", 12, False), ("Image ID", 24, False), ("Animal", 22, False), ("Action", 13, False),
       ("Link or platform ID", 48, False), ("Note", 50, False)]

# what goes to each platform: "stock" = the stock JPEG only (the cards carry a third-party photo, which stock sites'
# contributor terms do not let us license as our own); "package" = the whole export package (sold as a zip)
PLATFORMS = [
    dict(name="Adobe Stock", kind="stock", use="Main stock channel",
         format="JPEG, sRGB (a separate category takes transparent PNG)", min="4 MP", max="100 MP, 45 MB",
         rules="Title up to 200 characters; up to 49 keywords, the first 10 matter most; tick 'Created using generative "
               "AI tools' only if such tools made or changed the subject (these Blender renders: no); near-duplicates "
               "of one subject may be refused as similar content", link="https://helpx.adobe.com/stock/contributor.html"),
    dict(name="Shutterstock", kind="stock", use="Second stock channel", format="JPEG (or TIFF without layers)",
         min="4 MP", max="", rules="Highest JPEG quality; illustrations flagged as such in the upload form",
         link="https://submit.shutterstock.com/"),
    dict(name="Freepik", kind="stock", use="Strong demand for 3D and isometric illustrations",
         format="Check the contributor portal", min="", max="",
         rules="Verify current requirements and the AI declaration before the first upload",
         link="https://contributor.freepik.com/"),
    dict(name="Dreamstime", kind="stock", use="Easy to join, non-exclusive", format="JPEG", min="3 MP (check)", max="",
         rules="Verify before upload", link="https://www.dreamstime.com/sell-stock-photos-images"),
    dict(name="Gumroad", kind="package", use="Direct sales: one pack per animal or per set",
         format="The export package in a .zip (05 Publish/Gumroad)", min="", max="",
         rules="Licence text and pricing are the owner's; the brand goes on the cover and listing, not in the images",
         link="https://gumroad.com/"),
    dict(name="Creative Market", kind="package", use="Bundles of the collection (like Gumroad)", format="ZIP",
         min="", max="", rules="Shop approval needed; verify current terms", link="https://creativemarket.com/sell"),
]
PLATFORM_NAMES = [p["name"] for p in PLATFORMS]


def _font(**k):
    return Font(name="Arial", size=k.pop("size", 10), **k)


def _style_header(ws, cols):
    for i, (name, width, _) in enumerate(cols, start=1):
        c = ws.cell(row=1, column=i, value=name)
        c.font = _font(bold=True, color=WHITE)
        c.fill = PatternFill("solid", fgColor=DARK)
        c.alignment = Alignment(vertical="center")
        ws.column_dimensions[c.column_letter].width = width
    ws.freeze_panes = "B2"


def _readme(ws, title, intro, rows):
    ws.title = "Read Me"
    ws.cell(row=1, column=1, value=title).font = _font(size=16, bold=True)
    ws.cell(row=2, column=1, value=intro).font = _font()
    r = 4
    for a, b in rows:
        ca, cb = ws.cell(row=r, column=1, value=a), ws.cell(row=r, column=2, value=b)
        head = a in ("Convention", "Sheet", "Rule")
        for c in (ca, cb):
            c.font = _font(bold=head, color=WHITE if head else None)
            if head:
                c.fill = PatternFill("solid", fgColor=DARK)
            c.alignment = Alignment(wrap_text=True, vertical="top")
        r += 1
    ws.column_dimensions["A"].width = 24
    ws.column_dimensions["B"].width = 110


# ---- the registry: the animals ----------------------------------------------------------------------------------------
def build():
    wb = Workbook()
    _readme(wb.active, f"{ST.COLLECTION} · Registry",
            "Every animal of the collection with its information. Amber cells are yours to type in; every other cell is "
            "written by `python _system/studio/scripts/vf.py register <code>` from the animal's animal.json (the source "
            "of truth: fix a fact there, then register again). Where each item is published lives in the platform "
            "workbooks, 05 Publish/Platforms/Voxel Fauna · <Platform>.xlsx.",
            [("Convention", "Value"),
             ("Animal code", "six digits (000001, 000002, ...): the folder 02 Animals/<code> · <Common name>"),
             ("Image ID", "VF-{code}-{item}  e.g. VF-000001-MASTER-DYN; the stock image VF-{code}-STOCK"),
             ("Statuses", " → ".join(ST.STATUSES)),
             ("Background", "one OKLCH chroma for every animal, its own hue (vf_standards.BACKGROUND_RULE)"),
             (None, None),
             ("Sheet", "What it holds"),
             ("Animals", "One row per species, never two. Facts as printed on the cards, each sourced in animal.json "
                         "and docs/animal-info.md. Notes are yours."),
             ("Platforms", "One workbook per platform in 05 Publish/Platforms/: its rules, its items per animal with "
                           "their state, and its Publish Log (vf.py log <code or Image ID> <platform> <action>).")])
    ws = wb.create_sheet("Animals")
    _style_header(ws, ANIMALS)
    os.makedirs(os.path.dirname(VL.REGISTRY), exist_ok=True)
    wb.save(VL.REGISTRY)
    return VL.REGISTRY


def _row_of(ws, key):
    for r in range(2, ws.max_row + 1):
        if ws.cell(row=r, column=1).value == key:
            return r
    r = ws.max_row + 1
    while r > 2 and ws.cell(row=r - 1, column=1).value is None:
        r -= 1
    return r


def _write(ws, r, cols, values):
    for c, ((_, _, typed), v) in enumerate(zip(cols, values), start=1):
        cell = ws.cell(row=r, column=c)
        if typed:
            cell.fill = PatternFill("solid", fgColor=AMBER)
            if cell.value is None and v is not None:
                cell.value = v
        else:
            cell.value = v
        cell.font = _font()
        cell.alignment = Alignment(vertical="top", wrap_text=isinstance(v, str) and len(v) > 40)


def _text(v):
    return (v.get("text", "") if isinstance(v, dict) else v) or ""


def animal_row(folder, animal):
    info, look = animal.get("info") or {}, animal.get("look") or {}
    cl, cons = info.get("classification") or {}, info.get("conservation") or {}
    size = look.get("size") or {}
    stats = [f"{s.get('label')}: {s.get('value')}" for s in info.get("stats") or []] + [None] * 4
    facts = [_text(f) for f in info.get("facts") or []] + [None, None]
    pal = look.get("palette") or {}
    mo = animal.get("motion") or {}
    ph = info.get("photo") or {}
    ap = animal.get("approvals") or {}
    return [animal["code"], animal["common"], ((animal.get("i18n") or {}).get("id") or {}).get("common"),
            animal["scientific"], info.get("kicker"), cl.get("class"), cl.get("order"), cl.get("family"),
            cons.get("code"), cons.get("status"), cons.get("assessed"), cons.get("trend"), size.get("real_m"),
            size.get("measure"), *stats[:4], _text(info.get("habitat")), _text(info.get("diet")), facts[0], facts[1],
            look.get("background"), look.get("background_name"), next(iter(pal.values()), None),
            ", ".join(f"{k} {v}" for k, v in pal.items()),
            (f"{mo.get('plan')}: " + ", ".join(a for a in mo.get("actions") or [] if a != "pose")) if mo.get("plan") else None,
            f"{ph.get('author')} · {ph.get('licence')}" if ph.get("author") else None, len(animal.get("sources") or []),
            VL.rel(folder), animal.get("status"), ap.get("preview"), ap.get("final"), None]


# ---- the platform workbooks ------------------------------------------------------------------------------------------
def platform_path(name):
    return os.path.join(PLATFORM_DIR, f"{ST.COLLECTION} · {name}.xlsx")


def _platform(name):
    return next(p for p in PLATFORMS if p["name"].lower() == name.lower())


def build_platform(p):
    wb = Workbook()
    what = ("the stock image only (VF-<code>-STOCK.jpg, the whole dynamic master as an sRGB JPEG with its title and "
            "keywords; the upload CSVs are in 05 Publish/Stock)" if p["kind"] == "stock" else
            "the whole export package (two masters, the loop GIF, the English and Indonesian cards; the zip is in "
            "05 Publish/Gumroad)")
    _readme(wb.active, f"{ST.COLLECTION} · {p['name']}",
            f"What goes to {p['name']}: {what}. Amber cells are yours; every other cell is written by "
            "`vf.py register <code>` (the items) and `vf.py log <code or Image ID> \"" + p["name"] + "\" <action>` (the "
            "Publish Log, which also sets the item's State).",
            [("Rule", "Value"), ("Use", p["use"]), ("Format", p["format"]), ("Minimum", p["min"] or "-"),
             ("Maximum", p["max"] or "-"), ("Rules", p["rules"]), ("Link", p["link"]),
             ("Read on", f"{datetime.date.today().isoformat()}; check before a big batch (01 Guide/Voxel Fauna · "
                         "Stock Platforms.md): the rules change"),
             (None, None), ("Sheet", "What it holds"),
             ("Items", "One row per item and animal; set State as you upload (" + STATES.replace(",", ", ") + ")."),
             ("Publish Log", "One dated row per upload event, written by vf.py log.")])
    ws = wb.create_sheet("Items")
    _style_header(ws, ITEMS)
    dv = DataValidation(type="list", formula1=f'"{STATES}"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add("I2:I5000")
    _style_header(wb.create_sheet("Publish Log"), LOG)
    os.makedirs(PLATFORM_DIR, exist_ok=True)
    wb.save(platform_path(p["name"]))


def items_for(folder, animal, kind):
    """(Image ID, item, size, path) for one platform kind."""
    import package as PK
    import stock as SK
    code, E = animal["code"], PK.EXPORT
    if kind == "stock":
        return [(PK.export_id(code, SK.STOCK), "Stock JPEG", f"{E['master']}x{E['master']}",
                 SK.stock_file(folder, code))]
    size = {"MASTER-DYN": f"{E['master']}x{E['master']}", "MASTER-BLOCK": f"{E['master']}x{E['master']}",
            "LOOP": f"{E['loop']['size']}x{E['loop']['size']}", "CARD-EN": "A5 148x210 mm", "CARD-ID": "A5 148x210 mm"}
    name = {"MASTER-DYN": "Master, dynamic", "MASTER-BLOCK": "Master, blocky", "LOOP": "Loop GIF",
            "CARD-EN": "Card PDF, EN", "CARD-ID": "Card PDF, ID"}
    return [(PK.export_id(code, s), name.get(s, s), size.get(s, ""), PK.export_file(folder, code, s))
            for s, _, _ in E["items"]]


def upsert(folder, animal):
    """The animal's registry row and its rows in every platform workbook. Returns the number of rows written."""
    if not os.path.exists(VL.REGISTRY):
        build()
    wb = load_workbook(VL.REGISTRY)
    if "Animals" not in wb.sheetnames or wb["Animals"].cell(row=1, column=3).value != ANIMALS[2][0]:
        wb.close()
        build()                                   # the old layout (images and platforms inside): rebuilt fresh
        wb = load_workbook(VL.REGISTRY)
    ws = wb["Animals"]
    _write(ws, _row_of(ws, animal["code"]), ANIMALS, animal_row(folder, animal))
    wb.save(VL.REGISTRY)
    n = 1
    for p in PLATFORMS:
        path = platform_path(p["name"])
        if not os.path.exists(path):
            build_platform(p)
        pw = load_workbook(path)
        ws = pw["Items"]
        for iid, item, size, fpath in items_for(folder, animal, p["kind"]):
            _write(ws, _row_of(ws, iid), ITEMS, [iid, animal["code"], animal["common"], animal["scientific"], item,
                                                 size, VL.rel(fpath),
                                                 "Final" if os.path.exists(fpath) else "Missing",
                                                 "Not submitted", None, None])
            n += 1
        pw.save(path)
    return n


LOG_MD = os.path.join(VL.PUBLISH, "Voxel Fauna · Publish Log.md")


def log(ids, animal, platform, action, link="", note=""):
    """One dated row per item in the platform's Publish Log and the markdown log; the item's State set."""
    p = _platform(platform)
    path = platform_path(p["name"])
    if not os.path.exists(path):
        build_platform(p)
    wb = load_workbook(path)
    ws = wb["Publish Log"]
    today = datetime.date.today().isoformat()
    items = wb["Items"]
    for iid in ids:
        r = ws.max_row + 1
        for c, v in enumerate([today, iid, animal["common"], action, link, note], start=1):
            ws.cell(row=r, column=c, value=v).font = _font()
        for rr in range(2, items.max_row + 1):
            if items.cell(row=rr, column=1).value == iid:
                cell = items.cell(row=rr, column=9)
                cell.value = action
                cell.fill = PatternFill("solid", fgColor=AMBER)
                if link:
                    items.cell(row=rr, column=10, value=link)
    wb.save(path)
    new = not os.path.exists(LOG_MD)
    with open(LOG_MD, "a", encoding="utf-8") as f:
        if new:
            f.write(LOG_HEADER)
        for iid in ids:
            f.write(f"| {today} | `{iid}` | {animal['common']} | {p['name']} | {action} | {link or '-'} | {note or '-'} |\n")
    return len(ids)


LOG_HEADER = """# Voxel Fauna · Publish Log

Every upload event, newest at the bottom, the way Nilant's workbook records each upload in its Schedule. Written by
`python _system/studio/scripts/vf.py log <code or Image ID> <platform> <action> [--link URL] [--note "..."]`, which also
adds the row to the platform's workbook (`05 Publish/Platforms/Voxel Fauna · <Platform>.xlsx`, Publish Log) and sets
the item's State there. Actions: Submitted, Accepted, Rejected, Live, Removed, Updated. Note refusal reasons: they
shape the next uploads.

| Date | Image ID | Animal | Platform | Action | Link or platform ID | Note |
|---|---|---|---|---|---|---|
"""


def refresh_animals(folders=None):
    """Every animal's row in the registry (rebuilt from each animal.json); typed Notes are kept. The platform
    workbooks are untouched (an animal gets its platform rows at `vf.py register`, once its package exists)."""
    if not os.path.exists(VL.REGISTRY):
        build()
    wb = load_workbook(VL.REGISTRY)
    if "Animals" not in wb.sheetnames or wb["Animals"].cell(row=1, column=3).value != ANIMALS[2][0]:
        wb.close()
        build()
        wb = load_workbook(VL.REGISTRY)
    ws = wb["Animals"]
    n = 0
    for folder in folders or VL.animal_dirs():
        animal = VL.load(folder)
        _write(ws, _row_of(ws, animal["code"]), ANIMALS, animal_row(folder, animal))
        n += 1
    wb.save(VL.REGISTRY)
    return n
