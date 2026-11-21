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

## 2026-11-16 · The blocky-mob look, three rounds, and five more animals (Claude, with the owner)
- **Round 1** (owner: "make it have minecraft mobs vibes"): geometry `mob` (sharp boxes, matte), one box per part, the
  face on the front of the head. A pixel-shaded texel skin was tried on the fox and dropped (owner: "keep the texture
  flat solid"). Style rules from Blockbench's Minecraft style guide; `vf.py check` refuses game names in stock metadata.
- **Round 2** (owner's reference images: bulky, rotated sections, flat feet): `vf_voxel` joints with parents and
  mirrored `_l`/`_r` parts, plates, the posed animal grounded by the engine; voxels scaled to real size; `vf_color.py`
  (hex colours, OKLCH); a pose and an expression per species; backgrounds muted ×0.55.
- **Round 3** (owner: no holes, flat faces, "vivid but pastel", better flamingo feet, five more animals): one voxel
  layer per part; faces painted flat; backgrounds as capped-chroma pastels (the ×0.55 mute greyed soft colours); the
  panda moved to the hex #BFD7A7 (every Tailwind lime/green pastel sat within ΔE 30 of its white fur).
- **Five more animals** 000011 to 000015: ADW accounts; IUCN DOIs found and checked on Crossref (ADW stale for the
  elephant, EN not VU, and the hedgehog, NT since 2024); papers for the fun facts checked on Crossref; 10 photos from
  Commons (licences re-checked at download). "Hippopotamus" did not fit the 16:9 header (type never shrinks), so the
  folder and name are "Hippo".
- Lessons: a white hole in a black eye patch reads as a letter (panda); two dark voxels on a muzzle read as a second
  pair of eyes (giraffe); a straight trunk reads as a pipe, curl it up (elephant); a box bill needs a taper (toucan).
- Owner approved the look; standards relocked as v2.0.

## 2026-11-17 · The animation rig and motion library, proposed (Claude)
- Owner: "rig the animal now" (the rigging plan added on 2026-11-16).
- **`vf_rig.py`** (new, not in the lock): opens the built still `.blend`, adds the armature `VF · armature` (root on
  the ground → body → one bone per `g.joint` section on its hinge, parented like the joints), puts every section
  back in the model's drawn pose and skins it (see below), keys the actions, frames a scene `ANIM 1x1` on
  everything every action does, saves `<code> · <Name> · Rig.blend` and exports `· Rig.glb`. The action `pose`
  reproduces the still to 1.4 µm (fox, checked section by section against the still `.blend`).
- **Motion library:** every action is the still plus offsets in each section's own axes, converted to the bone's
  frame; walking legs replace their still angles; each frame is grounded on its posed voxel corners (numpy), so
  planted feet stay planted and the walk gets its bob for free. Actions per animal in `animal.json → motion`.
- **Previews:** the stills' two-pass shadow composite at 512 px and LOW samples, each pass rendered as one animation
  (switching holdouts per frame made EEVEE resync: 2.5 s a frame before, about 1.9 s after), GIFs at 12 fps.
- **Commands:** `vf.py rig <code>`, `vf.py rig-all --jobs 3` (three Blender runs at once, ~1.75× faster on the RTX
  3050), render.bat `R`; `verify` notes stale rigs; `check` validates `motion`. Docs: skill section 3, CLAUDE.md,
  PLAN.md, key-prompt.md (section names the rig relies on), How to Render.
- **Owner: "the rig still not rigging all the armature, the head for most animal still not rigged, the ear and gills
  also, the dolphin tail ... check whether the animal is rigged properly or not yet at T posed render".** The first
  version bone-parented each section: the parts followed their bones, but the mesh had no Armature modifier and no
  weights (nothing shows as rigged in weight paint or the modifier stack), and the head and ear motion was too small
  to read. Now the sections are joined into one mesh `VF · animal`, a vertex group per bone at weight 1.0, deformed by
  an Armature modifier; head turns doubled (±10°), ear flicks 26°, gills ±18°.
- **`vf.py rig-check`** (also inside every `rig`): one full weight per vertex; each bone bent 30° in turn must move its
  section and everything below it and nothing else; Workbench renders of the T-pose and of every bone bent, sections
  coloured by bone, bones drawn on top in yellow. All twenty-five PASS (7 to 19 bones each). The skinned `pose` action
  matches the still vertex by vertex to 5 µm (fox, elephant, axolotl, wolf, dolphin).
- **Six models reworked** (owner's list): polar bear (no neck; `body` + `torso` at the waist, front legs and head on the torso), flamingo (`leg` + `shin` + `foot` both sides, the folded leg bent at the knee), frog (thigh + shank-and-foot, upper arm + forearm-and-hand), koala, wolf and rabbit standing on four feet (koala: body raised on longer legs and the head lifted, the first try hid the front legs; wolf: knees, a neck ruff, the howl standing with neck and head raised 20° + 22°). Motion: the hop drives the lower legs, the walk rolls an upper body, the howl lifts the neck. All six pass `vf.py check` and the rig check; lineups refreshed.
- **Rabbit and frog after the owner's reference images, flamingo feet:** the rabbit and frog rebuilt (the frog first came out 19.4 voxels long, over its 16–18 budget: body and feet one voxel shorter, head turn eased); the folded flamingo foot drawn with the same `foot()` as the standing one (`d = -1`, toes back). All three pass the rig check; their loops re-rendered.
- **Every animal all the way to rigged and animated** (owner): `check` requires `motion`, `preview` and render.bat 2 rig and animate after the stills, `verify` fails without a current, passing rig; template and brief updated.
- **Turtle, rabbit, frog, flamingo, goat, zebra** (owner's list): the shell and the rabbit's rump lose their top layer, the rabbit's front legs grow to 6 voxels and its hind feet flatten to 1, the frog's feet sit under the thighs, the goat's hump goes, the zebra's mane runs down the back of the neck (the first, one-voxel mane hid behind the 7-wide neck from the camera: neck narrowed to 5, mane 3 wide and 3 deep). The flamingo's folded leg was drawn folded, so it could not walk: both legs are now built the same and the still lifts one within the 40° joints; `vf_rig` gains a two-legged walk (`_biped`, RIG leg_swing_biped 20°, knee_fold_biped 45°), the flamingo's actions are pose, idle, walk, flap.
- **Flamingo feet smaller** (owner): `foot()` now 3 × 3 on both legs; re-previewed, rigged (check PASS) and looped; lineups refreshed.

## 2026-11-17 · Approvals, the motion lock and the export package (Claude, with the owner)
- Owner: all 25 models good; answers: approve previews + motion, 4096 masters, GIF loop 1080, two cards (one per language), render.bat renders only and a second bat packages offline. 25 preview approvals recorded; `RIG` moved to `vf_standards.MOTION`, `vf_rig.py` added to the lock, `vf.py lock` (v2.2), stills and rigs rebuilt (verify clean).
- `blender/vf_export.py`: the two masters from the rig (`pose` action / rest pose grounded), framed in the centre safe square (FRAMING MASTER at run time), the stills' two-pass composite with dither, the animal pass kept as the card cut-out; the loop's frames at a LOOP profile (64 samples, 1080). `scripts/package.py`: stock crop, GIF, A5 card PDF via PyMuPDF (trim and bleed boxes) on the approved card system (infographic.Pen), Indonesian through a language context (headings, IUCN names) and `animal.json → i18n.id`; the ihdyo mark rendered from its SVG by PyMuPDF.
- `vf.py final` renders the package (resumes), `--low` for layouts; `vf.py package` / `package-all`; stock.py (the stock image only; the Gumroad zip of the package), registry.py (the six package items), check (the masters once Final; `i18n.id` once approved), overview, render_cli (option 3), `package.bat`.
- The first ULTRA test crashed the GPU (Vulkan device lost, empty passes), on OpenGL too, and the approved stills pipeline the same way: this PC has an Intel UHD 730. ULTRA runs on the RTX 3050; LOW validated everything here.
- **Card redesign** (owner): front without the photo, minimal and playful (package.py `_front`); the footer ink by background luminance (`ink_on`). All 25 cards fit in English and Indonesian at LOW.
- **Card v3** (owner: push the design, judge by best practice): audit of v2 (no clear second focal point, eight unrelated sizes, 5.7 pt labels, cramped bottom, divider noise, random confetti, no contrast check), then the rebuild; the circle sized from the larger of the model's width and 0.66 of its height so tall animals (giraffe, flamingo) get one too. All 25 pass in both languages.
- **Card v4** (owner): `_front` reads the shadow factor from the dynamic master (master / background; under the animal's edge the darkest ground nearby, so no halo), particles drawn before the shadow; FRONT.particles. **Giraffe** without the tongue: model.py, animal.json palette, voxel brief; rebuilt, rigged, loops, preview re-approved on the owner's word, LOW masters re-rendered.
- **Card v5** (owner): `_front` centres the animal's alpha box and scales so the wider half (with the shadow) fits; FRONT.particles count 12, shades 400-600; `_nilant()` places the Nilant logo by `ink_on`. All 25 repackaged at LOW; sheets `02 Animals/Voxel Fauna · Twenty-five examples · cards (EN|ID).jpg`.
- **Card v5 final** (owner): the Nilant head removed, the wordmark SVG alone (`_nilant()` renders it with PyMuPDF); all 25 repackaged at LOW. **Export package approved and locked** as standards v2.2 + the export package (`vf_export.py`, `package.py` in `LOCKED_FILES`).
- **Tone + motion v2** (owner): `vf_color.tone()` + `ANIMAL_TONE` in `vf_scene.plastic`; `vf_rig._alive()` on idle, walk (four legs, two legs, sprawl), flap, hop, swim, waddle; `MOTION.cycles`, `MOTION.life`. Reference sheet kept out of git (third-party image) in `_system/cache/reference/`. Before frames in `_system/cache/before-v2/`.

## 2026-11-21 · The owner's list: six-digit codes, hex colours, one-chroma backgrounds, the registry split, model fixes, candid poses, the face layer test (Claude)
- **Codes:** a one-off script renamed every `26-NNN` folder, file and text mention to `000NNN` (1115 text files, 1512
  names, the cache included); `vflib.animal_dirs` globs six digits, `next_code` gives `000101`; docs updated.
- **Colours:** `vf_color` without the Tailwind palette (hex, `"#RRGGBB-700"` ramp shades, `background()`, `ramp()`,
  `nearest_shade()`); every animal.json palette converted to the exact hex; new backgrounds (the first 25 chosen one by
  one: habitat or complement; 26–100 keeping their hue) at OKLCH chroma 0.06, lightness 0.87 or lowered for contrast;
  briefs' palette tables and background lines synced; infographic, package and stock on the ramp and the background
  name; `vf.py check` on hex and the background rule.
- **Registry:** `registry.py` rewritten (the Animals sheet with the information; six platform workbooks with Items and
  Publish Log); `vf.py registry`; `vf.py log` per platform; the old workbook (no typed data) rebuilt.
- **Engine:** `Grid.anchor()` + the loose-section check, `Grid.decal/eye/brow/mouth`, `face_meta`, decal shift in
  `scaled()` and `mirror()`; nested stacking in `vf_scene.stack_level`; `vf_rig`: `Pose.loc/scl` keyed for face
  bones, `_face()` (glances, blinks, brows), `_trunk()`, the walking yawn and the howl lift as `motion.options`, bird
  feet in hop and flap.
- **Models:** the fixes and poses (see DECISIONS); briefs' sizes, parts, pose lines and proportion tables refreshed.
- **Renders:** all 25 rebuilt and previewed at LOW (stills, rig, rig check, loops); before images kept in
  `_system/cache/before-2026-11-21/`; before/after sheets in `02 Animals/`.
- **Owner's follow-up:** "undo the expression change for all models. the animal should still see the camera in
  dynamic pose, otherwise make them look straight forward": the fox's painted face restored as committed; every head
  turned to the camera (yaw −14 to −16, its neck, mane or torso straight), the penguin, flamingo, toucan, macaw and
  dolphin straight ahead; briefs, docstrings, skill, key-prompt, CLAUDE.md updated; all 25 rebuilt again.
- **Owner, again:** "undo everything that face related, to make it look at camera except for the static basic
  pose": the face-layer code removed from `vf_voxel`, `vf_rig` and `vf_standards`; the birds' and the dolphin's
  heads turned to the camera too; the life layer centred on the camera (look 7°, bias 0, tilt 5°); all 25 rebuilt.
