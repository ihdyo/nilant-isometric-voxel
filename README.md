# Voxel Fauna · Folder Map

**Voxel Fauna** · isometric voxel animals made in Blender code, one species at a time, each as three illustrations
and three information artworks (1:1, 9:16, 16:9, 4096 px on the long side), for Gumroad, Adobe Stock and other stock
sites. A Nilant side collection: same folder conventions, same Blender render settings adapted for stills.

Folders follow the production flow: read the guide → make an animal → design → library → publish.

| Folder | Contents | When to open |
|---|---|---|
| **01 Guide** | `Voxel Fauna · Production Workflow`, `· Stock Platforms` (Adobe Stock, Shutterstock, Gumroad and the others), `· Prerequisites`. | At the start, then as a reference. |
| **02 Animals** | `_Template/` and one folder per species, `NNNNNN · Common Name` (six-digit code, e.g. `000001 · Red Fox`): `overview.md` (front page), `animal.json` (names, look, card copy, photo, sources, approvals), `docs/` (animal information, references, the voxel brief), `assets/photos/` (genuine photos), `blender/` (`model.py`, the built `.blend`, its stamp), `export/` (the export package: two masters, the stock image, the loop GIF, the A5 cards). | Every animal. |
| **03 Design** | `DESIGN-SYSTEM.md` (the look in one page), the colour rules (hex only), Poppins, approved reference stills. | When judging or changing the look. |
| **04 Library** | Licence and download log. | When something is downloaded. |
| **05 Publish** | `Voxel Fauna · Registry.xlsx` (the animals' information), `Platforms/` (one workbook per platform: items, state, publish log), `Voxel Fauna · Publish Log.md`, the publishing checklist, upload CSVs, Gumroad zips. | Uploading and tracking. |
| **_system** | The engine (Blender + Python), `render.bat`, data, logs, cache. | Rendering; AI help or big changes. |

## Rendering (double-click)

**`_system/studio/render/render.bat`** builds every animal's `.blend` and renders its images offline (Blender +
Python): `1` build, `2` LOW previews of all, `3` ULTRA finals of every approved animal, `4` one animal, `5` status.
Guide: `_system/studio/render/Voxel Fauna · How to Render.md`.

## Writing a model with Claude in the browser

Attach **`key-prompt.md`** (this folder) and the animal's **`docs/voxel-model.md`** to Claude Sonnet (high effort) and
send. Save the answer as the animal's `blender/model.py`, then `render.bat` → `1` and `2`.

## Making one animal (short version)

From this folder, in any terminal (`python` 3.10+ with Pillow and openpyxl; Blender 5.3):

1. `python _system/studio/scripts/vf.py new "Red Fox" "Vulpes vulpes"` → research: `docs/animal-info.md`,
   `docs/references.md`, photos in `assets/photos/`.
2. Palette and background in `animal.json`, the voxel brief `docs/voxel-model.md`, then `blender/model.py` (yourself
   or with `key-prompt.md`), `vf.py check 000001`.
3. `vf.py preview 000001` (or `render.bat` → 2) → `_system/cache/preview/000001/000001 · preview sheet.png`; when the
   owner likes it, `vf.py approve 000001 preview`.
4. The card copy in `animal.json → info` (Duolingo voice) and `i18n.id` (Indonesian), then `vf.py final 000001`
   (or `render.bat` → 3) → the two masters and the loop; then `render.bat` → P → the stock image, the GIF, the cards.
5. `render.bat` → P also writes the stock files, the Gumroad zip and the registry rows; upload with `05 Publish/Voxel Fauna · Publishing Checklist.md` and
   record each upload with `vf.py log 000001 "Adobe Stock" Submitted`.
6. The owner reviews the export package; `vf.py approve 000001 final`.

Ten example animals are in `02 Animals/` (000001 Red Fox … 000010 Giraffe). Full detail:
`01 Guide/Voxel Fauna · Production Workflow.md`. Check the setup with `vf.py doctor`, everything with `vf.py verify`.
