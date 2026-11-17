# 26-006 · American Flamingo

*Phoenicopterus ruber* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 26-006` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-006/26-006 · preview sheet.png`
- [ ] Phase 4 · Export package: 2 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Bird · Flamingo family · IUCN Least Concern
- Height: ~1.2 m
- Wingspan: 140–165 cm
- Weight: 2.1–4.1 kg
- Eggs: 1 a year
- Home turf: Salty lagoons, mudflats and shallow coastal lakes around the Caribbean, in big noisy flocks.
- On the menu: Tiny crustaceans, worms, molluscs and bits of plants, filtered from the mud with its bill.
- Fun fact: Its pink comes from its food! Pigments in tiny crustaceans tint the feathers and even the legs.
- Fun fact: It feeds with its head upside down, so its bent bill works the right way up.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-006-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-006-MASTER-DYN.png` |
| `VF-26-006-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-006-MASTER-BLOCK.png` |
| `VF-26-006-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-006-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-006-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `emerald-200`: Mint green, the complement of flamingo pink: the brightest bird of the collection gets the boldest contrast.
- Palette: pink `rose-400`, light `rose-200`, black `neutral-900`, bill `rose-100`, legs `rose-500`, feet `rose-700`, eye `amber-300`
- Photo on the information artwork: `assets/photos/01-head.jpg` (Wilfredor, CC0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-006 · American Flamingo.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Example animal seeded 2026-11-16 (owner: 'generate at least 10 example animals'); facts from ADW, IUCN and cited papers.
