"""Voxel Fauna · the information artwork composer (Pillow), Duolingo-style card system.

A plate is an INF render: the animal already placed in its zone on the flat background (vf_scene.render). This module
lays the cards around it, following vf_standards.INFO_LAYOUTS / INFO_STYLE:

  header   a kicker pill, the common name (up to two lines), the scientific name in italics, the IUCN status chip
  photo    a real photograph of the species in a white framed card, cropped to fill, with its credit underneath
  stats    white tiles with a darker lip: a coloured label over a big value
  cards    "Home turf" and "On the menu" on white cards, "Fun fact!" on a full-colour card with white type

Every colour is a Tailwind token derived from the background's own family (sky-200 -> sky-950 title, sky-700 labels,
sky-400 lips, sky-700 fun-fact card), checked for contrast (vf_standards.INK_RULE). Type never shrinks: too much text
raises Overflow naming the field to shorten.
"""
import os
import re

from PIL import Image, ImageDraw, ImageFont, ImageOps

import vflib as VL

ST = VL.ST
S = ST.INFO_STYLE
SHADES = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]


class Overflow(ValueError):
    pass


def _text(v):
    return (v.get("text", "") if isinstance(v, dict) else v) or ""


# ---- colour ---------------------------------------------------------------------------------------------------------
def _shift(token, steps):
    fam, sh = token.rsplit("-", 1)
    i = min(len(SHADES) - 1, max(0, SHADES.index(sh) + steps // 100 if sh in SHADES else 5))
    return f"{fam}-{SHADES[i]}"


def _first(fam, start, on, need, fallback="stone-950"):
    for s in SHADES[SHADES.index(start):]:
        t = f"{fam}-{s}"
        if t in VL.PALETTE and VL.contrast(t, on) >= need:
            return t
    return fallback


def colours(look):
    """Every colour of the artwork as tokens (checked) and RGB."""
    bg = look["background"]
    fam = bg.rsplit("-", 1)[0]
    R = ST.INK_RULE
    card = S["card"]
    fact = _first(fam, S["fact_shade"], "white", R["min_label_contrast"])
    t = dict(
        bg=bg, card=card, lip=_shift(bg, S["lip_steps"]),
        title=_first(fam, "950", bg, R["min_body_contrast"]),                 # on the background
        sci=_first(fam, "800", bg, R["min_label_contrast"]),
        credit=_first(fam, "800", bg, R["min_label_contrast"]),
        pill=_first(fam, "900", "white", R["min_body_contrast"]), pill_text="white",
        label=look.get("accent") or _first(fam, "700", card, R["min_label_contrast"]),   # on white cards
        value=_first(fam, "950", card, R["min_body_contrast"]),
        body=_first(fam, "900", card, R["min_body_contrast"]),
        fact=fact, fact_lip=_shift(fact, 200), fact_text="white", fact_head=_shift(bg, -100),
        photo_lip=_shift(bg, S["lip_steps"]),
    )
    if VL.contrast(t["label"], card) < R["min_label_contrast"]:
        raise ValueError(f"look.accent {t['label']} reads at {VL.contrast(t['label'], card):.1f}:1 on white cards")
    return {k: VL.rgb(v) for k, v in t.items()}, t


def status_chip(cons):
    code = (cons or {}).get("code") or ""
    if code not in S["status"]:
        return None
    fill = S["status"][code]
    text = "white" if VL.contrast("white", fill) >= 3.0 else "stone-950"
    return dict(label=f"IUCN · {S['status_names'][code]}", fill=VL.rgb(fill), text=VL.rgb(text), token=fill)


# ---- type -----------------------------------------------------------------------------------------------------------
_FONTS = {}


def font(role, px):
    name = ST.TYPE.get(role, role)
    path = os.path.join(VL.FONTS, name)
    if role == "italic" and not os.path.exists(path):
        path = os.path.join(VL.FONTS, ST.TYPE["italic_fallback"])
    key = (path, max(1, int(px)))
    if key not in _FONTS:
        _FONTS[key] = ImageFont.truetype(path, key[1])
    return _FONTS[key]


def faux_italic():
    return not os.path.exists(os.path.join(VL.FONTS, ST.TYPE["italic"]))


def tracked_width(text, f, tracking):
    return sum(f.getlength(c) for c in text) + tracking * f.size * max(len(text) - 1, 0)


def wrap(text, f, width):
    """Greedy wrap on plain spaces; a number stays with the word after it ("1 kg", "65 days")."""
    text = re.sub(r"(\d) (?=[A-Za-z°%])", "\\1\u00a0", text)
    words, lines, cur = [w for w in text.split(" ") if w], [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if f.getlength(trial) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


class Pen:
    """Draws into the canvas, or only measures when canvas is None. A line box is one em tall: the top of the tallest
    lowercase ascender (ASC em above the baseline) down to the descenders."""
    ASC = 0.74

    def __init__(self, canvas, u):
        self.c = canvas
        self.d = ImageDraw.Draw(canvas) if canvas is not None else None
        self.u = u
        self.errors = []

    def text(self, x, top, s, f, fill, tracking=0.0, baseline=None):
        by = baseline if baseline is not None else top + self.ASC * f.size
        if self.d is not None:
            if tracking:
                cx = x
                for ch in s:
                    self.d.text((cx, by), ch, font=f, fill=fill, anchor="ls")
                    cx += f.getlength(ch) + tracking * f.size
            else:
                self.d.text((x, by), s, font=f, fill=fill, anchor="ls")
        return f.size

    def italic(self, x, top, s, f, fill):
        if not faux_italic():
            return self.text(x, top, s, f, fill)
        if self.c is not None:
            h = int(1.1 * f.size) + 2
            w = int(f.getlength(s)) + 4
            sh = ST.TYPE["faux_italic_shear"]
            mask = Image.new("L", (w, h), 0)
            ImageDraw.Draw(mask).text((0, self.ASC * f.size), s, font=f, fill=255, anchor="ls")
            mask = mask.transform((int(w + sh * h) + 2, h), Image.AFFINE, (1, sh, -sh * h, 0, 1, 0),
                                  resample=Image.BICUBIC)
            self.c.paste(Image.new("RGB", mask.size, fill), (int(x), int(top)), mask)
        return f.size

    def pill(self, x, top, s, f, fill, text_fill, tracking):
        padx = 0.85 * f.size
        w = tracked_width(s, f, tracking) + 2 * padx
        h = 2.0 * f.size
        if self.d is not None:
            self.d.rounded_rectangle((x, top, x + w, top + h), radius=h / 2, fill=fill)
            self.text(x + padx, top, s, f, text_fill, tracking, baseline=top + h / 2 + 0.35 * f.size)
        return w, h

    def card(self, box, fill, lip):
        """A rounded card with its lip below; returns the inner box (padding applied)."""
        x0, y0, x1, y1 = box
        u = self.u
        lh = S["lip"] * u
        if self.d is not None:
            r = S["radius"] * u
            self.d.rounded_rectangle((x0, y0 + lh, x1, y1), radius=r, fill=lip)
            self.d.rounded_rectangle((x0, y0, x1, y1 - lh), radius=r, fill=fill)
        p = S["pad"] * u
        return x0 + p, y0 + p, x1 - p, y1 - lh - p


# ---- blocks ---------------------------------------------------------------------------------------------------------
def _px(box, W, H):
    return box[0] * W, box[1] * H, box[2] * W, box[3] * H


def header(pen, box, A, Z, C):
    u, tr = pen.u, ST.TYPE["tracking"]
    x0, y0, x1, y1 = box
    width = x1 - x0
    y = y0
    kicker = A["info"].get("kicker", "")
    if kicker:
        fk = font("label", Z["kicker"] * u)
        w, h = pen.pill(x0, y, kicker.upper(), fk, C["pill"], C["pill_text"], tr)
        if w > width:
            pen.errors.append(f"kicker '{kicker}' is wider than the header")
        y += h + 0.9 * Z["kicker"] * u
    ft = font("display", Z["title"] * u)
    lines = wrap(A["common"], ft, width)
    if len(lines) > 2:
        pen.errors.append(f"common name '{A['common']}' needs {len(lines)} lines")
    for i, ln in enumerate(lines):
        if i:
            y += 0.02 * ft.size
        if ft.getlength(ln) > width:
            pen.errors.append(f"the word '{ln}' is wider than the header")
        y += pen.text(x0, y, ln, ft, C["title"])
    y += 0.5 * Z["sci"] * u
    fs = font("italic", Z["sci"] * u)
    sw = fs.getlength(A["scientific"]) + ST.TYPE["faux_italic_shear"] * fs.size
    chip = status_chip(A["info"].get("conservation"))
    fc = font("label", Z["chip"] * u)
    cw = tracked_width(chip["label"].upper(), fc, tr) + 1.7 * fc.size if chip else 0
    if sw > width:
        pen.errors.append(f"scientific name '{A['scientific']}' is wider than the header")
    pen.italic(x0, y, A["scientific"], fs, C["sci"])
    if chip:
        if sw + 1.2 * u + cw <= width:                     # chip on the same line, centred on the name
            cy = y + 0.5 * fs.size - fc.size
            pen.pill(x0 + sw + 1.2 * u, cy, chip["label"].upper(), fc, chip["fill"], chip["text"], tr)
            y += max(fs.size, 2 * fc.size)
        else:
            y += fs.size + 0.6 * Z["chip"] * u
            pen.pill(x0, y, chip["label"].upper(), fc, chip["fill"], chip["text"], tr)
            y += 2 * fc.size
    else:
        y += fs.size
    if y > y1:
        pen.errors.append(f"header needs {(y - y0) / u:.1f}u of {(y1 - y0) / u:.1f}u")


def photo(pen, box, A, Z, C, folder):
    u = pen.u
    x0, y0, x1, y1 = box
    ph = (A["info"].get("photo") or {})
    fc = font("body", Z["credit"] * u)
    credit_h = 1.6 * fc.size
    card = (x0, y0, x1, y1 - credit_h)
    pen.card(card, C["card"], C["photo_lip"])
    fr = S["photo_frame"] * u
    ix0, iy0, ix1, iy1 = x0 + fr, y0 + fr, x1 - fr, card[3] - S["lip"] * u - fr
    path = os.path.join(folder, ph["file"]) if (folder and ph.get("file")) else None
    if path and os.path.exists(path):
        if pen.c is not None:
            with Image.open(path) as im:
                im = ImageOps.exif_transpose(im).convert("RGB")
                if ph.get("crop"):
                    cx0, cy0, cx1, cy1 = ph["crop"]
                    im = im.crop((cx0 * im.width, cy0 * im.height, cx1 * im.width, cy1 * im.height))
                w, h = int(ix1 - ix0), int(iy1 - iy0)
                im = ImageOps.fit(im, (w, h), Image.LANCZOS, centering=tuple(ph.get("centre", (0.5, 0.5))))
                mask = Image.new("L", (w, h), 0)
                ImageDraw.Draw(mask).rounded_rectangle((0, 0, w - 1, h - 1), radius=(S["radius"] - 0.5) * u, fill=255)
                pen.c.paste(im, (int(ix0), int(iy0)), mask)
        credit = f"Photo: {ph.get('author', '?')} · {ph.get('licence', '?')}"
        cw = fc.getlength(credit)                         # right-aligned under the card; may run left of it a little
        if cw > (x1 - x0) * 1.35:
            pen.errors.append(f"photo credit '{credit}' is too long (shorten info.photo.author)")
        pen.text(x1 - cw, card[3] + 0.4 * fc.size, credit, fc, C["credit"])
        lic = ph.get("licence", "")
        if not any(lic.startswith(ok) for ok in S["photo_licences"]):
            pen.errors.append(f"photo licence '{lic}' is not allowed on a sold image (allowed: {', '.join(S['photo_licences'])})")
    else:
        if pen.d is not None:
            pen.d.rounded_rectangle((ix0, iy0, ix1, iy1), radius=(S["radius"] - 0.5) * u, fill=C["lip"])
            fp = font("label", Z["credit"] * 1.6 * u)
            pen.text(ix0 + 1.2 * u, iy0 + 1.2 * u, "PHOTO", fp, C["card"], ST.TYPE["tracking"])
        if A["code"] != "00-000":
            pen.errors.append("no photo: set info.photo.file (a real photograph in assets/photos/)")


def stats(pen, box, A, Z, C, cols):
    u, tr = pen.u, ST.TYPE["tracking"]
    items = [(s["label"], s["value"]) for s in A["info"].get("stats", []) if s.get("value")][:ST.INFO_LIMITS["stats"]]
    if not items:
        return
    x0, y0, x1, y1 = box
    gap = 1.6 * u
    rows = (len(items) + cols - 1) // cols
    tw = (x1 - x0 - gap * (cols - 1)) / cols
    th = (y1 - y0 - gap * (rows - 1)) / rows
    fl, fv = font("label", Z["label"] * u), font("value", Z["value"] * u)
    for i, (label, value) in enumerate(items):
        c, r = i % cols, i // cols
        bx = x0 + c * (tw + gap)
        by = y0 + r * (th + gap)
        ix0, iy0, ix1, iy1 = pen.card((bx, by, bx + tw, by + th), C["card"], C["lip"])
        need = fl.size + 0.55 * fl.size + fv.size
        top = iy0 + max(0, (iy1 - iy0 - need) / 2)
        if tracked_width(label.upper(), fl, tr) > ix1 - ix0:
            pen.errors.append(f"stat label '{label}' is wider than its tile")
        if fv.getlength(value) > ix1 - ix0:
            pen.errors.append(f"stat value '{value}' is wider than its tile")
        if need > iy1 - iy0:
            pen.errors.append(f"stat tiles are too short for '{label}'")
        pen.text(ix0, top, label.upper(), fl, C["label"], tr)
        pen.text(ix0, top + 1.55 * fl.size, value, fv, C["value"])


def card(pen, kind, box, A, Z, C):
    u, tr = pen.u, ST.TYPE["tracking"]
    info = A["info"]
    if kind == "fact":
        facts = [_text(f) for f in info.get("facts", []) if _text(f)]
        text = facts[0] if facts else ""
        fill, lip, head_c, body_c, fb = C["fact"], C["fact_lip"], C["fact_head"], C["fact_text"], font("fact", Z["fact"] * u)
    else:
        text = _text(info.get(kind))
        fill, lip, head_c, body_c, fb = C["card"], C["lip"], C["label"], C["body"], font("body", Z["body"] * u)
    ix0, iy0, ix1, iy1 = pen.card(box, fill, lip)
    fh = font("heading", Z["heading"] * u)
    y = iy0
    y += pen.text(ix0, y, S["headings"][kind].upper(), fh, head_c, tr)
    y += 0.6 * fh.size
    lines = wrap(text, fb, ix1 - ix0)
    lead = ST.TYPE["leading"] * fb.size
    for i, ln in enumerate(lines):
        pen.text(ix0, y, ln, fb, body_c)
        y += lead if i < len(lines) - 1 else fb.size
    if y > iy1 + 0.2 * u:
        pen.errors.append(f"'{S['headings'][kind]}' card: the text needs {(y - iy0) / u:.1f}u of {(iy1 - iy0) / u:.1f}u "
                          f"({len(text)} characters; shorten info.{'facts[0]' if kind == 'fact' else kind})")


# ---- the composer ---------------------------------------------------------------------------------------------------
def compose(plate_path, out_path, animal, ratio, measure_only=False, strict=True, folder=None):
    """Lay the cards of one information artwork on its plate. Returns a report; raises Overflow (strict) when a text
    does not fit or the photo is missing or not allowed."""
    L = ST.INFO_LAYOUTS[ratio]
    img = Image.open(plate_path).convert("RGB")
    W, H = img.size
    u = min(W, H) / 100.0
    Z = L["size"]
    C, tokens = colours(animal["look"])
    pen = Pen(None if measure_only else img, u)
    header(pen, _px(L["header"], W, H), animal, Z, C)
    photo(pen, _px(L["photo"], W, H), animal, Z, C, folder)
    stats(pen, _px(L["stats"], W, H), animal, Z, C, L["stats_cols"])
    for kind, box in L["cards"]:
        card(pen, kind, _px(box, W, H), animal, Z, C)
    report = dict(ratio=ratio, size=(W, H), colours=tokens, faux_italic=faux_italic(), errors=list(pen.errors))
    if pen.errors and strict:
        raise Overflow(f"{ratio}: " + "; ".join(pen.errors))
    if not measure_only:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        img.save(out_path, optimize=True, dpi=(300, 300))
    return report
