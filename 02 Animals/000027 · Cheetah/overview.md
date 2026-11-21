# 000027 · Cheetah

*Acinonyx jubatus* · Voxel Fauna · status **Research**

> Written by `python _system/studio/scripts/vf.py overview 000027` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [ ] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 0 photo(s) in `assets/photos/`
- [ ] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **missing**
- [ ] Phase 3 · LOW preview approved by the owner
- [ ] Phase 4 · Export package: 0 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Cat family · IUCN Vulnerable
- Body length: 1.1–1.5 m
- Weight: 21–72 kg
- Top speed: 100–120 km/h
- Lifespan: 10–12 yrs
- Home turf: Open savannas, dry grasslands and semi-deserts across sub-Saharan Africa, with a tiny remnant population in Iran.
- On the menu: Thomson's gazelles, impalas, springboks, hares and ground birds chased down in high-speed daytime sprints.
- Fun fact: The fastest land mammal on Earth, accelerating from 0 to 100 km/h in about three seconds.
- Fun fact: Black tear marks running down its face deflect harsh savanna glare and help keep prey in focus.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000027-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000027-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000027-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-000027-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-000027-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `#E0D5A8` (soft straw): A warm golden savanna amber echoing sunlit grasslands and complementing the tawny spotted coat.
- Palette: coat `#FFD230`, spot `#171717`, belly `#FFFBEB`, tear `#1C1917`, white `#FAFAF9`, eye `#E17100`
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
| `blender/000027 · Cheetah.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-20 from Voxel Fauna · Registry.xlsx (batch 026-035); facts from ADW, IUCN Red List and peer-reviewed literature.
