# 26-024 · Red-eyed Tree Frog

*Agalychnis callidryas* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 26-024` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-024/26-024 · preview sheet.png`
- [ ] Phase 4 · Export package: 2 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Amphibian · Tree frog family · IUCN Least Concern
- Length: 4–7 cm
- Weight: 6–15 g
- Eggs: 10–100
- Lifespan: ~5 yrs
- Home turf: Rainforests near ponds, from southern Mexico to northern South America.
- On the menu: Flies, mosquitoes, grasshoppers and other bugs, snapped up at night.
- Fun fact: Unborn tadpoles can hatch early and drop into the water if a snake attacks their eggs!
- Fun fact: It flashes its big red eyes to startle a hungry predator.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-024-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-024-MASTER-DYN.png` |
| `VF-26-024-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-024-MASTER-BLOCK.png` |
| `VF-26-024-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-024-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-024-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `pink-200`: A soft pink, the complement of the leaf green, that makes the red eyes and orange toes glow.
- Palette: green `green-500`, red `red-500`, blue `blue-600`, yellow `amber-300`, toe `orange-400`, belly `stone-50`, pupil `neutral-950`
- Photo on the information artwork: `assets/photos/01-on-stem.jpg` (Bernard Gagnon, CC0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-024 · Red-eyed Tree Frog.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 10 animals', chose the mixed set incl. game mobs); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
