"""Voxel Fauna · stock packaging: upload-ready JPEGs and CSVs from an animal's six PNG masters.

    package(folder, animal, only=None)
      export/stock/<Image ID>.jpg   sRGB (ICC embedded), quality 95, 4:4:4, 300 ppi, title/description/keywords in XMP
      05 Publish/Stock/<code> · Adobe Stock.csv     Filename, Title, Keywords, Category, Releases
      05 Publish/Stock/<code> · Shutterstock.csv    Filename, Description, Keywords, Categories, Illustration, ...
      05 Publish/Gumroad/<code> · <Common name>.zip the six PNG masters

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
                 "cute", "low resolution", "pixel", "minimal", "geometric", "plastic toy", "solid background"]
INFO_KEYWORDS = ["infographic", "fact sheet", "education", "biology", "zoology", "information"]
ADOBE_ANIMALS = 1          # Adobe Stock category id "Animals"


def _titles(animal, kind):
    s = animal.get("stock") or {}
    bg = animal["look"]["background"].rsplit("-", 1)[0]
    if kind == "ILL":
        return s.get("title") or (f"{animal['common']} ({animal['scientific']}) isometric voxel 3D illustration "
                                  f"on a solid {bg} background")
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


def package(folder, animal, only=None):
    """Stock JPEGs and CSVs for `only` (default: the three illustrations: the information artworks carry a
    third-party photograph, which stock sites' contributor terms do not allow to be licensed as your own work);
    the Gumroad zip always holds all six PNGs (the photo's credit is on the artwork)."""
    code = animal["code"]
    if only is None:
        only = [f"ILL-{r}" for r in ST.RATIOS]
    icc = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()
    sdir = os.path.join(folder, "export", "stock")
    pdir = os.path.join(VL.PUBLISH, "Stock")
    os.makedirs(sdir, exist_ok=True)
    os.makedirs(pdir, exist_ok=True)
    adobe, shutter, lines, masters = [], [], [], []
    for kind in ST.KINDS:
        for ratio in ST.RATIOS:
            key = f"{kind}-{ratio}"
            src = VL.export_path(folder, code, kind, ratio)
            if not os.path.exists(src):
                lines.append(f"skip {key}: no export yet ({VL.rel(src)})")
                continue
            masters.append(src)
            if only and key not in only:
                continue
            iid = VL.image_id(code, kind, ratio)
            dst = os.path.join(sdir, iid + ".jpg")
            title, kws = _titles(animal, kind), _keywords(animal, kind)
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
    if adobe:
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
    if len(masters) == 6:
        gdir = os.path.join(VL.PUBLISH, "Gumroad")
        os.makedirs(gdir, exist_ok=True)
        z = os.path.join(gdir, f"{code} · {animal['common']} · {ST.COLLECTION}.zip")
        with zipfile.ZipFile(z, "w", zipfile.ZIP_STORED) as zf:      # PNGs are already compressed
            for m in masters:
                zf.write(m, os.path.basename(m))
        lines.append(f"-> {VL.rel(z)} (six PNG masters; add the licence and cover yourself)")
    return lines
