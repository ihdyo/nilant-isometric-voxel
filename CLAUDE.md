# Voxel Fauna · context for AI agents

**Voxel Fauna** is a Nilant side collection: isometric voxel animal illustrations made in Blender code, each species
delivered as an export package (owner, 2026-11-17): two 4096 master renders (the dynamic pose and the regular
blocky pose, each cropping to 1:1, 9:16 and 16:9), a looped animation (GIF) and an A5 card PDF
in English and in Bahasa Indonesia (front: minimal and playful, the model and the info, no photo for now; back:
the blocky model, "powered by ihdyo"), sold on **Gumroad** and stock sites (**Adobe Stock** first, then Shutterstock, Freepik and
others; see `01 Guide/Voxel Fauna · Stock Platforms.md`). The owner is ihdyo, who also runs Nilant (sibling folder
`../Nilant`); this project copies Nilant's directory conventions, naming, render.bat and Blender render configuration,
adapted for stills. Source of truth: `A:\WORK!!\_startup\nilant-voxel-isometric`; remote
`https://github.com/ihdyo/nilant-isometric-voxel` (branch `main`).

**Read before generating anything:** `.claude/skills/voxel-animal-production/SKILL.md` (the single source of truth for
production), `_system/log/DECISIONS.md` (newest rows win), `_system/log/PLAN.md` (what is open),
`03 Design/DESIGN-SYSTEM.md`. The owner's original brief was `00 TODO/voxel-isometric.txt` (removed by the owner on 2026-11-21; in git history);
`00 TODO/` holds the owner's current prompts until they are done.

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
5. **Every animal goes all the way to rigged and animated** (owner, 2026-11-17): `animal.json → motion` set,
   `vf.py preview` (stills, then rig, rig check and loops) or `vf.py rig`; `verify` fails for any animal with a
   model that is not rigged, checked and animated.
6. **Sections are named from `vf_standards.SECTION_STEMS` only** (2026-11-18; `key-prompt.md` rule 5): the rig's
   motions and the loop stacking go by the name (limbs `leg`/`shin`/`foot`/`flipper`/`arm` drawn behind the body,
   every other section over it, `STACK_LEVELS`), and `vf.py check` rejects any other name. A new kind of section is
   added to the standards (and the motion library) first, never invented in one model. Fix a render problem in the
   engine for every animal, never in one animal's model or files.

## Status (2026-11-18)
- Engine, skill, template, registry, guides, `render.bat` and `key-prompt.md` in place; rig `iso_top` approved;
  colour changed to Khronos PBR Neutral + neutral fill (owner: "the model colour is so pale").
- **Bulky, posed blocky-mob look APPROVED and locked, standards v2.1** (owner, 2026-11-16, after three rounds: "minecraft mobs vibes", "keep the
  texture flat solid", then "blocky bulk style like the attached image", rotatable sections, flat plates, a pose and
  an expression per animal, voxels scaled to real size, colours free of Tailwind; then stacked sections with no holes,
  expressions painted flat, vivid pastel backgrounds): geometry `mob`, `vf_voxel` layers, joints and plates,
  `vf_color.py`. Before/after: `03 Design/Reference/look · 2026-11-16 · bulky posed before-after.jpg` (round 2) and
  `look · 2026-11-16 · flat faces before-after.jpg` (round 3, the approved look).
- **Twenty-five example animals** (owner, 2026-11-16) 000001 Red Fox … 000010 Giraffe, 000011 African Elephant …
  000015 European Hedgehog, then 000016 Axolotl, 000017 Gray Wolf, 000018 Green Sea Turtle, 000019 Nine-banded
  Armadillo, 000020 Scarlet Macaw, 000021 Bottlenose Dolphin, 000022 Mountain Goat, 000023 European Rabbit, 000024
  Red-eyed Tree Frog, 000025 Plains Zebra: research docs with verified sources (ADW, IUCN assessments read on the
  IUCN site and their DOIs on Crossref, papers), 50 genuine photos (PD / CC0 / CC BY), voxel briefs, models, built
  `.blend`, LOW previews in `_system/cache/preview/`; all 25 previews approved (2026-11-17).
- **Plates switched off** (owner, 2026-11-16: "disable flat pixel for now"): `vf_standards.POSE["plates"] = False`;
  every part is whole voxels. **Information cards redesigned** to breathe (pixel-art icon badges, roomier cards, the
  photo as a tilted sticker). Both approved by the owner and locked as standards v2.1 (2026-11-16).
- **Animation rig** (owner, 2026-11-17: "rig the animal now"): `vf.py rig` / `rig-all` turn each built
  still `.blend` into `blender/<code> · <Name> · Rig.blend` + `· Rig.glb` (armature `VF · armature` from the joints,
  sections skinned to one mesh with rigid weights, the action `pose` = the approved still), with looping actions
  from the motion library in
  `vf_rig.py` (idle, walk, flap, hop, swim, waddle + species specials) chosen in `animal.json → motion`, and GIF
  previews in `_system/cache/preview/<code>/anim/`. All twenty-five rigged and checked (`vf.py rig-check`: every
  vertex on one bone, each bone bent moves exactly its sections; T-pose sheet
  `02 Animals/Voxel Fauna · Twenty-five examples · rig check (T-pose).jpg`); approved and locked in v2.2 (below);
  expressions and video exports not started (`_system/log/PLAN.md`).
- **Six models reworked** (owner, 2026-11-17): the polar bear in two body sections (upper and lower, no neck), the
  flamingo's and the frog's legs in upper and lower parts, the koala, wolf and rabbit standing on all four feet.
- **Owner approved all 25 models and the motion** (2026-11-17): the 25 preview approvals recorded, the motion locked
  as standards v2.2 (`vf_standards.MOTION`, `vf_rig.py` in the lock).
- **Export package APPROVED and locked, standards v2.2 + the export package** (owner, 2026-11-17: "i approve everything"): `blender/vf_export.py` renders the two masters and the loop
  frames from the rig (`vf.py final`, `render.bat` → 3, rendering only); `scripts/package.py` builds
  the GIF and the A5 cards offline (`vf.py package`, `render.bat` → P); Indonesian copy in
  `animal.json → i18n.id` for all 25. Checked end to end at LOW on all 25; the ULTRA renders run on the RTX 3050
  (this second PC has an Intel UHD 730, which crashes on a 4096 ULTRA pass). The card front v5: no photo, the Nilant
  wordmark top right, the model centred on its body with its own rendered shadow, a few particles in the background's
  tints, the fun fact on a straight-edged band; `vf_export.py` (with `EXPORT`) and `package.py` are in the lock.
- **Export trimmed** (owner, 2026-11-17): `export/` = the two masters, the loop GIF and the two cards, plus
  `VF-<code>-STOCK.jpg` (the whole dynamic master as the stock JPEG, no crop, no `stock/` folder).
- **Render fixes** (owner, 2026-11-18): no halo (`vf_scene._smooth_shadow`, shadow blurred over open ground only);
  no flicker in the loops (`STACK_LEVELS`: limbs 0, body 0.05, other sections 2.05 voxels towards the camera, in
  the loops' animal pass only; checked bias off/on on all 25); section names enforced (`SECTION_STEMS`). Every
  `.blend` and rig rebuilt; `vf_scene`, `vf_rig`, `vf_export`, `vf_standards`, `vf_color`, `package.py` differ from
  the lock (not relocked: the owner relocks after seeing the ULTRA results).
- **The owner's list of 2026-11-21 (the first prompt), done for 000001–000025, LOCKED as standards v2.3:**
  - **Six-digit animal codes** (`000001`, folders `000001 · Red Fox`, Image IDs `VF-000001-…`) for all 100 animals,
    in every file, name and document (`vflib.CODE_DIGITS`, `next_code`).
  - **Tailwind removed:** `03 Design/Color/tailwind-v4-palette.json` deleted; every colour is a hex (the tokens'
    exact values); card colours come from the background's hue on `vf_color.RAMP` (`"#RRGGBB-700"`).
  - **Backgrounds at one chroma:** OKLCH (0.87, 0.06, hue), the hue per animal from its habitat or the complement of
    its coat (`look.background`, `background_oklch`, `background_name`, `why`; `BACKGROUND_RULE`, ΔE ≥ 20).
  - **Registry split:** `05 Publish/Voxel Fauna · Registry.xlsx` lists the animals' information (all 100,
    `vf.py registry`); each platform has its own workbook in `05 Publish/Platforms/` (items, state, publish log).
  - **Models:** the red panda's tail at its first size (drawn behind the body), the flamingo's neck on the body (anchored), the lion's mane shorter,
    the wolf without a neck, the rabbit one block with inset thighs and side front legs, the frog's arms in one piece
    and its hind legs two clapperboard boards inset in the flanks, the toucan's bill duotone and smaller bird feet
    (toucan, penguin, macaw); every animal re-posed livelier with the head turned to the camera (yaw about −14°),
    the loops keeping it on the camera; only the static blocky pose looks straight ahead (owner: "make it look at
    camera except for the static basic pose").
  - **Engine:** `Grid.anchor()` sinks every turning section into its parent near its hinge (2.5 voxels,
    `ANCHOR_REACH`; no floating necks or tails); nested
    stacking levels (the tiger's flickering face); tails drawn behind the body in the loops (`STACK_BEHIND`); the trunk curl and sway, the hippo's walking yawn
    (`motion.options.walk_jaw`), a bird's feet in the hop and flap, the wolf's howl lifting the head (`howl_lift`).
  - **A face layer was tried on 000001 and removed entirely** (owner: "undo everything that face related"): every
    face stays painted flat, and the engine has no face-layer code.
  - All 25 rebuilt, rigged (rig check PASS) and looped at LOW; previews need the owner's approval again.
- Next: the owner's review of the 25 LOW
  previews (`vf.py approve <code> preview`), the ULTRA renders
  (`render.bat` → 3, then P) and `approve <code> final`; then `00 TODO/026-100.txt` (the next 75 animals). Still
  awaiting the owner: the Poppins italic download, contributor names and Gumroad licence.

## Hard rules
- **One source of truth each:** numbers in `_system/studio/blender/vf_standards.py`; an animal's names, look, card copy,
  photo, sources, stock metadata and approvals in its `animal.json`; its geometry in `blender/model.py`; its modelling
  brief in `docs/voxel-model.md` (palette must equal `animal.json`); the animals' information in
  `05 Publish/Voxel Fauna · Registry.xlsx` (built from `animal.json`); the platform targets and their publish logs in
  `05 Publish/Platforms/Voxel Fauna · <Platform>.xlsx` (+ `Voxel Fauna · Publish Log.md`).
- **Colours:** every colour is a `#RRGGBB` hex (owner, 2026-11-21: "remove the tailwind color palette completely").
  Backgrounds: OKLCH lightness 0.87, chroma 0.06 for every animal, the hue chosen per animal (`BACKGROUND_RULE`).
- **No AI-generated images, ever** (animals, references, backgrounds, photos on the artwork).
- **Photos:** genuine, public domain, CC0 or CC BY only (never BY-SA, NC, ND), logged in the animal's
  `docs/references.md` with author, licence and URL, credited on the information artwork. Stock sites get the
  stock image only (`STOCK.jpg`, the dynamic master; the cards carry a third-party photo); Gumroad gets the whole export package.
- **No brand in the exports** (owner, 2026-11-15): no logo, watermark, signature or URL in the masters, the stock
  image or the loop. The one exception (owner, 2026-11-17): the back of the A5 card carries "powered by" + the
  ihdyo mark + "ihdyo", small, black on a light background and white on a dark one (`03 Design/Logo/`); and the front of the card carries the
  Nilant wordmark ("nilant" alone, no head) top right (owner, 2026-11-17).
- **Facts:** every fact on an information artwork cites a source in `animal.json → sources` and matches
  `docs/animal-info.md`; the IUCN status comes from the IUCN assessment (ADW pages are often out of date); uncertain or
  general-knowledge statements are marked as such in the docs.
- **Card copy:** the Duolingo voice of the skill (section 5): short, warm, concrete, no AI-slop words.
- **Downloads** (photos, fonts, anything) only after the owner approves the batch; log fonts in `04 Library/README.md`.
- **Naming (Nilant/Kodey style):** numbered top folders `NN Name`; human-facing files `Voxel Fauna · Title`; animal
  folders `NNNNNN · Common Name` (six-digit code, `000001 · Red Fox`); exports named by Image ID `VF-<code>-<ILL|INF>-<ratio>.png`.
- **Language:** English everywhere.

## Map
| Path | What |
|---|---|
| `key-prompt.md` | attach it with one animal's `docs/voxel-model.md` to Claude Sonnet (browser) to write that animal's `model.py` |
| `00 TODO/` | the owner's brief and scratch prompts (not part of the pipeline) |
| `01 Guide/` | `Voxel Fauna · Production Workflow`, `· Stock Platforms`, `· Prerequisites` |
| `02 Animals/` | `_Template/` and one folder per species `NNNNNN · Common Name/`: `overview.md` (generated), `animal.json`, `docs/animal-info.md`, `docs/references.md`, `docs/voxel-model.md`, `assets/photos/`, `blender/model.py` + the built `.blend` + `build.json` + `README.md` (+ the animation rig `· Rig.blend`, `· Rig.glb`, `rig.json`), `export/` (the export package: `VF-<code>-MASTER-DYN.png`, `-MASTER-BLOCK.png`, `-LOOP.gif`, `-CARD-EN.pdf`, `-CARD-ID.pdf`; beside them `-STOCK.jpg`, the dynamic master as the stock JPEG, no crop) |
| `03 Design/` | `DESIGN-SYSTEM.md`, `Color/` (the colour rules; hex only), `Fonts/` (Poppins, OFL), `Logo/` (the owner's ihdyo mark, for the card back), `Reference/` (approved look sheets) |
| `04 Library/` | licence and download log |
| `05 Publish/` | `Voxel Fauna · Registry.xlsx` (Read Me, Animals: the animal information), `Platforms/Voxel Fauna · <Platform>.xlsx` (one per platform: Read Me, Items, Publish Log), `Voxel Fauna · Publish Log.md`, `Voxel Fauna · Publishing Checklist.md`, `Stock/` (CSVs), `Gumroad/` (zips) |
| `_system/studio/render/` | `render.bat` (double-click: build, LOW previews, ULTRA renders, offline), `P` in its menu packages offline: GIF, cards, stock JPEG and CSVs, zip, registry, `Voxel Fauna · How to Render.md`, `README.md` (status of every animal) |
| `_system/studio/blender/` | engine (bpy): `vf_standards.py`, `vf_voxel.py` (the grid), `vf_scene.py` (meshes, stage, cameras, profiles, passes, composite), `vf_job.py` (one Blender run: build, or open a .blend and render), `vf_rig.py` (the animation rig and motion library, locked), `vf_export.py` (the ULTRA export renders: masters and loop, proposed), `selftest_model.py` |
| `_system/studio/scripts/` | `vf.py` (command line), `render_cli.py` (render.bat's menu), `vflib.py`, `infographic.py` (card system), `package.py` (GIF, A5 cards; locked), `registry.py`, `stock.py` |
| `_system/data/`, `_system/log/`, `_system/cache/` | standards lock + brand; WORKLOG / DECISIONS / PLAN; previews, plates, job logs (git-ignored) |
| `.claude/skills/` | `voxel-animal-production` (ours, canonical); `bsk-*` generic Blender craft (MIT, from Nilant) |

## Commands (`python _system/studio/scripts/vf.py <command>` from the project root)
`doctor` · `list` · `new "<Common>" "<Genus species>"` · `check <code> [--strict]` · `build <code>` · `preview <code>`
(LOW from the .blend + contact sheet, then rig and loops) · `approve <code> preview|final` (owner's word only) ·
`final <code> [--low]` (the two masters and the loop frames; resumes) · `package <code> [--low]` · `package-all` · `package-pending [code]` · `render-all LOW|ULTRA` · `info <code> [--profile LOW|ULTRA]` (re-lay the cards only) ·
`overview <code>` · `register <code>` · `stock <code> [--only …]` · `log <code|Image ID> <platform> <action>` ·
`registry` (the Animals sheet from every animal.json) · `selftest [--ultra] [--ratios 1x1] [--compare]` · `rig <code> [--force] [--no-preview]` (animation rig + GIF loops) ·
`rig-all [--jobs 3]` (+ the motion lineup) · `rig-check [<code>]` (T-pose renders + bend test) · `verify` · `lock "<what and why>"` · `standards [--write]`.
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
- Bash heredocs in this harness mangle backslashes and some apostrophes: write files with the Write/Edit tools. A
  Python script fed through stdin (`python - <<EOF`) also failed to save `Voxel Fauna · Registry.xlsx` (OSError 22 on
  the `·` path) while the same code from a file worked: run multi-line Python from a file.
- **Anchored sections:** `load_model` runs `Grid.anchor()`, so a model's voxel count and its parts' layers include
  the anchor cells (a section's cells inside its parent). Count and compare models through `load_model`, never by
  reading `model.py` alone.
- **ULTRA needs the RTX 3050:** on the second PC (Intel UHD Graphics 730, integrated) any 4096 ULTRA pass ends in
  Vulkan `VK_ERROR_DEVICE_LOST` and empty passes ("shadow pass: almost no open ground"), on OpenGL too; LOW works.
  Check the GPU (`Get-CimInstance Win32_VideoController`) before blaming the code.
- **Halo:** blurring the shadow factor over the animal's holdout (counted as unshadowed) lifts a light ring along the
  silhouette; `vf_scene._smooth_shadow` blurs over the open ground only (normalised convolution). Keep it that way.
- **Loop flicker from stacked sections:** overlapping whole sections cut through each other differently every frame
  as they turn (the panda's head through the body, a leg's outer face in the plane of the body's side). Fixed by the
  per-section depth nudge in the loops' animal pass (`STACK_LEVELS`); a 2-voxel nudge on the body hid the leg parts
  in front of it and made the legs look shorter, so the body only gets 0.05. In Blender 5.3 a Geometry Nodes modifier
  input cannot be set with `mod[identifier] = value` ("id properties not supported"): the offset is a per-vertex
  attribute (`vf_bias`) read by a Named Attribute node. Check a new kind of animal with bias off/on frames.
- **Animation previews:** switching `is_holdout` between passes makes EEVEE resync, so `vf_rig` renders each pass as
  one animation (about 0.75 s animal + 1.1 s shadow a frame at 512 px on the RTX 3050) and composites afterwards. In
  Blender 5.3 an action takes its keys through a slot; a new action gets one on its first key, and reassigning an
  action picks the slot `OBVF · armature` by name.
