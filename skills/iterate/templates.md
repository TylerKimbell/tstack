# Iterate templates

Load this file when routing the request. It holds the Step 1 message, the spec and log
skeletons, the flow cards that fill the spec, and the brief template for Step 4.

## Step 1 message

One message, with every field the route uses filled in or drafted. Leave out fields the
route doesn't use.

| Field | No spec | New flow on a spec | Rerun | Review | Make it better |
|---|---|---|---|---|---|
| The thing | yes | if new | if missing | yes | yes |
| Where the spec will live | if unclear | | | if unclear | if unclear |
| The flow and its card | yes | yes | | yes | best fit, plus others |
| Target and budget | yes | yes | yes | report only | yes, or a single pass |
| Evaluators | yes | yes | if missing | yes | yes |
| Publishing | yes | yes | yes | | yes |
| Draft guardrails | yes | In scope changes | | yes | yes |
| Draft scenarios | yes | yes | new ones only | yes | yes |
| Fixtures and checks | yes | yes | if missing | yes | yes |
| Open proposals and "not covered" items | | | yes | | |
| Backfill | | | yes | | |

What each field needs:

- **The thing:** where it lives, how an evaluator reaches it (tools, account, limits), and
  any test tool it already has. For a prompt, the model it runs on in production.
- **Where the spec will live:** only when Step 2's rule doesn't settle it.
- **The flow and its card:** if the user names no flow, suggest the one that fits best and
  name one or two others.
- **Target and budget:** default 7/10 within 3 rounds for a new flow; on a rerun, one point
  above the last logged score, even across a break, within 2 rounds. Take the user's
  numbers, however large, and fill a missing one from the default. Never run more than
  one round without a limit. If the target is above 8 or more than 2 points above the last
  score, say the run may stop early on a plateau, and go ahead.
- **Evaluators:** default one, the session's model at the session's effort; up to three
  from Step 4's table, or the user's own panel. Name the primary. Warn about cost if Fable
  is on the panel.
- **Publishing:** only when fixes would or might reach people using the thing: live each
  round, live when the run ends, or a draft for the owner. For a draft, say where it lives
  and how an evaluator reaches it.
- **Draft guardrails:** from the skeleton. If they would leave the likely fixes as
  proposals, say so, so the owner can widen Fix directly; otherwise a run can end after one
  round with nothing to change.
- **Draft scenarios:** from the card. If you can reach the thing, look at it first;
  otherwise mark them "to confirm on first look" and confirm them yourself before round 1.
- **Fixtures and checks:** what the evaluator needs (test records, sample inputs, the
  facts a prompt assumes), and whether they're real or invented stand-ins, which can cap
  the score (Step 7, rule 6). Ask for facts only the owner knows, and before creating a
  record others can see.
- **Open proposals and "not covered" items:** from the run log, each with its status; one
  with no status counts as open.
- **Backfill:** what Step 2's Rerun item 2 would add, and anything that would be a break.

## Spec skeleton

Copy it and fill in every line by the end of Step 4. In a new spec, Settled decisions read
"None yet". Evaluators read this file, so it never holds scores or the run log.

```markdown
# Iterate spec: <the thing>

## The thing
<What it is, who uses it, what it's for, and how an evaluator reaches it.>

## Guardrails
**In scope:** <what evaluators judge>
**Out of scope:** <what they leave alone, such as whether the content is correct>
**Fix directly:** <changes that keep the owner's intent: structure, wording, labels, styling>
**Propose to the owner:** <changes to content, scope, dates, people, or purpose>

## Fixtures
<Test records and sample inputs, what's off limits, and how to reset between rounds.>

## Checks
<What to run before every round and what passing looks like, or "None" and why.>

---

## Flow: <name>
**Card:** <user walkthrough, lens review, skill dry run, prompt dry run, or custom>
**Who and what:** <the user and their job, or the reviewer and their lens>
**Target and budget:** <such as 7/10 within 3 rounds, or report only>
**Evaluators:** <the panel, with the primary marked>
**Publishing:** <live each round, live when the run ends, a draft for the owner, or none
and why (report only, or no fix can reach anyone)>

### Scenarios
1. <scenario>

### Questions at each scenario
- <what must be true there>

### Rubric
Score from 1 to 10, a judgement, not an average of the sub-scores.
Anchors: <from the card>
Sub-scores:
- <name>: <one-line definition>

### Settled decisions
- <decision>: <one-line reason>

### Brief
<The exact text every round's evaluators get.>
```

## Log skeleton

A separate file beside the spec. In a new log, Run state reads "not started" and the
entries read "None yet".

```markdown
# Iterate log: <the thing>

## Flow: <name>
**Run state:** <rounds used of this run's budget; the primary's best score since the
latest baseline; last round that made progress; where the starting version and the fixes
are>

<Rounds, newest last.>
```

## Flow cards

Pick the card that matches the flow and copy its parts into the spec. Adjust scenarios and
questions to the thing; keep the anchors and sub-score definitions unless the user agrees
otherwise. For a flow no card fits, write a custom card with the same five parts and show
it to the user.

### User walkthrough

A person doing a job with a page, app, document, or workflow.

- **Opener:** You are <user> doing <job> for the first time.
- **Scenarios:** the points the user reaches. For a timeline, the boundaries of the window
  the flow covers (before it starts, its first day, its last day, the day after) plus its
  midpoint and, for a window longer than two weeks, its quarter points, counted in the
  units the thing uses (the day before it starts is day 0; a half rounds up). For steps,
  each step plus the empty, half-done, and finished states. When the thing has both, use
  the timeline and put the step states on its days: empty on day 0 and the first day, half
  done at the midpoint, a few left on the last day, and those overdue the day after. Views
  or tabs aren't separate scenarios: check each view at every scenario, in the questions.
  If the window's unit is ambiguous (working or calendar days), mark it to confirm.
- **Questions:** What do I do now? What's due next, and by when? Where do I mark it done?
  When the user clicks, types, ticks, or switches anything, add: the next step is obvious
  without reading everything; labels say what they do in the user's words; missing
  information has a clear consequence; errors say how to fix them; nothing destructive
  happens on one click.
- **Anchors:** 10, every scenario done without help or guessing; 7, all done with some
  hesitation; 4, stuck in at least one; 1, unusable.
- **Sub-scores:**
  - Clear next step: at each scenario, what to do now is obvious from the top.
  - Findability: anything the user needs is reached without hunting.
  - Labels: titles, buttons, and notes say what they do in the user's words.
  - Timing: every item says when it's due, and shows up when it matters.
  - Effort: the scrolls, clicks, and reading each task takes.

### Lens review

A reviewer judging the thing against one lens, such as visual styling or accessibility.

- **Opener:** You are reviewing <thing> for <lens>.
- **Scenarios:** the pieces to examine one at a time: each distinct kind of component
  once, with its states counted as one piece, plus the whole thing at phone width. Up to
  twelve. For something that changes over time, look at the state that shows the most
  kinds of item state, and say which.
- **Questions:** For styling: does this piece match the others of its kind, does the eye
  land on what matters, and is colour used for meaning? Check each theme the thing has.
- **Anchors:** 10, every piece passes the lens; 7, small inconsistencies a user would
  rarely notice; 4, at least one piece clearly fails; 1, fails throughout.
- **Sub-scores** for a styling lens:
  - Navigation: moving between parts and back takes no hunting.
  - Hierarchy: the eye lands on what matters first; reference material looks secondary.
  - Density: cards, lists, and tables scan easily; nothing long stays expanded.
  - Consistency: the same kind of thing looks and behaves the same everywhere.
  - Typography and colour: readable sizes, enough contrast, colour carries meaning.

### Skill dry run

An agent following a skill or set of instructions on sample requests.

- **Opener:** You are an agent that has just loaded <skill>, working through sample
  requests. Write what you would produce; don't run anything outward-facing.
- **Scenarios:** four to eight realistic requests, including one the skill should decline
  or hand off, and one that resumes earlier work if the skill supports that.
- **Questions:** What do I do next? Where did I guess, and what did I guess? Would a second
  agent do the same?
- **Anchors:** 10, every request carried out without guessing; 7, all carried out with
  some guessing; 4, stuck or wrong in at least one; 1, unusable.
- **Sub-scores:**
  - Clarity: each instruction says what to do without interpretation.
  - Completeness: no step leaves the agent stuck or guessing.
  - Reproducibility: two agents would produce comparable output.
  - Scope fit: it handles the requests it should and turns away the ones it shouldn't.
  - Economy: nothing could be cut without losing behaviour.

### Prompt dry run

A model following a prompt on sample inputs. Run the prompt on the production model from
Step 1 when the tools allow (a runner setting, not part of the brief), and record which
model ran it, since scores may not carry over. With a panel, a different model on it judges
the outputs, so no model grades its own work; with one evaluator, it produces and judges
in the same pass, and the log says so. Clarifying an existing instruction is a direct fix;
adding an instruction is a proposal, unless the owner widened Fix directly in Step 1.

- **Opener:** You are the model this prompt instructs. Run it on each sample input, then
  judge the outputs. (With a judge from the panel: You are judging outputs this prompt
  produced on each sample input.)
- **Scenarios:** four to eight inputs from the fixtures: typical ones, an edge case, and
  one the prompt should refuse or redirect.
- **Questions:** Does each output follow every instruction? Would its reader act on it as
  is? Where did the prompt leave the model guessing? If it has no rule for an input it
  should refuse or redirect, report the gap as a proposal.
- **Anchors:** 10, every output usable as is; 7, all usable with small edits; 4, at least
  one wrong or unusable; 1, mostly unusable.
- **Sub-scores:**
  - Follows instructions: every output obeys every instruction in the prompt.
  - Output quality: the reader could use the output without edits.
  - Consistency: similar inputs get similar handling.
  - Scope fit: it handles what it should and refuses or redirects what it shouldn't.
  - Economy: the prompt has no instruction that changes nothing.

## Brief template

Fill it in once per flow, save it in the spec, and send it word for word every round.

```markdown
<Opener from the card.>
Report only: don't change the thing or its settings. Change data only in the fixtures
the spec names, and list what you changed. Never touch <real records and controls>.

**What it's for:** <one paragraph>

**Settled decisions, don't raise or score these:** <from the spec>

**Read:** <spec location>, the shared part and the "Flow: <name>" section, and any file
they point to. Don't open the run log beside it; form your own view. Judge only what this
flow's Who and what covers, even where the shared In scope is wider.

**Scenarios:** <each one, and what to do there>

**How to reach it:** <where it is, which tools to use, and what they can't do there>

**Report, in about 700 words:**
1. Score N/10 as a whole number, one line on what holds it back, and the sub-scores
   (<names>), also whole numbers.
2. How well it serves this flow overall.
3. Findings ranked by impact: where, what's wrong, the concrete change, and what the
   change replaces. Tag each [direct] or [proposal] using the spec's guardrails, and
   [high] or [low] impact.
4. Next point: what would raise the score by one, and whether that lies in the thing or
   in the test (invented stand-ins, tools that can't reach part of it).
5. Alternatives: a different format or structure that would work better, and what it
   would replace.
6. Keep: what works and shouldn't change.
7. What you changed in the fixtures, and what you couldn't check.
```
