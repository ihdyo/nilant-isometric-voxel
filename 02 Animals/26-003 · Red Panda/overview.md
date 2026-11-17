# 26-003 · Red Panda

*Ailurus fulgens* · Voxel Fauna · status **Preview approved**

> Written by `python _system/studio/scripts/vf.py overview 26-003` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-003/26-003 · preview sheet.png`
- [ ] Phase 4 · Export package: 0 of 6 (render.bat renders the masters and the loop; package.bat builds the stock image, the GIF and the cards)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Red panda family · IUCN Endangered
- Length: 56–63 cm
- Tail: 37–47 cm
- Weight: 3.7–6.2 kg
- Lifespan: 8–10 yrs
- Home turf: Cool Himalayan forests with lots of bamboo, 2,200 to 4,800 m up in the mountains.
- On the menu: Mostly bamboo leaves, plus berries, blossoms, bird eggs and tender young leaves.
- Fun fact: Plot twist: it isn't a giant panda's cousin. Red pandas have a whole family all to themselves!
- Fun fact: It climbs down trees head first, with a flexible spine and sharp claws.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-003-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-26-003-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-26-003-STOCK-1x1` | 1:1 dynamic for stock sites, the centre square of the dynamic master | not built yet |
| `VF-26-003-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-003-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-003-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `cyan-200`: Cool cyan, opposite the rusty red coat, like the misty Himalayan forest it lives in.
- Palette: fur `orange-700`, white `stone-50`, dark `orange-950`, ring `orange-300`, eye `neutral-950`
- Photo on the information artwork: `assets/photos/01-front.jpg` (Mathias Appel, CC0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-003 · Red Panda.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Example animal seeded 2026-11-16 (owner: 'generate at least 10 example animals'); facts from ADW, IUCN and cited papers.
