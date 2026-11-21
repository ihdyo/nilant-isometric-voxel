# 000045 · Javan Rhinoceros

*Rhinoceros sondaicus* · Voxel Fauna · status **Research**

> Written by `python _system/studio/scripts/vf.py overview 000045` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [ ] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 0 photo(s) in `assets/photos/`
- [ ] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **missing**
- [ ] Phase 3 · LOW preview approved by the owner
- [ ] Phase 4 · Export package: 0 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Rhinoceros family · IUCN Critically Endangered
- Body length: 3.1–3.2 m
- Weight: 0.9–2.3 t
- Single horn: up to 25 cm
- Lifespan: 30–40 yrs
- Home turf: Dense lowland tropical rainforests, coastal floodplains and mud wallows in Ujung Kulon National Park, West Java.
- On the menu: Shoots, twigs, young foliage and fallen forest fruits plucked with its pointed prehensile upper lip.
- Fun fact: One of the rarest large mammals on Earth, with the entire wild population surviving in Ujung Kulon National Park in Java, Indonesia.
- Fun fact: Deep skin folds give it a riveted armor-plated appearance, and only males grow a single horn (usually under 25 cm).

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000045-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000045-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000045-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-000045-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-000045-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `#B1E1C9` (soft mint): A soft tropical coastal-jungle mint green that evokes Ujung Kulon's rainforest and highlights the armor-plated skin folds.
- Palette: skin `#A6A09B`, fold `#57534D`, horn `#FEF3C6`, nail `#E7E5E4`, white `#FAFAF9`, eye `#171717`
- Photo on the information artwork: `assets/photos/01-side-profile.jpg` (WWF Indonesia / Ujung Kulon camera trap, CC BY 3.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000045 · Javan Rhinoceros.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-20 from Voxel Fauna · Registry.xlsx (batch 036-050); facts from ADW, IUCN Red List and peer-reviewed literature.
