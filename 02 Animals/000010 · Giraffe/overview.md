# 000010 · Giraffe

*Giraffa camelopardalis* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 000010` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/000010/000010 · preview sheet.png`
- [x] Phase 4 · Export package: 5 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Giraffe family · IUCN Vulnerable
- Height: up to 5.7 m
- Weight: up to 1.9 t
- Tongue: 45 cm
- Speed: 32–60 km/h
- Home turf: Dry savannas, open woodlands and scrub across Africa, south of the Sahara.
- On the menu: Mostly acacia leaves, grabbed with a 45 cm tongue. A big male eats up to 66 kg a day!
- Fun fact: That huge neck has just 7 bones, the same number as yours!
- Fun fact: Calves drop about 2 m to the ground at birth. Welcome to the world!

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000010-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000010-MASTER-DYN.png` |
| `VF-000010-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000010-MASTER-BLOCK.png` |
| `VF-000010-LOOP` | looped dynamic animation, 1080 square | `export/VF-000010-LOOP.gif` |
| `VF-000010-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | `export/VF-000010-CARD-EN.pdf` |
| `VF-000010-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | `export/VF-000010-CARD-ID.pdf` |

## Look

- Background: `#AADDF2` (savanna-sky blue): A clear savanna sky behind the tallest animal, opposite its amber patches.
- Palette: patch `#BB4D00`, base `#FEF3C6`, mane `#973C00`, dark `#292524`, eye `#0A0A0A`
- Photo on the information artwork: `assets/photos/01-standing.jpg` (flowcomm, CC BY 2.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000010 · Giraffe.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Example animal seeded 2026-11-16 (owner: 'generate at least 10 example animals'); facts from ADW, IUCN and cited papers.
