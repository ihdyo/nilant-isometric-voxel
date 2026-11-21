# 000026 · Snow Leopard

*Panthera uncia* · Voxel Fauna · status **Research**

> Written by `python _system/studio/scripts/vf.py overview 000026` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [ ] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 0 photo(s) in `assets/photos/`
- [ ] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **missing**
- [ ] Phase 3 · LOW preview approved by the owner
- [ ] Phase 4 · Export package: 0 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Cat family · IUCN Vulnerable
- Body length: 1–1.3 m
- Weight: 22–55 kg
- Lifespan: 15–18 yrs
- Pregnancy: 90–105 days
- Home turf: Steep, rocky alpine mountains and cliffs across Central and South Asia at 3,000–5,500 m.
- On the menu: Blue sheep, Siberian ibex, marmots, pikas and mountain birds ambushed on rocky ledges.
- Fun fact: Its thick tail is nearly as long as its body and works as a balance pole on cliffs and a scarf while sleeping.
- Fun fact: Unlike lions and tigers, snow leopards cannot roar because their vocal cords lack a thick elastic pad.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000026-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000026-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000026-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-000026-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-000026-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `#AFDBF7` (soft sky blue): A crisp glacial sky blue that echoes high Himalayan snowfields and sets off the smoky-grey spotted coat.
- Palette: coat `#D6D3D1`, spot `#57534D`, belly `#F5F5F4`, nose `#FFA1AD`, white `#FAFAF9`, eye `#00BC7D`
- Photo on the information artwork: `assets/photos/01-side-profile.jpg` (Ricky Wright, CC BY 2.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000026 · Snow Leopard.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-20 from Voxel Fauna · Registry.xlsx (batch 026-035); facts from ADW, IUCN Red List and peer-reviewed literature.
