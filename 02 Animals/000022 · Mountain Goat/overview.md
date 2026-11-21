# 000022 · Mountain Goat

*Oreamnos americanus* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 000022` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/000022/000022 · preview sheet.png`
- [x] Phase 4 · Export package: 5 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Cattle family · IUCN Least Concern
- Length: 1.2–1.8 m
- Weight: 57–82 kg
- Horns: 20–30 cm
- Lives up to: 5,000 m
- Home turf: Steep, rocky cliffs high in the mountains, from Alaska down to Washington and Idaho.
- On the menu: Grasses, mosses, lichens and shrubs. Most of its water comes from food and snow!
- Fun fact: Its hooves have rubbery soles that grip the rock like climbing shoes.
- Fun fact: Count the rings on its horns to tell its age, just like a tree!

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000022-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000022-MASTER-DYN.png` |
| `VF-000022-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000022-MASTER-BLOCK.png` |
| `VF-000022-LOOP` | looped dynamic animation, 1080 square | `export/VF-000022-LOOP.gif` |
| `VF-000022-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | `export/VF-000022-CARD-EN.pdf` |
| `VF-000022-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | `export/VF-000022-CARD-ID.pdf` |

## Look

- Background: `#DACCF7` (alpine lilac): Alpine dusk on the high ridges, a little darker so the white goat stands out.
- Palette: coat `#FAFAF9`, shade `#E7E5E4`, horn `#171717`, nose `#44403B`
- Photo on the information artwork: `assets/photos/01-lying.jpg` (Dave Grickson/USFWS, Public domain)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000022 · Mountain Goat.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 10 animals', chose the mixed set incl. game mobs); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
