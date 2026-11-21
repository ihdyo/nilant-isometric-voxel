# 000007 · Koala

*Phascolarctos cinereus* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 000007` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/000007/000007 · preview sheet.png`
- [x] Phase 4 · Export package: 5 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Marsupial · Koala family · IUCN Vulnerable
- Length: 72–78 cm
- Weight: 5–12 kg
- Sleep: 18 h a day
- Lifespan: 10+ yrs
- Home turf: Eucalyptus forests of eastern and south-eastern Australia, mostly below 600 m.
- On the menu: Eucalyptus leaves, about 500 g a day, from just a handful of favourite tree species.
- Fun fact: It naps up to 18 hours a day. A leafy, low-energy diet means lots of rest!
- Fun fact: No sweat glands, no problem: it cools off by licking its arms.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000007-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000007-MASTER-DYN.png` |
| `VF-000007-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-000007-MASTER-BLOCK.png` |
| `VF-000007-LOOP` | looped dynamic animation, 1080 square | `export/VF-000007-LOOP.gif` |
| `VF-000007-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | `export/VF-000007-CARD-EN.pdf` |
| `VF-000007-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | `export/VF-000007-CARD-ID.pdf` |

## Look

- Background: `#B9E0C0` (eucalyptus sage): The grey-green of the eucalyptus leaves it eats and sleeps in.
- Palette: fur `#A6A09B`, white `#F5F5F4`, nose `#292524`, eye `#0A0A0A`, paw `#57534D`
- Photo on the information artwork: `assets/photos/01-in-tree.jpg` (Les Anderson, CC0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000007 · Koala.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Example animal seeded 2026-11-16 (owner: 'generate at least 10 example animals'); facts from ADW, IUCN and cited papers.
