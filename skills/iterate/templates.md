# Iterate templates

Load this file when routing the request. It holds the Step 1 message, the spec skeleton,
the flow cards that fill it, and the brief template for Step 4.

## Step 1 message

One message, with every field for the route filled in or drafted. Leave out fields the
route doesn't use.

| Field | No spec | New flow on a spec | Rerun | Review | Make it better |
|---|---|---|---|---|---|
| The thing and how an evaluator reaches it | yes | if new | if missing | yes | yes |
| Where the spec will live | if unclear | | | if unclear | if unclear |
| The flow and its card | yes | yes | | yes | best fit, plus others |
| Target and budget | yes | yes | yes | report only | yes, or a single pass |
| Publishing, if fixes would or might reach live users | yes | yes | yes | | yes |
| Draft guardrails | yes | In scope changes | | yes | yes |
| Draft scenarios | yes | yes | new ones only | yes | yes |
| Fixtures and checks the evaluator needs: real or invented, facts only the owner knows, records others can see, any test tool the thing has | yes | yes | if missing | yes | yes |
| Open proposals and "not covered" items | | | yes | | |
| Backfill (Step 2, Rerun item 3) | | | yes | | |

## Spec skeleton

Copy it and fill in every line by the end of Step 4. In a new spec, Settled decisions and
Run log read "None yet".

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
**Publishing:** <live each round, live when the run ends, or a draft for the owner>

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
<The exact text every round's evaluator gets.>

### Run log
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
  the flow covers (before it starts, its first day, its last day, the day after) plus a
  few days between, counted in the units the thing uses. For steps, each step plus the
  empty, half-done, and finished states. When the thing has both, use the timeline and put
  the step states on its days: empty at the start, half done in the middle, overdue the
  day after. Views or tabs aren't separate scenarios: check each view at every scenario,
  in the questions. If the window's unit is ambiguous (working or calendar days), mark it
  to confirm.
- **Questions:** What do I do now? What's due next, and by when? Where do I mark it done?
  For anything clicked through, add: the next step is obvious without reading everything;
  labels say what they do in the user's words; missing information has a clear
  consequence; errors say how to fix them; nothing destructive happens on one click.
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
  twelve. For something that changes over time, look at one representative state and say
  which.
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

A model following a prompt on sample inputs. The evaluator produces the outputs and judges
them in the same pass; say so in the log, because a model grading its own outputs can
miss what it got wrong. Run it on the production model from Step 1 when you can, and
record which model ran it, since scores may not carry over. Clarifying an existing instruction is a direct fix;
adding an instruction is a proposal.

- **Opener:** You are the model this prompt instructs. Run it on each sample input, then
  judge the outputs.
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
they point to. Ignore the run log; form your own view. Judge only what this flow's Who and
what covers, even where the shared In scope is wider.

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
