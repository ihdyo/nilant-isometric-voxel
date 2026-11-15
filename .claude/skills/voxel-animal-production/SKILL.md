---
name: voxel-animal-production
description: The single source of truth for producing Voxel Fauna animals - isometric voxel animal illustrations made in Blender code for Gumroad, Adobe Stock and other stock sites. Covers the visual standards (true-isometric orthographic camera, large voxels, vivid solid Tailwind colours under Khronos PBR Neutral, one complementary flat background per species, composited shadow), the modelling standards (the voxel brief docs/voxel-model.md, key-prompt.md, the voxel grid in model.py), building and rendering (.blend from model.py, render.bat, ULTRA and LOW profiles adapted from Nilant), the six compositions, the Duolingo-style information artwork with a real photograph, research and sources, the registry and publish log, stock packaging, and the two owner approvals per animal. Use before creating, modelling, rendering, documenting or registering any animal, when asked to start the next animal, change the look, write card copy, render a preview or final, or prepare uploads.
---

# Voxel Fauna · voxel animal production

A collection of isometric voxel animal illustrations, one species per folder, each in six images: three
illustrations and three information artworks (1:1, 9:16, 16:9, 4096 px on the long side), sold on Gumroad and stock
sites (Adobe Stock first). It reuses Nilant's directory conventions and Blender render configuration
(`A:\WORK!!\_startup\Nilant`), adapted for still images. **Never rely on conversation history: this skill,
`CLAUDE.md` and the files are the instructions.**

## 0. Before touching any animal (every session)
1. Read this skill, `CLAUDE.md`, `_system/log/DECISIONS.md` (newest rows win) and `_system/log/PLAN.md`.
2. `python _system/studio/scripts/vf.py list`, then open the finished animals' `overview.md` and their previews or
   exports: new work must look like them (`03 Design/Reference/` holds the approved look sheets).
3. `python _system/studio/scripts/vf.py verify` must pass before and after your work.
4. Reuse the engine and the standards as they are. Do not change a standard (camera, voxel size, light, colour,
   materials, profiles, sizes, layouts, copy rules) without the owner's approval: show before/after stills, then
   `vf.py lock "what and why"` and `vf.py standards --write`.
5. Every animal passes two owner approvals: the LOW preview (`vf.py approve <code> preview`) before any ULTRA render,
   and the finished animal (`vf.py approve <code> final`). Never approve on the owner's behalf. The owner asked for
   the ten examples 26-001 to 26-010 at once (2026-11-16); after them, one new animal at a time unless the owner asks
   otherwise.

## 1. Visual standards
- **Camera:** orthographic, true isometric: azimuth 45° (Nilant pose convention: 0 = in front at −Y), elevation
  35.264°, deep focus. One camera setup for the whole collection; only the framing changes per composition.
- **Orientation:** head towards +X, back up, feet on z = 0, left flank at −Y. Through the camera the head is lower
  right and we see the face and the left flank together (three-quarter).
- **Large voxels:** 0.1 m voxels, the longest side 16–32 voxels (aim 24–30) whatever the species' real size; the
  smallest feature is one voxel. `merged` geometry (owner-approved 2026-11-15): one part's faces merge into flat planes,
  bevelled where the surface turns; parts meet with a visible seam, like an assembled toy.
- **Colour:** vivid but soft, solid Tailwind v4 tokens, satin plastic, no textures, no gradients. The view transform
  is **Khronos PBR Neutral** with a neutral `slate-100` sky fill (owner, 2026-11-16: Nilant's AgX + blue sky made the
  models pale; PBR Neutral renders base colours as authored). 3–6 palette keys per species; large areas shades
  50–800, small details any shade.
- **Background:** one flat Tailwind token per species, shade 50–300, complementing the animal (the hue opposite its
  main coat colour, or its habitat's colour for black, white or grey animals), at least ΔE 30 from the main colour.
  Nothing else in the frame.
- **Light and shadow:** rig `iso_top` (owner-approved): a warm key 55° high from the camera's front-left, a cool rim
  from behind without its own shadow; one soft shadow composited on the background.
- **Composition:** the whole animal visible, never cropped or stretched, centred with balanced space; each ratio
  framed on its own (`FRAMING`). Information artworks keep the animal in its zone and set the cards around it.
- **No brand in any export** (owner, 2026-11-15): no logo, watermark, signature or URL. The brand goes on the Gumroad
  cover and listing only. A photo credit line is not a brand and is required for CC BY photos.

## 2. Modelling standards
- Each animal has a **voxel brief**, `docs/voxel-model.md`: the palette table (must equal `animal.json → look.palette`;
  `vf.py check` compares them), size and pose, the proportions of each part (inclusive voxel ranges), the 3–5
  recognisable features in order, the colour map and the photos used.
- **`key-prompt.md`** (project root) + one `docs/voxel-model.md` is everything a model in a browser (Claude Sonnet,
  high effort) needs to write `blender/model.py`. It holds the full grid API, the conventions, the hard rules, the style
  rules, a worked example and a self-check. Keep it in step with `vf_voxel.py` and this section.
- `blender/model.py` defines `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (`box`, `ellipsoid`,
  `paint`, `carve`, `set`, `mirror`). It is the source of truth; the `.blend` is built from it and never edited by hand.
- Hard rules (enforced by `vf.py check`): longest side 16–32; lowest voxel at z = 0; one face-connected piece; only
  palette keys; parts named; the left side modelled then `g.mirror("-Y")`.
- Workflow: proportions from the photos → masses (`box`, `ellipsoid`) → step the silhouette → the recognisable
  features (made big enough to read at thumbnail size) → colour patches with `paint` → eyes (on a light voxel or the
  face corner, visible from the front-left) → `mirror` → `vf.py check` → `vf.py preview` and judge.
- Lessons from the first ten: a long neck must be about as long as the legs (giraffe); a mane must frame the face on
  every side, not sit behind it (lion); a solid dark muzzle block reads as a bear, keep only the nostrils dark
  (capybara); a dark eye on dark fur disappears, put it on the face corner or a light voxel (panda, penguin).
- Scene organisation (built by the engine): collections `Animal`, `Stage` (the ground), `Lights` (key and rim suns);
  six scenes `ILL 1x1` … `INF 16x9` linking them, each with its own orthographic camera `CAM · <scene>` and the ULTRA
  settings; a `README` text block. `blender/build.json` stamps the build (model, look and standards hashes).

## 3. Build and render (two profiles, one scene)
- **Build:** `vf.py build <code>` (or `render.bat` → 1) turns `model.py` into `blender/<code> · <Name>.blend`. A
  `.blend` is **stale** when `model.py`, the palette/background or the build standards changed since; stale files are
  rebuilt before any render.
- **Render from the built .blend:** `vf.py preview <code>` (LOW) and `vf.py final <code>` (ULTRA, needs the preview
  approval and refuses if the model or look changed after it) open the `.blend` and render. **`render.bat`**
  (`_system/studio/render/`, ported from Nilant's) renders every built animal offline: `2` LOW previews of all, `3`
  ULTRA finals of every approved animal; it skips finished images, so Ctrl+C is a pause.
- **ULTRA:** Nilant's ultra profile for one frame (EEVEE, full-resolution ray tracing with denoise, 4 shadow rays × 16
  steps, shadow resolution 1.0, light threshold 0.001, full-resolution fast GI), 256 samples on the animal pass (64 on
  the blurred shadow pass). About 5 min for a 1:1 and 1.5 min for a 9:16 or 16:9 on the owner's RTX 3050 (4 GB):
  15–20 min an animal.
- **LOW:** Nilant's still-review profile at ¼ size: 8 samples, 1 shadow ray × 2 steps, quarter-resolution ray tracing.
  About a second an image.
- **Not carried over from Nilant:** motion blur, bloom, the Bare Bones texture, 60 fps and video sizes, AgX (replaced
  by PBR Neutral for colour fidelity).
- **Shadow composite (EEVEE has no shadow catcher):** the animal over transparency (ground as holdout) and the shadow
  (animal as holdout, grey ground, Standard view); the shadow factor is blurred, given a 3 % dead zone and laid at
  strength 0.65 over the exact background hex in linear light. Open background = exactly the token's hex.

### The locked values
<!-- standards:begin -->
Standards version 1.0 · rig `iso_top` · geometry `merged` (generated from `vf_standards.py` by `vf.py standards --write`; do not edit by hand)

| Area | Value |
|---|---|
| Voxel | 0.1 m; longest side 16–32 voxels (target 24); smallest feature 1 voxel |
| Bevel | 0.012 m, 4 segments, profile 0.5 (round); `merged` geometry (bevel limit ANGLE, 30.0°) |
| Camera | ORTHO, azimuth 45.0°, elevation 35.264° (true isometric), distance 40.0 m, clip 0.1–200.0 m, no depth of field |
| Facing | head towards +X, back up, left flank at −Y (head lower right in frame) |
| Colour | view Khronos PBR Neutral, look None, exposure 0.0 |
| Key sun | orange-200, 2.4 W/m², rotation (35.0, 0.0, -50.0) + 45.0° turn, angle 0.12 rad, shadow True |
| Rim sun | indigo-200, 0.72 W/m², rotation (62.0, 0.0, 140.0) + 45.0° turn, angle 0.12 rad, shadow False |
| Sky fill | slate-100 × 0.5 |
| Plastic | roughness 0.62, specular 0.5, coat 0.08, coat_roughness 0.2, subsurface 0.1, subsurface_scale 0.06, subsurface_radius (0.8, 0.8, 0.8) (no texture) |
| Shadow | composited: strength 0.65, dead zone 0.03, blur 0.004 of the short side (twice), pass ground grey 0.25 |
| Background | one Tailwind token, shades 50–300, ΔE ≥ 30 from the main colour |
| Shared render base | BLENDER_EEVEE; use_raytracing True, use_shadows True, use_fast_gi True, fast_gi_method GLOBAL_ILLUMINATION, fast_gi_quality 0.75, fast_gi_step_count 12, fast_gi_ray_count 3, fast_gi_thickness_near 0.3, fast_gi_bias 0.02, fast_gi_distance 0.0; motion blur False; bloom False |
| ULTRA | scale 1.0; taa_render_samples 256, shadow_ray_count 4, shadow_step_count 16, shadow_resolution_scale 1.0, light_threshold 0.001, fast_gi_resolution 1; shadow pass samples 64; ray tracing resolution 1/1, denoise True |
| LOW | scale 0.25; taa_render_samples 8, shadow_ray_count 1, shadow_step_count 2, shadow_resolution_scale 1.0, light_threshold 0.01, fast_gi_resolution 2; shadow pass samples 8; ray tracing resolution 1/4, denoise True |
| Sizes (ULTRA) | 1x1 4096×4096, 9x16 2304×4096, 16x9 4096×2304 |
| Sizes (LOW) | 1x1 1024×1024, 9x16 576×1024, 16x9 1024×576 |
| Framing | ILL 1x1: zone (0.0, 0.0, 1.0, 1.0), fill 0.7; ILL 9x16: zone (0.0, 0.0, 1.0, 1.0), fill 0.82; ILL 16x9: zone (0.0, 0.0, 1.0, 1.0), fill 0.68; INF 1x1: zone (0.31, 0.32, 0.97, 0.71), fill 0.94; INF 9x16: zone (0.03, 0.215, 0.62, 0.475), fill 0.94; INF 16x9: zone (0.02, 0.08, 0.48, 0.95), fill 0.9 |
| Card system | radius 1.5u, lip 0.6u (background + 200), padding 1.4u, white tiles and cards, fun fact on the background family at 700; headings Home turf, On the menu, Fun fact! |
| Copy limits | common 22, scientific 34, kicker 30, stats 4, stat_label 12, stat_value 11, habitat 100, diet 95, fact 115, facts 2 |
| Photo licences | Public domain, CC0, CC BY 2.0, CC BY 2.5, CC BY 3.0, CC BY 4.0 (credited on the artwork) |
| Image ID | `VF-{code}-{kind}-{ratio}` (e.g. `VF-26-001-ILL-1x1`) |
<!-- standards:end -->

## 4. Production workflow (one animal, six phases, two approvals)
All commands: `python _system/studio/scripts/vf.py …` from the project root (or `render.bat` for building and
rendering).

1. **Research** — `vf.py new "<Common name>" "<Genus species>"`. Fill `docs/animal-info.md` from reliable sources
   (IUCN Red List assessment for the status, an Animal Diversity Web or museum/agency account for biology, papers with
   DOIs for surprising facts; check DOIs on Crossref; the ADW status is often out of date, always take the IUCN one),
   every statement numbered to `docs/references.md`; mark uncertain or general-knowledge statements as such. Photos:
   genuine, from Wikimedia Commons or agencies, licence **public domain, CC0 or CC BY only** (never BY-SA, NC, ND),
   at least two angles, logged with author, licence and page URL; downloads need the owner's OK of the batch.
2. **Modelling** — choose `look.palette` and `look.background` (write `look.why`), write `docs/voxel-model.md`, then
   `model.py` (yourself, or by attaching `key-prompt.md` + `docs/voxel-model.md` to Claude Sonnet in a browser),
   `vf.py check <code>` until clean.
3. **Preview** — `vf.py preview <code>` (or `render.bat` → 2) → `_system/cache/preview/<code>/<code> · preview
   sheet.png`. Judge with the checklist (section 8), fix, repeat; show the owner; **on the owner's OK only**
   `vf.py approve <code> preview`.
4. **Final** — `vf.py final <code>` (or `render.bat` → 3) → the six PNGs in `export/`. Look at every image full size.
   Copy changes later need no render: edit `animal.json`, then `vf.py info <code>`.
5. **Documentation and registry** — `vf.py overview <code>`, `vf.py register <code>`, `vf.py stock <code>`.
6. **Completion** — present the six exports; **on the owner's OK only** `vf.py approve <code> final`. Upload with the
   publishing checklist and record every upload event with `vf.py log`.

## 5. Information artwork (Duolingo-style cards, owner 2026-11-16)
- One card system in three arrangements (`INFO_LAYOUTS`), never a crop of another: chunky rounded white cards with a
  darker lip, a kicker pill, the name in Poppins ExtraBold, the scientific name in italics with an IUCN chip in the
  status colour, four stat tiles, "Home turf", "On the menu" and a full-colour "Fun fact!" card, and the **real
  photograph** in a white framed card with its credit (`Photo: <author> · <licence>`).
- Content (`animal.json → info`): `kicker` (Class · family in plain English, e.g. "Mammal · Dog family"),
  `conservation` (IUCN code and status), 4 `stats` (label ≤ 12, value ≤ 11 characters), `habitat` (≤ 100), `diet`
  (≤ 95), `facts` (2, ≤ 115; the first is printed), `photo` (file, author, licence, url, centre). Every item cites
  source ids and must match `docs/animal-info.md`.
- **Voice (Duolingo):** short, warm, playful, concrete. Lead with the surprising bit; one or two short sentences;
  everyday comparisons ("lighter than an apple"); second person when it helps; numbers with units; at most one
  exclamation per card; a light joke is fine, never at the animal's expense. Avoid AI-slop words: majestic,
  fascinating, remarkable, plays a crucial role, truly, testament, delve, tapestry, "Did you know that". A hypothesis
  is said as one ("maybe", "scientists think").
- Type never shrinks; too much text is an error naming the field to shorten (`vf.py check`). Numbers stay with their
  unit when lines wrap. Scientific names use real italics when `03 Design/Fonts/Poppins-MediumItalic.ttf` exists, else a
  sheared Poppins Medium.
- Colours come from the background's family (950 title and values, 700 labels and headings, background + 200 lips,
  the 700 shade for the fun-fact card with white type), checked for contrast.

## 6. Registry, publish log, IDs and stock
- Animal code `YY-SEQ`. Image ID `VF-<code>-<ILL|INF>-<ratio>`; the export file is `export/<Image ID>.png`. The
  registry `05 Publish/Voxel Fauna · Registry.xlsx` (Read Me, Animals, Images, Publish Log, Platforms; amber cells are
  the owner's); `vf.py register` upserts by code and ID.
- **Publish log** (as Nilant records each upload): `vf.py log <code|Image ID> <platform> <action> [--link] [--note]`
  appends a dated row to the registry's Publish Log sheet and to `05 Publish/Voxel Fauna · Publish Log.md`, and sets
  the image's platform cell. Actions: Submitted, Accepted, Rejected, Live, Removed, Updated.
- **Stock vs Gumroad:** the information artworks carry a third-party photograph, which stock sites' contributor terms
  do not let you license as your own work, so `vf.py stock` packages **only the three illustrations** for Adobe Stock
  and Shutterstock (JPEG, sRGB, XMP metadata, CSVs) and puts **all six** PNGs in the Gumroad zip, where the photo
  credit on the artwork satisfies CC BY. Start Adobe with ILL 1:1 and 16:9 (similar-content refusals); the
  generative-AI box stays unticked. Details: `01 Guide/Voxel Fauna · Stock Platforms.md`.

## 7. Key files
`key-prompt.md` (writes model.py) · `_system/studio/render/render.bat` (builds and renders offline) ·
`_system/studio/blender/vf_standards.py` (every number) · `_system/studio/scripts/vf.py` (the command line) ·
`02 Animals/_Template/` · `05 Publish/Voxel Fauna · Registry.xlsx` · `05 Publish/Voxel Fauna · Publish Log.md`.

## 8. Quality checklist (judge every preview and final against it)
- Modelling: the species is recognisable at thumbnail size; large consistent voxels; proportions match the photos;
  three-quarter orientation; eyes visible; consistent material treatment.
- Composition: isometric; the entire animal visible with balanced space; its own complementary background; one
  soft shadow.
- Rendering: LOW then ULTRA succeeded; sizes exactly 4096 on the long side; colours vivid (not grey or washed out);
  no artefacts (stray voxels, holes at seams, noise at ULTRA).
- Information artwork: every card fits; the copy reads in the Duolingo voice and matches the docs; the photo is the
  right species, well cropped, credited, licence allowed.
- Documentation: animal-info complete with sources; the IUCN status current; photos logged; the voxel brief matches
  the palette.
- Project: `.blend` current; files in the Voxel Fauna structure; IDs registered; uploads logged; `vf.py verify`
  passes; nothing temporary outside `_system/cache/`.

## 9. Cross-session rules
1. Read this skill before creating or modifying any animal. 2. Inspect the finished animals. 3. Reuse the engine and
the standards. 4. Same voxel, colour and material standards. 5. Three-quarter isometric view. 6. Large voxels.
7. An individual complementary background per species. 8. All six compositions. 9. Update the docs, the registry and
the publish log. 10. Never change a standard without documenting it (`DECISIONS.md`) and the owner's approval
(`vf.py lock`).

Generic Blender craft (supporting only; this skill wins where they differ): `bsk-blender-director`,
`bsk-creature-artist` (quadruped anatomy), `bsk-stylized-style` (shape language, palettes), `bsk-qa-review`.
