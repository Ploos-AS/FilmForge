#!/usr/bin/env python3
"""FilmForge M1 CLI."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import yaml

REQUIRED=("version","kind","id","title","format","canon","scenes")

def load(path):
    with Path(path).open(encoding="utf-8") as f: return yaml.safe_load(f)

def validate(p):
    errors=[]
    for k in REQUIRED:
        if k not in p: errors.append(f"missing required field: {k}")
    if p.get("kind")!="FilmForgeProject": errors.append("kind must be FilmForgeProject")
    fmt=p.get("format",{})
    if float(fmt.get("duration_target_minutes",0))<=0: errors.append("duration_target_minutes must be > 0")
    if int(fmt.get("fps",0))<=0: errors.append("fps must be > 0")
    canon=p.get("canon",{})
    if not canon.get("universe_id"): errors.append("canon.universe_id is required")
    return errors

def plan(p):
    scenes=p.get("scenes",[])
    shots=[s for scene in scenes for s in scene.get("shots",[])]
    return {
      "project":p.get("id"),
      "title":p.get("title"),
      "target_minutes":p.get("format",{}).get("duration_target_minutes"),
      "scene_count":len(scenes),
      "shot_count":len(shots),
      "canon":{
        k:len(p.get("canon",{}).get(k,[]))
        for k in ("characters","locations","props","styles")
      },
      "ready_for_shot_generation":bool(scenes)
    }

def main():
    ap=argparse.ArgumentParser(prog="filmforge")
    sp=ap.add_subparsers(dest="cmd",required=True)
    for cmd in ("validate","plan"):
        p=sp.add_parser(cmd); p.add_argument("project")
    a=ap.parse_args(); project=load(a.project)
    errors=validate(project)
    if a.cmd=="validate":
        if errors:
            print("\n".join(f"ERROR: {e}" for e in errors)); raise SystemExit(1)
        print("OK: valid FilmForge M1 project")
    else:
        if errors:
            print("\n".join(f"ERROR: {e}" for e in errors)); raise SystemExit(1)
        print(json.dumps(plan(project),indent=2))

if __name__=="__main__": main()
