# 000052 · Reindeer

*Rangifer tarandus* · Voxel Fauna · status **Research**

> Written by `python _system/studio/scripts/vf.py overview 000052` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [ ] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 0 photo(s) in `assets/photos/`
- [ ] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **missing**
- [ ] Phase 3 · LOW preview approved by the owner
- [ ] Phase 4 · Export package: 0 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Deer family · IUCN Vulnerable
- Shoulder: 0.9–1.4 m
- Weight: 60–318 kg
- Lifespan: 12–15 yrs
- Migration: Up to 5,000 km
- Home turf: Arctic tundra and subarctic boreal forests across northern Europe, Siberia and North America.
- On the menu: Reindeer lichen (caribou moss) dug from beneath snow in winter, plus grasses, sedges and willow leaves in summer.
- Fun fact: The only deer species in which both males and females grow antlers every year.
- Fun fact: Their eye tapetum shifts from gold in summer to deep blue in winter to see ultraviolet light on snow.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000052-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000052-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000052-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-000052-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-000052-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `#A6E0E7` (soft aqua): An icy Arctic-cyan backdrop that highlights its frosty white neck ruff and sweeping branching antlers.
- Palette: coat `#79716B`, ruff `#F5F5F4`, antler `#FEE685`, hoof `#262626`, white `#FAFAF9`, eye `#171717`
- Photo on the information artwork: `assets/photos/01-side.jpg` (Pending Wikimedia Commons selection, CC0 / CC BY)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000052 · Reindeer.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-20 from Voxel Fauna · Registry.xlsx (batch 000050 to 000075); biological data sourced from ADW and IUCN Red List.
