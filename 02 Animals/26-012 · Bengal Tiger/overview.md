# 26-012 · Bengal Tiger

*Panthera tigris tigris* · Voxel Fauna · status **Preview approved**

> Written by `python _system/studio/scripts/vf.py overview 26-012` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-012/26-012 · preview sheet.png`
- [ ] Phase 4 · Export package: 0 of 6 (render.bat renders the masters and the loop; package.bat builds the stock image, the GIF and the cards)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Cat family · IUCN Endangered
- Length: up to 3 m
- Weight: 225 kg max
- Lifespan: ≤15 yrs
- Fangs: 7.5–10 cm
- Home turf: Jungles, mangroves, marshes and tall grass in India, Bangladesh, Nepal, Bhutan and Myanmar.
- On the menu: Deer, wild pigs, antelopes and buffalo, stalked through the grass. One meal can be 40 kg!
- Fun fact: Tigers are great swimmers: one was recorded crossing 29 km of water!
- Fun fact: Bengal tigers have the longest fangs of any big cat alive: up to 10 cm, as long as your finger.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-012-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-26-012-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-26-012-STOCK-1x1` | 1:1 dynamic for stock sites, the centre square of the dynamic master | not built yet |
| `VF-26-012-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-012-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-012-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `green-200`: Jungle green, the complement of the orange coat: the tiger stands out the way it hides in the grass.
- Palette: fur `orange-500`, stripe `neutral-900`, white `stone-50`, nose `rose-300`, eye `amber-400`, pupil `neutral-950`
- Photo on the information artwork: `assets/photos/01-bandhavgarh.jpg` (Bernard Gagnon, CC BY 4.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-012 · Bengal Tiger.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 5 animals'); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
