# Voxel Fauna · context for AI agents

**Voxel Fauna** is a Nilant side collection: isometric voxel animal illustrations made in Blender code, each species
delivered as six images (illustration + Duolingo-style information artwork with a real photo, at 1:1, 9:16 and 16:9,
4096 px on the long side), sold on **Gumroad** and stock sites (**Adobe Stock** first, then Shutterstock, Freepik and
others; see `01 Guide/Voxel Fauna · Stock Platforms.md`). The owner is ihdyo, who also runs Nilant (sibling folder
`../Nilant`); this project copies Nilant's directory conventions, naming, render.bat and Blender render configuration,
adapted for stills. Source of truth: `A:\WORK!!\_startup\nilant-voxel-isometric`; remote
`https://github.com/ihdyo/nilant-isometric-voxel` (branch `main`).

**Read before generating anything:** `.claude/skills/voxel-animal-production/SKILL.md` (the single source of truth for
production), `_system/log/DECISIONS.md` (newest rows win), `_system/log/PLAN.md` (what is open),
`03 Design/DESIGN-SYSTEM.md`. The owner's original brief is `00 TODO/voxel-isometric.txt`.

## Consistency contract (the same result whichever model or person works here)
1. **`python _system/studio/scripts/vf.py verify` before calling any work done.** It checks the standards lock, that
   the skill's standards table matches the code, every animal's files (sources, photo licence, voxel brief vs palette,
   card copy fits) and which `.blend` files are stale.
2. **The standards are locked** in `_system/data/standards.lock.json`: `vf_standards.py` (every number), `vf_voxel.py`,
   `vf_scene.py`, `vf_job.py`, `infographic.py`. Change one only for a reason, show the owner before/after stills
   (`vf.py selftest`, `vf.py selftest --compare`, an animal's preview), and only after the OK run
   `vf.py lock "what and why"` then `vf.py standards --write`. Never relock to make `verify` pass.
3. **Built files come from scripts:** an animal's `.blend` from its `blender/model.py` (`vf.py build`), the images from
   the built `.blend` (`vf.py preview|final`, `render.bat`), `overview.md` and `blender/README.md` from `vf.py`, the
   registry rows from `vf.py register`, publish-log rows from `vf.py log`. Never edit a built file by hand.
4. **Two approvals per animal, both the owner's:** the LOW preview (`vf.py approve <code> preview`, before any ULTRA
   render) and the finished animal (`vf.py approve <code> final`). Never approve on the owner's behalf.

## Status (2026-11-16)
- Engine, skill, template, registry, guides, `render.bat` and `key-prompt.md` in place; rig `iso_top` approved;
  colour changed to Khronos PBR Neutral + neutral fill (owner: "the model colour is so pale").
- **Bulky, posed blocky-mob look APPROVED and locked, standards v2.1** (owner, 2026-11-16, after three rounds: "minecraft mobs vibes", "keep the
  texture flat solid", then "blocky bulk style like the attached image", rotatable sections, flat plates, a pose and
  an expression per animal, voxels scaled to real size, colours free of Tailwind; then stacked sections with no holes,
  expressions painted flat, vivid pastel backgrounds): geometry `mob`, `vf_voxel` layers, joints and plates,
  `vf_color.py`. Before/after: `03 Design/Reference/look · 2026-11-16 · bulky posed before-after.jpg` (round 2) and
  `look · 2026-11-16 · flat faces before-after.jpg` (round 3, the approved look).
- **Twenty-five example animals** (owner, 2026-11-16) 26-001 Red Fox … 26-010 Giraffe, 26-011 African Elephant …
  26-015 European Hedgehog, then 26-016 Axolotl, 26-017 Gray Wolf, 26-018 Green Sea Turtle, 26-019 Nine-banded
  Armadillo, 26-020 Scarlet Macaw, 26-021 Bottlenose Dolphin, 26-022 Mountain Goat, 26-023 European Rabbit, 26-024
  Red-eyed Tree Frog, 26-025 Plains Zebra: research docs with verified sources (ADW, IUCN assessments read on the
  IUCN site and their DOIs on Crossref, papers), 50 genuine photos (PD / CC0 / CC BY), voxel briefs, models, built
  `.blend`, LOW previews in `_system/cache/preview/`. **No preview approved yet**, so no ULTRA finals.
- **Plates switched off** (owner, 2026-11-16: "disable flat pixel for now"): `vf_standards.POSE["plates"] = False`;
  every part is whole voxels. **Information cards redesigned** to breathe (pixel-art icon badges, roomier cards, the
  photo as a tilted sticker). Both approved by the owner and locked as standards v2.1 (2026-11-16).
- **Rigging and animation** are planned in `_system/log/PLAN.md` (armature from the joints, walk/idle cycles,
  expressions), not started.
- Awaiting the owner: the twenty-five preview approvals, the Poppins italic download, contributor names and Gumroad licence.

## Hard rules
- **One source of truth each:** numbers in `_system/studio/blender/vf_standards.py`; an animal's names, look, card copy,
  photo, sources, stock metadata and approvals in its `animal.json`; its geometry in `blender/model.py`; its modelling
  brief in `docs/voxel-model.md` (palette must equal `animal.json`); the registry and publish log in
  `05 Publish/Voxel Fauna · Registry.xlsx` (+ `Voxel Fauna · Publish Log.md`).
- **Colours:** Tailwind v4 tokens by default (`03 Design/Color/tailwind-v4-palette.json`); a `#RRGGBB` hex where no
  token fits (owner, 2026-11-16: "for this project, break from tailwind coloring token"); backgrounds render muted.
- **No AI-generated images, ever** (animals, references, backgrounds, photos on the artwork).
- **Photos:** genuine, public domain, CC0 or CC BY only (never BY-SA, NC, ND), logged in the animal's
  `docs/references.md` with author, licence and URL, credited on the information artwork. Stock sites get the
  illustrations only (the information artworks carry a third-party photo); Gumroad gets all six.
- **No brand in the exports** (owner, 2026-11-15): no logo, watermark, signature or URL in the six images.
- **Facts:** every fact on an information artwork cites a source in `animal.json → sources` and matches
  `docs/animal-info.md`; the IUCN status comes from the IUCN assessment (ADW pages are often out of date); uncertain or
  general-knowledge statements are marked as such in the docs.
- **Card copy:** the Duolingo voice of the skill (section 5): short, warm, concrete, no AI-slop words.
- **Downloads** (photos, fonts, anything) only after the owner approves the batch; log fonts in `04 Library/README.md`.
- **Naming (Nilant/Kodey style):** numbered top folders `NN Name`; human-facing files `Voxel Fauna · Title`; animal
  folders `YY-SEQ · Common Name`; exports named by Image ID `VF-<code>-<ILL|INF>-<ratio>.png`.
- **Language:** English everywhere.

## Map
| Path | What |
|---|---|
| `key-prompt.md` | attach it with one animal's `docs/voxel-model.md` to Claude Sonnet (browser) to write that animal's `model.py` |
| `00 TODO/` | the owner's brief and scratch prompts (not part of the pipeline) |
| `01 Guide/` | `Voxel Fauna · Production Workflow`, `· Stock Platforms`, `· Prerequisites` |
| `02 Animals/` | `_Template/` and one folder per species `YY-SEQ · Common Name/`: `overview.md` (generated), `animal.json`, `docs/animal-info.md`, `docs/references.md`, `docs/voxel-model.md`, `assets/photos/`, `blender/model.py` + the built `.blend` + `build.json` + `README.md`, `export/` (six PNGs, `stock/` JPEGs) |
| `03 Design/` | `DESIGN-SYSTEM.md`, `Color/` (Tailwind v4 palette), `Fonts/` (Poppins, OFL), `Reference/` (approved look sheets) |
| `04 Library/` | licence and download log |
| `05 Publish/` | `Voxel Fauna · Registry.xlsx` (Read Me, Animals, Images, Publish Log, Platforms), `Voxel Fauna · Publish Log.md`, `Voxel Fauna · Publishing Checklist.md`, `Stock/` (CSVs), `Gumroad/` (zips) |
| `_system/studio/render/` | `render.bat` (double-click: build and render offline), `Voxel Fauna · How to Render.md`, `README.md` (status of every animal) |
| `_system/studio/blender/` | engine (bpy): `vf_standards.py`, `vf_voxel.py` (the grid), `vf_scene.py` (meshes, stage, cameras, profiles, passes, composite), `vf_job.py` (one Blender run: build, or open a .blend and render), `selftest_model.py` |
| `_system/studio/scripts/` | `vf.py` (command line), `render_cli.py` (render.bat's menu), `vflib.py`, `infographic.py` (cards), `registry.py`, `stock.py` |
| `_system/data/`, `_system/log/`, `_system/cache/` | standards lock + brand; WORKLOG / DECISIONS / PLAN; previews, plates, job logs (git-ignored) |
| `.claude/skills/` | `voxel-animal-production` (ours, canonical); `bsk-*` generic Blender craft (MIT, from Nilant) |

## Commands (`python _system/studio/scripts/vf.py <command>` from the project root)
`doctor` · `list` · `new "<Common>" "<Genus species>"` · `check <code> [--strict]` · `build <code>` · `preview <code>`
(LOW from the .blend + contact sheet) · `approve <code> preview|final` (owner's word only) · `final <code>` (ULTRA into
`export/`, resumes) · `render-all LOW|ULTRA` · `info <code> [--profile LOW|ULTRA]` (re-lay the cards only) ·
`overview <code>` · `register <code>` · `stock <code> [--only …]` · `log <code|Image ID> <platform> <action>` ·
`selftest [--ultra] [--ratios 1x1] [--compare]` · `verify` · `lock "<what and why>"` · `standards [--write]`.
`render.bat` runs build / previews / finals from a menu. Blender is found through `BLENDER`, then
`_system/studio/blender_path.txt` (written by render.bat), then the regular 5.3.0 install Nilant uses.

## Gotchas learned
- **EEVEE has no shadow catcher** (`is_shadow_catcher` is Cycles only; tested in 5.3.0), and a lit ground in AgX tops
  out near RGB 170,175,184 even with a white albedo. Hence the two-pass composite over the exact hex.
- **AgX greys out saturated colours:** orange-400 (255,137,4) rendered (197,118,59) under Nilant's AgX + blue sky;
  Khronos PBR Neutral + a slate-100 fill gives (241,123,40). Sheet: `03 Design/Reference/look · 2026-11-16 · colour fidelity.png`.
- **Nilant's key sun is 24° high:** from an isometric camera it throws a shadow 2.25× the animal's height off the
  frame; `iso_top` raises it to 55° and turns the rim's shadow off.
- **ADW conservation statuses are often stale** (panda, red panda, koala, giraffe, emperor penguin all differ from the
  current IUCN assessment): take the status from the IUCN DOI, verified on Crossref.
- **Wikimedia Commons rate-limits** (HTTP 429): retry with backoff, 1.5–2 s between calls, a generic User-Agent.
  Most top results are CC BY-SA, which cannot go on a sold image: filter licences first.
- The shadow pass at LOW is noisy and EEVEE darkens the frame edges a few percent: the blur and 3 % dead zone fix it.
- PNGs are read back in Blender as `Non-Color` with straight alpha; Blender's `image.save()` of a byte image writes the
  buffer as is.
- Poppins' own metrics leave a third of an em of air above each line; the composer measures one em from the ascender
  top (`Pen.ASC = 0.74`) and keeps numbers with their unit when wrapping.
- `cmd /c render.bat` from a shell whose working directory contains `!` fails ("not recognized"); run it by its full
  path or double-click it (it `cd`s to its own folder).
- Bash heredocs in this harness mangle backslashes and some apostrophes: write files with the Write/Edit tools.
