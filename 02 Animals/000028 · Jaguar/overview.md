# 000028 · Jaguar

*Panthera onca* · Voxel Fauna · status **Research**

> Written by `python _system/studio/scripts/vf.py overview 000028` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [ ] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 0 photo(s) in `assets/photos/`
- [ ] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **missing**
- [ ] Phase 3 · LOW preview approved by the owner
- [ ] Phase 4 · Export package: 0 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Cat family · IUCN Near Threatened
- Body length: 1.1–1.85 m
- Weight: 36–158 kg
- Lifespan: 12–15 yrs
- Pregnancy: 93–105 days
- Home turf: Tropical rainforests, flooded wetlands, mangroves and dry forests from Mexico through the Amazon to northern Argentina.
- On the menu: Capybaras, peccaries, caimans, river turtles, tapirs and fish—an opportunistic apex ambush predator.
- Fun fact: The largest cat in the Americas, possessing the strongest bite force relative to body size of any felid.
- Fun fact: Unlike most cats, jaguars love water and routinely swim across wide rivers to hunt caimans and turtles.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000028-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000028-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000028-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-000028-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-000028-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `#EECEAA` (soft sand): A rich tropical terracotta-orange evoking dappled rainforest canopy light and complementing the golden-orange rosette coat.
- Palette: coat `#FFB900`, rosette `#171717`, belly `#FFFBEB`, muzzle `#FEE685`, white `#FAFAF9`, eye `#FE9A00`
- Photo on the information artwork: `assets/photos/01-side-profile.jpg` (Charles J. Sharp, CC BY-SA 4.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000028 · Jaguar.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-20 from Voxel Fauna · Registry.xlsx (batch 026-035); facts from ADW, IUCN Red List and peer-reviewed literature.
