# 26-011 · African Elephant

*Loxodonta africana* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 26-011` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-011/26-011 · preview sheet.png`
- [ ] Phase 4 · Export package: 2 of 6 (render.bat renders the masters and the loop; package.bat builds the stock image, the GIF and the cards)
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
| `VF-26-011-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-011-MASTER-DYN.png` |
| `VF-26-011-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-011-MASTER-BLOCK.png` |
| `VF-26-011-STOCK-1x1` | 1:1 dynamic for stock sites, the centre square of the dynamic master | not built yet |
| `VF-26-011-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-011-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-011-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `orange-200`: A warm savanna-sunset orange, the complement of the cool grey skin and the colour of the dry grass it walks through.
- Palette: skin `gray-400`, shade `gray-500`, tusk `amber-50`, nail `stone-200`, white `stone-50`, eye `neutral-900`
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
| `blender/26-011 · African Elephant.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 5 animals'); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
