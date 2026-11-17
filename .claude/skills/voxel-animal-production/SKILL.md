---
name: voxel-animal-production
description: The single source of truth for producing Voxel Fauna animals - isometric voxel animal illustrations made in Blender code for Gumroad, Adobe Stock and other stock sites. Covers the visual standards (true-isometric orthographic camera, large voxels, vivid solid Tailwind colours under Khronos PBR Neutral, one complementary flat background per species, composited shadow), the modelling standards (the voxel brief docs/voxel-model.md, key-prompt.md, the voxel grid in model.py), building and rendering (.blend from model.py, render.bat, ULTRA and LOW profiles adapted from Nilant), the LOW review compositions, the export package (two master renders, the stock image, the loop GIF, the A5 card in English and Indonesian), the Duolingo-style card system with a real photograph, research and sources, the registry and publish log, stock packaging, and the two owner approvals per animal. Use before creating, modelling, rendering, documenting or registering any animal, when asked to start the next animal, change the look, write card copy, render a preview or final, or prepare uploads.
---

# Voxel Fauna · voxel animal production

A collection of isometric voxel animal illustrations, one species per folder, each delivered as an export package
(owner, 2026-11-17): two 4096 master renders (the dynamic pose and the regular blocky pose, each cropping to 1:1,
9:16 and 16:9), a 1:1 stock image, a looped animation and an A5 card in English and Indonesian; sold on Gumroad
and stock sites (Adobe Stock first). The six LOW compositions (illustrations and information artworks at 1:1, 9:16
and 16:9) remain the review sheets. It reuses Nilant's directory conventions and Blender render configuration
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
   the ten examples 26-001 to 26-010 at once (2026-11-16), then five more (26-011 to 26-015) and ten more
   (26-016 to 26-025); after them, one new animal at a time unless the owner asks otherwise.

## 1. Visual standards
- **Camera:** orthographic, true isometric: azimuth 45° (Nilant pose convention: 0 = in front at −Y), elevation
  35.264°, deep focus. One camera setup for the whole collection; only the framing changes per composition.
- **Orientation:** head towards +X, back up, feet on z = 0, left flank at −Y. Through the camera the head is lower
  right and we see the face and the left flank together (three-quarter).
- **Voxels scale with the animal** (owner, 2026-11-16: "add more pixel for larger animal, but keep it blocky
  bulky", "scale with real size"): 0.1 m voxels; the posed longest side follows the species' real longest dimension
  (`animal.json → look.size.real_m`, sourced): target 28 × L^0.4 ± 15 % (`SIZE_RULE`), so a 1 m red panda gets 28, a
  2.8 m lion 42, a 5 m giraffe 53. The smallest feature is one voxel.
- **Bulky blocky-mob look** (owner, 2026-11-16: "minecraft mobs vibes", "keep the texture flat solid", "blocky bulk
  style like the attached image"; approved by the owner 2026-11-16, standards v2.0): `mob` geometry, each section one or
  two big sharp-edged boxes (no bevel, flat shading), matte, flat solid colours: a big body box, a big head box,
  thick pillar legs, block tails, slab or plate ears. The style of block-building games, never a copy of one game's
  creature, and never named after a game in titles, keywords or listings (trademark; stock sites refuse it). The old
  look was `merged` (bevelled satin plastic, approved 2026-11-15).
- **Posed sections** (owner: "on assembling them, they can rotate the section so it looks more dynamic", "subtle
  tilts, but make it dynamic pose that different for every animal based on animal personality"): sections turn at
  their joints (≤ 40°), children follow their parent (ears and brows on the head); every species gets a pose from its
  personality (written in the brief). **Plates** (flat surfaces) are switched off for now (owner, 2026-11-16:
  "disable flat pixel for now, maybe it is exist in future, but not for current animals"): every part, feet
  included, is made of whole voxels; `vf.py check` refuses `plate()`.
- **Stacked sections** (owner: "stack the block, dont make a hole of it ... apply for all animal"): every part is its
  own layer of voxels; sections that overlap (an ear set into the head, the head into the mane) both stay whole, so a
  turned section never leaves a hole in its neighbour.
- **Expression, painted flat** (owner: "set the animal expression to not flat", then "dont extrude the mouth and
  eyebrow like that. they should flat", with a block-game character as the reference): eyes (a white eye with the
  pupil to the inside, or a dark eye with a glint, or a sleepy line), brows (a darker strip whose steps give the
  mood) and the mouth (a U smile, a smirk, a dot) are colours on the face voxels, flush; never plates or blocks.
- **Colour:** vivid but soft, matte, flat, no textures, no gradients. Tailwind v4 tokens by default; a hex is allowed
  where no token fits (owner, 2026-11-16: "for this project, break from tailwind coloring token"). The view transform
  is **Khronos PBR Neutral** with a neutral `slate-100` sky fill (owner, 2026-11-16: Nilant's AgX + blue sky made the
  models pale; PBR Neutral renders base colours as authored). 3–7 palette keys per species; large areas shades
  50–800, small details any shade.
- **Background:** one flat colour per species (a Tailwind token at shade 50–300, or a soft hex), complementing the
  animal (the hue opposite its main coat colour, or its habitat's colour for black, white or grey animals),
  rendered as a **vivid pastel** (owner: "the background color is too vibrant, make it slightly desaturated so the
  animal more popup", then "keep the background vivid but pastel (not too vibrant or neon), keep it calm"): OKLCH
  chroma capped at 0.07, lightness held in 0.85–0.93, hue kept (soft tokens such as sky-200 unchanged, neon ones
  calmed); the card lips and the fun-fact card get the same chroma factor; at least ΔE 30 between the main colour and
  the rendered background. Nothing else in the frame.
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
- `blender/model.py` defines `build(g)` on the grid of `_system/studio/blender/vf_voxel.py` (`box`, `paint`, `carve`,
  `set`, `plate`, `joint`, `mirror`). Parts are built in place in a straight rest pose, then turned at their joints
  (`joint(part, pivot, rotate, parent)`); `_l` parts mirror to `_r` with their joints; joints set after `mirror()`
  make the pose asymmetric. It is the source of truth; the `.blend` is built from it (one object per part, its origin
  on the hinge, its rotation set, so a section can still be turned in Blender to try a pose) and never edited by hand.
- Hard rules (enforced by `vf.py check`): the posed longest side inside the animal's size budget; rest-pose lowest
  voxel at z = 0 (the engine grounds the posed animal); one face-connected piece in the rest pose; joints ≤ 40° with
  the pivot on the part; only palette keys; the left side modelled then `g.mirror()`.
- Workflow (bulky blocky mob): proportions from the photos → one big box per section (body, head, thick legs, tail;
  a second box only for a real feature; no `ellipsoid`, no stair-stepped curves) → the recognisable features,
  exaggerated like a toy → colour shapes with `paint` (flat, no speckles) → the face painted flat (white eye + inner
  pupil, a brow strip, a mouth; the snout box with a dark nose row) → `mirror()` → the pose from the personality
  (head turned to the camera and cocked, ears, tail, a stride or a lifted paw) → `vf.py check` → `vf.py preview` and
  judge.
- Lessons from the first ten: a long neck must be about as long as the legs (giraffe); a mane must frame the face on
  every side, not sit behind it (lion); a solid dark muzzle block reads as a bear, keep only the nostrils dark
  (capybara); a dark eye on dark fur disappears, put it on a light voxel or a white dot (panda, penguin); a light
  voxel inside an ear reads as an extra eye on the front, keep ears one colour or rimmed (fox, red panda); two dark
  voxels on a muzzle's top corners read as a second pair of eyes (giraffe); black flippers on a black body vanish,
  hold them out over a white flank (penguin); long legs need a knee (upper leg + shin) or a stride looks stiff (lion,
  zebra, giraffe), and two-part legs read on birds and frogs too (flamingo, frog: upper and lower part), built the
  same on both sides so the animal can walk on them (a leg drawn folded never reaches the ground); four-legged
  animals stand on all four feet, never sit (owner, 2026-11-17: koala, wolf, rabbit), so every one can walk; a big
  head goes high on the front of the body or it hides the front legs (koala); a long body can be two sections, upper
  and lower, turning at the waist, with the head straight on the shoulders (polar bear); a hippo's muzzle is wider
  than its skull and the open jaw hinges under it.
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

### Animation rig and motion (APPROVED and locked 2026-11-17, standards v2.2)
- **Motion v2 (PROPOSED 2026-11-17, owner: "really dynamic ... tilt the head, ear, etc ... not blindly look at camera"):** every action carries the life layer `_alive()` (`MOTION.life`): the head looks around (yaw biased away from the camera), tilts and nods, shared with the neck; each ear perks and tips on its own beat; tails wag; folded wings flutter with one fuller flap a loop (the flamingo flaps a little as it walks); the body sways and rolls with the stride. Walk, flap, hop and waddle run two cycles a loop (`MOTION.cycles`, 48 frames), and the legs swing wider (26°, 20° with a knee, 24° on two legs). Every term is a whole number of cycles a loop, so loops stay seamless.
- `vf.py rig <code>` (or `vf.py rig-all --jobs 3`) opens the built still `.blend` and saves a rigged copy beside it,
  `blender/<code> · <Name> · Rig.blend`, plus `· Rig.glb` (glTF binary, Y up, one animation per action) and the stamp
  `blender/rig.json`. The still `.blend` and the stills are never touched. A rig is stale when the still is rebuilt,
  `animal.json → motion` changes or `vf_rig.py` changes; `verify` fails until it is rigged again (owner, 2026-11-17).
- **Armature `VF · armature`** ("rig" alone in this project means the light rig `iso_top`): `root` on the ground under
  the body (grounding and hops) → `body` (every section without a joint) → one bone per `g.joint` section on its
  hinge, parented like the joints. **Skin:** the sections joined into one mesh `VF · animal`, every vertex weighted
  1.0 to its section's bone (a vertex group per bone) and deformed by an Armature modifier: rigid, so the blocks
  stay crisp, and it reads as rigged in any tool (weight paint, glTF skin). The rest pose is the model as drawn (the
  T-pose); the action `pose` is the approved still (matches it to a few micrometres, vertex by vertex).
- **Rig check** (`vf.py rig-check [<code>]`, also run by every `rig`): every vertex carries exactly one full
  weight; each bone bent in turn moves its own section and everything below it, and nothing else; renders of the
  T-pose and of every bone bent, sections coloured by bone, bones in yellow on top, with the bone list →
  `_system/cache/preview/<code>/anim/VF-<code>-RIG-check.png` and the sheet of all
  `02 Animals/Voxel Fauna · Twenty-five examples · rig check (T-pose).jpg`. A FAIL names the bone, and `verify`
  fails until it passes.
- **Motion library** (`_system/studio/blender/vf_rig.py`): every action is the still plus offsets, so a loop starts
  and ends on the approved look; walking legs replace their still angles. Each frame is grounded on its posed voxels
  (lowest corner on z = 0), so planted feet stay planted without foot targets; a hop adds its height. Actions: `idle`
  (head look, ear flick, tail, trunk, jaw, gills, tongue), `walk` (diagonal pairs on stiff legs like a block-game mob,
  shins fold on the swing; a `sprawler` sweeps its legs about the vertical and bends its body; a two-legged bird
  steps leg over leg, the lower leg folding on the swing and the feet kept flat), `flap`, `hop`, `swim`,
  `waddle`, and the specials `howl`, `doze`, `shake`, `yawn`, `fan`, `reach`, `sniff`. 24 fps; idle 48 frames, walk 24
  (32 from 40 voxels long).
- **Per animal** (`animal.json → motion`): `plan` (walker, sitter, bird, swimmer, sprawler, hopper), `actions`,
  optional `frames` per action, `base` (still angles replaced in one action: the hippo walks with its jaw shut) and
  `signature` (the loop shown in the lineup; default the first after `idle`).
- **Section names matter:** the library finds sections by name, so models keep them: `head`, `neck`, `torso`, `mane`,
  `leg_fl/fr/hl/hr`, `shin_*`, `leg_l/r` + `foot_l/r` (two legs), `wing_*`, `flipper_l/r`, `flipper_hl/hr`, `arm_*`,
  `ear_*`, `tail`, `tail_tip`, `flukes`, `trunk_1…3`, `jaw`, `tongue`, `gill_*`, `snout`/`muzzle`/`nose`/`beak`.
- **Previews:** every action at 512 px, 12 fps, with the stills' two-pass shadow composite at LOW samples, into
  `_system/cache/preview/<code>/anim/VF-<code>-ANIM-<action>.gif`; `rig-all` also writes the lineup
  `02 Animals/Voxel Fauna · Twenty-five examples · motion (LOW preview).gif`.
- **On the owner's approval of the motion:** move `RIG` into `vf_standards.py`, add `vf_rig.py` to
  `vflib.LOCKED_FILES`, `vf.py lock`. Still to do (PLAN.md): expressions (blinks, mouth states), video exports (MP4
  loops through render.bat), knees for the short-legged walkers.

### The export package (APPROVED and locked 2026-11-17, standards v2.2 + the export package: the masters, the stock image, the loop and the card)
Per animal, in `export/` (the IDs `VF-<code>-<item>`; numbers in `blender/vf_export.py → EXPORT`, locked with the file):
| Item | What |
|---|---|
| `MASTER-DYN.png` | the master render, dynamic pose (the action `pose`, the approved still): 4096 square on the animal's background with the composited shadow; the animal inside the centre 2304 safe square, so a centred 1:1, 9:16 (2304 × 4096) or 16:9 (4096 × 2304) crop never cuts it |
| `MASTER-BLOCK.png` | the same for the regular blocky pose (the rest pose, every joint straight, set on the ground) |
| `STOCK.jpg` | the image for stock sites: the whole dynamic master (4096 square, 16.8 MP, no crop) as an sRGB JPEG with its title and keywords, beside the package in `export/` (owner 2026-11-17: no crop, no `stock/` folder); not in the Gumroad zip |
| `LOOP.gif` | the looped dynamic animation: the signature action (motion.signature, else the first after idle), 1080 square, 24 fps |
| `CARD-EN.pdf`, `CARD-ID.pdf` | the A5 card (148 × 210 mm, 3 mm bleed, 300 dpi, trim box set), one per language. Front, minimal and playful, no photograph for now: the animal's pastel, the name big with the scientific name and IUCN chip, the Nilant wordmark top right, the dynamic model (its body centred) with its own rendered shadow among a few small particles (the background family's 400-600 tints, mixed shapes), four boxless stats with pixel icons, home and menu in two columns, the fun fact on a full-bleed band with a straight top edge. Back: the blocky master with "powered by" + the ihdyo mark + "ihdyo", small at the bottom, black on a light background and white on a dark one (the only place the brand appears) |
- **Two batch files:** `render.bat` → 3 only renders (owner: "render.bat should be rendering only (2 image and 1
  motion)"): `vf.py final <code>` renders the two masters into `export/` and their cut-outs and the loop frames into
  `_system/cache/plates/<code>/ULTRA/` (`blender/vf_export.py`, from the rig `.blend`). `package.bat` (beside it)
  builds the rest offline (`scripts/package.py`): the stock crop, the GIF, both cards, the stock JPEG and CSVs, the
  Gumroad zip and the registry rows (`vf.py package-pending [code]`, or `render.bat` → P).
- **Layouts at LOW:** `vf.py final <code> --low` and `vf.py package <code> --low` build the whole package small into
  `_system/cache/export-low/<code>/` (page previews in `_system/cache/preview/<code>/card/`).
- **Indonesian copy:** `animal.json → i18n.id` (common, kicker, stats, habitat, diet, facts): the same facts and
  sources as `info`, translated; numbers in Indonesian style (1,5–1,8 m; 1.200 m); `check` requires it once the
  preview is approved. Type never shrinks: the packager names the text to shorten.
- **ULTRA needs the RTX 3050:** a 4096 ULTRA pass crashes an integrated GPU (Vulkan "device lost"; the Intel UHD 730
  of the second PC); LOW and the packaging run anywhere.

### The locked values
<!-- standards:begin -->
Standards version 2.2 · rig `iso_top` · geometry `mob` (generated from `vf_standards.py` by `vf.py standards --write`; do not edit by hand)

| Area | Value |
|---|---|
| Voxel | 0.1 m; posed longest side 16–56 voxels: target 28 × (real longest dimension in m)^0.4 ± 15%; smallest feature 1 voxel |
| Pose | sections turn at their joints, at most 40° on any axis, ears, snout and jaw follow their parent; plates (flat surfaces) switched off for now: whole voxels only; the face is painted flat; the posed animal is set on z = 0 |
| Motion | armature from the joints, sections skinned with rigid weights, rest pose = the model as drawn, action `pose` = the still; 24 fps; idle 48 frames, walk 24 (32 from 40 voxels long); legs swing 22° stiff, 17° over a knee folding 34°, two legs 20° folding 45°; hops 0.22 of the length; every frame grounded |
| Geometry | `mob`: one part's faces merge into flat planes; sharp box edges (no bevel), flat shading, flat solid colours; one voxel layer per part, so overlapping sections stack whole (no holes) |
| Camera | ORTHO, azimuth 45.0°, elevation 35.264° (true isometric), distance 40.0 m, clip 0.1–200.0 m, no depth of field |
| Facing | head towards +X, back up, left flank at −Y (head lower right in frame) |
| Colour | view Khronos PBR Neutral, look None, exposure 0.0 |
| Key sun | orange-200, 2.4 W/m², rotation (35.0, 0.0, -50.0) + 45.0° turn, angle 0.12 rad, shadow True |
| Rim sun | indigo-200, 0.72 W/m², rotation (62.0, 0.0, 140.0) + 45.0° turn, angle 0.12 rad, shadow False |
| Sky fill | slate-100 × 0.5 |
| Material | matte: roughness 0.86, specular 0.3, coat 0.0, coat_roughness 0.2, subsurface 0.0, subsurface_scale 0.06, subsurface_radius (0.8, 0.8, 0.8) (no texture) |
| Shadow | composited: strength 0.65, dead zone 0.03, blur 0.004 of the short side (twice), pass ground grey 0.25 |
| Background | one colour per animal (Tailwind shade 50–300 or hex, OKLCH L ≥ 0.8), rendered as a vivid pastel: OKLCH chroma ≤ 0.07, lightness 0.85–0.93 (card colours from its family get the same chroma factor); ΔE ≥ 30 from the main colour |
| Shared render base | BLENDER_EEVEE; use_raytracing True, use_shadows True, use_fast_gi True, fast_gi_method GLOBAL_ILLUMINATION, fast_gi_quality 0.75, fast_gi_step_count 12, fast_gi_ray_count 3, fast_gi_thickness_near 0.3, fast_gi_bias 0.02, fast_gi_distance 0.0; motion blur False; bloom False |
| ULTRA | scale 1.0; taa_render_samples 256, shadow_ray_count 4, shadow_step_count 16, shadow_resolution_scale 1.0, light_threshold 0.001, fast_gi_resolution 1; shadow pass samples 64; ray tracing resolution 1/1, denoise True |
| LOW | scale 0.25; taa_render_samples 8, shadow_ray_count 1, shadow_step_count 2, shadow_resolution_scale 1.0, light_threshold 0.01, fast_gi_resolution 2; shadow pass samples 8; ray tracing resolution 1/4, denoise True |
| Sizes (ULTRA) | 1x1 4096×4096, 9x16 2304×4096, 16x9 4096×2304 |
| Sizes (LOW) | 1x1 1024×1024, 9x16 576×1024, 16x9 1024×576 |
| Framing | ILL 1x1: zone (0.0, 0.0, 1.0, 1.0), fill 0.7; ILL 9x16: zone (0.0, 0.0, 1.0, 1.0), fill 0.82; ILL 16x9: zone (0.0, 0.0, 1.0, 1.0), fill 0.68; INF 1x1: zone (0.31, 0.32, 0.97, 0.71), fill 0.94; INF 9x16: zone (0.03, 0.215, 0.62, 0.475), fill 0.94; INF 16x9: zone (0.02, 0.08, 0.48, 0.95), fill 0.9 |
| Card system | radius 2.2u, lip 0.9u (background + 200), padding 2.0u, white tiles and cards, fun fact on the background family at 700; headings Home turf, On the menu, Fun fact! |
| Copy limits | common 22, scientific 34, kicker 30, stats 4, stat_label 12, stat_value 11, habitat 100, diet 95, fact 115, facts 2 |
| Photo licences | Public domain, CC0, CC BY 2.0, CC BY 2.5, CC BY 3.0, CC BY 4.0 (credited on the artwork) |
| Image ID | `VF-{code}-{kind}-{ratio}` (e.g. `VF-26-001-ILL-1x1`) |
<!-- standards:end -->

## 4. Production workflow (one animal, six phases, two approvals; every animal rigged and animated)
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
   set `animal.json → motion` (plan and actions, section 3), `vf.py check <code>` until clean.
3. **Preview, rig and motion** — every animal goes all the way to rigged and animated (owner, 2026-11-17: "for
   future generation of animals, ensure it have everything until it rigged and animated"). `vf.py preview <code>`
   (or `render.bat` → 2) renders the six stills → `_system/cache/preview/<code>/<code> · preview sheet.png`, then
   rigs the animal, runs the rig check and renders a loop of every action → `.../anim/` (`--stills` skips the
   motion while iterating on the model). Judge with the checklist (section 8), fix, repeat; show the owner the
   stills and the loops; **on the owner's OK only** `vf.py approve <code> preview`. `vf.py verify` fails for any
   animal with a model that is not rigged, checked and animated.
4. **Final** — `vf.py final <code>` (or `render.bat` → 3, on the RTX 3050) renders the two masters and the loop;
   then `render.bat` → P (or `vf.py package <code>`) builds the stock image, the GIF and the two cards. Look at every
   item full size (the card PDFs at 100 %). Copy changes later need no render: edit `animal.json`, package again.
5. **Documentation and registry** — `render.bat` → P writes the stock files, the Gumroad zip, the registry rows and
   the overview (or `vf.py stock`, `vf.py register`, `vf.py overview`).
6. **Completion** — present the export package; **on the owner's OK only** `vf.py approve <code> final`. Upload with the
   publishing checklist and record every upload event with `vf.py log`.

## 5. Information artwork (Duolingo-style cards, owner 2026-11-16)
- One card system in three arrangements (`INFO_LAYOUTS`), never a crop of another: chunky rounded white cards with a
  darker lip and room to breathe (owner, 2026-11-16: "make it breathe"), a kicker pill, the name in Poppins
  ExtraBold, the scientific name in italics with an IUCN chip in the status colour, four stat tiles each led by a
  pixel-art icon badge (span, weight, heart, egg, bolt or star by the label), "Home turf", "On the menu" and a
  full-colour "Fun fact!" card each led by an icon badge (house, apple, light bulb), the text centred in its card,
  and the **real photograph** in a thick white frame pasted like a slightly tilted sticker, with its credit
  (`Photo: <author> · <licence>`).
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
- **Stock vs Gumroad:** the cards carry a third-party photograph, which stock sites' contributor terms do not let
  you license as your own work, so `vf.py stock` packages **only the stock image** (`STOCK.jpg`, the dynamic master) for Adobe
  Stock and Shutterstock (JPEG, sRGB, XMP metadata, CSVs) and puts **the whole export package** in the Gumroad zip,
  where the photo credit on the card satisfies CC BY. The generative-AI box stays unticked. Details: `01 Guide/Voxel Fauna · Stock Platforms.md`.

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
7. An individual complementary background per species. 8. The whole export package, rigged and animated. 9. Update the docs, the registry and
the publish log. 10. Never change a standard without documenting it (`DECISIONS.md`) and the owner's approval
(`vf.py lock`).

Generic Blender craft (supporting only; this skill wins where they differ): `bsk-blender-director`,
`bsk-creature-artist` (quadruped anatomy), `bsk-stylized-style` (shape language, palettes), `bsk-qa-review`.
