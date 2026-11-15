# Voxel Fauna · open items

## Done
- 2026-11-15 · The look approved by the owner: rig `iso_top` + geometry `merged`
  (`03 Design/Reference/look · 2026-11-15 · rig and geometry.png`), standards relocked.
- 2026-11-16 · Colour fixed (Khronos PBR Neutral), Duolingo-style information cards with a real photo, render.bat,
  key-prompt.md, publish log, ten example animals with LOW previews.

## Waiting for the owner
1. **Review the ten LOW previews** (`_system/cache/preview/<code>/<code> · preview sheet.png`, or the lineup in the
   handover) and approve each one you like: `vf.py approve <code> preview`. Then `render.bat` → `3` renders the ULTRA
   finals of the approved ones (about 15–20 min each).
2. **Approve one download:** `Poppins-MediumItalic.ttf` (Google Fonts, OFL, ~150 KB) for true italic scientific
   names; previews use a sheared Medium until then.
3. Fill `_system/data/brand.json → contributor_names`; write the Gumroad licence text and cover (brand allowed there).
4. Optional: try `key-prompt.md` in a browser on one brief (e.g. rename `26-001`'s `model.py`, attach the prompt and
   `docs/voxel-model.md`, compare the result) to see how Sonnet does with it.

## Next for the engine
- Judge the first ULTRA finals at full size (seams on `merged` parts, shadow strength, card type at 100 %).
- If Adobe refuses the 9:16 illustrations as similar content, record it in the Stock Platforms guide and the log.
- Optional: transparent-background PNG variants (Adobe's PNG category) from the animal pass; a Gumroad cover template;
  owner-taken photos so information artworks can go to stock sites too.
- Verify the two "general knowledge, to verify" lines (koala's Australian listing; red panda false thumb; giraffe
  species split) against primary sources before those animals' finals.
