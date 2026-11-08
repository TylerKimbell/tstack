# Iterate log: the iterate skill

## Flow: dry run

**Run state:** ended after round 10 (rule 2, budget spent: 4 of 4); best score since the
round 5 baseline 8; last round that made progress 10; fixes uncommitted in the working
tree, round 10's not yet scored.

The baseline and the last three rounds are in full; older rounds are one line each. Round 5
is the current baseline: scenarios 6 and 7, their fixtures, and the brief changed just
before it.

- 2026-11-08, round 1 (first baseline), 7/10: added the rerun path, score anchors, and the
  decline rule.
- 2026-11-08, round 2, 8/10: lens anchors, scenario counts, sub-score definitions, rerun
  backfill.
- 2026-11-08, round 3, 8/10 and 8/10: plateau; routing table and per-flow cards proposed
  (both later accepted).
- 2026-11-08, round 4 (baseline after the restructure), 8/10 and 8/10: routing rows
  combine, Step 1 message template accepted.
- 2026-11-08, between rounds 4 and 5: the owner added autonomy and six stop rules.
  **Break:** scenarios 6 and 7, their fixtures, and the brief changed.
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
  - [proposal, accepted before round 7] A: a "Run state" block per flow (rounds used, best score, last round
    with progress, publishing, draft location), with Step 7 checking it.
  - [proposal, declined before round 7] B: Step 7 as a decision table, with one worked example per fixture
    type.
  - [held, still open] Test changes, held so round 6 stays comparable: say each scenario is
    independent (scenarios 1 and 2 versus 4), and add [direct] and impact tags to the
    plateau and progress fixture logs.
- 2026-11-08, round 6, 8/10 and 8/10: one break rule for any change to the flow's
  section; evaluators judge the draft; run ended on budget (2 of 2).
- 2026-11-08, before round 7: rerun at 9/10 within 4 rounds, one evaluator. Backfilled
  Publishing, Run state, and Target and budget. Accepted: a Run state line, the Step 1
  "What it needs" column, widening Fix directly overrides the prompt card. Declined: a
  Step 7 decision table, a worked example spec. Test changes held.
- 2026-11-08, round 7, 8/10: the first scored round after a break is a new baseline that
  sets the best score; five smaller fixes.
- **2026-11-08, round 8, one fresh subagent. 8/10.** Clarity 8, completeness 8,
  reproducibility 8, scope fit 9, economy 7. All seven scenarios routed correctly;
  scenario 4 used the new baseline rule ("none yet"), scenario 6 stopped under rules 3
  and 5, scenario 7 continued without contacting the user. Checks pass. Cost: about 121k
  tokens, 6 minutes. Held back by: free choice of timeline scenarios, no way to record a
  stop, no Publishing value when nothing reaches users. Next point: mostly in the test
  (the held fixture changes), a little in the skill. High-impact [direct] fixes applied:
  1. Progress: yes (best score unchanged at 8). The evaluator says it read the run log
  while reading the spec, against the brief.
  - [direct][high] "A few days between" let two agents pick different timeline scenarios.
    Now the midpoint and, past two weeks, the quarter points.
  - [direct][low] Applied: the review row also catches a lens named without a target
    ("review the styling"); Publishing may be "none and why"; a stop is recorded in the
    round's entry and the Run state; "any matching column" for combined routes; Rerun
    item 1 no longer repeats Step 1.
  - [direct][low] Not applied: on resume, check open decisions are in Settled decisions
    (Step 5 already requires it; the gap is the progress fixture's); widening In scope
    isn't a break (already follows from the break rule, which covers only the flow's own
    section); the rerun default after a break (the default still works).
  - Alternatives, not applied: Run state as a stop-rule worksheet (next point, [direct]
    count); a header note in the Step 1 table for combined routes.
  - Test-side, still held: as in round 7, plus the fixtures omit their briefs and the
    plateau fixture has no draft location.
- **2026-11-08, round 9, one fresh subagent. 8/10.** Clarity 8, completeness 8,
  reproducibility 8, scope fit 9, economy 7. All seven scenarios routed correctly;
  scenario 6 stopped under rules 3 and 5, scenario 7 continued without contacting the
  user. Checks pass. Cost: about 122k tokens, 6 minutes. Held back by: the run log leaks
  into the evaluator (it read the log in the same file and says its score may be
  anchored on the logged 8s; round 8's did too), and small numbering choices in timeline
  and lens scenarios. Next point: split, leaning toward the test. High-impact [direct]
  fixes applied: 1. Progress: yes (best score unchanged at 8).
  - [direct][high] "Ignore the run log" can't keep an evaluator cold. Step 4 now points the
    evaluator at a copy of the spec without its Run log, in the scratch folder, and the
    brief template reads that copy.
  - [direct][low] Applied: timeline day 0 is the day before the window and halves round up;
    a lens on something that changes looks at the state with the most kinds of item state;
    the rerun default is one point above the last logged score, even across a break; the
    summary publishes fixes now when Step 1 chose "live when the run ends" (nothing said
    to before); cut Step 2's "opener becomes the brief's first line" (the brief template
    says it).
  - [direct][low] Not applied: count untagged logged fixes as [direct] (impact would still
    be unknown; the gap is the held fixture change); accepting a card-gap proposal is a
    break (already follows from the break rule); a Run state line for report-only runs.
  - [proposal, open] Keep the run log in its own file beside the spec, replacing the
    skeleton's Run log section.
  - Test-side, held for the owner: this spec's brief still says "ignore its run log" on
    the full spec. Following the new Step 4 means a log-free copy and a brief change, which
    is a break, so round 10 keeps the old brief and may stay anchored.
- **2026-11-08, round 10, one fresh subagent. 8/10.** Clarity 8, completeness 8,
  reproducibility 8, scope fit 9, economy 7. All seven scenarios routed correctly;
  scenario 6 stopped under rules 3 and 5, scenario 7 continued without contacting the
  user. Checks pass. Cost: about 118k tokens, 6 minutes. The evaluator read the run log
  before scoring, as in rounds 8 and 9. Held back by: wording at the edges two agents
  would read differently, and fixture guesses in scenarios 5 to 7. Next point: split
  evenly between the skill and the test. High-impact [direct] fixes applied: 2. Progress:
  yes. Applied after the round and not yet scored (SKILL.md 201 lines, templates.md 212):
  - [direct][high] Round 9's fix put a per-run placeholder in the brief template's Read
    line, which must stay word for word. It now reads "the copy of the spec in the scratch
    folder named above".
  - [direct][high] "For anything clicked through" was unclear for a page with ticks and
    views. Now "when the user clicks, types, ticks, or switches anything".
  - [direct][low] Applied: step states for the window's first and last days; the summary
    names fixes applied after the last scored round; "a one-line request to confirm";
    report-only runs get Run state "report only"; the combine-rows paragraph rewritten;
    the prompt card's production model is a runner setting, not part of the brief.
  - [direct][low] Not applied: say in Step 1 when a break is already unavoidable (adds
    length for a rare case).
  - Alternative, not applied: an example scenarios line per card.
  - **Run ended: rule 2, budget spent (4 of 4 rounds).** Rule 1: no, 8 against a target of
    9. Rule 3: no, rounds 9 and 10 both made progress (N is 2). Rule 4: no, round 10 had
    [direct] findings. Rule 5: no, the next point was split, and every round applied a
    high-impact fix. Rule 6: no.

**Open proposals and held test changes** (for the owner):
- [proposal, open] Keep the run log in its own file beside the spec (round 9). The log
  leak raised in rounds 8 to 10 points the same way.
- [proposal, open] Fold the routing table into the Step 1 table (round 7).
- [held, test change, break] Point this spec's brief at a copy of the spec without its run
  log, as Step 4 now says. The brief still says "ignore its run log", and rounds 8 to 10
  read it anyway, so their scores may be anchored on earlier 8s.
- [held, test change, break] Say each scenario is independent; tag the fixture logs'
  fixes [direct] or [proposal] and by impact; add Run state lines to the fixtures, or
  leave them out on purpose; fix the plateau fixture's publishing wording and give it a
  draft location; add round 5's pending-owner decision to the progress fixture; add the
  fixtures' briefs. Evaluators say these cause about half the guesses in scenarios 6
  and 7.
- Not covered by any round: a live run on a real thing; evaluators from a different model.
- **2026-11-08, after round 10: changes from the owner's review of the live run.** Applied
  to the skill, not yet scored:
  - **Evaluator panel:** up to three from the session's model family at the session's
    effort (`opus`, `sonnet`, `haiku` in Claude Code; Sol, Terra, Luna in Codex), or the
    user's own panel. Fable only when named or the session runs on it, with a cost warning.
  - **Primary:** the strongest model on the panel; its score is the score of record. Only
    its findings, findings two or more evaluators raise, or clarity findings it didn't
    contradict get applied. Replaces the median, the spread rule, and "three evaluators
    when the score swings".
  - **Prompt dry runs:** with a panel, a different model judges the outputs.
  - **Rule 4, flat score:** the run ends when the primary's best score hasn't risen in 2N
    rounds, whatever fixes landed; breaks don't restart it. Closes the gap where a
    high-impact tag every round kept rounds 5 to 10 "in progress" at a flat 8.
  - **Run log in its own file** (`-log` beside the spec), with the Run state line, so
    evaluators can't read earlier scores. Replaces the spec copy without the log.
  - **Before-and-after comparison** as the last step of every run that applied a fix: one
    fresh evaluator compares the starting and final versions blind. In this review it
    preferred the round-10 version over the round-6 baseline with clear confidence, while
    every score stayed at 8.
  - Cleanup: the Step 1 notes moved under the table as a list; lines rewrapped; the
    duplicate "no run log" sentence gone.
  - **Break in comparability:** the brief's Read line changed (the log moved), and the
    evaluator panel is now part of the flow. The next round is a new baseline.
  - [proposal, open] Test changes still held: say each scenario is independent; tag the
    fixture logs' fixes [direct] and by impact; fix the plateau fixture's publishing wording.
