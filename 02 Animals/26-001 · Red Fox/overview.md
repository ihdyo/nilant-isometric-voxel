# 26-001 · Red Fox

*Vulpes vulpes* · Voxel Fauna · status **Registered**

> Written by `python _system/studio/scripts/vf.py overview 26-001` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-001/26-001 · preview sheet.png`
- [x] Phase 4 · Export package: 5 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [x] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Dog family · IUCN Least Concern
- Length: 46–90 cm
- Tail: 30–56 cm
- Weight: 3–14 kg
- Lifespan: ~3 yrs wild
- Home turf: Forests, tundra, deserts, farms and even cities. No wild dog roams more of the planet!
- On the menu: Mice, voles and rabbits, plus bugs, fruit and leftovers. Up to 1 kg of food a day.
- Fun fact: Foxes pounce on mice under snow, and leaps aimed roughly north-east land far more often. A magnetic sense, maybe!
- Fun fact: It has the widest range of any wild dog, from the Arctic Circle to North Africa.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-001-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-001-MASTER-DYN.png` |
| `VF-26-001-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-001-MASTER-BLOCK.png` |
| `VF-26-001-LOOP` | looped dynamic animation, 1080 square | `export/VF-26-001-LOOP.gif` |
| `VF-26-001-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | `export/VF-26-001-CARD-EN.pdf` |
| `VF-26-001-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | `export/VF-26-001-CARD-ID.pdf` |

## Look

- Background: `teal-200`: Teal sits opposite the fox's rusty orange on the colour wheel; a soft 200 keeps it pastel.
- Palette: fur `orange-600`, white `stone-50`, dark `stone-800`, eye `neutral-950`
- Photo on the information artwork: `assets/photos/01-side-standing.jpg` (Alexis Lours, CC BY 4.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-001 · Red Fox.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Example animal seeded 2026-11-16 (owner: 'generate at least 10 example animals'); facts from ADW, IUCN and cited papers.
