# 26-023 · European Rabbit

*Oryctolagus cuniculus* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 26-023` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-023/26-023 · preview sheet.png`
- [ ] Phase 4 · Export package: 2 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Rabbit family · IUCN Endangered
- Length: 38–50 cm
- Weight: 1.5–2.5 kg
- Litter: 5–6 young
- Pregnancy: ~30 days
- Home turf: Sandy fields, scrub and woods. Native to Spain, Portugal and France, now on 5 continents.
- On the menu: Grass, leaves and roots. It even eats some droppings to digest them twice!
- Fun fact: It thumps its back feet on the ground to warn the warren that danger is near.
- Fun fact: It's the wild ancestor of every pet rabbit, about 80 breeds in all.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-023-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-023-MASTER-DYN.png` |
| `VF-26-023-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-023-MASTER-BLOCK.png` |
| `VF-26-023-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-023-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-023-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `lime-200`: Fresh meadow green, the complement of the grey-brown fur: a rabbit's favourite place.
- Palette: fur `stone-400`, belly `stone-200`, tail `stone-50`, ear `rose-200`, nose `rose-300`, eye `neutral-950`
- Photo on the information artwork: `assets/photos/01-close-up.jpg` (Rolf Dietrich Brecher, CC BY 2.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-023 · European Rabbit.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 10 animals', chose the mixed set incl. game mobs); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
