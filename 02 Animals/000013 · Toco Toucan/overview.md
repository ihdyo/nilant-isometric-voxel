# 000013 · Toco Toucan

*Ramphastos toco* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 000013` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/000013/000013 · preview sheet.png`
- [x] Phase 4 · Export package: 5 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Bird · Toucan family · IUCN Least Concern
- Length: ~61 cm
- Weight: 592–760 g
- Lifespan: ~20 yrs
- Bill: 1/3 length
- Home turf: Open woods, savannas and plantations in South America, mostly lowland Brazil and nearby.
- On the menu: Mostly fruit, tossed up and gulped down whole, plus insects and the odd egg.
- Fun fact: That huge bill is an air conditioner: toucans send warm blood into it to cool down on hot days.
- Fun fact: The biggest bill for its size of any bird: a third of its length, yet only a twentieth of its weight.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000013-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000013-MASTER-DYN.png` |
| `VF-000013-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000013-MASTER-BLOCK.png` |
| `VF-000013-LOOP` | looped dynamic animation, 1080 square | `export/VF-000013-LOOP.gif` |
| `VF-000013-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | `export/VF-000013-CARD-EN.pdf` |
| `VF-000013-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | `export/VF-000013-CARD-ID.pdf` |

## Look

- Background: `#BAD7FC` (tropical-sky blue): A tropical sky, opposite the toucan's yellow bill.
- Palette: body `#171717`, throat `#FAFAF9`, bill `#FDC700`, bill_low `#FF8904`, ring `#FF8904`, eye `#00A6F4`, vent `#E7000B`, feet `#90A1B9`
- Photo on the information artwork: `assets/photos/01-side.jpg` (Pablo, CC BY 4.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000013 · Toco Toucan.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 5 animals'); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
