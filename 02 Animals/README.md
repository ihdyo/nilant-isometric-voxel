# Animals · One Folder per Species

Each species has a folder named with its **code** `YY-SEQ · Common Name` (Nilant's convention: `YY` = year, `SEQ` =
number in that year). Create one only with `python _system/studio/scripts/vf.py new "<Common name>" "<Genus species>"`:
it copies `_Template/`, takes the next code and sets the status to Research. One folder per species, never two.

| Code | Animal | Background | Status (2026-11-16) |
|---|---|---|---|
| `26-001 · Red Fox` | *Vulpes vulpes* · LC | teal-200 | LOW preview, awaiting the owner |
| `26-002 · Giant Panda` | *Ailuropoda melanoleuca* · VU | #BFD7A7 | LOW preview, awaiting the owner |
| `26-003 · Red Panda` | *Ailurus fulgens* · EN | cyan-200 | LOW preview, awaiting the owner |
| `26-004 · Emperor Penguin` | *Aptenodytes forsteri* · NT | sky-200 | LOW preview, awaiting the owner |
| `26-005 · Capybara` | *Hydrochoerus hydrochaeris* · LC | indigo-200 | LOW preview, awaiting the owner |
| `26-006 · American Flamingo` | *Phoenicopterus ruber* · LC | emerald-200 | LOW preview, awaiting the owner |
| `26-007 · Koala` | *Phascolarctos cinereus* · VU | amber-200 | LOW preview, awaiting the owner |
| `26-008 · Lion` | *Panthera leo* · VU | violet-200 | LOW preview, awaiting the owner |
| `26-009 · Polar Bear` | *Ursus maritimus* · VU | blue-300 | LOW preview, awaiting the owner |
| `26-010 · Giraffe` | *Giraffa camelopardalis* · VU | sky-300 | LOW preview, awaiting the owner |
| `26-011 · African Elephant` | *Loxodonta africana* · EN | orange-200 | LOW preview, awaiting the owner |
| `26-012 · Bengal Tiger` | *Panthera tigris tigris* · EN (species) | green-200 | LOW preview, awaiting the owner |
| `26-013 · Toco Toucan` | *Ramphastos toco* · LC | blue-200 | LOW preview, awaiting the owner |
| `26-014 · Hippo` | *Hippopotamus amphibius* · VU | yellow-200 | LOW preview, awaiting the owner |
| `26-015 · European Hedgehog` | *Erinaceus europaeus* · NT | emerald-100 | LOW preview, awaiting the owner |
| `26-016 · Axolotl` | *Ambystoma mexicanum* · CR | cyan-200 | LOW preview, awaiting the owner |
| `26-017 · Gray Wolf` | *Canis lupus* · LC | indigo-200 | LOW preview, awaiting the owner |
| `26-018 · Green Sea Turtle` | *Chelonia mydas* · LC | sky-200 | LOW preview, awaiting the owner |
| `26-019 · Nine-banded Armadillo` | *Dasypus novemcinctus* · LC | lime-200 | LOW preview, awaiting the owner |
| `26-020 · Scarlet Macaw` | *Ara macao* · LC | emerald-200 | LOW preview, awaiting the owner |
| `26-021 · Bottlenose Dolphin` | *Tursiops truncatus* · LC | orange-100 | LOW preview, awaiting the owner |
| `26-022 · Mountain Goat` | *Oreamnos americanus* · LC | violet-300 | LOW preview, awaiting the owner |
| `26-023 · European Rabbit` | *Oryctolagus cuniculus* · EN | lime-200 | LOW preview, awaiting the owner |
| `26-024 · Red-eyed Tree Frog` | *Agalychnis callidryas* · LC | pink-200 | LOW preview, awaiting the owner |
| `26-025 · Plains Zebra` | *Equus quagga* · NT | orange-300 | LOW preview, awaiting the owner |

The ten examples were made together at the owner's request (2026-11-16), then five and ten more the same day. Backgrounds are
rendered as calm pastels of the colour listed. `vf.py list` (or `render.bat` → `5`) shows the
live state; each folder's `overview.md` shows its stage.

## Inside an animal folder

| Path | Contents |
|---|---|
| `overview.md` | The front page: progress through the six phases, the export package with its IDs, the look, the files. Written by `vf.py overview` (and after preview, final, approve, register). |
| `animal.json` | The source of truth: names, status, `look` (palette, background, why), `info` (what the information artwork prints, every item citing a source id), `sources`, `stock` (titles, keywords), `approvals`, `notes`, `history`. |
| `docs/animal-info.md` | The full biological documentation, every statement numbered to a source. |
| `docs/references.md` | The numbered sources and every photograph (what it shows, author, licence, URL, use). |
| `docs/voxel-model.md` | The voxel brief: palette (= `animal.json`), size and pose, proportions per part, features, colour map, photos. Attach it with `key-prompt.md` to write `model.py`. |
| `assets/photos/` | Genuine photographs (public domain, CC0 or CC BY): modelling references; the hero photo also goes on the information artwork, credited. |
| `blender/model.py` | The voxel model (source of truth). |
| `blender/<code> · <Name>.blend` | The editable Blender project, built from `model.py` by `vf.py build` (or `render.bat`). Never edited by hand. |
| `blender/build.json`, `blender/README.md` | Stamp of the last build (Blender version, model, look and standards hashes, framing, render times) and its summary. |
| `export/` | `VF-<code>-ILL-1x1.png`, `-ILL-9x16`, `-ILL-16x9`, `-INF-1x1`, `-INF-9x16`, `-INF-16x9` (4096 px long side), and `stock/` JPEGs from `vf.py stock`. |
