# 000043 · Spectral Tarsier

*Tarsius tarsier* · Voxel Fauna · status **Research**

> Written by `python _system/studio/scripts/vf.py overview 000043` (also after build, preview, final, approve, register). Edit `animal.json`, the docs and `blender/model.py`, never this page.

## Progress

- [ ] Phase 1 · Research: `docs/animal-info.md`, `docs/references.md`, 0 photo(s) in `assets/photos/`
- [ ] Phase 2 · Modelling: `docs/voxel-model.md`, `blender/model.py`, .blend **missing**
- [ ] Phase 3 · LOW preview approved by the owner
- [ ] Phase 4 · Export package: 0 of 5 (render.bat renders the masters and the loop; render.bat, P builds the GIF, the cards and the stock JPEG)
- [ ] Phase 5 · Registered in `05 Publish/Voxel Fauna · Registry.xlsx`
- [ ] Phase 6 · Approved by the owner

## At a glance

- Mammal · Tarsier family · IUCN Vulnerable
- Body length: 9.5–14 cm
- Tail length: 20–26 cm
- Weight: 100–150 g
- Lifespan: 10–12 yrs
- Home turf: Lowland tropical rainforests, secondary scrub, bamboo thickets and mangroves on Sulawesi and nearby islands in Indonesia.
- On the menu: Grasshoppers, beetles, moths, cicadas, spiders, small lizards and frogs—the only 100% carnivorous primates.
- Fun fact: Each eyeball is as large as its entire brain; because its eyes cannot move in their sockets, it rotates its head nearly 180° like an owl.
- Fun fact: Elongated ankle bones (tarsals) give tarsiers their name and launch them across 3-meter leaps between tree trunks.

## Deliverables (the export package)

| ID | What | File |
|---|---|---|
| `VF-000043-MASTER-DYN` | master render, dynamic pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000043-MASTER-BLOCK` | master render, regular blocky pose, 4096 square (crops to 1:1, 9:16, 16:9) | not built yet |
| `VF-000043-LOOP` | looped dynamic animation, 1080 square | not built yet |
| `VF-000043-CARD-EN` | A5 card, English: front the dynamic pose over the photo with the info, back the blocky pose | not built yet |
| `VF-000043-CARD-ID` | A5 card, Bahasa Indonesia: the same card in Indonesian | not built yet |

## Look

- Background: `#C7D2FD` (soft lavender): A deep nocturnal Sulawesi twilight indigo that highlights the enormous golden eyes and tiny acrobatic frame.
- Palette: coat `#A6A09B`, ear `#FFCCD3`, belly `#E7E5E4`, finger `#FFA1AD`, white `#FAFAF9`, eye `#FE9A00`
- Photo on the information artwork: `assets/photos/01-side-profile.jpg` (Alfonso Diaz, CC BY 2.0)

## Files

| Path | What |
|---|---|
| `animal.json` | source of truth: names, look, the card copy and its sources, the photo, stock metadata, approvals |
| `docs/animal-info.md` | the full biological documentation, every statement sourced |
| `docs/voxel-model.md` | the voxel brief: palette, proportions, parts, features (attach it with `key-prompt.md` to write `model.py`) |
| `docs/references.md` | every source and every photograph with author and licence |
| `assets/photos/` | genuine photographs: modelling references and the information artwork's photo |
| `blender/model.py` | the voxel model (source of truth for the .blend) |
| `blender/000043 · Spectral Tarsier.blend` | the editable Blender project, built from model.py |
| `blender/build.json`, `blender/README.md` | the build stamp and its summary |
| `export/` | the export package (+ the `stock/` JPEG) |

## Notes

- Seeded 2026-11-20 from Voxel Fauna · Registry.xlsx (batch 036-050); facts from ADW, IUCN Red List and peer-reviewed literature.
