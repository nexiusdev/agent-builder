#!/usr/bin/env python3
"""Mirror launched agents' live setup into their builder project folders and report drift.

Config (JSON):
{
  "projects_dir": "/path/to/agent-projects",
  "skills_dir": "/path/to/live/skills",          # one folder per live skill
  "profiles_dir": "/path/to/live/agent/profiles", # <agent_id>/profile.json with name/title/description
  "projects": {"<slug>": {"agent_id": "...", "skills": ["skill-a", "skill-b"]}}
}
Never edits design files or live agents. Writes <project>/live/ and live/SYNC-REPORT.md.
"""
import argparse, datetime, hashlib, json, pathlib, shutil

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()[:12]
def tree(d): return {str(f.relative_to(d)): digest(f) for f in sorted(d.rglob("*")) if f.is_file()} if d.exists() else {}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--config", required=True); a = ap.parse_args()
    cfg = json.loads(pathlib.Path(a.config).read_text())
    root, skills, profiles = (pathlib.Path(cfg[k]) for k in ("projects_dir", "skills_dir", "profiles_dir"))
    now = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    for slug, p in cfg["projects"].items():
        proj = root / slug; live = proj / "live"; live.mkdir(parents=True, exist_ok=True)
        prof_path = profiles / p["agent_id"] / "profile.json"
        prof = json.loads(prof_path.read_text()) if prof_path.exists() else {}
        (live / "profile.json").write_text(json.dumps({k: prof.get(k) for k in ("name", "title", "description")}, indent=2, ensure_ascii=False))
        out = [f"# Live sync report: {prof.get('name', slug)}", "", f"Synced {now}. Design files untouched.", ""]
        drift = 0 if prof else 1
        if not prof: out.append("- profile: MISSING live profile")
        if (live / "skills").exists(): shutil.rmtree(live / "skills")
        for sk in p["skills"]:
            src, draft = skills / sk, proj / ".agents/skills" / sk
            if not src.exists(): out.append(f"- {sk}: MISSING from live skills"); drift += 1; continue
            shutil.copytree(src, live / "skills" / sk)
            if not draft.exists(): out.append(f"- {sk}: live only (no design draft)"); drift += 1
            elif tree(draft) != tree(src): out.append(f"- {sk}: DIFFERS from design draft"); drift += 1
            else: out.append(f"- {sk}: matches design draft")
        out += ["", f"Drift items: {drift}"]
        (live / "SYNC-REPORT.md").write_text("\n".join(out) + "\n")
        with open(live / "sync-log.md", "a") as f: f.write(f"- {now}: {drift} drift item(s)\n")
        print(f"{slug}: {drift} drift item(s)")

if __name__ == "__main__": main()
