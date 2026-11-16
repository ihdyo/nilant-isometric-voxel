"""Voxel Fauna · one Blender run: build an animal's .blend from its model script, or open a built .blend, and render.

    blender -b --factory-startup --python vf_job.py -- <job.json>

job.json (written by scripts/vf.py, never by hand), one of:
    build   {"model": ".../blender/model.py", "look": {...}, "budget": [min, max], "blend": ".../<code> · <Name>.blend",
             "readme": "...", "renders": [...]}                     model.py -> scenes -> saved .blend (+ optional renders)
    render  {"open": ".../<code> · <Name>.blend", "renders": [...]}
                                                   renders straight from the built .blend (render.bat, final)
    renders: [{"scene": "ILL 1x1", "profile": "LOW", "out": ".../VF-26-001-ILL-1x1.png"}, ...]
plus "work" (a temp folder for the passes) and "result" (where this run reports). The result lists the model report,
the framing, every render's timing and any error, so the caller can say what broke.
"""
import json
import os
import sys
import time
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def main():
    job_path = sys.argv[sys.argv.index("--") + 1]
    job = json.load(open(job_path, encoding="utf-8"))
    result = dict(ok=False, started=time.strftime("%Y-%m-%d %H:%M:%S"))
    try:
        import bpy
        import vf_standards as ST
        import vf_scene as V

        result["blender"] = bpy.app.version_string
        if job.get("open"):
            bpy.ops.wm.open_mainfile(filepath=job["open"])
            V.log(f"opened {job['open']}")
            result["frames"] = {s.name: dict(ortho_scale=s.camera.data.ortho_scale) for s in bpy.data.scenes if s.camera}
        else:
            from vf_voxel import load_model
            grid = load_model(job["model"])
            errors, notes = grid.report(tuple(job.get("budget") or ST.BUDGET), ST.POSE["max_angle"], ST.POSE["plates"])
            result["model"] = dict(errors=errors, notes=notes, size=grid.size(), voxels=len(grid.v))
            if errors:
                raise ValueError("model check failed: " + "; ".join(errors))
            frames = V.build(grid, job["look"], job.get("rig"), job.get("geometry"))
            result["frames"] = {k: dict(v) for k, v in frames.items()}
            if job.get("blend"):
                V.save(job["blend"], job.get("readme", ""))
        result["renders"] = []
        for r in job.get("renders", []):
            os.makedirs(os.path.dirname(r["out"]), exist_ok=True)
            result["renders"].append(V.render(r["scene"], r["profile"], r["out"], job["work"]))
            json.dump(result, open(job["result"] + ".partial", "w", encoding="utf-8"), default=str)
        result["ok"] = True
    except Exception as e:
        result["error"] = f"{type(e).__name__}: {e}"
        result["trace"] = traceback.format_exc()
        print("VF: FAILED", result["error"], flush=True)
    try:
        import vf_scene as V
        result["log"] = list(V.REPORT)
    except Exception:
        pass
    result["finished"] = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(job["result"], "w", encoding="utf-8") as f:
        json.dump(result, f, indent=1, default=str)


main()
