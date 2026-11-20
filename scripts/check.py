#!/usr/bin/env python3
"""Check note frontmatter and relative links. Standard library only. Exit 1 on any error."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = {
    "tracks": {"title": None, "question": None, "status": {"open", "paused", "closed"}},
    "projects": {"title": None, "track": None, "repo": None, "maintainers": None,
                 "status": {"scaffold", "active", "paused", "done", "archived"}, "started": None},
    "findings": {"title": None, "track": None, "project": None,
                 "result": {"positive", "negative", "inconclusive"},
                 "strength": {"cryptographic", "hardware-attested", "sampled", "timed", "measured", "argued"},
                 "status": {"reported", "reproduced", "retracted"},
                 "evidence": None, "date": None, "authors": None},
    "sources": {"title": None, "url": None, "kind": {"paper", "post", "code", "talk", "dataset"}, "tracks": None},
}
REFS = {"track": "tracks", "project": "projects"}  # key -> folder its value must name
LINK = re.compile(r"\]\(([^)\s]+)\)")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def frontmatter(text):
    if not text.startswith("---\n"):
        return None
    head = text[4:].split("\n---\n", 1)[0]
    pairs = (line.split(":", 1) for line in head.splitlines() if ":" in line)
    return {k.strip(): v.strip() for k, v in pairs}


def check_note(path, folder, errors):
    fm = frontmatter(path.read_text())
    if fm is None:
        errors.append(f"{path}: missing frontmatter")
        return
    for key, allowed in SCHEMA[folder].items():
        value = fm.get(key, "")
        if not value:
            errors.append(f"{path}: missing '{key}'")
        elif allowed and value not in allowed:
            errors.append(f"{path}: '{key}: {value}' not in {sorted(allowed)}")
        elif key in REFS and not (ROOT / REFS[key] / f"{value}.md").exists():
            errors.append(f"{path}: '{key}: {value}' names no file in {REFS[key]}/")
    if folder == "findings":
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md", path.name):
            errors.append(f"{path}: name must be YYYY-MM-DD-<slug>.md")
        if not DATE.fullmatch(fm.get("date", "")):
            errors.append(f"{path}: 'date' must be YYYY-MM-DD")


def check_links(path, errors):
    text = re.sub(r"```.*?```|`[^`\n]*`", "", path.read_text(), flags=re.S)  # ignore code
    for target in LINK.findall(text):
        if re.match(r"[a-z]+:|#", target):
            continue
        if not (path.parent / target.split("#")[0]).exists():
            errors.append(f"{path}: broken link {target}")


def main():
    errors = []
    for folder in SCHEMA:
        for path in sorted((ROOT / folder).glob("*.md")):
            check_note(path, folder, errors)
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" not in path.parts:
            check_links(path, errors)
    for e in errors:
        print(e.replace(str(ROOT) + "/", ""))
    print(f"{len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
