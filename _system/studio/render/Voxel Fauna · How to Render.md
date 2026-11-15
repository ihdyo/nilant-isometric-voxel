# Voxel Fauna · How to render

`render.bat` (this folder) is the one-stop renderer, ported from Nilant's: **double-click it**. It works offline (no
internet, no Claude). Blender builds and renders; Python (with Pillow and openpyxl) lays the information cards.

- **Blender:** it uses the path remembered in `..\blender_path.txt`, else the `BLENDER` environment variable, else the
  first `blender.exe` it finds (the regular Blender 5.3.0 install on the owner's PC). Delete the text file to choose
  again. The Microsoft Store Blender cannot run in a console.
- **Python:** the first `python.exe` that can import Pillow and openpyxl (remembered in `python_path.txt`). If none:
  install Python 3.10+ and run `pip install pillow openpyxl`.

## The home screen

The top lines count the animals: built, stale, previewed, preview-approved, with all six finals. The menu:

| Group | Key | What it does |
|---|---|---|
| **Render** | `1` Build | Builds every animal's `.blend` from its `blender/model.py` when it is missing or stale (the model, the palette or the standards changed). Seconds per animal. |
| | `2` LOW previews | Builds what is stale, then renders the six compositions of every animal at LOW into `_system\cache\preview\<code>\` with a contact sheet. Seconds per animal. |
| | `3` ULTRA finals | Renders the six final images (4096 px) of every animal **the owner approved** (`vf.py approve <code> preview`) into its `export\`. About 15–20 minutes per animal on the RTX 3050. Skips images already finished. |
| | `4` One animal | Pick a code, then build, preview or final for that animal only. |
| **Check** | `5` Status | Every animal in the colour of its state (below). |
| | `6` One animal's files | The six final files of one animal and where its preview is. |
| **Control** | `Q` Quit | |

### The colours

| Colour | Means |
|---|---|
| Green | done: all six finals rendered (and approved) |
| Yellow | preview approved: the finals are waiting to render (option 3) |
| Blue | LOW preview rendered, waiting for the owner's look |
| Cyan | built, not previewed yet |
| Red | stale: the model, palette or standards changed since the `.blend` was built (option 1) |
| Grey | not built (no model yet) |

## Pausing and carrying on

Press `Ctrl+C` or close the window. Every finished image is kept; run the same option again and it renders only what
is missing or older than the animal's `.blend`. Shutting the computer down is a pause too.

## Without the menu

`render.bat status`, `render.bat build`, `render.bat preview`, `render.bat final`, `render.bat 26-001 preview`,
`render.bat 26-001 final`. The same work from a terminal: `python _system/studio/scripts/vf.py render-all LOW|ULTRA`.

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
