"""Voxel Fauna · stock packaging: the stock JPEG, the upload CSVs and the Gumroad zip.

    package(folder, animal, only=None)
      export/VF-<code>-STOCK.jpg    the whole dynamic master (4096 square, no crop; owner 2026-11-17) as an sRGB JPEG
                                    (ICC embedded), quality 95, 4:4:4, 300 ppi, title/description/keywords in XMP
      05 Publish/Stock/<code> · Adobe Stock.csv     Filename, Title, Keywords, Category, Releases
      05 Publish/Stock/<code> · Shutterstock.csv    Filename, Description, Keywords, Categories, Illustration, ...
      05 Publish/Gumroad/<code> · <Common name>.zip the export package: two masters, the loop GIF, the two cards

Titles and keywords come from animal.json -> stock (title, keywords); missing ones are built from the names.
Platform rules (01 Guide/Voxel Fauna · Stock Platforms.md): Adobe Stock 4-100 MP, 45 MB, up to 49 keywords.
"""
import csv
import os
import zipfile
from xml.sax.saxutils import escape

from PIL import Image, ImageCms

import vflib as VL

ST = VL.ST
BASE_KEYWORDS = ["voxel", "isometric", "3d illustration", "voxel art", "cube", "blocky", "animal", "wildlife",
                 "cute", "low resolution", "pixel", "minimal", "geometric", "block toy", "solid background"]
INFO_KEYWORDS = ["infographic", "fact sheet", "education", "biology", "zoology", "information"]
# The look borrows the blocky-mob style of block-building games (owner, 2026-11-16); a game's name in a title or
# keyword is a trademark Adobe Stock and Shutterstock refuse (and a claim of affiliation). vf.py check fails on these.
TRADEMARKS = ("minecraft", "mojang", "roblox", "lego", "crossy road", "fortnite", "nintendo", "pokemon", "pokémon")


def trademark_hits(animal):
    """Game or brand names found in the stock title, info title or keywords (must be empty)."""
    s = animal.get("stock") or {}
    text = " | ".join([s.get("title") or "", s.get("info_title") or ""] + list(s.get("keywords") or [])).lower()
    return [t for t in TRADEMARKS if t in text]
ADOBE_ANIMALS = 1          # Adobe Stock category id "Animals"


def _titles(animal, kind):
    s = animal.get("stock") or {}
    import infographic as IG
    bg = animal["look"].get("background_name") or "pastel"
    if kind == "ILL":
        return s.get("title") or (f"{animal['common']} ({animal['scientific']}) isometric voxel 3D illustration "
                                  f"on a soft {bg} background")
    return s.get("info_title") or (f"{animal['common']} ({animal['scientific']}) infographic: isometric voxel 3D "
                                   f"illustration with habitat, diet and facts")


def _keywords(animal, kind):
    s = animal.get("stock") or {}
    words = list(s.get("keywords") or [])
    words += [animal["common"].lower(), animal["scientific"].lower()]
    words += INFO_KEYWORDS if kind == "INF" else []
    words += BASE_KEYWORDS
    seen, out = set(), []
    for w in words:
        w = w.strip().lower()
        if w and w not in seen:
            seen.add(w)
            out.append(w)
    return out[:49]


def _xmp(title, keywords):
    kw = "".join(f"<rdf:li>{escape(k)}</rdf:li>" for k in keywords)
    t = escape(title)
    return ('<?xpacket begin="" id="W5M0MpCehiHzreSzNTczkc9d"?><x:xmpmeta xmlns:x="adobe:ns:meta/">'
            '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description rdf:about="" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/">'
            f'<dc:title><rdf:Alt><rdf:li xml:lang="x-default">{t}</rdf:li></rdf:Alt></dc:title>'
            f'<dc:description><rdf:Alt><rdf:li xml:lang="x-default">{t}</rdf:li></rdf:Alt></dc:description>'
            f'<dc:subject><rdf:Bag>{kw}</rdf:Bag></dc:subject></rdf:Description></rdf:RDF></x:xmpmeta>'
            '<?xpacket end="w"?>').encode("utf-8")


STOCK = "STOCK"            # the stock image's Image ID suffix: VF-<code>-STOCK.jpg in export/


def stock_file(folder, code):
    import package as PK
    return os.path.join(folder, "export", PK.export_id(code, STOCK) + ".jpg")


STOCK_PARTS = ("jpeg", "csv", "zip")           # the stock JPEG, the upload CSVs, the Gumroad zip


def zip_file(folder, animal):
    return os.path.join(VL.PUBLISH, "Gumroad", f"{animal['code']} · {animal['common']} · {ST.COLLECTION}.zip")


def package(folder, animal, only=None, parts=None):
    """The stock JPEG (the whole dynamic master, no crop, in export/ beside the package; owner 2026-11-17: "keep stock
    but dont crop it from master") and its upload CSVs; the cards carry a third-party photograph, so stock sites get
    the stock image only. The Gumroad zip holds the export package (the two masters, the loop GIF and the English and
    Indonesian cards). `only` is kept for the command line and ignored: there is one stock image per animal.
    `parts` (a subset of STOCK_PARTS, default all) builds only those: the render menu's choice (the CSVs need the JPEG's
    title and keywords, which come from animal.json, so they do not need the JPEG to be rebuilt)."""
    import package as PK
    parts = set(parts or STOCK_PARTS)
    code = animal["code"]
    icc = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()
    pdir = os.path.join(VL.PUBLISH, "Stock")
    os.makedirs(pdir, exist_ok=True)
    adobe, shutter, lines = [], [], []
    masters = [PK.export_file(folder, code, s) for s, _, _ in PK.EXPORT["items"]]
    src = PK.export_file(folder, code, "MASTER-DYN")
    if not os.path.exists(src):
        lines.append(f"skip the stock image: no dynamic master yet ({VL.rel(src)}; render.bat, 3)")
    else:
        iid = PK.export_id(code, STOCK)
        dst = stock_file(folder, code)
        title, kws = _titles(animal, "ILL"), _keywords(animal, "ILL")
        if "jpeg" in parts:
            with Image.open(src) as im:
                im = im.convert("RGB")
                mp = im.width * im.height / 1e6
                im.save(dst, "JPEG", quality=95, subsampling=0, optimize=True, dpi=(300, 300), icc_profile=icc,
                        xmp=_xmp(title, kws))
            mb = os.path.getsize(dst) / 1e6
            ok = 4 <= mp <= 100 and mb <= 45
            lines.append(f"{iid}.jpg  {mp:.1f} MP  {mb:.1f} MB  {'ok' if ok else 'OUTSIDE ADOBE LIMITS'}")
        adobe.append([iid + ".jpg", title[:200], ", ".join(kws), ADOBE_ANIMALS, ""])
        shutter.append([iid + ".jpg", title[:200], ",".join(kws[:50]), "Animals/Wildlife", "yes", "no", "no"])
    if adobe and "csv" in parts:
        p = os.path.join(pdir, f"{code} · Adobe Stock.csv")
        with open(p, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Filename", "Title", "Keywords", "Category", "Releases"])
            w.writerows(adobe)
        lines.append(f"-> {VL.rel(p)}")
        p = os.path.join(pdir, f"{code} · Shutterstock.csv")
        with open(p, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Filename", "Description", "Keywords", "Categories", "Illustration", "Mature content", "Editorial"])
            w.writerows(shutter)
        lines.append(f"-> {VL.rel(p)}")
    missing = [m for m in masters if not os.path.exists(m)]
    if "zip" not in parts:
        pass
    elif not missing:
        gdir = os.path.join(VL.PUBLISH, "Gumroad")
        os.makedirs(gdir, exist_ok=True)
        z = zip_file(folder, animal)
        with zipfile.ZipFile(z, "w", zipfile.ZIP_STORED) as zf:      # PNG, GIF and PDF are already compressed
            for m in masters:
                zf.write(m, os.path.basename(m))
        lines.append(f"-> {VL.rel(z)} (the export package: {len(masters)} files; add the licence and cover yourself)")
    else:
        lines.append(f"no Gumroad zip yet: missing {', '.join(os.path.basename(m) for m in missing)}")
    return lines
