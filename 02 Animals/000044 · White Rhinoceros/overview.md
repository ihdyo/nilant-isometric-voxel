# 000044 · White Rhinoceros

*Ceratotherium simum* · Voxel Fauna · status **Research**

> Written by `python _system/studio/scripts/vf.py overview 000044` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [ ] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 0 photo(s) in `assets/photos/`
- [ ] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **missing**
- [ ] Phase 3 · LOW preview approved by the owner
- [ ] Phase 4 · Export package: 0 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Rhinoceros family · IUCN Near Threatened
- Body length: 3.4–4.2 m
- Weight: 1.4–3.6 t
- Front horn: up to 1.5 m
- Lifespan: 40–50 yrs
- Home turf: Open grasslands, savannas and bushveld with waterholes and mud wallows across southern and eastern Africa.
- On the menu: Short savanna grasses cropped cleanly with its wide, square, flat upper lip.
- Fun fact: The second-largest land mammal after the elephant; its name comes from Dutch 'wijd' ('wide'), referring to its square grazing lip.
- Fun fact: Unlike African elephants, white rhino calves run in front of their mothers rather than behind them.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000044-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000044-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000044-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-000044-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-000044-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `#BAD7FC` (soft periwinkle): A clear African sky blue that complements the pale slate-grey armor skin and wide savanna silhouette.
- Palette: skin `#A6A09B`, shade `#79716B`, horn `#FFFBEB`, nail `#E7E5E4`, white `#FAFAF9`, eye `#171717`
- Photo on the information artwork: `assets/photos/01-side-profile.jpg` (Charles J. Sharp, CC BY 4.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000044 · White Rhinoceros.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-20 from Voxel Fauna · Registry.xlsx (batch 036-050); facts from ADW, IUCN Red List and peer-reviewed literature.
