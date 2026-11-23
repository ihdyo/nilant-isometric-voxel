# Voxel Fauna · How to render

`render.bat` (this folder) is the one-stop renderer, ported from Nilant's: **double-click it**. It works offline (no
internet, no Claude). Blender builds and renders; Python (with Pillow and openpyxl) lays the information cards.

- **Blender:** it uses the path remembered in `..\blender_path.txt`, else the `BLENDER` environment variable, else the
  first `blender.exe` it finds (the regular Blender 5.3.0 install on the owner's PC). Delete the text file to choose
  again. The Microsoft Store Blender cannot run in a console.
- **Python:** the first `python.exe` that can import Pillow and openpyxl (remembered in `python_path.txt`). If none:
  install Python 3.10+ and run `pip install pillow openpyxl`.

## The home screen

`render.bat` opens with a cover (a pixel fox and the title) while it reads the animals, then the home screen: counts of
the animals (built, stale, previewed, preview-approved, with the whole export package) and boxes of steps, each with the
number of animals that still need it:

| Group | Key | What it does |
|---|---|---|
| **Render** | `1` Build | The `.blend` of each chosen animal from its `blender/model.py` (when missing or stale, or always with *Rebuild*). |
| | `2` LOW previews | The six review compositions at LOW into `_system\cache\preview\<code>\` with a contact sheet, then the rig, the rig check and the GIF loops. About 1-2 minutes per animal. |
| | `3` ULTRA masters + loop | For animals **the owner approved** (`vf.py approve <code> preview`): the two 4096 masters into `export\`, the loop frames into the cache. Rendering only; choose P afterwards. About 15 minutes per animal on the RTX 3050 (the integrated Intel GPU cannot render ULTRA). |
| | `P` Package | Offline, no Blender, **piece by piece** (below). |
| | `R` Rig + loops | The rig and GIF loops again. |
| **Check** | `5` Status | Every animal in the colour of its state (below). |
| | `6` One animal's files | Which package files exist, with sizes. |
| **More** | `4` One animal, any step | Type a code or a number, then the step: the same job screen with that animal chosen. |
| | `Q` Quit | |

## The job screen: which animals, and what

Every step opens the same screen. **Animals** starts as the ones that still need the step ("N todo" on the home screen).
Press `A` to choose by hand, or type a quick choice right on the screen: `todo`, `all` (every animal the step can run
on), `none`. Under it, **checkboxes**: type a number to tick or untick it (several at once: `1 3 5`), Enter to run.

**Choosing animals** (`A`): a paged checklist (`n` / `p` for pages, `g3` to jump). Type any mix, separated by spaces:

| You type | It does |
|---|---|
| `3` , `5-9` | toggles those list numbers |
| `000012` , `000010-000020` | toggles that code, or a range of codes |
| `fox` , `/fox` | adds every animal whose name, code or scientific name contains it |
| `!fox` | removes the matches |
| `all` , `none` , `todo` , `done` , `invert` | the whole list, nothing, the ones that still need it, the ones that are done, the opposite |
| Enter / `q` | keep the choice / cancel |

An animal a step cannot run on is grey with the reason (no preview approval, not rendered yet, no model) and is skipped.

**Package** (what to build; the default is everything that is missing or older than its source):

| # | Piece | File |
|---|---|---|
| 1 | Loop GIF | `VF-<code>-LOOP.gif` |
| 2 | A5 card, English | `VF-<code>-CARD-EN.pdf` |
| 3 | A5 card, Bahasa Indonesia | `VF-<code>-CARD-ID.pdf` |
| 4 | Stock JPEG | `VF-<code>-STOCK.jpg` |
| 5 | Stock upload CSVs | `05 Publish\Stock\<code> · Adobe Stock.csv`, `· Shutterstock.csv` |
| 6 | Gumroad zip | `05 Publish\Gumroad\<code> · <Name> · Voxel Fauna.zip` (the masters, GIF and cards in one zip) |
| 7 | Registry + overview | the registry rows and `overview.md` |

Presets (type the word): `full`, `stock` (JPEG, CSVs, registry), `pdf` (both cards), `gif`, `gumroad` (GIF, cards, zip,
registry). Options: *Build again even if current*, *LOW test set* (GIF and cards from the LOW renders, in the cache).

**ULTRA renders**: the dynamic master, the blocky master, the loop frames (any mix; presets `full`, `masters`, `loop`),
*Render again*, *LOW test render*. **LOW previews**: *Stills only*, *Render again*, *Rig again*, *Rigs at the same time*.
**Rig**: *Rig again*, *No GIF loops*, *Redraw the lineup sheets*, *Rigs at the same time*. **Build**: *Rebuild even if
current*. Every step ends with **Shut this PC down when it finishes** (60 seconds to cancel with `shutdown /a`): tick it
for a long ULTRA batch overnight.

Your choices are remembered in `render_options.json` beside `render.bat` (git-ignored), so the next run starts where
you left off.

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

Every option works on the command line too (`render.bat <command> --help`). Animals are codes, ranges, names or `all`;
none means the ones that still need it. The command line starts from the defaults, not from `render_options.json`.

```
render.bat status | files 000001
render.bat build   [animals] [--force]
render.bat preview [animals] [--stills] [--force] [--rig-force] [--jobs 3]
render.bat final   [animals] [--parts dyn,block,loop] [--low] [--force]
render.bat package [animals] [--preset full|stock|pdf|gif|gumroad | --parts gif,card_en,card_id,stock,csv,zip,registry] [--low] [--force]
render.bat rig     [animals] [--force] [--no-preview] [--jobs 3] [--lineups]
render.bat package 000001-000010 --preset stock         the stock files of ten animals
render.bat final   all --parts dyn,block --shutdown     both masters of everything, then shut down
render.bat 000001 final                                 the older short form
```

The engine behind them is `python _system/studio/scripts/vf.py` (`render-all`, `final`, `package`).

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
| `animal_path.txt` | this PC's path to the `02 Animals` folder (git-ignored; asked once if it is not found) |
| `render_options.json` | the choices of each step, remembered (git-ignored) |
| `Voxel Fauna · How to Render.md` | this guide |

## Package (P, after the renders)

Choose `P` (or `render.bat package`) when the ULTRA renders are done. Offline, no Blender: the pieces above, for the
animals you chose, in the order GIF, cards, stock JPEG, CSVs, zip, registry (the zip after the files in it). It needs
Python with Pillow, openpyxl and PyMuPDF (`pip install pillow openpyxl pymupdf`). A card whose text does not fit
stops with the field to shorten (`animal.json -> info`, or `i18n.id` for the Indonesian card); the other animals go on.
