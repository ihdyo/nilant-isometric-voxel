# Voxel Fauna · open items

## Done
- 2026-11-15 · The look approved by the owner: rig `iso_top` + geometry `merged`
  (`03 Design/Reference/look · 2026-11-15 · rig and geometry.png`), standards relocked.
- 2026-11-16 · Colour fixed (Khronos PBR Neutral), Duolingo-style information cards with a real photo, render.bat,
  key-prompt.md, publish log, ten example animals with LOW previews.
- 2026-11-16 · The bulky, posed blocky-mob look approved by the owner after three rounds (geometry `mob`, joints,
  plates, stacked sections, faces painted flat, voxels scaled to real size, vivid pastel backgrounds), standards
  relocked as v2.0 (`03 Design/Reference/look · 2026-11-16 · flat faces before-after.jpg`); five more animals
  (000011 to 000015).
- 2026-11-16 · Plates switched off (solid feet), knees for the long-legged animals, the hippo, wolf and rabbit
  reworked, ten more animals (000016 to 000025), the information cards redesigned to breathe; standards relocked as
  v2.1 on the owner's OK.

## Waiting for the owner
1. **Review the twenty-five LOW previews** (`_system/cache/preview/<code>/<code> · preview sheet.png`, or the lineups in
   `02 Animals/`) and approve each one you like: `vf.py approve <code> preview`. Then `render.bat` → `3` renders the ULTRA
   finals of the approved ones (about 15–20 min each).
2. **Approve one download:** `Poppins-MediumItalic.ttf` (Google Fonts, OFL, ~150 KB) for true italic scientific
   names; previews use a sheared Medium until then.
3. Fill `_system/data/brand.json → contributor_names`; write the Gumroad licence text and cover (brand allowed there).
4. Optional: try `key-prompt.md` in a browser on one brief (e.g. rename `000001`'s `model.py`, attach the prompt and
   `docs/voxel-model.md`, compare the result) to see how Sonnet does with it.

## Next: rigging and animation (owner, 2026-11-16: "add the todo to rig the animal and provide the dynamic animation
and expression of the animals like walking, and other animation that usualy the animal doing")
- [x] **Rig from the joints** (2026-11-17, PROPOSED): in a new `vf_rig.py` rather than `vf_scene`, so the stills and
  their `.blend` stay untouched: `vf.py rig` saves `<code> · <Name> · Rig.blend` + `· Rig.glb` beside the still.
  Armature `VF · armature`: root → body → one bone per joint section; the sections skinned to one mesh with rigid
  weights (owner, 2026-11-17: the bone-parented first version did not read as rigged); rest pose = the model as
  drawn (T-pose), action `pose` = the approved still. All twenty-five rigged; `vf.py rig-check` passes on all.
- [x] **Every new animal goes all the way** (owner, 2026-11-17): `motion` required by `check` once a model exists,
  `vf.py preview` and `render.bat` 2 rig, check and animate after the stills, `verify` fails otherwise; the template
  has a motion block and a Motion section in the brief.
- [ ] **Approve the motion** (owner): the GIF loops in `_system/cache/preview/<code>/anim/` and the lineup
  `02 Animals/Voxel Fauna · Twenty-five examples · motion (LOW preview).gif`. On the OK: `vf_rig.RIG` → 
  `vf_standards.py`, `vf_rig.py` into `vflib.LOCKED_FILES`, `vf.py lock "…"`, `vf.py standards --write`.
- [ ] **Knees everywhere a gait needs them:** upper leg + shin on the lion, polar bear, giraffe, elephant, tiger,
  goat, zebra (2026-11-16) and the wolf, flamingo, frog and rabbit hind feet (2026-11-17); the short-legged ones
  (fox, red panda, panda, capybara, armadillo, koala, hedgehog, hippo) walk on stiff legs, like a block-game mob;
  add knees if the owner wants a softer gait.
- [~] **Animation library by body plan,** keyed on the bones, looping, 24 fps. Done: idle (head look, ear flick,
  tail, trunk, jaw, gills), walk (diagonal pairs, shins fold, head bob, tail sway; sprawl walk for the axolotl), flap,
  hop, swim, waddle, every frame grounded on its posed voxels. Open: trot and run; sit / lie down / get up; graze;
  preen; swimmer leap; breathing.
- [~] **Species specials.** Done: wolf howl, koala doze, lion head shake, hippo yawn, elephant ear fan and trunk
  swing, giraffe neck reach, penguin waddle, toucan hop, sniff (fox, capybara, polar bear, hedgehog, armadillo).
  Open: flamingo leg swap, frog eye flash, dolphin leap, toucan fruit toss, hedgehog curl, rabbit thump, tiger
  prowl, macaw wing show.
- [ ] **Expressions:** the face is painted on the head voxels, so expressions are paint states swapped in time:
  eyes open / closed / happy arcs / sleepy lines / surprised, brows, mouth shapes (smile, open, O, smirk), blinks
  every few seconds; store them per species beside the model (e.g. `blender/faces.py`) and key them with the actions.
- [~] **Output:** GIF previews done (512 px square, 12 fps, LOW samples, the stills' shadow composite). Open: MP4
  loops (square and vertical) with Nilant's video profiles (motion blur back on for video), through `render.bat`;
  stills and the information artworks stay as they are.
- [ ] **Owner to decide:** which formats and lengths (social loops, stock video, Gumroad bonus), and which animals
  first.

## Next: the export package (owner, 2026-11-17)
- [x] The owner approved all 25 models and the motion: 25 preview approvals recorded, the motion locked (v2.2).
- [x] `vf_export.py` (masters + loop frames from the rig, `render.bat` → 3), `package.py` (stock crop, GIF, A5 cards
  EN and ID, `render.bat` P), stock and registry on the new items, Indonesian copy for all 25 (`i18n.id`).
- [x] Checked end to end at LOW on all 25 (`vf.py final <code> --low`, `vf.py package <code> --low`).
- [x] **Owner:** approved the package (cards v5, masters, loop) from the LOW set, 2026-11-17; `vf_export.py` (with
  `EXPORT`) and `package.py` joined the lock (standards v2.2 + the export package).
- [ ] ULTRA finals on the RTX 3050 (`render.bat` → 3, then P (package)), then the owner's `approve <code> final`.
- [ ] **Owner, on the RTX 3050:** `render.bat` → 3 (about 15 min an animal), then P (package).
- [ ] Optional: crop marks on the card PDF if the print shop asks; MP4 loops beside the GIF.

## Next for the engine
- Judge the first ULTRA finals at full size (seams on `merged` parts, shadow strength, card type at 100 %).
- If Adobe refuses the 9:16 illustrations as similar content, record it in the Stock Platforms guide and the log.
- Optional: transparent-background PNG variants (Adobe's PNG category) from the animal pass; a Gumroad cover template;
  owner-taken photos so information artworks can go to stock sites too.
- Verify the two "general knowledge, to verify" lines (koala's Australian listing; red panda false thumb; giraffe
  species split) against primary sources before those animals' finals.

## Open: standards v2.3 (owner, 2026-11-17)
- [ ] **Owner:** OK the calmer colours and motion v2 from the before/after sheets; then `vf.py lock`, `vf.py standards --write`, and `vf.py approve <code> preview` for the 25 again (the rebuild changed every model key).

## Open: the owner's list of 2026-11-21 (`00 TODO/readme first.txt`, done for 000001–000025)
- [x] Six-digit codes everywhere (all 100 animals), Tailwind removed (hex only), one-chroma backgrounds, the registry
  split into the animals (registry) and one workbook per platform.
- [x] The twelve model and motion fixes, livelier poses for all 25 (the head to the camera; the static blocky pose
  straight), sections anchored into their parents,
  nested stacking; all 25 rebuilt, rigged (rig check PASS) and looped at LOW.
- [x] The face layer, tried on 000001, removed with its code on the owner's word ("undo everything that face
  related"): every face stays painted flat.
- [x] Standards relocked as v2.3 on the owner's "lock it" (2026-11-21).
- [ ] **Owner: approve the 25 LOW previews again** (`vf.py approve <code> preview`; the models changed since the
  approvals of 2026-11-17).
- [ ] ULTRA renders and packages again (`render.bat` → 3, then P): the existing `export/` files are from the old
  models and backgrounds.
- [ ] Then `00 TODO/026-100.txt`: recheck the registry and the information of 000026–000100, build them, LOW previews
  in `02 Animals/_preview` (every 25: rig sections, GIFs, renders, card fronts and backs), move the existing lineups
  there.
