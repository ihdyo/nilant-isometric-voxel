# 000016 · Axolotl

*Ambystoma mexicanum* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 000016` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/000016/000016 · preview sheet.png`
- [x] Phase 4 · Export package: 5 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Amphibian · Salamander family · IUCN Critically Endangered
- Length: ~23 cm
- Weight: 60–110 g
- Eggs: 100–300
- Lifespan: ≤15 yrs
- Home turf: The canals of Lake Xochimilco in Mexico City, high in the mountains. Its other lake was drained.
- On the menu: Snails, worms, insects, small fish and even other axolotls!
- Fun fact: It keeps its feathery baby gills all its life and is famous for regrowing lost body parts.
- Fun fact: Almost every lab axolotl descends from just 33 shipped from Mexico to Paris in 1864!

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000016-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000016-MASTER-DYN.png` |
| `VF-000016-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000016-MASTER-BLOCK.png` |
| `VF-000016-LOOP` | looped dynamic animation, 1080 square | `export/VF-000016-LOOP.gif` |
| `VF-000016-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | `export/VF-000016-CARD-EN.pdf` |
| `VF-000016-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | `export/VF-000016-CARD-ID.pdf` |

## Look

- Background: `#A6E1E4` (lake teal): The water of Lake Xochimilco, opposite the axolotl's pink.
- Palette: skin `#FFCCD3`, gill `#FF637E`, belly `#FFE4E6`, eye `#0A0A0A`
- Photo on the information artwork: `assets/photos/01-pale-pair.jpg` (ZeWrestler, CC BY 3.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000016 · Axolotl.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 10 animals', chose the mixed set incl. game mobs); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
