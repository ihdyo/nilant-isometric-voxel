# 26-009 · Polar Bear

*Ursus maritimus* · Voxel Fauna · status **Preview approved**

> Written by `python _system/studio/scripts/vf.py overview 26-009` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-009/26-009 · preview sheet.png`
- [ ] Phase 4 · Export package: 0 of 6 (render.bat renders the masters and the loop; package.bat builds the stock image, the GIF and the cards)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Bear family · IUCN Vulnerable
- Length: 1.8–2.5 m
- Weight: 150–800 kg
- Shoulder: up to 1.6 m
- Lifespan: 25–30 yrs
- Home turf: Sea ice across the Arctic Ocean, especially the ice edge where seals come up for air.
- On the menu: Mostly ringed seals, ambushed at their breathing holes in the ice. Very patient eaters!
- Fun fact: Its fur isn't actually white! The hairs are clear, and the skin underneath is black.
- Fun fact: Huge front paws work like paddles, making it an excellent swimmer.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-009-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-26-009-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-26-009-STOCK-1x1` | 1:1 dynamic for stock sites, the centre square of the dynamic master | not built yet |
| `VF-26-009-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-009-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-009-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `blue-300`: Arctic blue: the cold sea-ice world, with the creamy white bear standing out in full.
- Palette: fur `amber-50`, dark `neutral-900`, shine `white`
- Photo on the information artwork: `assets/photos/01-on-ice.jpg` (Christopher Michel, CC BY 2.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-009 · Polar Bear.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Example animal seeded 2026-11-16 (owner: 'generate at least 10 example animals'); facts from ADW, IUCN and cited papers.
