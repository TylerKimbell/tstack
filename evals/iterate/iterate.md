# Iterate spec: the iterate skill

The spec for improving `skills/iterate/SKILL.md` with the iterate skill itself. Claude never
loads this file as part of the skill; it's here so anyone working on the skill can rerun the
same flows and compare scores.

## The thing

`skills/iterate/SKILL.md`, with its `templates.md`, teaches an agent to improve something in repeatable rounds, one
testing flow at a time: write a spec, have a fresh subagent run the flow and score it, fix
what's in scope, log, and rerun toward a target. It has to work on any kind of thing (a
page, an artifact, a skill, a prompt, a document, a workflow) and for any flow (a user
doing a job, or a reviewer with a lens), and two agents following it should produce
comparable specs, briefs, and scores.

## Guardrails

**In scope:** whether an agent can follow the skill without guessing, whether two agents
would do the same thing, whether it fits the requests it should handle and declines the
ones it shouldn't, and its length.

**Out of scope:** the tstack README, the other skills, and the plugin manifests, except
that the README row must still describe the skill.

**Fix directly:** wording, step order, examples, and a missing instruction that serves
what the skill already does.

**Propose to the owner:** changing what the skill is for, adding or removing a step,
renaming it, changing the flow model, or changing the report format.

## Fixtures

- `fixtures/existing-spec.md`: a spec that already has a manager flow and a run log, for
  scenario 4.
- `fixtures/sample-prompt.md`: a short prompt to improve, for scenario 3.
- `fixtures/plateau-spec.md`: a long run that has stalled, for scenario 6.
- `fixtures/progress-spec.md`: a long run that is still making progress, for scenario 7.
- A scratch folder for the evaluator's output: a new empty temporary folder each round,
  outside this repository. That's the reset; nothing in the repository changes during a
  round.

## Checks

Run `python3 evals/iterate/check.py` from the repository root before every round. It checks
that the skill's frontmatter has the right name and a description under 1024 characters,
that the plugin manifests are valid JSON, that the README has a row for the skill, and that
every file this spec names exists.

---

## Flow: dry run

**Who and what:** an agent that has just loaded iterate and has a request from a user. It
judges whether it can carry out the request from the skill alone.
**Card:** skill dry run.
**Target and budget:** 8/10 within 3 rounds.

The evaluator doesn't run any rounds or spawn subagents. For each scenario it writes, in
the scratch folder, what it would produce by following the skill: the flow section of the
spec, the round-1 brief, and the questions it would ask the user first. Then it reviews the
skill.

### Scenarios

1. **User flow on a page.** "Iterate on our 90-day onboarding plan page as a new hire in
   their first week. Get it to 7/10." The page is a shared web page with a To do view and a
   Learning view, and a "view as of day N" control. It has no spec yet.
2. **Lens flow.** "Review the styling of that same onboarding page." Treat the page as
   having the spec you wrote for scenario 1, with no styling flow in it.
3. **No budget given.** "Make this prompt better," with `fixtures/sample-prompt.md`.
4. **Spec already exists.** "Run the manager flow on the onboarding page again," with
   `fixtures/existing-spec.md` as the page's spec.
5. **Not iterate's job.** "The Save button on the onboarding page throws an error. Fix it."
6. **A stalled long run.** You are partway through a run on the onboarding page with
   `fixtures/plateau-spec.md` as its spec. Round 13 has just been logged. Decide what
   happens next.
7. **A long run still improving.** You are partway through a run on the support prompt with
   `fixtures/progress-spec.md` as its spec. Round 6 has just been logged. Decide what
   happens next.

### Questions at each scenario

- What do I do next, at each step of the skill?
- Where did I have to guess, and what did I guess?
- Would a second agent write the same flow section, brief, and questions?
- Did the skill handle this request the right way: run it, ask first, reuse the spec, or say
  it isn't the right tool?
- In a run already under way: does the skill say clearly whether to continue or stop, and
  does it keep going without checking in with the user while it is still making progress?

### Rubric

Score from 1 to 10, a judgement, not an average of the sub-scores. Anchors: 10, every
request carried out without guessing; 7, all carried out with some guessing; 4, stuck or
wrong in at least one; 1, unusable. Sub-scores:

- **Clarity:** each instruction says what to do without interpretation.
- **Completeness:** no step leaves the agent stuck or guessing.
- **Reproducibility:** two agents would produce comparable specs, briefs, and scores.
- **Scope fit:** it handles the requests it should and turns away the ones it shouldn't.
- **Economy:** nothing in it could be cut without losing behavior.

### Settled decisions

- **One flow per run.** Running the skill once per flow is the owner's design. Don't score
  it as a gap.
- **Specs live with the thing, never in the skill's folder.** The owner chose this so
  installed copies of the skill stay clean.

### Brief

The runner adds two lines at the top: the repository root and the scratch folder path.

> You're an agent that has just loaded the `iterate` skill. This round checks whether an
> agent could carry out real requests from the skill alone. Report only: don't change
> anything in the repository, and write only in the scratch folder named above.
>
> **What the skill is for:** improving something in repeatable rounds, one testing flow at
> a time. It writes a spec, has a fresh subagent run the flow and score it against a fixed
> rubric, fixes what's in scope, logs the round, and reruns toward a target. It should work
> on any kind of thing and any flow, and two agents following it should produce comparable
> specs, briefs, and scores.
>
> **Settled decisions, don't raise or score these:** one flow per run; specs live with the
> thing being improved, never in the skill's folder.
>
> **Read**, with paths relative to the repository root:
> - `skills/iterate/SKILL.md`, the version on disk now, and any file it tells you to load.
> - `evals/iterate/iterate.md`: the shared part (The thing, Guardrails, Fixtures, Checks)
>   and the "Flow: dry run" section. Ignore its run log; form your own view.
> - The fixtures in `evals/iterate/fixtures/` when a scenario names them.
>
> Don't run rounds, spawn subagents, open a browser, or use any tool other than reading
> files and writing in the scratch folder.
>
> **For each of the seven scenarios** in the dry-run section, follow the skill as if the
> user had just sent that request, and write `scenario-N.md` in the scratch folder with:
> 1. The questions you'd ask the user before starting, or "none" and why.
> 2. The spec you'd write for the flow (for scenario 4, what you'd change in the existing
>    spec instead).
> 3. The round-1 brief you'd send the evaluator.
> 4. **Guesses:** every place the skill left you guessing, and what you guessed.
>
> For scenario 5, write what you'd do instead. For scenarios 6 and 7, a run is already under
> way: write what you do after the last logged round and why, naming any rule you apply.
> If you stop, write the final summary. If you continue, say what the next round does and
> whether you contact the user. Where a scenario needs facts you don't have, such as the
> page itself, invent a plausible stand-in and mark it as invented.
>
> **Then report, in about 700 words:**
> 1. Score N/10 as a whole number, one line on what holds it back, and whole-number
>    sub-scores for clarity, completeness, reproducibility, scope fit, and economy.
> 2. How well the skill serves an agent carrying out these requests.
> 3. Findings ranked by impact: the section of `SKILL.md`, what's wrong, the concrete
>    change (replacement wording where you can), and what it replaces. Tag each
>    **[direct]** or **[proposal]** using the spec's guardrails, and **[high]** or **[low]**
>    impact.
> 4. Next point: what would raise the score by one, and whether that lies in the skill or
>    in this test.
> 5. Alternatives: a different structure that would work better, and what it would
>    replace.
> 6. Keep: what works and shouldn't change.
> 7. What you wrote in the scratch folder, and what you couldn't check.

### Run log

Rounds 1 to 3 tested the skill before the restructure. Round 4 is a new baseline: the skill
gained a routing table and moved its templates and flow cards to `templates.md`, and this
spec changed with it (scenarios 1 and 2 now say which spec exists, the anchors match the
skill dry run card, and the brief reads files the skill points to). Don't compare round 4
with earlier rounds.

- **2026-11-08, round 1 (baseline), fresh subagent. 7/10.** Clarity 7, completeness 6,
  reproducibility 6, scope fit 6, economy 8. Scenarios 1 to 5. Checks pass. Held back by:
  no path for rerunning a flow, no score anchors, no rule for declining. Findings and what
  changed:
  - No rerun path; target and budget not stored. Added "Rerun a flow" to Step 2, a pointer
    from Step 1, and a "Target and budget" field per flow.
  - Open proposals had no way to carry into a later run. They're now marked open in the log
    and raised at the start of a rerun.
  - No score anchors. Added anchors (10, 7, 4, 1) and "a judgement, not an average".
  - No decline rule. The description and intro now say a single defect isn't an iterate
    job: fix it normally and offer a check.
  - The brief's "don't change its data" conflicted with fixtures. Now: change data only in
    the named fixtures, and list it.
  - Step 1 now asks in one message, suggests a default target, and shows draft guardrails.
  - Smaller: timeline boundaries refer to the flow's window; usability rules go into each
    flow's questions; a 2-point threshold for using three evaluators; a prompt dry run is
    defined, with its own sub-score row; `openai.yaml` mentions lens flows.
  - Proposals, accepted by the owner: a "report only" budget; a copyable spec skeleton and
    brief template, replacing the bullet descriptions in Steps 2 and 4.
  - Declined: moving Step 3 before Step 2 (small gain, churns reviewed steps).
  - Effect to watch: the skill grew from 192 to 255 lines with the templates; economy may
    drop.
  - Not covered: real scores across several evaluators.
- **2026-11-08, round 2, fresh subagent. 8/10 (target met).** Clarity 8, completeness 7,
  reproducibility 7, scope fit 8, economy 7. Scenarios 1 to 5, all routed correctly
  (ask in one message, report only, suggest flows, rerun path, decline). Checks pass.
  Held back by: score anchors fit only user flows; no scenario count or sub-score
  definitions. Economy fell 8 to 7, as expected from the templates.
  - **Break in comparability:** score anchors were added to this flow's rubric between
    rounds 1 and 2 without being logged, so round 2 used a slightly different scale than
    the baseline.
  - Findings; the owner approved the [direct] ones, applied before round 3:
    - [direct] Anchors don't fit a lens flow; add lens anchors.
    - [direct] No scenario count (4 to 8; a lens up to 12 pieces) and no one-line sub-score
      definitions.
    - [direct] Rerun of an older spec: which missing parts to backfill, and that changing the
      rubric or scenarios breaks comparability.
    - [direct] Step 1 doesn't say to wait for an answer when nothing is open, or to ask
      before creating test records others can see.
    - [direct] "Make this better" without rounds: offer a flow, or do one pass.
    - [direct] Brief template has no dry-run opener and doesn't name the sub-scores.
    - [direct] "Fill in every line" doesn't match the step order.
    - [direct] A new flow may need the shared In scope widened.
    - [direct] The last two sentences of the skill-or-prompt section repeat Step 2.
    - [proposal, open] A prompt dry run grades its own outputs: split producing from judging,
      or accept it and say so.
    - [proposal, open] Move the skeleton and brief template to a `templates.md`, bringing
      SKILL.md to about 170 lines.
    - [proposal, open] Per-flow-type cards (opener, scenarios, anchors, sub-scores) in place of
      the table and scattered guidance.
- **2026-11-08, round 3, two fresh subagents (A and B) on the same brief. 8/10 and 8/10.**
  Both: clarity 8, completeness 7, reproducibility 7, scope fit 9, economy 7. Spread 0.
  Scenarios 1 to 5 routed correctly for both. Checks pass. Same score as round 2: a
  plateau. Held back by: routing spread across the intro, Step 1, and the rerun paragraph;
  open content (sub-score definitions, lens pieces, prompt anchors); length (269 lines).
  Findings, pending the owner:
  - Both raised: no anchors for a prompt dry run; the decline rule's "add a check" is
    ambiguous (make it a line in the spec's Checks); a rerun should also backfill anchors
    and sub-score definitions, logged as a rubric change.
  - A only: applying a fix to a live shared thing should count as publishing (ask first);
    Step 1 should say where to look for an existing spec; how to choose lens pieces;
    `<thing>.iterate.md` when `iterate.md` is taken; repeat the fixture-visibility ask on
    reruns.
  - B only: a spec without this flow shouldn't re-ask the shared parts; Step 1 should ask
    how the evaluator reaches the thing; one-line definitions in the sub-score table;
    prompt fixtures need the facts the prompt assumes; Checks may be "None" with a reason.
  - [proposal, open] Both: a routing table at the top (no spec, spec without this flow,
    rerun, report only, single pass, decline).
  - [proposal, open] Both endorse per-flow-type cards; B calls it the best fix for
    reproducibility.
  - [proposal, open] Prompt self-grading: B recommends accepting it and saying so.
  - [proposal, open] B: show draft scenarios and sub-scores in Step 1, not only guardrails.
  - Eval spec gap (B): scenarios 1 and 2 don't say whether the page already has
    `fixtures/existing-spec.md`. Fixing it changes the scenarios, so it needs the owner and
    breaks comparability.
  - Not covered: a live run on a real thing; evaluators from a different model.
- **2026-11-08, round 4 (new baseline after the restructure), two fresh subagents. 8/10
  and 8/10.** Both: clarity 8, completeness 7, reproducibility 7, scope fit 9, economy 8.
  Spread 0. All five scenarios routed to the right row for both; cards made rubrics and
  briefs near identical. Checks pass. Held back by: overlapping routing rows, an
  incomplete rerun backfill list, and scenarios, budget, and spec location still chosen
  from examples rather than rules. Findings; the owner approved the [direct] ones and the
  Step 1 message template, applied after the round (SKILL.md 166 lines, templates.md 198):
  - Both raised: rows overlap ("review" plus "spec without this flow"; say rows combine);
    the rerun backfill misses Card, how to reach the thing, and old sub-score names (keep
    the names, add definitions); Step 1 drafts guardrails "(Step 2)" before
    `templates.md` is loaded; no default budget for a rerun past its target; a thing that
    is both a timeline and a list of steps; lens themes should be "each theme the thing
    has".
  - A only: define "single pass"; log a new check in the next round's entry; prompt card:
    clarifying a rule is direct, adding one is a proposal, and a missing refusal rule is
    reported as a proposal.
  - B only: ask where the spec goes when there's no writable folder beside the thing; the
    "make this better" row should offer the best-fitting flow with Step 1 in the same
    message; deploying a declined defect's fix still needs a go-ahead; record which model
    ran a prompt dry run.
  - [proposal, accepted] Both: a Step 1 message template (one fixed set of fields per
    route). Also settles round 3's open proposal to show draft scenarios in Step 1.
  - [proposal, open] B: a short worked example spec in `templates.md` (adds length).
  - Not covered: a live run on a real thing; evaluators from a different model.
- **2026-11-08, between rounds 4 and 5: stop rules (requested by the owner).** The skill
  is now autonomous after Step 1: no check-ins during a run, disagreements kept and logged
  as pending the owner, publishing decided in Step 1, and six stop rules (target, budget,
  no progress over a window scaled to the budget, nothing to change, ceiling in the test,
  can't go on safely) with a final summary that says how to unblock the next point.
  Reports now give whole-number scores, an impact tag, and where the next point lies.
  **Break in comparability:** scenarios 6 and 7 (stalled and still-improving long runs)
  and their fixtures were added, and the brief changed to cover them and the new report
  items. Round 5 starts a new baseline. Run budget for this change: 2 rounds, two
  evaluators each, target 9/10.
- **2026-11-08, round 5 (new baseline), two fresh subagents. 8/10 and 8/10; median 8.**
  A: clarity 8, completeness 7, reproducibility 7, scope fit 9, economy 7. B: clarity 8,
  completeness 7, reproducibility 8, scope fit 9, economy 7. All seven scenarios routed
  correctly for both; scenario 6 stopped under rules 3 and 5, scenario 7 continued without
  contacting the user. Checks pass. Cost: about 117k and 116k tokens. Next point: both
  place it in the skill, with a smaller drag from the test. High-impact [direct] fixes
  applied: 4. Progress: yes.
  - [direct][high] Both: fixes left in a draft had no rule at the end of a run. Publishing
    now has three choices (live each round, live when the run ends, a draft for the
    owner), the skeleton has a Publishing field, and the summary says where fixes are.
  - [direct][high] Both: Step 1 asked only about fixtures others can see. It now asks what
    the evaluator needs, real or invented, and facts only the owner knows.
  - [direct][high] A: "a break doesn't move the baseline" was unclear. Best score and window
    now count from the break.
  - [direct][high] B: rule 4 could read as "nothing left after fixing". Now "the round
    produced no [direct] finding".
  - [direct][low] Applied: guardrails that leave likely fixes as proposals are flagged in
    Step 1; a missing target or budget is filled from the default; combined routes ask the
    union of fields; the rerun row starts at Step 1's Rerun column; report-only rounds end
    with the summary and an offer of a run; evaluator impact tags are kept or the change is
    logged; each evaluator judges only its flow's Who and what (also in the brief
    template); scenarios marked "to confirm on first look" when the thing can't be
    reached; rule 3 says "counting this one"; the summary lists every rule that holds;
    "would or might reach"; rerun a scenario yourself where no check confirms a fix.
  - [direct][low] Partly applied: the Step 1 bullets now give only what the table lacks.
    SKILL.md is 209 lines (was 198), templates.md 205.
  - [proposal, open] A: a "Run state" block per flow (rounds used, best score, last round
    with progress, publishing, draft location), with Step 7 checking it.
  - [proposal, open] B: Step 7 as a decision table, with one worked example per fixture
    type.
  - [proposal, open] Test changes, held so round 6 stays comparable: say each scenario is
    independent (scenarios 1 and 2 versus 4), and add [direct] and impact tags to the
    plateau and progress fixture logs.
- **2026-11-08, round 6, two fresh subagents. 8/10 and 8/10; median 8.** Both: clarity 8,
  completeness 7, reproducibility 7, scope fit 9, economy 7. All seven scenarios routed
  correctly for both; the stop and continue cases were applied mechanically. Checks pass.
  Cost: about 118k and 121k tokens. Next point: both place it in the skill, with small
  drags from the test. High-impact [direct] fixes applied: 4. Progress: yes. Fixes applied
  after the round, not yet scored by a round (SKILL.md 219 lines, templates.md 207):
  - [direct][high] A: only rubric gaps were named as breaks. Any change to scenarios,
    questions, rubric, or brief is now a break, with the rule in one place in Step 2.
  - [direct][high] A and B: combining routes re-asked what the spec already answers. Now
    the union minus what the spec answers, with narrow fields kept narrow.
  - [direct][high] B: with fixes in a draft, evaluators would keep scoring the live
    version. The evaluator now judges the draft, and Step 1 asks where it lives.
  - [direct][high] B: Step 2 named an "opener" field the skeleton lacks. The opener is now
    the brief's first line.
  - [direct][low] Applied: report-only runs still write the flow section and brief; Step 1
    asks for existing test tools and a prompt's production model; views aren't separate
    scenarios; ambiguous day units are marked to confirm; scenarios marked "to confirm"
    are confirmed before round 1; checks and fixture reset start every round; return to
    one evaluator when the spread is under 2; rule 3 can't hold before N rounds; rule 6
    is about fixes to the thing; an unmatched publishing choice counts as a draft; rerun
    items now point to the Step 1 table, and scenarios and questions stay as written.
  - [proposal, open] A and B, and round 5's A: a Run state line per flow. Now raised by
    three evaluators.
  - [proposal, open] B: fold the Step 1 bullets into the templates table as a "What it
    needs" column (about 25 lines).
  - [proposal, open] A: the owner's answer on widening Fix directly overrides the prompt
    card's split.
  - [proposal, open] Test changes, still held: scenarios are independent; tag fixture log
    fixes [direct] and by impact; the plateau fixture's publishing wording.
  - **Run ended: rule 2, budget spent (2 of 2 rounds).** No other rule holds: both rounds
    made progress, both placed the next point in the skill. Target 9 not reached.
