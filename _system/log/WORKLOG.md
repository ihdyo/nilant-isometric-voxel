# Voxel Fauna · work log

## 2026-11-15 · Project initialised (Claude, with the owner's answers)
- Read the brief (`00 TODO/voxel-isometric.txt`) and Nilant: `CLAUDE.md`, `README.md`, `STRUCTURE.md`, the studio
  skills (`nilant-modelling`, `-materials`, `-lighting`, `-lens-look`, `-render`, `-camera`), the engine
  (`nilant_stage`, `nilant_kit.render_setup`, `nilant_farm.pro_light`, `nilant_look`, `intro_overhaul.polish_set`,
  `nilant_takes.LENSES`), the workbook, `Master Prompt.txt`.
- Owner's answers: 4096 px long side; own registry workbook here; no brand in the exports; init = set up and prove
  the engine with a test render, then stop.
- Research on platforms (Adobe Stock: JPEG sRGB 4–100 MP ≤ 45 MB, similar-content refusals, the generative-AI
  checkbox; Shutterstock: JPEG ≥ 4 MP; Freepik renamed Magnific in April 2026). Written up in
  `01 Guide/Voxel Fauna · Stock Platforms.md`.
- Built the structure (Nilant's numbered folders mapped: `02 Animals`, `animal.json`), the skill
  `voxel-animal-production`, the engine (`vf_standards`, `vf_voxel`, `vf_scene`, `vf_job`), the command line
  (`vf.py`, `infographic`, `registry`, `stock`), the template, the registry workbook, guides and logs. Copied Poppins,
  the Tailwind palette and four generic `bsk-*` Blender skills from Nilant.
- Experiments in Blender 5.3.0: (1) a white-albedo ground under Nilant's rig in AgX renders at RGB 170,175,184, so
  pastel backgrounds cannot come from a lit ground; (2) EEVEE ignores `is_shadow_catcher`; holdout works and keeps
  shadows and depth. → two-pass composite over the exact hex.
- First LOW render with Nilant's rig exactly: a shadow 2.25× the animal's height running off the frame, plus a second
  shadow from the rim. Per-voxel cubes drew a grid on every face. Compare sheet of rig (`nilant`, `iso_top`) ×
  geometry (`block`, `merged`): `_system/cache/selftest/compare-sheet.png`. Provisional choice `iso_top` + `merged`,
  awaiting the owner (DECISIONS).
- Background exactness: a hard 0.985 cut-off left only 44–75 % of open pixels at the exact hex (LOW sampling noise,
  a few percent of falloff at the frame edges). A blurred shadow factor with a 3 % dead zone fixed every corner.
- Information layouts tuned against maximum-length text (21-character two-line name): 1:1 header 79 %, 9:16 header
  96 % and lower box 94 %, 16:9 column 97 % of their boxes. Poppins' line metrics replaced by a one-em line box.
- LOW selftest, six compositions: 0.4–1.7 s per image, 10 s for the whole run including the .blend.
- Sandboxed flow test (in `_system/cache/flowtest`, deleted after): `new` refuses a second folder for a species;
  `check` catches facts without sources; `register` twice gives 1 animal row and 6 image rows; `stock` writes 16.8 /
  9.4 MP JPEGs, both CSVs and the Gumroad zip.
- ULTRA on the RTX 3050 Laptop (4 GB): 4096×4096 renders (3.8 GB of VRAM). With 256 samples on both passes: ILL 1x1
  418 s (animal 232, shadow 186), INF 1x1 392 s. The shadow pass then kept 64 samples (it is blurred): ILL 16x9 78 s
  (animal 56, shadow 22), INF 16x9 84 s. Estimate per animal: 15–20 min. At 100 % the image is clean (no sampling
  noise, soft contact occlusion in concave corners, thin bevel highlights, exact background).
- Standards locked as v1.0 (provisional rig and geometry); `vf.py verify`: 0 problems.
- The owner approved the look (`iso_top` + `merged`). The compare sheet is now the first reference still
  (`03 Design/Reference/look · 2026-11-15 · rig and geometry.png`); `vf_standards.py` comments say APPROVED; relocked.

## 2026-11-16 · Colour, Duolingo cards, render.bat, key prompt, publish log, ten animals (Claude)
Owner: the model colour is pale; the info text reads like AI slop (make it Duolingo-style); put a real photo on the
infographic; at least 10 example animals with info and a voxel md; a publish log like Nilant; copy Nilant's render.bat
to render every built .blend offline; a root key-prompt.md that lets Sonnet in a browser write the model script from
two files; commit to GitHub.
- **Colour:** measured the lit top face of orange-400 under six treatments. AgX Base Contrast + blue sky
  (197,118,59) → Khronos PBR Neutral + slate-100 fill (241,123,40). Adopted (`vf_standards.COLOR`, `SKY`).
- **Cards:** `infographic.py` rewritten: white rounded cards with a lip, kicker pill, IUCN chip in status colour,
  2×2 / column stat tiles, Home turf / On the menu / Fun fact! cards, a framed real photo with its credit. Layouts
  tuned until every one of the ten animals' copy fits all three ratios (`vf.py check` caught 16 overflows first).
  Numbers now stay with their unit when lines wrap.
- **Build/render split:** `vf_job.py` can open a built `.blend` and render it; `vf.py build`, staleness from the model,
  look and build-standards hashes, `render-all`, resume (skips finished images). `render.bat` + `render_cli.py`
  ported from Nilant (finds and remembers Blender and a Python with Pillow/openpyxl; colour menu; Ctrl+C pauses).
- **Photos:** Wikimedia Commons API search filtered to PD / CC0 / CC BY (most top hits are CC BY-SA), contact sheets
  reviewed, 20 photos downloaded at 1600 px (HTTP 429 → retry with backoff); one candidate dropped because it was a
  mislabelled greater flamingo.
- **Research:** ADW accounts read for all ten; their IUCN statuses were stale for five species, so statuses come from
  the IUCN assessments, whose DOIs (and two papers') were checked on Crossref (two wrong DOIs from memory caught:
  the flamingo one was the Chilean flamingo, the lion one did not exist).
- **Models:** ten `model.py` written following `key-prompt.md`; first lineup → giraffe neck too short, lion mane
  behind the face, capybara too boxy with an invisible eye → fixed. All ten build and render; LOW previews done.
- **Publish log:** registry gains a Publish Log sheet; `vf.py log` writes it and the markdown log (tested in a sandbox).
- Stock packaging now defaults to the illustrations only (the information artworks carry a third-party photo).
