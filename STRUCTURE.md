# Voxel Fauna · directory structure

Mapped from Nilant's structure (`../Nilant/STRUCTURE.md`), 2026-11-15. Not an app: guides, one folder per animal,
design assets, a licence log, a registry workbook and an engine (Blender for the pictures, Python for the type, the
registry and the stock files). Naming follows Nilant (and Kodey): numbered top folders `NN Name`, human-facing files
`Voxel Fauna · Title`, animal folders `NNNNNN · Common Name` (six-digit code).

| Nilant | Voxel Fauna | Why |
|---|---|---|
| `02 Videos/<YY-SEQ · Title>/` | `02 Animals/<NNNNNN · Common Name>/` | one project per animal instead of per video |
| `video.json` | `animal.json` | the structured source of truth |
| `overview.md` (by `npm run brief`) | `overview.md` (by `vf.py overview`) | generated front page |
| `docs/` brief, script, scenes | `docs/animal-info.md`, `docs/references.md` | research instead of a script |
| `assets/` voice take | `assets/photos/` genuine reference photos | |
| `blender/` | `blender/model.py`, `<code> · <Name>.blend`, `build.json` | the animal owns its model script and project |
| `export/` Video.mp4, Thumbnail.png | `export/VF-<code>-<ILL|INF>-<ratio>.png`, `export/stock/` | six stills |
| `_system/studio/blender/nilant_*` | `_system/studio/blender/vf_*` | the shared engine |
| `npm run …` (Node) | `python _system/studio/scripts/vf.py …` | stills need no Remotion |
| `_system/studio/render/render.bat` | `_system/studio/render/render.bat` | the same double-click renderer: build, previews, finals, offline |
| `05 Publish/Nilant · Schedule & Metrics.xlsx` | `05 Publish/Voxel Fauna · Registry.xlsx` + `Voxel Fauna · Publish Log.md` | the animals' information instead of a schedule; the platform targets and their dated publish logs in `05 Publish/Platforms/` |
| `_system/data/standards.lock.json` | same | the consistency contract |

```
nilant-voxel-isometric/
├── CLAUDE.md                     context for AI agents (status, contract, hard rules, map, commands, gotchas)
├── README.md                     folder map and the short workflow
├── STRUCTURE.md                  this file
├── key-prompt.md                 attach with an animal's docs/voxel-model.md to Claude Sonnet: writes its model.py
├── .gitignore
├── .claude/skills/
│   ├── voxel-animal-production/  THE production skill (single source of truth)
│   └── bsk-blender-director, bsk-creature-artist, bsk-stylized-style, bsk-qa-review   generic Blender craft (MIT, from Nilant)
├── 00 TODO/                      the owner's prompts while they are open (the first brief is in git history)
├── 01 Guide/
│   ├── Voxel Fauna · Production Workflow.md
│   ├── Voxel Fauna · Stock Platforms.md
│   └── Voxel Fauna · Prerequisites.md
├── 02 Animals/
│   ├── README.md
│   ├── _Template/                copied by `vf.py new`
│   ├── 000001 · Red Fox/ … 000025 · Plains Zebra/   the twenty-five example animals (2026-11-16)
│   └── <NNNNNN · Common Name>/
│       ├── overview.md           front page (generated)
│       ├── animal.json           source of truth: names, look, card copy + sources, photo, stock metadata, approvals
│       ├── docs/                 animal-info.md, references.md, voxel-model.md (the brief key-prompt.md needs)
│       ├── assets/photos/        genuine photographs (PD / CC0 / CC BY): modelling references + the card photo
│       ├── blender/              model.py (source), <code> · <Name>.blend (built), build.json (stamp), README.md
│       └── export/               VF-<code>-ILL-1x1.png … VF-<code>-INF-16x9.png, stock/ (JPEGs)
├── 03 Design/
│   ├── DESIGN-SYSTEM.md
│   ├── Color/                    README.md (the colour rules: hex only, one-chroma backgrounds)
│   ├── Fonts/                    Poppins (OFL)
│   └── Reference/                approved stills
├── 04 Library/
│   └── README.md                 licence and download log
├── 05 Publish/
│   ├── Voxel Fauna · Registry.xlsx        Read Me, Animals (the animal information)
│   ├── Platforms/                         Voxel Fauna · <Platform>.xlsx: Read Me, Items, Publish Log
│   ├── Voxel Fauna · Publish Log.md       every upload event (vf.py log)
│   ├── Voxel Fauna · Publishing Checklist.md
│   ├── README.md
│   ├── Stock/                    <code> · Adobe Stock.csv, <code> · Shutterstock.csv
│   └── Gumroad/                  <code> · <Name> · Voxel Fauna.zip
└── _system/
    ├── README.md
    ├── data/                     standards.lock.json, brand.json
    ├── log/                      WORKLOG.md, DECISIONS.md, PLAN.md
    ├── cache/                    previews, plates, selftest, jobs (git-ignored, safe to delete)
    └── studio/
        ├── blender_path.txt      this PC's blender.exe (written by render.bat; git-ignored)
        ├── render/               render.bat, Voxel Fauna · How to Render.md, README.md (status), python_path.txt
        ├── blender/              vf_standards.py, vf_voxel.py, vf_scene.py, vf_job.py, selftest_model.py
        └── scripts/              vf.py, render_cli.py, vflib.py, infographic.py, registry.py, stock.py
```

## Generated and ignored
- `_system/cache/` – previews, information plates, selftest renders, job logs.
- `*.blend1` – Blender's backups.
- Tracked on purpose: every `.blend` (built, but the editable deliverable), the exports, the registry, the photos
  (public domain, CC0 or CC BY only, each logged with its author and licence in the animal's `docs/references.md`).
