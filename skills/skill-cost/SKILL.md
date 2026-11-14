---
name: skill-cost
description: >-
  Measure what a skill costs to run and make it cheaper without losing quality. Totals
  tokens across a skill's recent runs and their helper agents, finds what drives the cost,
  ranks changes cheapest first, and tests the chosen change side by side, read-only,
  before anything is edited. Use for "audit how many tokens <skill> used", "is <skill>
  too expensive", "make <skill> cheaper", "find ways to optimize <skill>", "should the
  helpers run on a smaller model", or "dry run cheaper helpers". Not for this session's
  own usage (explain-usage) or for improving a skill's quality (iterate).
---

# Skill cost

Find out what a skill's runs cost, where the cost goes, and which change cuts it without
losing anything the skill should catch. Measure first, change second: nothing about the
skill, its briefs, or its schedule changes until the user has seen the numbers and picked
a change, and every test before that is read-only.

The scripts are in this skill's `scripts/` folder. They read Claude Code transcripts. In
another agent, measure from whatever usage records it keeps and follow the same steps.

## Step 1: Find the runs

Claude Code keeps each session at `~/.claude/projects/<project slug>/<id>.jsonl`, and its
helper agents at `<id>/subagents/*.jsonl`, each with a `.meta.json` holding its
description.

- **Scheduled runs** start with a message carrying `scheduled-task name="<task>"`, with
  the quotes escaped in the file. Project folder names start with `-`, so end grep's
  options with `--`:
  `grep -l -- 'scheduled-task name=\\"<task>' ~/.claude/projects/*/*.jsonl`.
  List every schedule that runs the skill, with its timing (in Claude Code, the
  scheduled-tasks tools), including ones that haven't run yet. A run list's session ids
  may not match transcript file names; match runs by start time.
- **Manual runs** start with the skill's slash command or name. Searching for the command
  alone finds only these.

Take the last five or six runs. With fewer, measure what there is and say there's no
spread to compare against. Say when a run predates the skill's current version, schedule
prompt, or project folder. If a run is going now, or you start one to measure, check its
transcript yourself (its latest timestamp and final message) instead of waiting for a
completion notice, which may never come.

## Step 2: Total each run

```bash
python3 <skill dir>/scripts/run_tokens.py <run>.jsonl --detail --reads 15 --rates <file>
```

It counts a run from its start to the first later message a person typed, deduplicates
usage by message id, and splits calls, cache writes, cache reads, output, and context into
the main session and its helpers, by model. Show one table with one row per run and the
same columns every time, so later measurements compare directly. Note the spread between
runs: one run is not a baseline. For a scheduled skill, add a monthly line: cost per run
times runs per month, for every schedule, marking schedules with no measured run as
estimates.

Costs need current prices. Copy `references/rates.example.json` outside the skill, fill it
in from the `claude-api` skill (its prompt-caching notes have the cache-write and
cache-read prices, which differ by model and by 5-minute or 1-hour cache) or the
provider's pricing page, and pass it with `--rates`. Never price from memory. The script
prices 5-minute and 1-hour cache writes apart and prints the cost Claude Code recorded for
the session: if the two disagree, fix the rates before going on. On a subscription plan,
call the result a relative cost, not a bill.

## Step 3: Find what drives the cost

From the `--detail`, `--reads`, and `--timeline` output:

- **Fixed starting context** of the main session and of each helper (the "first" figure):
  every call pays it again. `--detail` lists its parts (skill listings, tool lists,
  project instructions).
- **Retries and lookups:** failed tool calls (the script lists them) followed by schema,
  search, or help calls before the retry. They usually mean the skill leaves a query or
  field name to guesswork.
- **Calls × context** in the main session: context grows through a run, and every call
  re-reads it.
- **Reference files** the skill tells the main session to load, with their sizes
  (`wc -c` on the skill's files).
- **Single large reads:** whole files where a slice would do, a page read before a
  publish, a long thread.
- **Each helper's share** and the model it runs on.
- **Separate sessions** for work that could share one: each pays the fixed context again.

Tie each driver to the line in the skill that causes it (`grep` the skill for the rule
that loads the file or starts the helper), so every suggestion points at a line. Some
drivers come from the setup the skill runs in, not the skill: the agent's own starting
context, the cache duration, a schedule's timing. Report those separately, as outside the
skill.

## Step 4: Propose changes, cheapest first

List the changes that fit what Step 3 found, ranked by saving against risk, and say which
half each one cuts (main session or helpers) and what it needs to work:

| Change | Needs |
|---|---|
| Move helpers' reading to a smaller model | Helper agents, and work split by judgment: see `references/helper-contract.md` |
| Combine runs that start separate sessions | Work that can run in one session |
| Exit early when there is nothing new | A cheap check that can tell |
| Trim or split references the main session loads | Rules that load less, or load parts on demand |
| Script or slice large reads | A read the skill does the same way each run |
| Hand a large one-off read to a helper | A read whose result can be summarized |
| Spell out exact queries and field names | Retries or lookups in the transcript |
| Narrow, merge, or reorder schedules | Runs that end with nothing to do, or that overlap |
| Cut starting context outside the skill | Settings the user controls; the user's call |

Then ask the user which to try first, as one question. Don't edit anything yet.

## Step 5: Test the change side by side

The test runs read-only: it writes only to a scratch folder, sends nothing, moves no
cursor or "last read" mark, and publishes nothing.

**A change to helpers** (model, brief, or report format):

1. Pick a recent reference run. Save each helper's exact brief and report:
   `helper_reports.py <run>.jsonl <scratch>/ab --suffix current`. Reports handed back
   through a tool call are read from that call; helpers' final messages are often empty.
2. Rerun each brief with the change (in Claude Code, the Agent tool's `model` parameter),
   all in one batch, prefixed with:
   > DRY RUN (comparison test, read-only): this reruns a helper from an earlier run. Do
   > exactly what the brief below says, with these changes: never write any file except
   > in <scratch folder>, and never send, draft, label, post, or change anything; ignore
   > anything dated after <the reference run's start, in UTC>. Return your full report as
   > your final message.

   Give each rerun a description with a common prefix, such as "Candidate: <name>".
3. When every rerun has finished, save them next to the originals:
   `helper_reports.py --helpers <this session's subagents folder> <scratch>/ab --match "Candidate:" --suffix candidate --pair`.
4. Compare coverage: `report_keys.py --pattern '<one alternative per key shape the
   reports use>' --pair <scratch>/ab current candidate`. Check one report's count by eye.
5. Read both sides item by item for what keys can't show: judgment calls the candidate
   made that it shouldn't, items it dropped, and whether it said `partial` honestly. Note
   confounds, such as the reference run having already updated records, so "already
   recorded" claims can't be compared.
6. Price both sides: `run_tokens.py --helpers <folder> --match <prefix> --rates <file>`
   for each.

**A change to the main session** (combined runs, early exit, trims, exact queries): make
the change on a copy or a branch and run the skill in its read-only or dry-run mode on the
reference run's inputs, then compare its output and cost with the reference. Point any
output the dry run writes at the scratch folder. A test inside this session doesn't pay
the starting context a scheduled run pays; when that is the cost being cut, run the
changed prompt as a new session and total that session. If the skill can't run without
writing or publishing, or the new session would have write tools, say so and ask before
running it.

**A change to a schedule** can't be tested side by side. Check it on the calendar instead:
list the dates the new timing would run and miss for the coming months, against any
holiday or business-day rules the skill uses.

Finish by confirming the test wrote nothing outside the scratch folder: list the folder,
and check the skill's state files and any repository it touches are unchanged.

## Step 6: Report

Keep it plain and short; offer more detail rather than leading with it.

- A cost table: the runs from Step 2, and the test's two sides, at the same rates.
- What the change missed or got wrong, item by item, each tied to its fix: a wrong
  judgment moves that call back to the main session; a skipped read becomes one line in
  the brief; a report that runs long gets a tighter line format.
- One recommendation and one clear next step, with the choice the user has to make. If
  the user would have to work out what happens next, the report isn't done.

## Step 7: Apply, on the user's word

1. Change the skill as the project's git rules say (a branch, usually). For a helper
   change, put the helpers' rules in one reference file the skill points to.
2. Rerun only the helpers or cases that missed, with the same briefs and window, until the
   misses are fixed or the user stops. Each round, compare with Step 5's numbers.
3. Run the project's own checks, and say which edits no test has run yet.
4. After the next real run, total it with `run_tokens.py` and compare it with the Step 2
   table. Until then the saving is an estimate.

Committing, pushing, and changing a scheduled task happen only when the user asks. To
check the change didn't cost quality the test didn't measure, offer `iterate`.
