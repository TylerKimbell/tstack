"""Checks for the iterate self-test. Run from the repository root before every round.

Exits non-zero and names what failed, so a round never starts on a broken skill.
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
failures = []

# Skill frontmatter: right name, description present and under the 1024-character limit.
skill = (ROOT / "skills/iterate/SKILL.md").read_text()
front = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
if not front:
    failures.append("SKILL.md has no frontmatter")
else:
    block = front.group(1)
    if not re.search(r"^name: iterate$", block, re.M):
        failures.append("SKILL.md frontmatter name is not 'iterate'")
    desc = re.search(r"^description: >-\n((?:  .*\n?)+)", block, re.M)
    if not desc:
        failures.append("SKILL.md frontmatter has no folded description")
    elif len(" ".join(desc.group(1).split())) >= 1024:
        failures.append("SKILL.md description is 1024 characters or longer")

# The templates file must exist and the skill must point to it.
if not (ROOT / "skills/iterate/templates.md").is_file():
    failures.append("skills/iterate/templates.md is missing")
elif "templates.md" not in skill:
    failures.append("SKILL.md never mentions templates.md")

# Plugin manifests must parse.
for name in ("plugin.json", "marketplace.json"):
    try:
        json.loads((ROOT / ".claude-plugin" / name).read_text())
    except (OSError, ValueError) as err:
        failures.append(f".claude-plugin/{name}: {err}")

# The README must still describe the skill.
if "| `iterate` |" not in (ROOT / "README.md").read_text():
    failures.append("README.md has no row for iterate")

# Every fixture the spec names must exist.
spec = (HERE / "iterate.md").read_text()
for path in sorted(set(re.findall(r"`(fixtures/[^`]+)`", spec))):
    if not (HERE / path).is_file():
        failures.append(f"spec names missing fixture {path}")

for failure in failures:
    print("FAIL", failure)
for name in ("SKILL.md", "templates.md"):
    path = ROOT / "skills/iterate" / name
    if path.is_file():
        print(f"{name}: {len(path.read_text().splitlines())} lines")
print("all checks pass" if not failures else f"{len(failures)} check(s) failed")
sys.exit(1 if failures else 0)
