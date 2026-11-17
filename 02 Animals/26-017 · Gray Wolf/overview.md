# 26-017 · Gray Wolf

*Canis lupus* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 26-017` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-017/26-017 · preview sheet.png`
- [ ] Phase 4 · Export package: 2 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Dog family · IUCN Least Concern
- Length: 0.9–1.3 m
- Weight: 23–80 kg
- Pack: 5–9 wolves
- Top speed: 55–70 km/h
- Home turf: Tundra, forests, prairies and dry lands across North America, Europe and Asia.
- On the menu: Moose, elk, bison and deer, hunted as a team. One wolf can eat 9 kg in a meal!
- Fun fact: Every pet dog on Earth, from Chihuahua to Great Dane, descends from the gray wolf.
- Fun fact: Howls help a pack find each other and tell other packs: this patch is taken!

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-017-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-017-MASTER-DYN.png` |
| `VF-26-017-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-017-MASTER-BLOCK.png` |
| `VF-26-017-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-017-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-017-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `indigo-200`: A soft dusk indigo, the hour of the howl, cool and calm behind the grey coat.
- Palette: fur `stone-400`, back `stone-600`, light `stone-100`, nose `neutral-900`
- Photo on the information artwork: `assets/photos/01-front.jpg` (Gary Kramer, Public domain)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-017 · Gray Wolf.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 10 animals', chose the mixed set incl. game mobs); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
