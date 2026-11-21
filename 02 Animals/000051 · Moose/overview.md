# 000051 · Moose

*Alces alces* · Voxel Fauna · status **Research**

> Written by `python _system/studio/scripts/vf.py overview 000051` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [ ] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 0 photo(s) in `assets/photos/`
- [ ] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **missing**
- [ ] Phase 3 · LOW preview approved by the owner
- [ ] Phase 4 · Export package: 0 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Deer family · IUCN Least Concern
- Shoulder: 1.4–2.1 m
- Weight: 200–700 kg
- Lifespan: 15–25 yrs
- Antler span: Up to 1.8 m
- Home turf: Boreal forests, willow swamps, lakeshores and river valleys across North America, Europe and Asia.
- On the menu: Willow, birch and aspen twigs in winter, plus underwater pondweeds and water lilies in summer.
- Fun fact: The largest living member of the deer family—bulls grow palm-shaped antlers spanning up to 1.8 metres.
- Fun fact: Strong swimmers that can dive up to 5 metres deep to graze on sodium-rich aquatic plants.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000051-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000051-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000051-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-000051-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-000051-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `#ADDCF5` (soft sky blue): A crisp northern-lake sky blue that sets off the deep chocolate coat and broad pale-cream palmate antlers.
- Palette: coat `#292524`, antler `#FEF3C6`, leg `#D6D3D1`, muzzle `#44403B`, white `#FAFAF9`, eye `#171717`
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
| `blender/000051 · Moose.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-20 from Voxel Fauna · Registry.xlsx (batch 000050 to 000075); biological data sourced from ADW and IUCN Red List.
