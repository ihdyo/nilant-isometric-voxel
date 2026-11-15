# Voxel Fauna · Prerequisites

Checked on the owner's Windows PC on 2026-11-15 (`vf.py doctor`).

| What | Version | Notes |
|---|---|---|
| Blender | 5.3.0 (regular install, the one Nilant uses) | Found through `BLENDER`, then `_system/studio/blender_path.txt`, then `C:\Users\ihdyo\AppData\Local\Programs\Blender 5.3.0\…\blender.exe`. Runs headless (`-b --factory-startup`); its bundled numpy does the shadow composite. |
| GPU | NVIDIA GeForce RTX 3050 Laptop, 4 GB | ULTRA at 4096×4096 renders on it (3.8 GB used): 1:1 about 4–5 min, 16:9 / 9:16 about 1.5 min, one animal 15–20 min. Close other GPU-heavy apps during `vf.py final`. |
| Python | 3.10+ (3.12.6 here) | with **Pillow** (type, JPEGs) and **openpyxl** (registry): `pip install pillow openpyxl` |
| Fonts | Poppins (OFL) in `03 Design/Fonts/` | Optional `Poppins-MediumItalic.ttf` for true italics in scientific names (pending the owner's OK to download). |

No Node, no Remotion, no internet needed to render. `vf.py doctor` checks all of it.
