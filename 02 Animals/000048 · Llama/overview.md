# 000048 · Llama

*Lama glama* · Voxel Fauna · status **Research**

> Written by `python _system/studio/scripts/vf.py overview 000048` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [ ] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 0 photo(s) in `assets/photos/`
- [ ] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **missing**
- [ ] Phase 3 · LOW preview approved by the owner
- [ ] Phase 4 · Export package: 0 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Camel family · IUCN Domesticated
- Head height: 1.7–1.8 m
- Weight: 130–200 kg
- Lifespan: 15–25 yrs
- Pregnancy: 350 days
- Home turf: High-altitude Andean plateaus, puna grasslands and mountain slopes across Peru, Bolivia, Ecuador, Chile and Argentina.
- On the menu: Coarse Andean grasses, shrubs, lichens and herbs grazed cleanly with a split upper lip.
- Fun fact: Domesticated in the Andes over 4,000 years ago from wild guanacos, llamas have banana-shaped inward-curving ears.
- Fun fact: Their blood carries extra hemoglobin with high oxygen affinity, letting them thrive above 4,000 meters in thin mountain air.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000048-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000048-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000048-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-000048-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-000048-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `#C3B88C` (soft straw): A warm Andean highland golden ochre that complements the creamy-brown woolly fleece.
- Palette: coat `#FEF3C6`, patch `#973C00`, face `#44403B`, pad `#57534D`, white `#FAFAF9`, eye `#1C1917`
- Photo on the information artwork: `assets/photos/01-side-profile.jpg` (Mathias Appel, CC0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000048 · Llama.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-20 from Voxel Fauna · Registry.xlsx (batch 036-050); facts from ADW, IUCN Red List and peer-reviewed literature.
