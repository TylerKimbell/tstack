# Iterate spec: 90-day onboarding plan page

## The thing

A shared web page where a manager sets up a 90-day plan for a new hire, and the new hire
uses it every day: a To do view for tasks and asks, and a Learning view for courses by week.
Evaluators reach it in a browser through a test plan tagged TEST.

## Guardrails

**In scope:** layout, labels, order, timing, and whether each item points to one real place.
**Out of scope:** whether the courses and docs are well chosen.
**Fix directly:** layout, section order, labels, hints, empty states, and wording that keeps
the same expectation.
**Propose to the owner:** adding, removing, or moving content; changing dates, people, or
time estimates.

## Fixtures

A test new hire tagged TEST, starting three weeks out, every setup field filled. "See it as
it looks on Day N" shows any day. The page's real content (course links, team names) is not
available to evaluators, so they work from placeholder content. Reset: untick everything on
the test plan.

## Checks

Program > Run checks. Every check should pass.

---

## Flow: new hire walkthrough
**Card:** user walkthrough
**Who and what:** a new hire using the plan every day for their first 30 days.
**Target and budget:** 9/10 within 100 rounds. Fixes stay in a draft until the run ends.

### Scenarios
1. Day 0. 2. Day 1. 3. Day 8. 4. Day 16. 5. Day 30. 6. Day 31.

### Questions at each scenario
- What do I do now? What's due next, and by when? Where do I mark it done?

### Rubric
Score from 1 to 10, a judgement, not an average of the sub-scores.
Anchors: 10, every scenario done without help or guessing; 7, all done with some
hesitation; 4, stuck in at least one; 1, unusable.
Sub-scores:
- Clear next step: at each scenario, what to do now is obvious from the top.
- Findability: anything the user needs is reached without hunting.
- Labels: titles, buttons, and notes say what they do in the user's words.
- Timing: every item says when it's due, and shows up when it matters.
- Effort: the scrolls, clicks, and reading each task takes.

### Settled decisions
- Switching views returns to where you were: the owner chose this.

### Brief
(Saved; omitted from this fixture.)

### Run log
Rounds 1 to 9 condensed:
- Round 1 (baseline): 6/10. 4 high-impact fixes (Day 1 work buried, no due dates on asks).
- Round 2: 7/10. 3 high-impact fixes (overdue items vanished, unlabelled tags).
- Round 3: 8/10. 2 high-impact fixes (counts disagreed across the page).
- Rounds 4 to 9: 8/10 each. 0 high-impact fixes; 2 to 4 low-impact fixes per round
  (spacing, a label's wording, tooltip text). Next point placed in the thing.

- **Round 10: 8/10.** Clear next step 8, findability 8, labels 9, timing 8, effort 7.
  Fixes: 2 low-impact (a button label, a hint's wording); 0 high-impact. Next point: in the
  thing, "fewer scrolls on Day 16". Proposal, open: move the AI toolkit courses to week 3.
- **Round 11: 8/10.** Clear next step 8, findability 8, labels 9, timing 8, effort 7.
  Fixes: 1 low-impact (empty-state text); 0 high-impact. Next point: in the thing, "fewer
  scrolls on Day 16"; the evaluator added that Day 16 scrolling comes from the length of
  the placeholder course list.
- **Round 12: 8/10.** Clear next step 8, findability 8, labels 9, timing 8, effort 7.
  Fixes: 2 low-impact (a heading's wording, chip spacing); 0 high-impact. Next point: in
  the test: "can't judge whether the real course list fits on screen; placeholder content
  is longer than the real list is likely to be."
- **Round 13: 8/10.** Clear next step 8, findability 8, labels 9, timing 8, effort 7.
  Fixes: 1 low-impact (a tooltip); 0 high-impact. Next point: in the test: "effort depends
  on real content; placeholder course names are long and generic."
