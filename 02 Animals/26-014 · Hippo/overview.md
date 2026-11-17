# 26-014 · Hippo

*Hippopotamus amphibius* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 26-014` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-014/26-014 · preview sheet.png`
- [ ] Phase 4 · Export package: 2 of 6 (render.bat renders the masters and the loop; package.bat builds the stock image, the GIF and the cards)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Hippo family · IUCN Vulnerable
- Length: 2.9–5 m
- Weight: 1.3–3.2 t
- Lifespan: ~55 yrs
- Top speed: 30 km/h
- Home turf: Rivers, lakes and swamps across sub-Saharan Africa. Water about 2 m deep is just right.
- On the menu: Grass, grass and more grass: about 40 kg a night, grazed in 4 to 5 hours on land.
- Fun fact: Hippos make their own sunscreen: a red skin oil that blocks the sun and fights germs.
- Fun fact: Calves are born in or near water and even nurse underwater, ears folded and nostrils shut.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-014-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-014-MASTER-DYN.png` |
| `VF-26-014-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-014-MASTER-BLOCK.png` |
| `VF-26-014-STOCK-1x1` | 1:1 dynamic for stock sites, the centre square of the dynamic master | not built yet |
| `VF-26-014-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-014-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-014-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `yellow-200`: A warm sunny yellow, the complement of the purple-grey skin: a hot African afternoon, time for a wallow.
- Palette: skin `#8E7C8F`, pink `rose-200`, mouth `rose-400`, tusk `amber-50`, eye `neutral-950`
- Photo on the information artwork: `assets/photos/01-two-in-water.jpg` (William Warby, CC BY 2.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-014 · Hippo.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 5 animals'); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
