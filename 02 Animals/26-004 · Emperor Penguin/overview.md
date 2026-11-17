# 26-004 · Emperor Penguin

*Aptenodytes forsteri* · Voxel Fauna · status **Registered**

> Written by `python _system/studio/scripts/vf.py overview 26-004` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-004/26-004 · preview sheet.png`
- [x] Phase 4 · Export package: 5 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [x] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Bird · Penguin family · IUCN Near Threatened
- Height: 101–132 cm
- Weight: 25–45 kg
- Lifespan: 15–20 yrs
- Dives to: 564 m
- Home turf: Sea ice and icy seas around Antarctica, where the winter wind chill drops to −60 °C.
- On the menu: Fish, krill and squid, caught on long deep dives. Adults eat 2 to 3 kg a day.
- Fun fact: Dads balance the egg on their feet for about 65 days of winter and eat nothing at all.
- Fun fact: Huddles of up to 5,000 penguins share body heat through the polar night.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-004-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-004-MASTER-DYN.png` |
| `VF-26-004-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-004-MASTER-BLOCK.png` |
| `VF-26-004-LOOP` | looped dynamic animation, 1080 square | `export/VF-26-004-LOOP.gif` |
| `VF-26-004-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | `export/VF-26-004-CARD-EN.pdf` |
| `VF-26-004-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | `export/VF-26-004-CARD-ID.pdf` |

## Look

- Background: `sky-200`: Pale polar sky: cool and calm, with the black back and the yellow ear patch standing out.
- Palette: black `slate-900`, white `slate-50`, yellow `amber-400`, cream `amber-100`, bill `orange-400`
- Photo on the information artwork: `assets/photos/01-pair.jpg` (Denis Luyten, Public domain)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-004 · Emperor Penguin.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Example animal seeded 2026-11-16 (owner: 'generate at least 10 example animals'); facts from ADW, IUCN and cited papers.
