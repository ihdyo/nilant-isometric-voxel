# 000020 · Scarlet Macaw

*Ara macao* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 000020` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/000020/000020 · preview sheet.png`
- [x] Phase 4 · Export package: 5 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Bird · Parrot family · IUCN Least Concern
- Length: ~89 cm
- Weight: ~1.2 kg
- Lifespan: 40–50 yrs
- Eggs: 2–4
- Home turf: Rainforest treetops from southern Mexico to the Amazon, below 1,000 m.
- On the menu: Fruit and nuts, even unripe ones, plus riverbank clay that helps it digest them.
- Fun fact: Most scarlet macaws are lefties: they hold their food with the left foot.
- Fun fact: Pairs stay together for life and preen each other's feathers.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000020-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000020-MASTER-DYN.png` |
| `VF-000020-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000020-MASTER-BLOCK.png` |
| `VF-000020-LOOP` | looped dynamic animation, 1080 square | `export/VF-000020-LOOP.gif` |
| `VF-000020-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | `export/VF-000020-CARD-EN.pdf` |
| `VF-000020-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | `export/VF-000020-CARD-ID.pdf` |

## Look

- Background: `#B6E1C3` (canopy green): The rainforest canopy macaws fly over, opposite their scarlet.
- Palette: red `#E7000B`, yellow `#FFB900`, blue `#155DFC`, face `#FAFAF9`, bill `#E7E5E4`, dark `#171717`, eye `#FEF3C6`
- Photo on the information artwork: `assets/photos/01-flying.jpg` (ImagePerson, CC BY 4.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000020 · Scarlet Macaw.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 10 animals', chose the mixed set incl. game mobs); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
