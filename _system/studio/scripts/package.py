"""Voxel Fauna · the export package, built offline from the ULTRA renders (Pillow + PyMuPDF; no Blender).

PROPOSED 2026-11-17 (owner: "render.bat should be rendering only (2 image and 1 motion). then create one bat again to
offlinely build the cards, crop 1:1 to stock, etc etc."). APPROVED 2026-11-17 and locked (v2.2 + the export package) with vf_export.EXPORT.

From the renders of blender/vf_export.py (the two masters in export/, the cut-outs and the loop frames in the cache):
  loop_gif     VF-<code>-LOOP.gif: the looped dynamic animation, EXPORT.loop.size square, 24 fps, plays forever
  card_pdf     VF-<code>-CARD-EN.pdf and -CARD-ID.pdf: A5 portrait with a 3 mm bleed at 300 dpi, two pages:
                 front  minimal and playful, no photograph (owner, 2026-11-17): the animal's own pastel, the kicker,
                        the name big, the scientific name and IUCN chip, the dynamic model with its own rendered shadow
                        (from the dynamic master) among small particles in the family's tints and mixed shapes, four
                        boxless stats with pixel icons, home and menu in two columns, the fun fact on a full-bleed band
                        with a straight top edge
                 back   the regular blocky master on its background, "powered by" + the ihdyo mark + "ihdyo", small at
                        the bottom, black on a light background and white on a dark one (the only place of the brand)
English copy comes from animal.json -> info; the Indonesian from animal.json -> i18n.id (the same facts and sources,
translated: common, kicker, stats [{label, value}], habitat, diet, facts).
"""
import contextlib
import copy
import io
import math
import os

from PIL import Image, ImageDraw, ImageFilter, ImageOps

import vflib as VL
import infographic as IG

ST = VL.ST
import vf_export as VE  # noqa: E402  (blender/ is on the path through vflib; vf_export imports no bpy at load)

EXPORT = VE.EXPORT
LOGO = os.path.join(VL.DESIGN, "Logo", "ihdyo-white.svg")

# the words on the card that are not the animal's own copy, per language
LANG = {
    "en": dict(headings=dict(habitat="Home turf", diet="On the menu", fact="Fun fact!"),
               status={}, photo="Photo", powered="powered by"),
    "id": dict(headings=dict(habitat="Rumahnya", diet="Menu makan", fact="Fakta seru!"),
               status={"LC": "Risiko Rendah", "NT": "Hampir Terancam", "VU": "Rentan", "EN": "Genting",
                       "CR": "Kritis", "EW": "Punah di Alam Liar", "EX": "Punah", "DD": "Kurang Data",
                       "NE": "Belum Dievaluasi"},
               stat_icons=(("panjang", "span"), ("tinggi", "span"), ("ekor", "span"), ("tempurung", "span"),
                           ("cangkang", "span"), ("bahu", "span"), ("lidah", "span"), ("tanduk", "span"),
                           ("paruh", "span"), ("taring", "span"), ("rentang", "span"), ("berat", "weight"),
                           ("usia", "heart"), ("umur", "heart"), ("telur", "egg"), ("anak", "egg"),
                           ("bunting", "egg"), ("hamil", "egg"), ("kecepatan", "bolt"), ("lari", "bolt"),
                           ("selam", "bolt"), ("napas", "bolt"), ("jalan", "bolt")),
               photo="Foto", powered="powered by"),
}

# the front (owner, 2026-11-17: "minimalist but playful ... dont show the real photos on the card for now"), in u
# (1 % of the trim width) from the trim's top-left corner; type sizes in u
FRONT = dict(
    margin=8.0,              # u: sides and top inside the trim (11.8 mm); every block starts on this left edge
    safe=4.2,                # u: nothing readable closer to the trim than this (6.2 mm, over the 5 mm print rule)
    rhythm=2.0,              # u: the spacing unit; gaps between groups are multiples of it
    hero_bottom=86.0, stats=(89.0, 105.0), pair=(107.0, 120.0), band=125.0,   # u from the trim top
    logo=2.2,                # u: the Nilant wordmark's height, top right on the kicker line
    model=(0.92, 0.96),      # the model with its shadow at most this share of the hero band's width, height
    particles=dict(count=12, size=(0.5, 1.5), gap=3.0,        # u; the family's own tints (none near white), mixed
                   shades=("400", "500", "600"),               # shapes
                   shapes=("square", "dot", "ring", "triangle", "plus")),
    # the type scale: ratio 1.25 from 1.6u (6.7 pt, the smallest size on the card)
    size=dict(small=1.6, body=2.0, sub=2.5, value=3.1, title=9.5),
    contrast=dict(body=4.5, large=3.0),   # WCAG: body text and large text (the title, the values)
)
BACK = dict(footer=dict(bottom=6.0, powered=1.7, name=2.5, mark=3.1, gap=0.9, shadow=0.4))


# ---- paths ------------------------------------------------------------------------------------------------------------
def export_id(code, suffix):
    return f"VF-{code}-{suffix}"


def export_file(folder, code, suffix, low=False):
    ext = dict((s, e) for s, e, _ in EXPORT["items"])[suffix]
    d = os.path.join(VL.CACHE, "export-low", code) if low else os.path.join(folder, "export")
    return os.path.join(d, f"{export_id(code, suffix)}.{ext}")


def plates(code, low=False):
    return os.path.join(VL.CACHE, "plates", code, "LOW" if low else "ULTRA")


# ---- the loop ---------------------------------------------------------------------------------------------------------
def loop_gif(frames, out_gif, fps):
    ims = [Image.open(p).convert("RGB").quantize(colors=255, method=Image.Quantize.MEDIANCUT,
                                                 dither=Image.Dither.NONE) for p in frames]
    os.makedirs(os.path.dirname(out_gif), exist_ok=True)
    ims[0].save(out_gif, save_all=True, append_images=ims[1:], duration=round(1000 / fps), loop=0, disposal=1)
    return out_gif


# ---- the card -----------------------------------------------------------------------------------------------------------
def card_px():
    c = EXPORT["card"]
    mm = c["dpi"] / 25.4
    tw, th = c["trim_mm"]
    b = c["bleed_mm"]
    return round((tw + 2 * b) * mm), round((th + 2 * b) * mm), round(b * mm), tw * mm / 100.0


@contextlib.contextmanager
def language(lang):
    """The card system's words (headings, IUCN names, the stat icons' keywords) in one language, restored after."""
    S = IG.S
    keep = dict(headings=dict(S["headings"]), status_names=dict(S["status_names"]), stat_icons=S["stat_icons"])
    L = LANG[lang]
    S["headings"].update(L["headings"])
    S["status_names"].update(L["status"])
    if L.get("stat_icons"):
        S["stat_icons"] = tuple(L["stat_icons"]) + tuple(keep["stat_icons"])
    try:
        yield L
    finally:
        S["headings"].clear()
        S["headings"].update(keep["headings"])
        S["status_names"].clear()
        S["status_names"].update(keep["status_names"])
        S["stat_icons"] = keep["stat_icons"]


def localized(animal, lang):
    """The animal as the card system reads it, its copy in one language (en: as it is; id: animal.json -> i18n.id)."""
    if lang == "en":
        return animal
    t = ((animal.get("i18n") or {}).get(lang)) or {}
    missing = [k for k in ("common", "kicker", "stats", "habitat", "diet", "facts") if not t.get(k)]
    if missing:
        raise ValueError(f"i18n.{lang} is missing {', '.join(missing)} (the card in that language needs them)")
    A = copy.deepcopy(animal)
    A["common"] = t["common"]
    info = A["info"]
    info["kicker"] = t["kicker"]
    info["stats"] = [dict(s, label=l["label"], value=l["value"]) for s, l in zip(info["stats"], t["stats"])]
    info["habitat"] = dict(info["habitat"], text=t["habitat"]) if isinstance(info.get("habitat"), dict) \
        else t["habitat"]
    info["diet"] = dict(info["diet"], text=t["diet"]) if isinstance(info.get("diet"), dict) else t["diet"]
    info["facts"] = [dict(f, text=tx) if isinstance(f, dict) else tx for f, tx in zip(info["facts"], t["facts"])]
    return A


def _cover(im, size, centre=(0.5, 0.5)):
    return ImageOps.fit(ImageOps.exif_transpose(im).convert("RGB"), size, Image.LANCZOS, centering=tuple(centre))


def _shadowed(canvas, cut, x, y, u, spec):
    """Paste a cut-out with a soft shadow under it (the alpha blurred, dropped and darkened)."""
    a = cut.getchannel("A")
    sh = Image.new("RGBA", cut.size, (0, 0, 0, 0))
    sh.putalpha(a.point(lambda v: int(v * spec["alpha"])))
    pad = int(3 * spec["blur"] * u)
    big = Image.new("RGBA", (cut.width + 2 * pad, cut.height + 2 * pad), (0, 0, 0, 0))
    big.paste(sh, (pad, pad))
    big = big.filter(ImageFilter.GaussianBlur(spec["blur"] * u))
    canvas.alpha_composite(big, (int(x - pad), int(y - pad + spec["drop"] * u)))
    canvas.alpha_composite(cut, (int(x), int(y)))


def _text_on_photo(canvas, xy, s, f, fill=(255, 255, 255), shadow=0.6, anchor="rs"):
    """Small white type on a photograph or a pale background, with a soft dark halo so it reads."""
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.text(xy, s, font=f, fill=(0, 0, 0, int(255 * shadow)), anchor=anchor)
    layer = layer.filter(ImageFilter.GaussianBlur(max(1, f.size * 0.12)))
    canvas.alpha_composite(layer)
    ImageDraw.Draw(canvas).text(xy, s, font=f, fill=fill, anchor=anchor)


def _lum(rgb):
    def ch(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb[:3]
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def ink_on(rgb):
    """Black on a light colour, white on a dark one (owner: "if background color light use black colored")."""
    return (17, 17, 17) if _lum(rgb) > 0.18 else (255, 255, 255)


def front(animal, folder, lang, cut_png, master_png=None):
    """The front: the animal's own pastel, its name big, the dynamic model with its rendered shadow among particles,
    then the stats, home and menu in two columns, and the fun fact on a straight-edged band. No photograph."""
    W, H, b, u = card_px()
    A = localized(animal, lang)
    orig_icon = IG.stat_icon                     # a translated stat keeps the icon of its English label
    icons = {loc["label"]: orig_icon(en["label"]) for en, loc in zip(animal["info"]["stats"], A["info"]["stats"])}
    IG.stat_icon = lambda label: icons.get(label) or orig_icon(label)
    try:
        if master_png is None:                    # the dynamic master beside the cut-out (LOW or ULTRA)
            low = os.sep + "LOW" + os.sep in cut_png or "/LOW/" in cut_png
            master_png = export_file(folder, animal["code"], "MASTER-DYN", low)
        return _front(animal, A, lang, cut_png, master_png, W, H, b, u)
    finally:
        IG.stat_icon = orig_icon


def _contrast(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def _front(animal, A, lang, cut_png, master_png, W, H, b, u):
    """Hierarchy: the name, then the model, then the numbers, then the words, then the fun fact as the base of the page.
    One left edge, a 2u spacing rhythm, one type scale, space instead of lines, contrast checked."""
    C, _ = IG.colours(animal["look"])
    Z = FRONT["size"]
    R = FRONT["rhythm"] * u
    tr = ST.TYPE["tracking"]
    X0, X1 = b + FRONT["margin"] * u, W - b - FRONT["margin"] * u
    Y = lambda v: b + v * u  # noqa: E731
    errors = []
    canvas = Image.new("RGBA", (W, H), C["bg"] + (255,))
    d = ImageDraw.Draw(canvas)
    pen = IG.Pen(canvas, u)
    fs_small, fs_body = IG.font("label", Z["small"] * u), IG.font("body", Z["body"] * u)

    def need(fg, bg, kind, what):
        c = _contrast(fg, bg)
        if c < FRONT["contrast"][kind]:
            errors.append(f"{what} reads at {c:.1f}:1 (needs {FRONT['contrast'][kind]}:1)")

    with language(lang) as L:
        info = A["info"]
        # ---- the top line: the kicker on the left, the Nilant wordmark on the right
        y = Y(FRONT["margin"])
        pen.text(X0, y, info.get("kicker", "").upper(), fs_small, C["sci"], tr)
        nl = _nilant(FRONT["logo"] * u, C["bg"])
        canvas.alpha_composite(nl, (int(X1 - nl.width), int(y + 0.5 * fs_small.size - nl.height / 2)))
        need(C["sci"], C["bg"], "body", "the kicker")
        # ---- the name, the scientific name and the IUCN chip
        y += fs_small.size + R
        ft = IG.font("display", Z["title"] * u)
        lines = IG.wrap(A["common"], ft, X1 - X0)
        if len(lines) > 2:
            errors.append(f"common name '{A['common']}' needs {len(lines)} lines")
        for ln in lines:
            if ft.getlength(ln) > X1 - X0:
                errors.append(f"the word '{ln}' is wider than the card")
            pen.text(X0, y, ln, ft, C["title"])
            y += 0.98 * ft.size
        need(C["title"], C["bg"], "large", "the name")
        y += 0.35 * R
        fs = IG.font("italic", Z["sub"] * u)
        pen.italic(X0, y, A["scientific"], fs, C["sci"])
        need(C["sci"], C["bg"], "body", "the scientific name")
        sw = fs.getlength(A["scientific"]) + ST.TYPE["faux_italic_shear"] * fs.size
        chip = IG.status_chip(info.get("conservation"))
        if chip:
            label = chip["label"].upper()
            cw = IG.tracked_width(label, fs_small, tr) + 1.7 * fs_small.size
            if X0 + sw + R + cw <= X1:
                pen.pill(X0 + sw + R, y + 0.5 * fs.size - fs_small.size, label, fs_small, chip["fill"], chip["text"], tr)
                y += max(fs.size, 2 * fs_small.size)
            else:
                y += fs.size + 0.5 * R
                pen.pill(X0, y, label, fs_small, chip["fill"], chip["text"], tr)
                y += 2 * fs_small.size
        else:
            y += fs.size
        # ---- the hero: the model with its own rendered shadow (read from the dynamic master, which is composited on
        # this very background colour: shadow = master / background), particles in the family's tints around it
        zy0, zy1 = y + 1.5 * R, Y(FRONT["hero_bottom"])
        if zy1 - zy0 < 32 * u:
            errors.append(f"the title block leaves only {(zy1 - zy0) / u:.0f}u for the model")
        import numpy as np
        cut = Image.open(cut_png).convert("RGBA")
        master = Image.open(master_png).convert("RGB")
        if master.size != cut.size:
            master = master.resize(cut.size, Image.LANCZOS)
        A = np.asarray(cut.getchannel("A"), dtype=np.float32) / 255.0
        bgv = np.array(C["bg"], dtype=np.float32)
        f = np.clip(np.asarray(master, dtype=np.float32) / np.maximum(bgv, 1.0), 0.0, 1.0)
        # where the animal covers the master its colour hides the ground: there (and in a thin ring around it, where
        # the edge pixels mix both) take the darkest ground value nearby, so the shadow runs on under the feet
        ring = np.asarray(cut.getchannel("A").filter(ImageFilter.MaxFilter(5)), dtype=np.float32) > 0
        g = f.copy()
        g[ring] = 1.0
        near = np.stack([np.asarray(Image.fromarray((g[..., i] * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(9)),
                                    dtype=np.float32) / 255.0 for i in range(3)], axis=2)
        f[ring] = near[ring]
        dark = (f.min(axis=2) < 0.985) | (A > 0)
        ys, xs = np.nonzero(dark)
        bx0, by0, bx1, by1 = xs.min(), ys.min(), xs.max() + 1, ys.max() + 1
        # the animal's own middle sits on the card's middle (the shadow trails off to its side); the scale keeps the
        # wider half (animal middle to the far end of the animal or its shadow) inside the half-width
        axs = np.nonzero((A > 0).any(axis=0))[0]
        acx = (axs.min() + axs.max() + 1) / 2
        mw, mh = FRONT["model"]
        half = max(acx - bx0, bx1 - acx)
        k = min(mw * (X1 - X0) / 2 / half, mh * (zy1 - zy0) / (by1 - by0))
        size = (max(1, round((bx1 - bx0) * k)), max(1, round((by1 - by0) * k)))
        cut = cut.crop((bx0, by0, bx1, by1)).resize(size, Image.LANCZOS)
        fimg = Image.fromarray((f[by0:by1, bx0:bx1] * 255).astype(np.uint8), "RGB").resize(size, Image.LANCZOS)
        ox, oy = int((X0 + X1) / 2 - (acx - bx0) * k), int((zy0 + zy1 - size[1]) / 2)
        # particles first (so the shadow falls on them): many small shapes in the family's own tints, never on the
        # animal, placed with a little room between them
        rnd = __import__("random").Random(animal["code"] + lang)
        fam = IG._token_of(animal["look"]["background"]).rsplit("-", 1)[0]
        tints = [VL.rgb(IG._mute(f"{fam}-{s}")) for s in FRONT["particles"]["shades"] if f"{fam}-{s}" in VL.PALETTE]
        occ = np.asarray(cut.getchannel("A").filter(ImageFilter.MaxFilter(9)), dtype=np.uint8) > 0
        placed = []
        P = FRONT["particles"]
        tries = 0
        while len(placed) < P["count"] and tries < 4000:
            tries += 1
            s = rnd.uniform(*P["size"]) * u
            qx, qy = rnd.uniform(X0 + s, X1 - s), rnd.uniform(zy0 + s, zy1 - s)
            lx, ly = int(qx - ox), int(qy - oy)
            if 0 <= lx < size[0] and 0 <= ly < size[1]:
                x0_, y0_ = max(0, int(lx - s)), max(0, int(ly - s))
                if occ[y0_:int(ly + s) + 1, x0_:int(lx + s) + 1].any():
                    continue
            if any((qx - px) ** 2 + (qy - py) ** 2 < (P["gap"] * u + s + ps) ** 2 for px, py, ps in placed):
                continue
            placed.append((qx, qy, s))
            col = rnd.choice(tints)
            shape = rnd.choice(P["shapes"])
            rot = rnd.uniform(0, math.pi)
            if shape == "square":
                d.polygon([(qx + s * math.cos(rot + q * math.pi / 2), qy + s * math.sin(rot + q * math.pi / 2))
                           for q in range(4)], fill=col)
            elif shape == "dot":
                d.ellipse((qx - s * 0.8, qy - s * 0.8, qx + s * 0.8, qy + s * 0.8), fill=col)
            elif shape == "ring":
                d.ellipse((qx - s, qy - s, qx + s, qy + s), outline=col, width=max(2, round(0.35 * s)))
            elif shape == "triangle":
                d.polygon([(qx + s * math.cos(rot + q * 2 * math.pi / 3), qy + s * math.sin(rot + q * 2 * math.pi / 3))
                           for q in range(3)], fill=col)
            elif shape == "plus":
                w2 = 0.3 * s
                for ang in (rot, rot + math.pi / 2):
                    dx, dy = math.cos(ang), math.sin(ang)
                    nx, ny = -dy * w2, dx * w2
                    d.polygon([(qx - dx * s + nx, qy - dy * s + ny), (qx + dx * s + nx, qy + dy * s + ny),
                               (qx + dx * s - nx, qy + dy * s - ny), (qx - dx * s - nx, qy - dy * s - ny)], fill=col)
        # the shadow: multiply the card by the master's shadow factor, then the animal on top
        region = canvas.crop((ox, oy, ox + size[0], oy + size[1])).convert("RGB")
        reg = np.asarray(region, dtype=np.float32) * (np.asarray(fimg, dtype=np.float32) / 255.0)
        canvas.paste(Image.fromarray(np.clip(reg, 0, 255).astype(np.uint8), "RGB"), (ox, oy))
        canvas.alpha_composite(cut, (ox, oy))
        d = ImageDraw.Draw(canvas)
        pen = IG.Pen(canvas, u)
        # ---- the numbers: two by two, a pixel icon badge, the label over the big value; space, not boxes
        items = [(s["label"], s["value"]) for s in info.get("stats", []) if s.get("value")][:4]
        sy0, sy1 = Y(FRONT["stats"][0]), Y(FRONT["stats"][1])
        fv = IG.font("value", Z["value"] * u)
        colw, rowh = (X1 - X0) / 2, (sy1 - sy0) / 2
        bs = fs_small.size + 0.45 * fs_small.size + fv.size
        for i, (label, value) in enumerate(items):
            x, yy = X0 + (i % 2) * colw, sy0 + (i // 2) * rowh + (rowh - bs) / 2
            pen.badge(x, yy, bs, IG.stat_icon(label), C["badge"], C["icon"])
            tx = x + bs + 0.6 * R
            if IG.tracked_width(label.upper(), fs_small, tr) > x + colw - tx - R / 2 or \
                    fv.getlength(value) > x + colw - tx - R / 2:
                errors.append(f"stat '{label}: {value}' is wider than its column")
            pen.text(tx, yy, label.upper(), fs_small, C["sci"], tr)
            pen.text(tx, yy + 1.45 * fs_small.size, value, fv, C["title"])
        # ---- the words: home and menu in two columns on the same left edges as the numbers
        py0, py1 = Y(FRONT["pair"][0]), Y(FRONT["pair"][1])
        lead = ST.TYPE["leading"] * fs_body.size
        for j, kind in enumerate(("habitat", "diet")):
            x = X0 + j * colw
            w = colw - (R if j == 0 else 0)
            pen.text(x, py0, IG.S["headings"][kind].upper(), fs_small, C["sci"], tr)
            yy = py0 + fs_small.size + 0.6 * R
            body = IG.wrap(IG._text(info.get(kind)), fs_body, w)
            for ln in body:
                pen.text(x, yy, ln, fs_body, C["body"])
                yy += lead
            if yy - lead + fs_body.size > py1 + 0.2 * u:
                errors.append(f"'{IG.S['headings'][kind]}' needs {len(body)} lines (shorten info.{kind})")
        need(C["body"], C["bg"], "body", "the body text")
        # ---- the base: the fun fact on a full-bleed band with a straight top edge
        top = Y(FRONT["band"])
        d.rectangle((0, round(top), W, H), fill=C["fact"])
        facts = [IG._text(f) for f in info.get("facts", []) if IG._text(f)]
        ff = IG.font("fact", Z["body"] * u)
        yy = top + 1.5 * R
        pen.text(X0, yy, IG.S["headings"]["fact"].upper(), fs_small, C["fact_head"], tr)
        yy += fs_small.size + 0.6 * R
        lead_f = ST.TYPE["leading"] * ff.size
        lines = IG.wrap(facts[0] if facts else "", ff, X1 - X0)
        for ln in lines:
            pen.text(X0, yy, ln, ff, C["fact_text"])
            yy += lead_f
        if yy - lead_f + ff.size > H - b - FRONT["safe"] * u:
            errors.append(f"'{IG.S['headings']['fact']}' needs {len(lines)} lines (shorten info.facts[0])")
        need(C["fact_text"], C["fact"], "body", "the fun fact")
    return canvas.convert("RGB"), errors


def _nilant(height_px, bg):
    """The Nilant wordmark alone ("nilant", no head; owner 2026-11-17), the dark-type version on a light background,
    the white on a dark one, trimmed to its ink and scaled with the aspect ratio locked."""
    import fitz
    name = "nilant-wordmark-on-light.svg" if ink_on(bg) != (255, 255, 255) else "nilant-wordmark-on-dark.svg"
    page = fitz.open(os.path.join(VL.DESIGN, "Logo", name))[0]
    z = 4 * height_px / page.rect.height
    pm = page.get_pixmap(matrix=fitz.Matrix(z, z), alpha=True)
    im = Image.open(io.BytesIO(pm.tobytes("png"))).convert("RGBA")
    im = im.crop(im.getchannel("A").getbbox())
    h = max(1, round(height_px))
    return im.resize((max(1, round(im.width * h / im.height)), h), Image.LANCZOS)


def _logo(height_px):
    import fitz
    doc = fitz.open(LOGO)
    page = doc[0]
    z = height_px / page.rect.height
    pm = page.get_pixmap(matrix=fitz.Matrix(z, z), alpha=True)
    return Image.open(io.BytesIO(pm.tobytes("png"))).convert("RGBA")


def back(animal, lang, master_block_png):
    """The back: the regular blocky master cropped to the card, "powered by" + the ihdyo mark + "ihdyo" at the
    bottom in black or white, whichever the background asks for."""
    W, H, b, u = card_px()
    with Image.open(master_block_png) as im:
        im = im.convert("RGB")
        cw = round(im.height * W / H)
        x = (im.width - cw) // 2
        canvas = im.crop((x, 0, x + cw, im.height)).resize((W, H), Image.LANCZOS).convert("RGBA")
    F = BACK["footer"]
    L = LANG[lang]
    fp, fn = IG.font("body", F["powered"] * u), IG.font("heading", F["name"] * u)
    mark = _logo(F["mark"] * u)
    gap = F["gap"] * u
    tw_p, tw_n = fp.getlength(L["powered"]), fn.getlength("ihdyo")
    total = tw_p + gap + mark.width + gap * 0.6 + tw_n
    x = (W - total) / 2
    base = H - b - F["bottom"] * u
    # the ink follows the background (owner, 2026-11-17): black on a light pastel, white on a dark one
    ink = ink_on(canvas.getpixel((W // 2, int(base - 4 * u)))[:3])
    mx = x + tw_p + gap
    my = base - mark.height + 0.12 * mark.height
    tinted = Image.new("RGBA", mark.size, ink + (255,))
    tinted.putalpha(mark.getchannel("A"))
    d = ImageDraw.Draw(canvas)
    d.text((x, base), L["powered"], font=fp, fill=ink, anchor="ls")
    canvas.alpha_composite(tinted, (int(mx), int(my)))
    d.text((mx + mark.width + gap * 0.6, base), "ihdyo", font=fn, fill=ink, anchor="ls")
    return canvas.convert("RGB")


def card_pdf(animal, folder, lang, cut_dyn, master_block, out_pdf, strict=True):
    """The A5 card in one language: page 1 the front, page 2 the back; trim box = A5, bleed box = the page."""
    import fitz
    f, errors = front(animal, folder, lang, cut_dyn)
    if errors and strict:
        raise IG.Overflow(f"card {lang}: " + "; ".join(errors))
    bk = back(animal, lang, master_block)
    c = EXPORT["card"]
    pt = 72 / 25.4
    tw, th = c["trim_mm"]
    bl = c["bleed_mm"]
    Wp, Hp = (tw + 2 * bl) * pt, (th + 2 * bl) * pt
    doc = fitz.open()
    for im in (f, bk):
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=94, subsampling=0, dpi=(c["dpi"], c["dpi"]))
        page = doc.new_page(width=Wp, height=Hp)
        page.insert_image(page.rect, stream=buf.getvalue())
        try:
            page.set_bleedbox(page.rect)
            page.set_trimbox(fitz.Rect(bl * pt, bl * pt, Wp - bl * pt, Hp - bl * pt))
        except Exception:
            pass
    doc.set_metadata(dict(title=f"{animal['common']} · Voxel Fauna card ({lang.upper()})", author="ihdyo",
                          subject=f"{animal['code']} · {animal['scientific']}", creator="Voxel Fauna package.py"))
    os.makedirs(os.path.dirname(out_pdf), exist_ok=True)
    doc.save(out_pdf, garbage=3, deflate=True)
    previews = []
    for side, im in (("front", f), ("back", bk)):
        p = os.path.splitext(out_pdf)[0] + f".{side}.jpg"
        if os.path.dirname(p).endswith("export"):            # previews of the pages live in the cache, not in export/
            p = os.path.join(VL.CACHE, "preview", animal["code"], "card", os.path.basename(p))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        im.resize((im.width // 2, im.height // 2), Image.LANCZOS).save(p, quality=88)
        previews.append(p)
    return dict(pdf=out_pdf, errors=errors, previews=previews)


# ---- one animal ---------------------------------------------------------------------------------------------------------
def package(folder, animal, low=False, strict=True):
    """Everything offline for one animal, from its renders: the GIF and the two cards (the stock JPEG: stock.py)."""
    code = animal["code"]
    pl = plates(code, low)
    mdyn, mblock = export_file(folder, code, "MASTER-DYN", low), export_file(folder, code, "MASTER-BLOCK", low)
    cut_dyn = os.path.join(pl, "cut-dyn.png")
    missing = [p for p in (mdyn, mblock, cut_dyn) if not os.path.exists(p)]
    if missing:
        raise SystemExit(f"{code}: render first (vf.py final {code}{' --low' if low else ''}): missing "
                         + ", ".join(VL.rel(p) for p in missing))
    out = {}
    frames = sorted(os.path.join(pl, "loop", f) for f in os.listdir(os.path.join(pl, "loop")) if f.endswith(".png")) \
        if os.path.isdir(os.path.join(pl, "loop")) else []
    if not frames:
        raise SystemExit(f"{code}: no loop frames in {VL.rel(os.path.join(pl, 'loop'))} (vf.py final {code})")
    out["loop"] = loop_gif(frames, export_file(folder, code, "LOOP", low), ST.MOTION["fps"])
    out["cards"] = {lang: card_pdf(animal, folder, lang, cut_dyn, mblock,
                                   export_file(folder, code, f"CARD-{lang.upper()}", low), strict)
                    for lang in ("en", "id")}
    return out
