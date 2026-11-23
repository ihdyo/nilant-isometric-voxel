"""Voxel Fauna · the render menu's cover: a pixel-art fox, the title in block letters, a few floating voxels.

    cover(color=True, block="█", width=80)  ->  [lines]   (ANSI true colour when `color`, plain blocks when not)
    mini(color=True, block="█")             ->  [lines]   (three rows: a small cube strip for the corner of a panel)

Pure text: no Blender, no Pillow. The fox is the collection's first animal (26-001 Red Fox in the fox card's colours).
"""
import re

FOX = (
    "KK............KK",
    "KOO..........OOK",
    ".OOOOOOOOOOOOOO.",
    ".OOOOOOOOOOOOOO.",
    ".OOKOOOOOOOOKOO.",
    ".OOOOOOOOOOOOOO.",
    ".WOOOOOOOOOOOOW.",
    "..WWOOOOOOOOWW..",
    "...WWWWWWWWWW...",
    "....WWWKKWWW....",
    ".....WWWWWW.....",
    "......WWWW......",
    "..SSSSSSSSSSSS..",
)
FOX_COLOURS = {"K": (46, 34, 38), "O": (248, 112, 48), "W": (246, 236, 222), "S": (60, 70, 82)}

FONT = {
    "V": ("X...X", "X...X", "X...X", ".X.X.", "..X.."),
    "O": (".XXX.", "X...X", "X...X", "X...X", ".XXX."),
    "X": ("X...X", ".X.X.", "..X..", ".X.X.", "X...X"),
    "E": ("XXXXX", "X....", "XXXX.", "X....", "XXXXX"),
    "L": ("X....", "X....", "X....", "X....", "XXXXX"),
    "F": ("XXXXX", "X....", "XXXX.", "X....", "X...."),
    "A": (".XXX.", "X...X", "XXXXX", "X...X", "X...X"),
    "U": ("X...X", "X...X", "X...X", "X...X", ".XXX."),
    "N": ("X...X", "XX..X", "X.X.X", "X..XX", "X...X"),
}
SPARKS = (            # (row, column in cells from the fox's left edge, colour): voxels floating around the fox
    (1, -6, (94, 234, 212)), (3, -9, (45, 212, 191)), (6, -5, (153, 246, 228)), (9, -8, (94, 234, 212)),
    (0, 19, (45, 212, 191)), (2, 22, (153, 246, 228)), (5, 20, (94, 234, 212)), (8, 24, (45, 212, 191)),
    (11, 21, (153, 246, 228)),
)


def _fg(rgb):
    return f"\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"


def _mix(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _paint(text, rgb, color):
    return f"{_fg(rgb)}{text}\x1b[0m" if color and text.strip() else text


def _plain(s):
    return re.sub(r"\x1b\[[0-9;]*m", "", s)


def _center(line, width):
    return " " * max(0, (width - len(_plain(line))) // 2) + line


def title_rows(word, c0, c1, color, block="█", px=2, gap=2):
    """The word in 5-row block letters (each cell `px` blocks wide), the colour running from c0 (top) to c1 (bottom)."""
    rows = []
    for r in range(5):
        cells = (" " * gap).join("".join(block * px if ch == "X" else " " * px for ch in FONT[letter][r])
                                 for letter in word)
        rows.append(_paint(cells, _mix(c0, c1, r / 4), color))
    return rows


def fox_rows(color, block="█"):
    rows = []
    for r, line in enumerate(FOX):
        row = []
        for col, ch in enumerate(line):
            row.append(_paint(block * 2, FOX_COLOURS[ch], color) if ch in FOX_COLOURS else "  ")
        rows.append("".join(row))
    return rows


def cover(color=True, block="█", width=80):
    """The whole cover as a list of lines, centred in `width` columns."""
    fox_w = len(FOX[0]) * 2
    left = (width - fox_w) // 2
    lines = []
    for r, line in enumerate(FOX):                             # the fox, with sparks floating around it
        cells = [(left + i * 2, _paint(block * 2, FOX_COLOURS[ch], color), 2) for i, ch in enumerate(line)
                 if ch in FOX_COLOURS]
        cells += [(left + sc * 2, _paint(block, rgb, color), 1) for sr, sc, rgb in SPARKS
                  if sr == r and 0 <= left + sc * 2 < width - 2]
        out, pos = "", 0
        for x, s, w in sorted(cells, key=lambda c: c[0]):
            out += " " * max(0, x - pos) + s
            pos = x + w
        lines.append(out)
    lines.append("")
    lines += [_center(r, width) for r in title_rows("VOXEL", (255, 160, 60), (248, 100, 40), color, block)]
    lines.append("")
    lines += [_center(r, width) for r in title_rows("FAUNA", (94, 234, 212), (20, 160, 150), color, block)]
    lines.append("")
    tag = "isometric voxel animals · built, rigged and animated in Blender · offline"
    by = "a Nilant side collection · powered by ihdyo"
    lines.append(_center(_paint(tag, (160, 168, 180), color), width))
    lines.append(_center(_paint(by, (110, 118, 130), color), width))
    return lines


def mini(color=True, block="█"):
    """A three-row strip of little cubes in the cover's colours (a corner decoration)."""
    cols = [(248, 112, 48), (255, 160, 60), (246, 236, 222), (94, 234, 212), (45, 212, 191), (46, 34, 38)]
    rows = []
    for r in range(3):
        rows.append("".join(_paint(block * 2, cols[(i + r) % len(cols)], color) for i in range(len(cols))))
    return rows
