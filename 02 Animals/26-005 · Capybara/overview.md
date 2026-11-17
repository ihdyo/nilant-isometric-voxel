# 26-005 · Capybara

*Hydrochoerus hydrochaeris* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 26-005` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-005/26-005 · preview sheet.png`
- [ ] Phase 4 · Export package: 2 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Guinea pig family · IUCN Least Concern
- Length: 106–134 cm
- Weight: 35–66 kg
- Lifespan: ~6 yrs wild
- Group: 3–30
- Home turf: Riverbanks, marshes and flooded grasslands across South America. Water is never far away.
- On the menu: Grasses and water plants, with the odd bit of bark or fruit. A champion grazer!
- Fun fact: The world's biggest rodent can stay completely underwater for up to five minutes.
- Fun fact: Each morning it re-eats the previous day's food to get more out of it. Gross, but clever!

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-005-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-005-MASTER-DYN.png` |
| `VF-26-005-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-005-MASTER-BLOCK.png` |
| `VF-26-005-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-005-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-005-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `indigo-200`: A soft periwinkle, opposite the warm brown coat, like a calm evening sky over a river.
- Palette: fur `amber-800`, dark `orange-950`, eye `neutral-950`
- Photo on the information artwork: `assets/photos/01-resting.jpg` (Wilfredor, CC0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-005 · Capybara.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Example animal seeded 2026-11-16 (owner: 'generate at least 10 example animals'); facts from ADW, IUCN and cited papers.
