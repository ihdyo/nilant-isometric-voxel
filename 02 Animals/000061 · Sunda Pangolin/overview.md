# 000061 · Sunda Pangolin

*Manis javanica* · Voxel Fauna · status **Research**

> Written by `python _system/studio/scripts/vf.py overview 000061` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [ ] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 0 photo(s) in `assets/photos/`
- [ ] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **missing**
- [ ] Phase 3 · LOW preview approved by the owner
- [ ] Phase 4 · Export package: 0 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Pangolin family · IUCN Critically Endangered
- Length: 0.9–1.2 m
- Weight: 4–7 kg
- Lifespan: 15–20 yrs
- Scales: ~20% of weight
- Home turf: Primary and secondary tropical forests, peat swamps and wooded gardens across Southeast Asia.
- On the menu: Tree-nesting ants and termites, extracted with a sticky tongue longer than its entire body.
- Fun fact: The world's only truly scaly mammal—its overlapping armour scales are made of keratin, the same protein as human fingernails.
- Fun fact: When threatened, it curls into an impenetrable armoured ball that even a tiger's jaws cannot crack open.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000061-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000061-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000061-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-000061-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-000061-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `#B0E1CA` (soft mint): A lush Southeast-Asian-forest emerald pastel that sets off its overlapping olive-brown keratin scales.
- Palette: scale `#57534D`, shade `#44403B`, skin `#FEE685`, claw `#D6D3D1`, eye `#171717`
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
| `blender/000061 · Sunda Pangolin.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-20 from Voxel Fauna · Registry.xlsx (batch 000050 to 000075); biological data sourced from ADW and IUCN Red List.
