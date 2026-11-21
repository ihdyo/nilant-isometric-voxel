# 000011 · African Elephant

*Loxodonta africana* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 000011` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/000011/000011 · preview sheet.png`
- [x] Phase 4 · Export package: 5 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Elephant family · IUCN Endangered
- Shoulder: 2.2–4 m
- Weight: 2–6.1 t
- Lifespan: 60–70 yrs
- Pregnancy: 22 months
- Home turf: Savannas, woodlands, forests and even deserts across Africa, from sea level up to 4,000 m.
- On the menu: Leaves, grass, fruit, bark and roots, munched nearly all day. Plus about 190 litres of water!
- Fun fact: Elephants seem to call each other by name: a 2024 study found rumbles meant for one elephant only.
- Fun fact: Herds are led by the biggest, boss female, and up to 70 family members follow her.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000011-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000011-MASTER-DYN.png` |
| `VF-000011-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000011-MASTER-BLOCK.png` |
| `VF-000011-LOOP` | looped dynamic animation, 1080 square | `export/VF-000011-LOOP.gif` |
| `VF-000011-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | `export/VF-000011-CARD-EN.pdf` |
| `VF-000011-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | `export/VF-000011-CARD-ID.pdf` |

## Look

- Background: `#ECCFA9` (dry-grass gold): Sun-baked savanna grass, warm against the elephant's grey skin.
- Palette: skin `#99A1AF`, shade `#6A7282`, tusk `#FFFBEB`, nail `#E7E5E4`, white `#FAFAF9`, eye `#171717`
- Photo on the information artwork: `assets/photos/01-side-walking.jpg` (Hobbyfotowiki, CC0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000011 · African Elephant.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 5 animals'); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
