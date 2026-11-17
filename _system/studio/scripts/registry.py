"""Voxel Fauna · the image registry workbook (05 Publish/Voxel Fauna · Registry.xlsx), styled like Nilant's
Schedule & Metrics workbook: Arial, a dark header row, amber cells for typing, every other cell written by vf.py.

    build()               creates the workbook (only when it does not exist: never over typed data)
    upsert(folder, a)     adds or updates one animal and its six images, keyed by code and Image ID; typed (amber)
                          columns are never overwritten
"""
import datetime
import os

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

import vflib as VL

ST = VL.ST
DARK, AMBER, WHITE = "262626", "FEF3C6", "FFFFFF"
PLATFORM_STATES = "Not submitted,Submitted,Accepted,Rejected,Live"

ANIMALS = [("Code", 9, False), ("Common name", 22, False), ("Scientific name", 26, False), ("Folder", 34, False),
           ("Background", 13, False), ("Status", 16, False), ("Preview approved", 15, False),
           ("Final approved", 14, False), ("Images", 8, False), ("Notes", 40, True)]
IMAGES = [("Image ID", 22, False), ("Animal code", 11, False), ("Common name", 20, False),
          ("Scientific name", 24, False), ("Kind", 12, False), ("Ratio", 7, False), ("Size (px)", 11, False),
          ("File", 58, False), ("Status", 14, False), ("Adobe Stock", 14, True), ("Shutterstock", 14, True),
          ("Gumroad", 14, True), ("Other", 18, True), ("Notes", 36, True)]
LOG = [("Date", 12, False), ("Image ID", 22, False), ("Animal", 20, False), ("Platform", 14, False),
       ("Action", 13, False), ("Link or platform ID", 48, False), ("Note", 50, False)]
LOG_ACTIONS = ("Submitted", "Accepted", "Rejected", "Live", "Removed", "Updated")
PLATFORM_COLUMN = {"Adobe Stock": 10, "Shutterstock": 11, "Gumroad": 12}

PLATFORMS = [
    ("Adobe Stock", "Main stock channel", "JPEG, sRGB (a separate category takes transparent PNG)", "4 MP", "100 MP, 45 MB",
     "Title up to 200 characters; up to 49 keywords, the first 10 matter most; tick 'Created using generative AI "
     "tools' only if such tools made or changed the subject (these Blender renders: no); near-duplicates of one "
     "subject may be refused as similar content", "https://helpx.adobe.com/stock/contributor.html"),
    ("Shutterstock", "Second stock channel", "JPEG (or TIFF without layers)", "4 MP", "",
     "Highest JPEG quality; illustrations flagged as such in the upload form", "https://submit.shutterstock.com/"),
    ("Gumroad", "Direct sales: one pack per animal or per set", "PNG masters in a .zip", "", "",
     "Licence text and pricing are the owner's; the brand goes on the cover and listing, not in the images",
     "https://gumroad.com/"),
    ("Freepik", "Recommended: strong demand for 3D and isometric illustrations", "Check the contributor portal", "",
     "", "Verify current requirements and the AI declaration before the first upload", "https://contributor.freepik.com/"),
    ("Dreamstime", "Recommended: easy to join, non-exclusive", "JPEG", "3 MP (check)", "", "Verify before upload",
     "https://www.dreamstime.com/sell-stock-photos-images"),
    ("Creative Market", "Recommended: bundles of the collection (like Gumroad)", "ZIP of PNGs", "", "",
     "Shop approval needed; verify current terms", "https://creativemarket.com/sell"),
]


def _style_header(ws, cols):
    for i, (name, width, _) in enumerate(cols, start=1):
        c = ws.cell(row=1, column=i, value=name)
        c.font = Font(name="Arial", bold=True, color=WHITE)
        c.fill = PatternFill("solid", fgColor=DARK)
        c.alignment = Alignment(vertical="center")
        ws.column_dimensions[c.column_letter].width = width
    ws.freeze_panes = "A2"


def build():
    wb = Workbook()
    rm = wb.active
    rm.title = "Read Me"
    rows = [
        (f"{ST.COLLECTION} · Registry", None),
        ("Every animal of the collection and its export package, with where each item is published. Amber cells are yours "
         "to type in; every other cell is written by `python _system/studio/scripts/vf.py register <code>`.", None),
        (None, None),
        ("Convention", "Value"),
        ("Animal code", "YY-SEQ, as Nilant's video codes (26-001, 26-002, ...): the folder 02 Animals/<code> · <Common name>"),
        ("Image ID", "VF-{code}-{item}  e.g. VF-26-001-MASTER-DYN"),
        ("Items", "; ".join(f"{s} = {w}" for s, _, w in _PK().EXPORT["items"])),
        ("File", "in the animal's export/ folder (render.bat renders the masters, render.bat, P builds the rest); the "
                 "stock image VF-{code}-STOCK.jpg (the whole dynamic master as a JPEG) is beside them"),
        ("Statuses", " → ".join(ST.STATUSES)),
        ("Platform cells", PLATFORM_STATES.replace(",", ", ")),
        (None, None),
        ("Sheet", "What to do"),
        ("Animals", "One row per species. Never a second row for the same species. Notes are yours."),
        ("Images", "Six rows per animal. Set each platform's state as you upload (Submitted, Accepted, Rejected, Live)."),
        ("Publish Log", "One dated row per upload event (as Nilant's Schedule records each upload): written by "
                        "`vf.py log <code or Image ID> <platform> <action>`, which also sets the Images cell and "
                        "appends to 05 Publish/Voxel Fauna · Publish Log.md."),
        ("Platforms", "Where the images go and each platform's file rules (check them before a big batch: they change)."),
    ]
    for r, (a, b) in enumerate(rows, start=1):
        rm.cell(row=r, column=1, value=a)
        rm.cell(row=r, column=2, value=b)
        for c in (1, 2):
            rm.cell(row=r, column=c).font = Font(name="Arial", size=10)
    rm["A1"].font = Font(name="Arial", size=16, bold=True)
    for r in (4, 13):
        for c in (1, 2):
            cell = rm.cell(row=r, column=c)
            cell.font = Font(name="Arial", bold=True, color=WHITE)
            cell.fill = PatternFill("solid", fgColor=DARK)
    rm.column_dimensions["A"].width = 22
    rm.column_dimensions["B"].width = 110

    for title, cols in (("Animals", ANIMALS), ("Images", IMAGES)):
        ws = wb.create_sheet(title)
        _style_header(ws, cols)
    ws = wb["Images"]
    dv = DataValidation(type="list", formula1=f'"{PLATFORM_STATES}"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add("J2:M2000")
    ws = wb.create_sheet("Publish Log")
    _style_header(ws, LOG)

    ws = wb.create_sheet("Platforms")
    cols = [("Platform", 16, False), ("Use", 40, False), ("Format", 34, False), ("Minimum", 12, False),
            ("Maximum", 16, False), ("Rules", 90, False), ("Link", 44, False)]
    _style_header(ws, cols)
    for r, row in enumerate(PLATFORMS, start=2):
        for c, v in enumerate(row, start=1):
            cell = ws.cell(row=r, column=c, value=v)
            cell.font = Font(name="Arial", size=10)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=len(PLATFORMS) + 3, column=1,
            value=f"Rules as read on {datetime.date.today().isoformat()}; see 01 Guide/Voxel Fauna · Stock Platforms.md").font = \
        Font(name="Arial", size=9, italic=True)
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
        cell.font = Font(name="Arial", size=10)


def _PK():
    import package
    return package


def upsert(folder, animal):
    if not os.path.exists(VL.REGISTRY):
        build()
    wb = load_workbook(VL.REGISTRY)
    code = animal["code"]
    ap = animal.get("approvals") or {}
    ws = wb["Animals"]
    r = _row_of(ws, code)
    _write(ws, r, ANIMALS, [code, animal["common"], animal["scientific"], VL.rel(folder), animal["look"]["background"],
                            "Registered" if animal["status"] not in ("Approved",) else animal["status"],
                            ap.get("preview"), ap.get("final"), f'=COUNTIF(Images!$B$2:$B$2000,A{r})', None])
    ws = wb["Images"]
    n = 0
    PK = _PK()
    E = PK.EXPORT
    shape = {"MASTER-DYN": ("Master", "1x1", f"{E['master']}x{E['master']}"),
             "MASTER-BLOCK": ("Master", "1x1", f"{E['master']}x{E['master']}"),
             "LOOP": ("Loop GIF", "1x1", f"{E['loop']['size']}x{E['loop']['size']}"),
             "CARD-EN": ("Card PDF", "A5", "148x210 mm"), "CARD-ID": ("Card PDF", "A5", "148x210 mm")}
    import stock as SK
    rows = [(s, PK.export_file(folder, code, s), w) for s, _, w in E["items"]] + [
        (SK.STOCK, SK.stock_file(folder, code), "the stock image: the dynamic master as an sRGB JPEG, for stock sites")]
    shape[SK.STOCK] = ("Stock", "1x1", f"{E['master']}x{E['master']}")
    old = PK.export_id(code, "STOCK-1x1")                 # the cropped stock PNG (dropped 2026-11-17): its row goes
    for rr in range(ws.max_row, 1, -1):
        if ws.cell(row=rr, column=1).value == old:
            ws.delete_rows(rr)
    for suffix, path, what in rows:
        iid = PK.export_id(code, suffix)
        kname, ratio, size = shape.get(suffix, (suffix, "", ""))
        r = _row_of(ws, iid)
        _write(ws, r, IMAGES, [iid, code, animal["common"], animal["scientific"], kname, ratio, size,
                               VL.rel(path), "Final" if os.path.exists(path) else "Missing",
                               "Not submitted", "Not submitted", "Not submitted", None, what])
        n += 1
    wb.save(VL.REGISTRY)
    return n + 1


LOG_MD = os.path.join(VL.PUBLISH, "Voxel Fauna · Publish Log.md")


def log(ids, animal, platform, action, link="", note=""):
    """Append one dated row per image to the Publish Log sheet and the markdown log; set the Images platform cell."""
    if not os.path.exists(VL.REGISTRY):
        build()
    wb = load_workbook(VL.REGISTRY)
    if "Publish Log" not in wb.sheetnames:
        _style_header(wb.create_sheet("Publish Log", index=3), LOG)
    ws = wb["Publish Log"]
    today = datetime.date.today().isoformat()
    for iid in ids:
        r = ws.max_row + 1
        for c, v in enumerate([today, iid, animal["common"], platform, action, link, note], start=1):
            ws.cell(row=r, column=c, value=v).font = Font(name="Arial", size=10)
        col = PLATFORM_COLUMN.get(platform)
        img = wb["Images"]
        for rr in range(2, img.max_row + 1):
            if img.cell(row=rr, column=1).value == iid:
                cell = img.cell(row=rr, column=col or 13)
                cell.value = action if col else f"{platform}: {action}"
                cell.fill = PatternFill("solid", fgColor=AMBER)
    wb.save(VL.REGISTRY)
    new = not os.path.exists(LOG_MD)
    with open(LOG_MD, "a", encoding="utf-8") as f:
        if new:
            f.write(LOG_HEADER)
        for iid in ids:
            f.write(f"| {today} | `{iid}` | {animal['common']} | {platform} | {action} | {link or '-'} | {note or '-'} |\n")
    return len(ids)


LOG_HEADER = """# Voxel Fauna · Publish Log

Every upload event, newest at the bottom, the way Nilant's workbook records each upload in its Schedule. Written by
`python _system/studio/scripts/vf.py log <code or Image ID> <platform> <action> [--link URL] [--note "..."]`, which also
adds the row to the **Publish Log** sheet of `Voxel Fauna · Registry.xlsx` and sets the image's platform cell there.
Actions: Submitted, Accepted, Rejected, Live, Removed, Updated. Note refusal reasons: they shape the next uploads.

| Date | Image ID | Animal | Platform | Action | Link or platform ID | Note |
|---|---|---|---|---|---|---|
"""
