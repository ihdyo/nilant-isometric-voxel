# 26-021 · Bottlenose Dolphin

*Tursiops truncatus* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 26-021` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-021/26-021 · preview sheet.png`
- [ ] Phase 4 · Export package: 2 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Dolphin family · IUCN Least Concern
- Length: 2.3–3.8 m
- Weight: 250–500 kg
- Top speed: 30 km/h
- Breath hold: 4.5 min
- Home turf: Warm and mild seas worldwide, from bays and river mouths to the open ocean.
- On the menu: Fish and squid, found with echolocation. Up to 16 kg of food a day!
- Fun fact: Every dolphin has its own signature whistle, a bit like a name, and keeps it for life.
- Fun fact: It sleeps with half its brain at a time, so it never forgets to breathe.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-021-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-021-MASTER-DYN.png` |
| `VF-26-021-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-021-MASTER-BLOCK.png` |
| `VF-26-021-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-021-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-021-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `orange-100`: A warm sunny peach, the complement of the cool grey: a summer sea at sunset.
- Palette: grey `slate-400`, back `slate-500`, belly `slate-100`, eye `neutral-950`
- Photo on the information artwork: `assets/photos/01-face.jpg` (NOAA Fisheries, Public domain)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-021 · Bottlenose Dolphin.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 10 animals', chose the mixed set incl. game mobs); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
