# Voxel Fauna · Production Workflow

Six phases, two approvals by the owner. The rules behind each step are in the skill
`.claude/skills/voxel-animal-production/SKILL.md`; this page is the walk-through. Commands run from the project root:
`python _system/studio/scripts/vf.py <command>` (written `vf.py` below). Building and rendering can also be done from
**`_system/studio/render/render.bat`** (double-click).

## Phase 1 · Research
1. `vf.py new "Red Fox" "Vulpes vulpes"` → `02 Animals/26-NNN · Red Fox/` with status Research.
2. `docs/animal-info.md`: identification and taxonomy, IUCN status, physical traits, size and weight, lifespan, diet,
   habitat, distribution, behaviour, social structure, reproduction, predators and threats, adaptations, ecological
   role, interesting facts, and what is uncertain. Every statement carries `[n]`.
3. `docs/references.md`: numbered sources. The **IUCN assessment** (by its DOI, checked on Crossref) for the status;
   an Animal Diversity Web or museum/agency species account for the biology; papers with DOIs for surprising facts.
   ADW statuses are often out of date: always use the IUCN one.
4. Photographs: genuine, never AI. Wikimedia Commons or agencies; licence **public domain, CC0 or CC BY** only (never
   BY-SA, NC or ND, which cannot go on a sold image); at least two angles (a side view for modelling, a striking one
   for the card). Ask the owner before downloading a batch. Log each in `references.md` (shows, author, licence,
   page URL).

## Phase 2 · Modelling
1. `animal.json → look`: 3–6 palette keys (first = main colour), one soft background, the reason in `look.why`.
2. `docs/voxel-model.md`: the voxel brief (palette table equal to `animal.json`, size and pose, proportions of each
   part, the 3–5 recognisable features, colour map, photos used).
3. `blender/model.py`: write it yourself, or attach **`key-prompt.md`** + `docs/voxel-model.md` to Claude Sonnet (high
   effort) in a browser and save its answer.
4. `vf.py check <code>` until it reports no errors (budget, ground, one piece, palette keys, brief vs palette).

## Phase 3 · Preview and review
1. `vf.py preview <code>` (or `render.bat` → `2` for every animal): builds the `.blend` if needed and renders all six
   compositions at LOW from it into `_system/cache/preview/<code>/`, with `<code> · preview sheet.png`.
2. Judge against the checklist (skill, section 8): species recognisable at thumbnail size, proportions against the
   photos, eyes visible, colours vivid, background complementary, the cards fit and read well.
3. Fix and repeat. Show the owner. On the owner's OK: `vf.py approve <code> preview`.

## Phase 4 · Final production
1. The card copy in `animal.json → info` (Duolingo voice; every item cites source ids; `vf.py check` says if a text is
   too long for any layout). The photo: `info.photo` (file, author, licence, url, centre).
2. `vf.py final <code>` (or `render.bat` → `3` for every approved animal): ULTRA from the approved `.blend` into
   `export/`, about 15–20 minutes an animal; it resumes after a pause and skips finished images.
3. Look at all six at full size. Copy changes later: edit `animal.json`, then `vf.py info <code>` (no render).

## Phase 5 · Documentation and registry
1. `vf.py overview <code>`; `vf.py register <code>` → rows in `05 Publish/Voxel Fauna · Registry.xlsx`.
2. `vf.py stock <code>` → JPEGs of the illustrations and upload CSVs (stock sites), the Gumroad zip of all six.
3. `vf.py verify`.

## Phase 6 · Completion and publishing
1. Present the folder and the six exports to the owner. On the owner's OK: `vf.py approve <code> final`.
2. Upload with `05 Publish/Voxel Fauna · Publishing Checklist.md`; record every event:
   `vf.py log <code> "Adobe Stock" Submitted --kinds ILL`, later `vf.py log VF-26-001-ILL-1x1 "Adobe Stock" Accepted --link <url>`.

## When something goes wrong
- Blender job failed: the message names the error; the full log is `_system/cache/jobs/<code>-<step>/blender.log`.
- `.blend` stale: the model, palette or standards changed; build again (`render.bat` → `1`), and get a new preview
  approval if the model or look changed after the last one.
- `verify` says a standard changed: someone edited the engine; revert, or show the owner and lock it.
- A card overflows: shorten the named field (limits in `vf_standards.INFO_LIMITS`); never shrink the type.
