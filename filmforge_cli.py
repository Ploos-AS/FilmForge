#!/usr/bin/env python3
"""FilmForge M1.1 CLI."""
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
def main():
    ap=argparse.ArgumentParser(prog="filmforge"); sp=ap.add_subparsers(dest="cmd",required=True)
    for cmd in ("validate","plan","foundry"):
        q=sp.add_parser(cmd); q.add_argument("project")
    a=ap.parse_args(); p=load(a.project)
    if a.cmd=="foundry":
        if p.get("kind")!="FilmForgeUniverseFoundry": raise SystemExit("ERROR: kind must be FilmForgeUniverseFoundry")
        print(json.dumps(foundry(p),indent=2)); return
    e=validate(p)
    if e: print("\n".join(f"ERROR: {x}" for x in e)); raise SystemExit(1)
    print("OK: valid FilmForge M1.1 project" if a.cmd=="validate" else json.dumps(plan(p),indent=2))
if __name__=="__main__": main()
