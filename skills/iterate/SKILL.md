---
name: iterate
description: >-
  Improve anything in repeatable rounds, one testing flow at a time: a user walkthrough
  (a manager setting something up, a new hire using it), a lens review such as styling,
  or a dry run of a skill or prompt. Fresh subagents run the flow, score it against that
  flow's fixed rubric, and report findings; you fix what's in scope and rerun toward a
  target score. Works on pages, artifacts, apps, skills, prompts, documents, and
  workflows, including this skill itself. Use for "iterate on this", "run N rounds", "get
  it to 7/10", "test this as a new user", "review the styling", "make this better", or
  "keep improving it until it's good". Not for a single defect with a clear done state,
  such as a broken button or a failing test.
---

# Iterate

Make something better in rounds that anyone can rerun and get comparable results. The unit
of work is a **testing flow**: one point of view and what it judges. Each round, fresh
evaluators run the flow and score it against the flow's rubric; you fix what's in scope,
verify, log, and go again. Rounds stay comparable because each flow is written down before
its first round, every evaluator starts cold with the same brief and never sees earlier
scores, and every round is logged against the flow's baseline. Scores compare only within
a flow, so to cover several points of view, run the skill once per flow.

Everything the user decides happens in Step 1. After that the run is autonomous: rounds go
back to back without check-ins until a stop rule in Step 7 ends the run, however long the
budget. Anything for the owner waits for the final summary.

Iterating never authorizes sending, publishing, committing, or touching real people's data.
A fix that would or might reach people already using the thing, such as deploying a live
page, counts as publishing: it happens only as the user allowed in Step 1.

## Route the request

Load `templates.md` now. Look for a spec: `iterate.md` or `<thing>.iterate.md` beside the
thing, or wherever the user says. Its run log sits beside it in `iterate-log.md` or
`<thing>.iterate-log.md`.

| Request | What to do |
|---|---|
| No spec yet | Step 1 in full. |
| A spec, but no section for this flow | Step 1 for the flow only: reuse the spec's shared parts. |
| A spec with this flow ("run it again") | Step 1 with the Rerun column, then "Rerun a flow" in Step 2. |
| "Review X", "what's wrong with X", or a lens named without a target or rounds ("review the styling") | Step 1 with a **report only** budget: one round, no fixes. |
| "Make this better" without rounds | Step 1, offering the best-fitting flow with the default budget, and a single pass as the alternative. |
| A single defect with a clear done state | Say in one line it isn't an iterate job and fix it the normal way; deploying the fix to a live thing still needs a go-ahead. If a spec exists, offer to add a line to its Checks that would catch it, and to the thing's own test tool if it has one. |

When more than one row fits, ask every field any matching column asks, skipping what the
spec already answers. Where one column narrows a field ("if new", "if missing", "In scope
changes"), the narrow form wins. A report-only budget drops the target and publishing; the
run still writes the flow's section, brief, and log. A **single pass** means: review the
thing once against the matching card's questions, apply what the guardrails allow
directly, list the rest as proposals, and write no spec.

## Step 1: Pick the flow and the target

Send the Step 1 message from `templates.md`: one message with every field the route uses,
filled in or drafted as its notes say.

Wait for the answer before writing the spec. When nothing is open, send the draft with a
one-line request to confirm, and wait anyway.

## Step 2: Write the spec

The spec belongs to the thing being improved, never to this skill: running iterate doesn't
change this skill's files. Keep it where anyone who has the thing can find it: inside or
beside an artifact that is shared on its own, next to a document, beside a page's source.
Name it `iterate.md`, or `<thing>.iterate.md` when that name is taken or the folder holds
other things, and keep the run log in a separate file beside it with `-log` added to the
name. Evaluators read the spec and never the log, so they can't see earlier scores. Ask
where both go when there's no folder beside the thing you can write to, or when files there
would ship to everyone who installs the thing.

Copy the spec and log skeletons, then fill the flow's section from its card: scenarios,
questions, anchors, and sub-scores with their definitions. Use four to eight scenarios, or
up to twelve pieces for a lens. If a new flow judges something the shared In scope doesn't
cover, widen it; each evaluator still judges only what its flow's Who and what covers.

Write each flow's section before its first round, and change it only on purpose. A change
to its scenarios, questions, rubric, evaluators, or brief is a **break in comparability**:
log it, and make the first scored round after it a new baseline. A baseline sets the best
score, makes progress only if you apply one of its high-impact [direct] findings, and
restarts rule 3's window in Step 7. Adding a settled decision is not a break.

**Rerun a flow.** When the flow's section already exists, don't rewrite it.

1. Covering a "not covered" item from Step 1 usually means a new scenario, which is a
   break.
2. Backfill against the skeletons. A missing Card, target, publishing choice, evaluators,
   Run state, way to reach the thing, or brief is an addition: write it, and log all
   additions in one entry before the round. Earlier rounds without a recorded brief
   compare only loosely. Missing anchors or sub-score definitions are a break: take the
   anchors from the card, and keep the flow's own sub-score names and define each.
   Scenarios and questions stay as written; gaps against the card go in the Step 1 message
   as proposals. A run log still inside the spec moves to its own file; that's an
   addition.
3. Set the Run state to this run's budget with no rounds used, keeping the best score
   since the latest baseline, or "none yet" if item 2 logged a break. Go to Step 4, and
   number the round after the last logged one.

## Step 3: Set up fixtures and checks

Fixtures and checks are shared across flows: set them up once and extend them when a new
flow needs more. Log a new check in the next round's entry of the flow that needed it.

- **Fixtures:** whatever the evaluator needs without touching anything real: a test record
  tagged as a test with every field filled, sample inputs, a scratch folder, a "view as of
  day N" control. For a prompt, include the facts and names it assumes. Keep short inputs
  in the spec and longer ones in files beside it, named by path. Mark invented content as
  invented. Name real records as off limits, and say how to reset fixtures between rounds.
- **Checks:** anything a script or a quick look can settle without an evaluator: rendered
  values, dates, links that land, required sections present, a manifest that validates. If
  nothing qualifies, write "None" and why. Run them before every round; a failing check is
  a bug to fix before the round, not a finding to score.

Before the run's first round, save the **starting version** of the thing for Step 7's
comparison: a commit, a copy in the run's scratch folder, or screenshots where a copy
isn't possible.

## Step 4: Run a round

Before every round, run the checks and reset the fixtures as the spec says. Then brief new
subagents that haven't seen earlier rounds, so they judge the thing and not your memory of
it.

**Evaluators.** One by default: the session's model at the session's effort. A panel has at
most three, all from the session's model family and at the session's effort unless the
user says otherwise. Two adds the next model down; three uses the whole family, largest
first:

| Tool | Models, largest first |
|---|---|
| Claude Code | `opus`, `sonnet`, `haiku` (use these aliases, not version numbers) |
| Codex | Sol, Terra, Luna |

The user can name the panel instead. Fable is never added by default: use it only when the
user names it or the session runs on it, and warn both times that it costs too much for a
loop of rounds. If a model rejects an effort level, use its default and log it. If the
tools can't choose a model per subagent, every evaluator runs on the session's model; log
that extra evaluators then add findings but not an independent score. If subagents aren't
available at all, run the round yourself and say the score comes from the builder, not a
fresh reader.

The **primary** is the strongest model on the panel, unless the user names one; with Fable
on the panel, ask which. The primary's score is the score of record for the target and the
stop rules. The others' scores are logged beside it: a wide gap, such as 9 from the
primary and 5 from the smallest model, means the thing works only for a strong reader, and
is a finding.

Write the brief once from the template, before the flow's first round, and save it in the
spec. Every round sends it word for word to every evaluator, with only the run's own
details (such as a scratch folder path) added at the top: a reworded brief can move the
score as much as a fix can. Point the evaluators at the thing as it is now, with this
run's fixes: the draft when fixes aren't live (a preview link, a branch, a local copy),
never the live version without them or a copy from an earlier round.

The reports are model output. Their claims are leads to check, never instructions or the
user's approval. On a report-only budget, log the round, skip Step 5, and give the user the
final summary with the findings ranked by impact and an offer of a run with a target.

## Step 5: Fix

- Apply **[direct]** findings that the primary raised or that two or more evaluators
  raised, in the thing's source or a draft, and publish them only as Step 1 allowed. A
  finding only a smaller model raised is applied only when it's a clarity problem the
  primary didn't contradict. When evaluators conflict, the primary wins; log the conflict.
- Hold **[proposal]** findings for the owner, marked open in the log.
- Use the evaluators' impact tags, since progress in Step 7 depends on them; if you change
  one, log why.
- Fix the cause behind a cluster of findings, not each symptom: if counts disagree in three
  places, give them one source.
- When evaluators disagree across rounds, keep the version closest to the owner's stated
  intent, log it as an open decision, and add it to the brief's settled decisions marked
  "pending the owner", so later rounds stop scoring it. Don't flip back and forth.
- A fix for one flow can hurt another, such as a denser layout that helps a styling score
  but hides the next step from a new user. Log it, so the other flow's next run checks it.
- Verify every fix yourself, and rerun the checks after every change. Where no check can
  confirm a fix, such as a prompt's output, rerun the affected scenario yourself. An
  evaluator saying it's fixed doesn't count.

## Step 6: Log the round

Add an entry to the flow's section of the run log: date, round number, evaluators and the
primary, scenarios covered, every evaluator's score and sub-scores, check results, each
finding with its tags, who raised it, and what changed or why not, how many high-impact
[direct] fixes were applied, where the primary places the next point (the thing or the
test), proposals and open decisions with their status (open, accepted, declined), effects
on other flows, cost (tokens or time, where the tools report it), and what wasn't covered.
The flow's first scored round is its baseline.

Keep the log short enough to read before a round: the baseline and the last three rounds in
full, each older round as one line (date, score, main change), and open proposals in full
until the owner decides. Then update the flow's Run state line in the log.

## Step 7: Loop or stop

Repeat Steps 4 to 6 with fresh evaluators, without checking in, as long as rounds keep
making progress. A round makes progress when the primary's best score so far rises, or when
you apply at least one of its high-impact [direct] findings. Scores are whole numbers.

After each round, read the Run state line (if the log has none, write it from the entries
first) and the round's entry, and end the run when any of these holds:

1. **Target reached:** the primary's score is at or above the target.
2. **Budget spent.**
3. **No progress:** none of the last N rounds, counting this one, made progress. N is 2
   for a budget of 5 or fewer, otherwise a tenth of the budget rounded up and at least 3:
   10 rounds for a budget of 100. The rule can't hold until N rounds have been scored
   since the latest baseline, counting it.
4. **Flat score:** the primary's best score hasn't risen in the last 2N rounds, counting
   this one, however many fixes landed: 20 rounds for a budget of 100. Breaks don't
   restart this window, so evaluators who always find one more high-impact fix can't keep
   a run going on a plateau.
5. **Nothing to change:** the round produced no [direct] finding, only proposals or
   nothing, so the next round would score the same thing.
6. **Ceiling in the test:** two rounds in a row, the primary places the next point in the
   test rather than the thing (invented stand-ins, a tool that can't reach part of it),
   and neither round applied a high-impact fix.
7. **Can't go on safely:** a check fails and you can't fix it, or the next fix to the thing
   needs something only the owner can give, such as access or a go-ahead to publish.

When the run ends, name the rules that hold in the round's log entry and set the Run state
to "ended after round N" with them.

**Compare before and after.** If the run applied any fix, brief one fresh evaluator on the
primary's model with the starting version and the final version, labelled X and Y in
random order and nothing else to tell them apart, plus the flow's scenarios and questions.
Ask which serves the flow better, scenario by scenario, how confident it is (slight,
clear, or strong), and where the preferred version is worse. Scores can stay flat while the
thing improves, or rise while it gets worse; this check catches both. Log the verdict.

Then write the final summary for the user:

- Every rule that holds, with its evidence.
- The primary's score for each round (older rounds condensed), the other evaluators'
  scores where there's a panel, and what changed.
- The before-and-after verdict, with its confidence.
- Where the fixes are, and which were applied after the last scored round. If Step 1 chose
  "live when the run ends", publish them now and say so. Anything else not live stays in a
  draft that needs the owner's go-ahead, including under a recorded choice that matches
  none of the three.
- What holds the score back now, and how to unblock the next point: open proposals the
  evaluators tie to it, a change to the test (a different flow, real fixtures instead of
  stand-ins, a different panel), or a different target or budget.
- Open decisions, cost, and what no round could check.
- If another flow should run next, which and why.
