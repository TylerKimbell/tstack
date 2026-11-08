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


def read(path):
    """Return a file's text, or record a failure and return "" if it can't be read."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, ValueError) as err:
        failures.append(f"{path.relative_to(ROOT).as_posix()}: {err}")
        return ""


# Skill frontmatter: right name, description present and under the 1024-character limit.
skill = read(ROOT / "skills/iterate/SKILL.md")
front = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
if skill and not front:
    failures.append("SKILL.md has no frontmatter")
elif front:
    block = front.group(1)
    if not re.search(r"^name: iterate$", block, re.M):
        failures.append("SKILL.md frontmatter name is not 'iterate'")
    desc = re.search(r"^description: >-\n((?:  .*\n?)+)", block, re.M)
    if not desc:
        failures.append("SKILL.md frontmatter has no folded description")
    elif len(" ".join(desc.group(1).split())) >= 1024:
        failures.append("SKILL.md description is 1024 characters or longer")

# The templates file must exist and the skill must point to it.
templates = read(ROOT / "skills/iterate/templates.md")
if skill and templates and "templates.md" not in skill:
    failures.append("SKILL.md never mentions templates.md")

# Plugin manifests must parse.
for name in ("plugin.json", "marketplace.json"):
    try:
        json.loads((ROOT / ".claude-plugin" / name).read_text(encoding="utf-8"))
    except (OSError, ValueError) as err:
        failures.append(f".claude-plugin/{name}: {err}")

# The README must still describe the skill.
readme = read(ROOT / "README.md")
if readme and "| `iterate` |" not in readme:
    failures.append("README.md has no row for iterate")

# The run log and Run state live only in iterate-log.md, so evaluators can't read scores.
spec = read(HERE / "iterate.md")
if not (HERE / "iterate-log.md").is_file():
    failures.append("evals/iterate/iterate-log.md is missing")
if "### Run log" in spec or "**Run state:**" in spec:
    failures.append("iterate.md holds a run log or Run state; move it to iterate-log.md")

# Every fixture the spec names must exist.
for path in sorted(set(re.findall(r"`(fixtures/[^`]+)`", spec))):
    if not (HERE / path).is_file():
        failures.append(f"spec names missing fixture {path}")

for failure in failures:
    print("FAIL", failure)
for name, text in (("SKILL.md", skill), ("templates.md", templates)):
    if text:
        print(f"{name}: {len(text.splitlines())} lines")
print("all checks pass" if not failures else f"{len(failures)} check(s) failed")
sys.exit(1 if failures else 0)
