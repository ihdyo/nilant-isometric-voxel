# Publish · Registry, Uploads and Packs

| File | Use |
|---|---|
| `Voxel Fauna · Registry.xlsx` | The record. **Read Me** (ID convention, statuses), **Animals** (one row per species: code, names, folder, background, status, approval dates, image count), **Images** (six rows per animal: Image ID, kind, ratio, size, file, and one amber cell per platform: Not submitted / Submitted / Accepted / Rejected / Live), **Platforms** (each platform's file rules). Amber cells are yours; the rest is written by `vf.py register`. |
| `Voxel Fauna · Publish Log.md` | Every upload event, dated (the same rows as the workbook's **Publish Log** sheet), written by `vf.py log`. |
| `Voxel Fauna · Publishing Checklist.md` | Before and after every upload. |
| `Stock/` | `<code> · Adobe Stock.csv`, `<code> · Shutterstock.csv` (from `vf.py stock`) |
| `Gumroad/` | `<code> · <Name> · Voxel Fauna.zip` (the six PNG masters, from `vf.py stock`) |

`vf.py register` adds or updates rows by code and Image ID; it never duplicates a row or overwrites an amber cell.
Close the workbook in Excel before running it.
