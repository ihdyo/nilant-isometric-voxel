# _system · engine, data, logs

| Path | What |
|---|---|
| `studio/blender/vf_standards.py` | every number of the look (camera, voxel, bevel, light rigs, plastic, shadow, profiles, sizes, framing, the information layouts, IDs), each marked NILANT / ADAPTED / NEW with its reason |
| `studio/blender/vf_voxel.py` | the voxel grid an animal's `model.py` writes (plain Python) and its checks |
| `studio/blender/vf_scene.py` | the Blender side: meshes, stage, six composition scenes and cameras, profiles, the two passes and the composite |
| `studio/blender/vf_job.py` | one background Blender run (written as a job file by `vf.py`) |
| `studio/blender/selftest_model.py` | the placeholder creature of `vf.py selftest` |
| `studio/scripts/vf.py` | the command line (see `CLAUDE.md → Commands`) |
| `studio/scripts/vflib.py` | paths, palette maths, Blender runner, IDs, the standards fingerprint |
| `studio/scripts/infographic.py` | the information artwork composer (Pillow) |
| `studio/scripts/registry.py` | the registry workbook |
| `studio/scripts/stock.py` | stock JPEGs, upload CSVs, Gumroad zips |
| `studio/blender_path.txt` | optional, git-ignored: this PC's `blender.exe` |
| `data/standards.lock.json` | fingerprint of the approved engine (`vf.py lock`, checked by `vf.py verify`) |
| `data/brand.json` | the collection's names and the owner's publishing identity |
| `log/` | `WORKLOG.md` (what happened), `DECISIONS.md` (what was decided, newest wins), `PLAN.md` (what is open) |
| `cache/` | previews, information plates, selftest renders, Blender job logs; safe to delete, git-ignored |
