#!/usr/bin/env python3
"""Save each helper agent's exact brief and its returned report from a past run.

Usage:
  helper_reports.py RUN.jsonl OUT_DIR [--match TEXT] [--suffix NAME]
  helper_reports.py --helpers DIR OUT_DIR [--match TEXT] [--suffix NAME]

For every helper transcript in RUN/subagents/ (or DIR), writes:
  OUT_DIR/<helper>.brief.md      the first message the helper got: its brief, word for word
  OUT_DIR/<helper>.<suffix>.md   the report it returned (suffix defaults to "report")

<helper> is the helper's description, lower-cased with spaces as hyphens. Use --suffix to
keep two sides of a side-by-side test apart (such as "current" and "candidate").

--pair names each helper after the brief already in OUT_DIR that shares the most lines
with its own brief, so a rerun lands next to the original it reran even when its
description differs. Save the original run first, then the rerun with --pair. The rerun's
own brief is then written as <helper>.<suffix>.brief.md, leaving the original's in place.

Where the report is: a helper that hands its result back with a tool call (a tool whose
name contains "handback", or SendMessage) has an empty or short final message, and the
report is that tool call's input. Otherwise the report is the helper's last text reply.
"""

import argparse
import glob
import json
import os
import re
import sys

REPORT_KEYS = ("report", "message", "content", "text", "result")


def records(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                yield json.loads(line)
            except ValueError:
                continue


def text_of(content):
    if isinstance(content, str):
        return content
    return "\n".join(b.get("text", "") for b in content or []
                     if isinstance(b, dict) and b.get("type") == "text")


def brief_and_report(path):
    """Return (brief, report, where the report came from) for one helper transcript."""
    brief, final, handback = None, None, None
    for d in records(path):
        m = d.get("message") or {}
        if d.get("type") == "user" and brief is None:
            brief = text_of(m.get("content"))
        if d.get("type") != "assistant":
            continue
        text = text_of(m.get("content"))
        if text.strip():
            final = text
        for b in m.get("content") or []:
            if not (isinstance(b, dict) and b.get("type") == "tool_use"):
                continue
            name = b.get("name", "")
            if "andback" in name.lower() or name == "SendMessage":
                inp = b.get("input") or {}
                found = next((inp[k] for k in REPORT_KEYS if isinstance(inp.get(k), str)), None)
                handback = found or json.dumps(inp, indent=1)
    if handback:
        return brief or "", handback, "hand-back tool call"
    return brief or "", final or "", "final message"


def best_pair(brief, folder):
    """The name of the brief in folder sharing the most lines with this one, or None."""
    lines = {l.strip() for l in brief.splitlines() if len(l.strip()) > 20}
    best, score = None, 0.0
    for path in glob.glob(os.path.join(folder, "*.brief.md")):
        name = os.path.basename(path)[: -len(".brief.md")]
        if name.count(".") or not lines:   # skip briefs saved by an earlier --pair
            continue
        with open(path, encoding="utf-8") as f:
            theirs = {l.strip() for l in f.read().splitlines() if len(l.strip()) > 20}
        overlap = len(lines & theirs) / max(1, len(theirs))
        if overlap > score:
            best, score = name, overlap
    return best if score >= 0.5 else None


def slug(desc, match):
    if match and desc.lower().startswith(match.lower()):
        desc = desc[len(match):]
    return re.sub(r"[^a-z0-9]+", "-", desc.lower()).strip("-") or "helper"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", nargs="?", help="a run's transcript (.jsonl)")
    ap.add_argument("out", help="folder to write the briefs and reports into")
    ap.add_argument("--helpers", metavar="DIR", help="read helper transcripts from DIR instead")
    ap.add_argument("--match", help="only helpers whose description contains this text")
    ap.add_argument("--suffix", default="report", help="name for the report files")
    ap.add_argument("--pair", action="store_true",
                    help="name each helper after the matching brief already in OUT_DIR")
    args = ap.parse_args()

    folder = args.helpers or os.path.join(os.path.splitext(args.source or "")[0], "subagents")
    if not os.path.isdir(folder):
        sys.exit(f"No helper folder at {folder}")
    os.makedirs(args.out, exist_ok=True)
    found = 0
    for sp in sorted(glob.glob(os.path.join(folder, "*.jsonl"))):
        try:
            with open(sp[:-6] + ".meta.json", encoding="utf-8") as f:
                desc = json.load(f).get("description", "")
        except (OSError, ValueError):
            desc = os.path.basename(sp)[:-6]
        if args.match and args.match.lower() not in desc.lower():
            continue
        brief, report, where = brief_and_report(sp)
        name = slug(desc, args.match)
        brief_file = f"{name}.brief.md"
        if args.pair:
            paired = best_pair(brief, args.out)
            if paired:
                name, brief_file = paired, f"{paired}.{args.suffix}.brief.md"
            else:
                print(f"{name}: no matching original brief in {args.out}; saved under its own name")
        with open(os.path.join(args.out, brief_file), "w", encoding="utf-8",
                  newline="\n") as f:
            f.write(brief)
        with open(os.path.join(args.out, f"{name}.{args.suffix}.md"), "w", encoding="utf-8",
                  newline="\n") as f:
            f.write(report)
        found += 1
        print(f"{name}: brief {len(brief):,} chars, report {len(report):,} chars ({where})")
    if not found:
        sys.exit("No helper transcripts matched.")


if __name__ == "__main__":
    main()
