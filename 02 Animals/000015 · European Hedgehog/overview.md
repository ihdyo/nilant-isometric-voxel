# 000015 · European Hedgehog

*Erinaceus europaeus* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 000015` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/000015/000015 · preview sheet.png`
- [x] Phase 4 · Export package: 5 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
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
| `VF-000015-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000015-MASTER-DYN.png` |
| `VF-000015-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000015-MASTER-BLOCK.png` |
| `VF-000015-LOOP` | looped dynamic animation, 1080 square | `export/VF-000015-LOOP.gif` |
| `VF-000015-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | `export/VF-000015-CARD-EN.pdf` |
| `VF-000015-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | `export/VF-000015-CARD-ID.pdf` |

## Look

- Background: `#CBDCB1` (garden green): Garden leaves and hedges, where hedgehogs hunt beetles at night.
- Palette: spines `#973C00`, tips `#FEF3C6`, face `#C8A47E`, nose `#171717`, eye `#0A0A0A`, feet `#79716B`
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
| `blender/000015 · European Hedgehog.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 5 animals'); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
