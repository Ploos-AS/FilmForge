#!/usr/bin/env python3
"""FilmForge M2 CLI."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import yaml
REQUIRED=("version","kind","id","title","format","canon","scenes")
CRITERIA=("premise","emotional_potential","visual_identity","originality","production_feasibility","franchise_depth")
def load(path):
    with Path(path).open(encoding="utf-8") as x: return yaml.safe_load(x)
def validate(p):
    e=[f"missing required field: {k}" for k in REQUIRED if k not in p]
    if p.get("kind")!="FilmForgeProject": e.append("kind must be FilmForgeProject")
    if float(p.get("format",{}).get("duration_target_minutes",0))<=0: e.append("duration_target_minutes must be > 0")
    if int(p.get("format",{}).get("fps",0))<=0: e.append("fps must be > 0")
    if not p.get("canon",{}).get("universe_id"): e.append("canon.universe_id is required")
    return e
def plan(p):
    scenes=p.get("scenes",[]); shots=[s for x in scenes for s in x.get("shots",[])]
    return {"project":p.get("id"),"title":p.get("title"),"target_minutes":p.get("format",{}).get("duration_target_minutes"),"scene_count":len(scenes),"shot_count":len(shots),"canon":{k:len(p.get("canon",{}).get(k,[])) for k in ("characters","locations","props","styles")},"ready_for_shot_generation":bool(scenes)}
def foundry(p):
    rows=[]
    for c in p.get("candidates",[]):
        scores=c.get("scores",{}); vals=[float(scores[k]) for k in CRITERIA if k in scores]
        rows.append({"id":c.get("id"),"title":c.get("title"),"reviewed":len(vals)==len(CRITERIA),"score":round(sum(vals)/len(vals),1) if vals else None})
    return {"foundry":p.get("id"),"candidate_count":len(rows),"candidates":rows}
def coverage(p):
    if p.get("kind") != "FilmForgeShotCoverage":
        return {"ok": False, "errors": ["kind must be FilmForgeShotCoverage"]}
    shots = p.get("shots", [])
    errors = []
    seen = set()
    total = 0.0
    scenes = {}
    for shot in shots:
        sid = shot.get("id")
        if not sid: errors.append("shot missing id")
        elif sid in seen: errors.append(f"duplicate shot id: {sid}")
        seen.add(sid)
        try: dur = float(shot.get("seconds", 0))
        except (TypeError, ValueError): dur = 0
        if dur <= 0: errors.append(f"{sid or 'unknown'} duration must be > 0")
        total += dur
        scene = shot.get("scene")
        scenes[scene] = scenes.get(scene, 0.0) + dur
    return {"ok": not errors, "film_id": p.get("film_id"), "shot_count": len(shots),
            "total_seconds": round(total, 3), "total_minutes": round(total / 60, 3),
            "scene_seconds": scenes, "errors": errors}

def main():
    ap=argparse.ArgumentParser(prog="filmforge"); sp=ap.add_subparsers(dest="cmd",required=True)
    for cmd in ("validate","plan","foundry","coverage"):
        q=sp.add_parser(cmd); q.add_argument("project")
    a=ap.parse_args(); p=load(a.project)
    if a.cmd=="coverage":
        result=coverage(p); print(json.dumps(result,indent=2)); raise SystemExit(0 if result["ok"] else 1)
    if a.cmd=="foundry":
        if p.get("kind")!="FilmForgeUniverseFoundry": raise SystemExit("ERROR: kind must be FilmForgeUniverseFoundry")
        print(json.dumps(foundry(p),indent=2)); return
    e=validate(p)
    if e: print("\n".join(f"ERROR: {x}" for x in e)); raise SystemExit(1)
    print("OK: valid FilmForge project" if a.cmd=="validate" else json.dumps(plan(p),indent=2))
if __name__=="__main__": main()
