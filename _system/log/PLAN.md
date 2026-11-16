# Voxel Fauna · open items

## Done
- 2026-11-15 · The look approved by the owner: rig `iso_top` + geometry `merged`
  (`03 Design/Reference/look · 2026-11-15 · rig and geometry.png`), standards relocked.
- 2026-11-16 · Colour fixed (Khronos PBR Neutral), Duolingo-style information cards with a real photo, render.bat,
  key-prompt.md, publish log, ten example animals with LOW previews.
- 2026-11-16 · The bulky, posed blocky-mob look approved by the owner after three rounds (geometry `mob`, joints,
  plates, stacked sections, faces painted flat, voxels scaled to real size, vivid pastel backgrounds), standards
  relocked as v2.0 (`03 Design/Reference/look · 2026-11-16 · flat faces before-after.jpg`); five more animals
  (26-011 to 26-015).
- 2026-11-16 · Plates switched off (solid feet), knees for the long-legged animals, the hippo, wolf and rabbit
  reworked, ten more animals (26-016 to 26-025), the information cards redesigned to breathe; standards relocked as
  v2.1 on the owner's OK.

## Waiting for the owner
1. **Review the twenty-five LOW previews** (`_system/cache/preview/<code>/<code> · preview sheet.png`, or the lineups in
   `02 Animals/`) and approve each one you like: `vf.py approve <code> preview`. Then `render.bat` → `3` renders the ULTRA
   finals of the approved ones (about 15–20 min each).
2. **Approve one download:** `Poppins-MediumItalic.ttf` (Google Fonts, OFL, ~150 KB) for true italic scientific
   names; previews use a sheared Medium until then.
3. Fill `_system/data/brand.json → contributor_names`; write the Gumroad licence text and cover (brand allowed there).
4. Optional: try `key-prompt.md` in a browser on one brief (e.g. rename `26-001`'s `model.py`, attach the prompt and
   `docs/voxel-model.md`, compare the result) to see how Sonnet does with it.

## Next: rigging and animation (owner, 2026-11-16: "add the todo to rig the animal and provide the dynamic animation
and expression of the animals like walking, and other animation that usualy the animal doing")
- [ ] **Rig from the joints.** Every `g.joint` section already has its own Blender object with its origin on the
  hinge and a parent chain (body → leg → shin, head → ear …). Turn that into an armature in `vf_scene`: one bone per
  section, parented like the joints, each section bone-parented (rigid, no skinning: the blocky look stays crisp). The
  model's rest pose is the bind pose; today's still pose becomes one named pose among several.
- [ ] **Knees everywhere a gait needs them:** the long-legged animals have upper leg + shin since 2026-11-16; give
  the short-legged ones (fox, red panda, panda, capybara, armadillo, wolf front legs) knees too before walk cycles.
- [ ] **Animation library by body plan,** keyed on the bones, looping, 24 or 30 fps:
  quadruped walk, trot and run (diagonal leg pairs, knees folding, head bob, tail sway); idle (breathing scale on
  the body, ear flicks, slow head turns, blinks); sit / lie down / get up; sniff and graze; bird hop, wing flap,
  preen; swimmer glide and leap; hopper hop.
- [ ] **Species specials:** wolf howl, flamingo one-leg balance and leg swap, frog hop and eye flash, dolphin leap
  and splash-free arc, toucan fruit toss, elephant trunk swing and ear fan, hippo yawn, hedgehog curl into a ball,
  rabbit thump, giraffe neck reach, penguin waddle, koala doze, lion head shake, tiger prowl, macaw wing show.
- [ ] **Expressions:** the face is painted on the head voxels, so expressions are paint states swapped in time:
  eyes open / closed / happy arcs / sleepy lines / surprised, brows, mouth shapes (smile, open, O, smirk), blinks
  every few seconds; store them per species beside the model (e.g. `blender/faces.py`) and key them with the actions.
- [ ] **Output:** short loops (MP4 and GIF previews, square and vertical) rendered with Nilant's video profiles
  (motion blur back on for video), through `render.bat`; stills and the information artworks stay as they are.
- [ ] **Owner to decide:** which formats and lengths (social loops, stock video, Gumroad bonus), and which animals
  first.

## Next for the engine
- Judge the first ULTRA finals at full size (seams on `merged` parts, shadow strength, card type at 100 %).
- If Adobe refuses the 9:16 illustrations as similar content, record it in the Stock Platforms guide and the log.
- Optional: transparent-background PNG variants (Adobe's PNG category) from the animal pass; a Gumroad cover template;
  owner-taken photos so information artworks can go to stock sites too.
- Verify the two "general knowledge, to verify" lines (koala's Australian listing; red panda false thumb; giraffe
  species split) against primary sources before those animals' finals.
