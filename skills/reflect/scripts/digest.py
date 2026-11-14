#!/usr/bin/env python3
"""Turn a Claude Code session transcript into a short Markdown digest for reflect.

The digest keeps what reflect needs to find a reusable method: every message the user
typed, the agent's replies, one line per tool call, and tool errors. It drops tool
output, thinking, and bookkeeping records, which are most of a transcript's size.

Usage:
  digest.py --list [--limit N]          recent transcripts, newest first
  digest.py [SESSION] [--out FILE]      digest one session (default: this session)
  digest.py SESSION --turns 5-12,14     digest only those user turns

SESSION is a transcript path, a transcript id (the .jsonl file name), or a Claude
desktop app session id (local_...). With none, the script uses CLAUDE_CODE_SESSION_ID,
which Claude Code sets for the running session.
"""

import argparse
import glob
import json
import os
import re
import sys
from datetime import datetime

# Where Claude Code keeps transcripts: <config dir>/projects/<project slug>/<id>.jsonl
CONFIG_DIR = os.environ.get("CLAUDE_CONFIG_DIR", os.path.expanduser("~/.claude"))
PROJECTS = os.path.join(CONFIG_DIR, "projects")
# Where the Claude desktop app records its sessions (macOS). Each record names the
# transcript id as cliSessionId. Other platforms fall back to the transcript id.
APP_SESSIONS = os.path.expanduser(
    "~/Library/Application Support/Claude/claude-code-sessions"
)

REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)


# --- Finding the transcript -------------------------------------------------------

def transcript_for_id(tid):
    """Return the path of the transcript whose file name is <tid>.jsonl, or None."""
    hits = glob.glob(os.path.join(PROJECTS, "*", tid + ".jsonl"))
    return hits[0] if hits else None


def app_record(local_id):
    """Return the desktop app's JSON record for a local_ session id, or None."""
    hits = glob.glob(os.path.join(APP_SESSIONS, "**", local_id + ".json"), recursive=True)
    if not hits:
        return None
    with open(hits[0]) as f:
        return json.load(f)


def resolve(session):
    """Turn whatever the user gave into a transcript path, or exit with a reason."""
    if not session:
        session = os.environ.get("CLAUDE_CODE_SESSION_ID")
        if not session:
            sys.exit("No session given and CLAUDE_CODE_SESSION_ID is not set. "
                     "Pass a transcript path or id, or run --list.")
    if os.path.isfile(session):
        return session
    if session.startswith("local_"):
        rec = app_record(session)
        if not rec:
            sys.exit(f"No desktop app record for {session}. Export the session's "
                     "transcript from the app and pass the .jsonl path instead.")
        for key in ("cliSessionId", "lastAssistantCliSessionId"):
            path = rec.get(key) and transcript_for_id(rec[key])
            if path:
                return path
        sys.exit(f"The app record for {session} names no transcript that exists on disk.")
    path = transcript_for_id(session)
    if not path:
        sys.exit(f"No transcript named {session}.jsonl under {PROJECTS}.")
    return path


# --- Reading records -------------------------------------------------------------

def records(path):
    """Yield the transcript's records, skipping lines that are not valid JSON."""
    with open(path) as f:
        for line in f:
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def text_of(content):
    """Join the text blocks of a message's content, which is a string or a list."""
    if isinstance(content, str):
        return content
    parts = []
    for block in content or []:
        if block.get("type") == "text":
            parts.append(block.get("text", ""))
    return "\n".join(parts)


def is_prompt(rec):
    """True for a plain user message: not a tool result, injected meta record, or helper."""
    if rec.get("type") != "user" or rec.get("isMeta") or rec.get("isSidechain"):
        return False
    content = rec.get("message", {}).get("content")
    if isinstance(content, list) and any(b.get("type") == "tool_result" for b in content):
        return False
    return bool(text_of(content).strip())


def is_human(rec):
    """True for a message the user typed, not an injected reminder or event."""
    if not is_prompt(rec):
        return False
    origin = rec.get("origin") or {}
    if origin:
        return origin.get("kind") == "human"
    if rec.get("turnOrigin"):
        return rec["turnOrigin"] == "human"
    # Older transcripts have neither: treat plain text without a reminder wrapper as typed.
    return not text_of(rec["message"]["content"]).strip().startswith("<")


def opener_label(rec):
    """Name who sent a session's opening prompt when it wasn't the user typing it."""
    origin = rec.get("origin") or {}
    who = origin.get("subkind") or rec.get("turnOrigin") or origin.get("kind") or "unknown"
    names = {"scheduled-trigger": "a scheduled task", "scheduled": "a scheduled task",
             "host_synthetic": "the app or another session"}
    return f"opening prompt from {names.get(who, who)}"


def prompt_text(rec):
    """A prompt's text without reminder wrappers, or the whole text if that leaves nothing."""
    raw = text_of(rec["message"]["content"])
    return REMINDER.sub("", raw).strip() or raw.strip()


# How much of a tool's input to show. --max-text 0 sets this to 0, which means no clip,
# so a thread read in full also shows full commands, briefs, and queries.
INPUT_SCALE = 1

# Bookkeeping tools whose inputs say nothing about the method.
QUIET_TOOLS = ("update_plan", "mark_chapter", "TodoWrite", "TaskUpdate", "TaskCreate")

# A leading "cd <folder> &&" or "cd <folder>;" hides the real command in a clipped line.
LEADING_CD = re.compile(r'^cd\s+("[^"]*"|\'[^\']*\'|\S+)\s*(&&|;)\s*')


def one_line(text, limit):
    """Collapse whitespace and clip, for inputs shown inside a single line."""
    text = " ".join(str(text).split())
    limit = limit * INPUT_SCALE
    return text if not limit or len(text) <= limit else text[:limit].rstrip() + " [...]"


def tool_line(block):
    """Describe one tool call in a line, keeping the inputs that carry the method.

    The user's choices (questions asked, buttons offered), the commands run, and how
    helper agents were set up matter most to reflect, so those tools get more detail.
    """
    name = block.get("name", "?")
    inp = block.get("input") or {}
    short = name.split("__")[-1]  # MCP tools: keep the tool's own name
    if name == "Bash":
        desc = inp.get("description") or ""
        raw = inp.get("command", "").strip()
        # Move a leading "cd <folder> &&" out of the clipped command, keeping the folder.
        where = LEADING_CD.match(raw)
        cmd = one_line(LEADING_CD.sub("", raw), 200)
        loc = f" (in {where.group(1)})" if where else ""
        return f"Bash{loc}: {one_line(desc, 120)} `{cmd}`" if desc else f"Bash{loc}: `{cmd}`"
    if name in ("Agent", "Task"):
        setup = ", ".join(x for x in (inp.get("subagent_type"), inp.get("model")) if x)
        return (f"Agent ({setup or 'defaults'}): {one_line(inp.get('description', ''), 100)}"
                f" | prompt: {one_line(inp.get('prompt', ''), 300)}")
    if name == "AskUserQuestion":
        qs = []
        for q in inp.get("questions") or []:
            opts = " / ".join(o.get("label", "") for o in q.get("options") or [])
            qs.append(f"{one_line(q.get('question', ''), 200)} [{opts}]")
        return "Asked the user: " + " | ".join(qs)
    if short == "wrap_up":
        line = f"Wrap-up: {one_line(inp.get('recap', ''), 240)}"
        if inp.get("ask"):
            labels = " / ".join(a.get("label") or a.get("action", "")
                                for a in inp.get("actions") or [])
            line += f" | Asked: {inp['ask']} [{labels}]"
        return line
    if short in QUIET_TOOLS:
        return short
    for key in ("description", "file_path", "skill", "query", "url", "pattern", "title",
                "prompt"):
        val = inp.get(key)
        if isinstance(val, str) and val.strip():
            return f"{short}: {one_line(val, 140)}"
    # Anything else (a connector's query, a record id): show the input itself.
    if inp:
        return f"{short}: {one_line(json.dumps(inp, ensure_ascii=False), 200)}"
    return short


def clip(text, limit):
    text = text.strip()
    if limit and len(text) > limit:
        return text[:limit].rstrip() + f" [... {len(text) - limit} more chars]"
    return text


# --- Building the digest -----------------------------------------------------------

WRITERS = ("Write", "Edit", "NotebookEdit", "MultiEdit")


def parse_turns(spec):
    """Turn "9-11,13" into the set {9, 10, 11, 13}, or exit with a usage message."""
    wanted = set()
    for part in spec.replace(" ", "").split(","):
        a, _, b = part.partition("-")
        if not a.isdigit() or (b and not b.isdigit()):
            sys.exit(f"--turns takes ranges like 9-11,13; got {spec!r}")
        wanted.update(range(int(a), int(b or a) + 1))
    return wanted


def build(path, max_text, turns):
    """Return the digest as Markdown. turns is a set of turn numbers, or None for all."""
    title, cwd, branch, start, end = None, None, None, None, None
    out, turn = [], 0
    asks = set()     # tool_use ids of AskUserQuestion calls, to find their answers
    written = []     # files the agent wrote or edited, in first-touched order
    last_text = None  # index in out of the turn's latest agent text, and its full text

    def end_turn():
        # The last reply of a turn usually holds its conclusion, so it is never clipped.
        nonlocal last_text
        if last_text:
            out[last_text[0]] = last_text[1].strip()
        last_text = None

    def in_range():
        return turns is None or turn in turns

    for rec in records(path):
        kind = rec.get("type")
        ts = rec.get("timestamp")
        if ts:
            start = start or ts
            end = ts
        if kind == "custom-title":
            title = rec.get("customTitle") or rec.get("title") or title
        cwd = cwd or rec.get("cwd")
        branch = branch or rec.get("gitBranch")
        if rec.get("isSidechain"):
            continue

        human = is_human(rec)
        if human or (turn == 0 and is_prompt(rec)):
            end_turn()
            turn += 1
            if in_range():
                text = prompt_text(rec)
                who = "user" if human else opener_label(rec)
                out.append(f"\n## Turn {turn}: {who} ({(ts or '')[11:16]} UTC)\n")
                out.append(text or "(empty)")
                out.append("\n### Agent\n")
            continue

        if not in_range():
            continue

        if kind == "user":
            content = rec.get("message", {}).get("content")
            if isinstance(content, list):
                # Tool results: keep the user's answers to questions, and errors, which
                # show where a step had to be redone. Drop everything else.
                for b in content:
                    if b.get("type") != "tool_result":
                        continue
                    res = b.get("content")
                    res = res if isinstance(res, str) else text_of(res)
                    if b.get("tool_use_id") in asks:
                        out.append(f"- User answered: {one_line(res, 500)}")
                    elif b.get("is_error"):
                        out.append(f"- Error: {one_line(res, 300)}")
            elif rec.get("isCompactSummary"):
                out.append("(The session was compacted here. Records before it are complete.)")
            elif isinstance(content, str) and "<command-name>" in content:
                m = re.search(r"<command-name>(.*?)</command-name>", content)
                if m:
                    out.append(f"Command: {m.group(1)}")
        elif kind == "assistant":
            for b in rec.get("message", {}).get("content") or []:
                if b.get("type") == "tool_use":
                    if b.get("name") == "AskUserQuestion":
                        asks.add(b.get("id"))
                    fp = (b.get("input") or {}).get("file_path")
                    if b.get("name") in WRITERS and fp and fp not in written:
                        written.append(fp)
                    out.append("- " + tool_line(b))
                elif b.get("type") == "text" and b.get("text", "").strip():
                    out.append(clip(b["text"], max_text))
                    last_text = (len(out) - 1, b["text"])
    end_turn()

    head = [
        "# Session digest",
        "",
        f"- Transcript: {path}",
        f"- Title: {title or 'unknown'}",
        f"- Folder: {cwd or 'unknown'} (branch {branch or 'unknown'})",
        f"- Time: {start or '?'} to {end or '?'} (UTC)",
        f"- User turns: {turn}" + (f" (showing {sorted(turns)})" if turns else ""),
        "",
        "User messages are in full. Agent text over the limit is clipped, except each",
        "turn's last reply. Tool calls are one line each; their output is left out except",
        "the user's answers to questions, and errors. Buttons the agent offered appear on",
        "Wrap-up lines; a user message that matches a button label is that choice.",
    ]
    foot = ["", "## Files written or edited", ""]
    foot += [f"- {f}" for f in written] or ["- none"]
    foot += ["", "Files in scratch or temp folders may already be gone. Check before relying on them."]
    return "\n".join(head + out + foot) + "\n"


def list_recent(limit):
    """Print recent transcripts with their first typed message, newest first."""
    paths = sorted(glob.glob(os.path.join(PROJECTS, "*", "*.jsonl")),
                   key=os.path.getmtime, reverse=True)[:limit]
    for p in paths:
        first, title = "", ""
        for rec in records(p):
            if rec.get("type") == "custom-title":
                title = rec.get("customTitle") or rec.get("title") or title
            if not first and is_prompt(rec):
                first = " ".join(prompt_text(rec).split())
                if not is_human(rec):
                    first = f"({opener_label(rec)}) {first}"
        when = datetime.fromtimestamp(os.path.getmtime(p)).strftime("%Y-%m-%d %H:%M")
        tid = os.path.basename(p)[:-6]
        print(f"{when}  {tid}  {title or '-'}\n    {first[:110]}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("session", nargs="?", help="transcript path, transcript id, or local_ id")
    ap.add_argument("--list", action="store_true", help="list recent transcripts")
    ap.add_argument("--limit", type=int, default=15, help="how many to list (default 15)")
    ap.add_argument("--turns", help="user turns to include, such as 5-12 or 9-11,13")
    ap.add_argument("--max-text", type=int, default=1500,
                    help="clip each agent text block to this many chars; 0 = no limit, "
                         "which also prints tool inputs in full")
    ap.add_argument("--out", help="write the digest here instead of stdout")
    args = ap.parse_args()

    if args.list:
        list_recent(args.limit)
        return
    global INPUT_SCALE
    INPUT_SCALE = 0 if args.max_text == 0 else 1
    turns = parse_turns(args.turns) if args.turns else None
    digest = build(resolve(args.session), args.max_text, turns)
    if args.out:
        with open(args.out, "w") as f:
            f.write(digest)
        print(f"Wrote {args.out} ({len(digest)} chars)")
    else:
        sys.stdout.write(digest)


if __name__ == "__main__":
    main()
