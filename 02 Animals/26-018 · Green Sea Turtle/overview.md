# 26-018 · Green Sea Turtle

*Chelonia mydas* · Voxel Fauna · status **Final**

> Written by `python _system/studio/scripts/vf.py overview 26-018` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [x] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 2 photo(s) in `assets/photos/`
- [x] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **current**
- [x] Phase 3 · LOW preview approved by the owner (2026-11-17) · sheet `_system/cache/preview/26-018/26-018 · preview sheet.png`
- [ ] Phase 4 · Export package: 2 of 6 (render.bat renders the masters and the loop; package.bat builds the stock image, the GIF and the cards)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Reptile · Sea turtle family · IUCN Least Concern
- Shell: 1–1.2 m
- Weight: 150–200 kg
- Eggs: 75–200
- Lifespan: ≤75 yrs
- Home turf: Warm coasts and seagrass meadows in tropical seas worldwide. It nests on sandy beaches.
- On the menu: Grown-ups graze seagrass and algae like underwater cows. Babies also eat small animals.
- Fun fact: It's named for the green fat under its shell, not for the shell itself!
- Fun fact: Warm nests hatch mostly girls and cool nests mostly boys.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-26-018-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-018-MASTER-DYN.png` |
| `VF-26-018-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | `export/VF-26-018-MASTER-BLOCK.png` |
| `VF-26-018-STOCK-1x1` | 1:1 dynamic for stock sites, the centre square of the dynamic master | not built yet |
| `VF-26-018-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-26-018-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-26-018-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `sky-200`: A clear sea blue, far from the brown shell and olive skin: the turtle back in the water.
- Palette: shell `amber-800`, seam `amber-500`, skin `lime-800`, belly `amber-100`, eye `neutral-950`
- Photo on the information artwork: `assets/photos/01-on-sand.jpg` (Marius Burger, CC0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/26-018 · Green Sea Turtle.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-16 (owner: 'create another 10 animals', chose the mixed set incl. game mobs); facts from ADW, the IUCN assessment and cited papers; photos approved by the owner as a batch.
