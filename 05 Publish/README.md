# Publish · Registry, Uploads and Packs

| File | Use |
|---|---|
| `Voxel Fauna · Registry.xlsx` | The animals (owner 2026-11-21: "the registry excel should list the animal info"). **Read Me** (ID convention, statuses), **Animals** (one row per species: code, names in English and Indonesian, classification, IUCN status, real size, the four stats, habitat, diet, the two facts, background and palette, motion, photo credit, folder, status, approval dates; Notes amber). Written from every `animal.json` by `vf.py registry` (all animals) and `vf.py register <code>`. |
| `Platforms/Voxel Fauna · <Platform>.xlsx` | One workbook per platform (owner: "the platform target should listed in different excel files"): Adobe Stock, Shutterstock, Freepik, Dreamstime (the stock JPEG), Gumroad, Creative Market (the export package). **Read Me** (the platform's rules), **Items** (one row per item and animal: Image ID, file, file status, and the amber State / link / notes), **Publish Log**. Written by `vf.py register` and `vf.py log`. |
| `Voxel Fauna · Publish Log.md` | Every upload event, dated (the same rows as the platform workbooks' **Publish Log** sheets), written by `vf.py log`. |
| `Voxel Fauna · Publishing Checklist.md` | Before and after every upload. |
| `Stock/` | `<code> · Adobe Stock.csv`, `<code> · Shutterstock.csv` (from `vf.py stock`) |
| `Gumroad/` | `<code> · <Name> · Voxel Fauna.zip` (the export package, from `render.bat` → P / `vf.py stock`) |

`vf.py register` adds or updates rows by code and Image ID; it never duplicates a row or overwrites an amber cell.
Close the workbook in Excel before running it.
