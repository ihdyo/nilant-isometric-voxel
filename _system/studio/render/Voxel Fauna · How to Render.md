# Voxel Fauna · How to render

`render.bat` (this folder) is the one-stop renderer, ported from Nilant's: **double-click it**. It works offline (no
internet, no Claude). Blender builds and renders; Python (with Pillow and openpyxl) lays the information cards.

- **Blender:** it uses the path remembered in `..\blender_path.txt`, else the `BLENDER` environment variable, else the
  first `blender.exe` it finds (the regular Blender 5.3.0 install on the owner's PC). Delete the text file to choose
  again. The Microsoft Store Blender cannot run in a console.
- **Python:** the first `python.exe` that can import Pillow and openpyxl (remembered in `python_path.txt`). If none:
  install Python 3.10+ and run `pip install pillow openpyxl`.

## The home screen

The top lines count the animals: built, stale, previewed, preview-approved, with the whole export package. The menu:

| Group | Key | What it does |
|---|---|---|
| **Render** | `1` Build | Builds every animal's `.blend` from its `blender/model.py` when it is missing or stale (the model, the palette or the standards changed). Seconds per animal. |
| | `2` LOW previews | Builds what is stale, then renders the six review compositions of every animal at LOW into `_system\cache\preview\<code>\` with a contact sheet, then rigs, checks and animates it. About 1–2 minutes per animal. |
| | `3` ULTRA renders | Renders, for every animal **the owner approved** (`vf.py approve <code> preview`), the two master renders (4096 square, dynamic and regular blocky pose) into its `export\` and the frames of its looped animation into the cache. Rendering only: choose P afterwards. About 15 minutes per animal on the RTX 3050 (the integrated Intel GPU of the second PC cannot render ULTRA). Skips renders already finished. |
| | `P` Package | After 3, offline and without Blender: the stock image, loop GIF, the two A5 cards, the stock files, the Gumroad zip and the registry rows of every rendered animal, with a progress line (steps, percent, time left). Lights up when something is waiting. |
| | `4` One animal | Pick a code, then build, preview, final or package for that animal only. |
| **Motion** | `R` Rig | Approved (2026-11-17). Rigs every animal from its built `.blend` (`blender\<code> · <Name> · Rig.blend` and `· Rig.glb`, the stills untouched) and renders a GIF loop of each action into `_system\cache\preview\<code>\anim\`, then the lineup GIF in `02 Animals\`. About 1–2 minutes per animal, three at a time; skips rigs that are current. |
| **Check** | `5` Status | Every animal in the colour of its state (below). |
| | `6` One animal's files | The export package of one animal (which items exist) and where its preview is. |
| **Control** | `Q` Quit | |

### The colours

| Colour | Means |
|---|---|
| Green | done: the whole export package built (and approved) |
| Yellow | preview approved: the ULTRA renders wait (option 3, then P) |
| Blue | LOW preview rendered, waiting for the owner's look |
| Cyan | built, not previewed yet |
| Red | stale: the model, palette or standards changed since the `.blend` was built (option 1) |
| Grey | not built (no model yet) |

## Pausing and carrying on

Press `Ctrl+C` or close the window. Every finished image is kept; run the same option again and it renders only what
is missing or older than the animal's `.blend`. Shutting the computer down is a pause too.

## Without the menu

`render.bat status`, `render.bat build`, `render.bat preview`, `render.bat final`, `render.bat package`, `render.bat 000001 preview`,
`render.bat 000001 final`. The same work from a terminal: `python _system/studio/scripts/vf.py render-all LOW|ULTRA`.

## Quality

| | ULTRA (final) | LOW (preview) |
|---|---|---|
| Size | 4096 on the long side (1:1 4096², 9:16 2304×4096, 16:9 4096×2304) | a quarter (1024 on the long side) |
| Light | 256 samples (64 on the shadow pass), full-resolution ray tracing, 4 shadow rays | 8 samples, quarter-resolution ray tracing |
| Time | about 5 min a 1:1, 1.5 min a 9:16 or 16:9 (RTX 3050 Laptop) | about a second an image |

The values live in `_system/studio/blender/vf_standards.py` (`PROFILES`) and are listed in the skill
`voxel-animal-production`.

## What is in this folder

| Path | What |
|---|---|
| `render.bat` | the renderer (double-click) |
| `README.md` | every animal at a glance (rewritten by `render.bat` and `vf.py render-all`) |
| `python_path.txt` | this PC's Python (git-ignored) |
| `Voxel Fauna · How to Render.md` | this guide |

## Package (P, after the renders)

Choose `P` in `render.bat` (or `render.bat package`, `render.bat package 000001` for one animal) when the ULTRA renders are done. Offline, no Blender: for every
animal with its two masters it builds `VF-<code>-LOOP.gif` (1080 square, 24 fps), `VF-<code>-CARD-EN.pdf` and `VF-<code>-CARD-ID.pdf` (A5, 3 mm bleed,
300 dpi: front the model over the real photo with the information, back the blocky model with "powered by ihdyo"),
then `VF-<code>-STOCK.jpg` (the whole dynamic master as the stock JPEG, no crop) and its CSVs, the Gumroad zip and the registry rows. `render.bat package 000001` does one animal. It needs
Python with Pillow, openpyxl and PyMuPDF (`pip install pillow openpyxl pymupdf`). A card whose text does not fit
stops with the field to shorten (`animal.json → info`, or `i18n.id` for the Indonesian card).
