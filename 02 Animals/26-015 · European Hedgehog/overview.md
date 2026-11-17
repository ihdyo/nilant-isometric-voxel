# 26-015 · European Hedgehog

*Erinaceus europaeus* · Voxel Fauna · status **Preview approved**

> Written by `python _system/studio/scripts/vf.py overview 26-015` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-015/26-015 · preview sheet.png`
- [ ] Phase 4 · Export package: 0 of 6 (render.bat renders the masters and the loop; package.bat builds the stock image, the GIF and the cards)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Hedgehog family · IUCN Near Threatened
- Spines: ~5,000
- Weight: 0.8–1.2 kg
- Lifespan: up to 6 yrs
- Litter: 4–6 young
- Home turf: Hedgerows, fields, parks and gardens across Europe, maybe even yours!
- On the menu: Beetles, earwigs, moths and snails, plus the odd egg or bit of fruit.
- Fun fact: In winter it hibernates, but wakes every week or two for a day of snacks and a wee.
- Fun fact: Hoglets are born with their spines tucked under soft skin; they pop up within a day.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-015-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-26-015-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-26-015-STOCK-1x1` | 1:1 dynamic for stock sites, the centre square of the dynamic master | not built yet |
| `VF-26-015-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-015-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-015-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `emerald-100`: A fresh garden green, where hedgehogs snuffle at night; the brown spines stand out warm against it.
- Palette: spines `amber-800`, tips `amber-100`, face `#C8A47E`, nose `neutral-900`, eye `neutral-950`, feet `stone-500`
- Photo on the information artwork: `assets/photos/01-walking.jpg` (Christian Kahle, CC0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-015 · European Hedgehog.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 5 animals'); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
