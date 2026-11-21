# 000002 · Giant Panda

*Ailuropoda melanoleuca* · Voxel Fauna · status **Registered**

> Written by `python _system/studio/scripts/vf.py overview 000002` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/000002/000002 · preview sheet.png`
- [x] Phase 4 · Export package: 5 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [x] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Bear family · IUCN Vulnerable
- Length: 1.5–1.8 m
- Weight: 80–125 kg
- Lifespan: 10–15 yrs
- Bamboo: over 99%
- Home turf: Cool, misty mountain forests full of bamboo in central China, 1,200 to 3,900 m up.
- On the menu: Bamboo, bamboo, bamboo! It munches 10 to 12 hours a day, with the odd fish or insect.
- Fun fact: That 'thumb' isn't a finger. It's a pad over a wrist bone, perfect for gripping bamboo.
- Fun fact: A newborn panda weighs just 85 to 140 g. That's lighter than an apple!

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000002-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000002-MASTER-DYN.png` |
| `VF-000002-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000002-MASTER-BLOCK.png` |
| `VF-000002-LOOP` | looped dynamic animation, 1080 square | `export/VF-000002-LOOP.gif` |
| `VF-000002-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | `export/VF-000002-CARD-EN.pdf` |
| `VF-000002-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | `export/VF-000002-CARD-ID.pdf` |

## Look

- Background: `#C4DEB6` (bamboo green): The green of the bamboo it eats all day; black and white pop on it.
- Palette: white `#FAFAF9`, black `#171717`
- Photo on the information artwork: `assets/photos/01-sitting.jpg` (Jeff Kubina, Public domain)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000002 · Giant Panda.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Example animal seeded 2026-11-16 (owner: 'generate at least 10 example animals'); facts from ADW, IUCN and cited papers.
