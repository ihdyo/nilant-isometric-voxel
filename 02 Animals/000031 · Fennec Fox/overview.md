# 000031 · Fennec Fox

*Vulpes zerda* · Voxel Fauna · status **Research**

> Written by `python _system/studio/scripts/vf.py overview 000031` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [ ] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 0 photo(s) in `assets/photos/`
- [ ] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **missing**
- [ ] Phase 3 · LOW preview approved by the owner
- [ ] Phase 4 · Export package: 0 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Dog family · IUCN Least Concern
- Body length: 24–41 cm
- Weight: 0.8–1.5 kg
- Ear length: up to 15 cm
- Lifespan: 10–14 yrs
- Home turf: Sandy deserts and arid semi-deserts across the Sahara and northern Africa.
- On the menu: Insects, scorpions, lizards, small rodents, birds, eggs, desert roots and fruits—getting almost all its water from food.
- Fun fact: The smallest wild canid in the world, yet its ears reach 15 cm long to radiate desert heat and hear prey underground.
- Fun fact: Thick fur covers even the soles of its paws, protecting them from scorching Sahara sand.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000031-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000031-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000031-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-000031-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-000031-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `#D3C89C` (soft straw): A soft Sahara sand-cream pastel that harmonizes with the pale desert coat and oversized warm ears.
- Palette: coat `#FEE685`, ear_in `#FFCCD3`, belly `#FAFAF9`, tip `#171717`, white `#FAFAF9`, eye `#1C1917`
- Photo on the information artwork: `assets/photos/01-side-profile.jpg` (Drew Avery, CC BY 2.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000031 · Fennec Fox.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-20 from Voxel Fauna · Registry.xlsx (batch 026-035); facts from ADW, IUCN Red List and peer-reviewed literature.
