# Iterate spec: 90-day onboarding plan page

## The thing

A shared web page where a manager sets up a 90-day plan for a new hire, and the new hire
uses it every day: a To do view for tasks and asks, and a Learning view for courses by week.
Progress is shared, so the manager sees what's done.

## Guardrails

**In scope:** layout, labels, order, timing, and whether each item points to one real
place. **Out of scope:** whether the courses and docs are well chosen.

**Fix directly:** layout, section order, labels, hints, empty states, and wording that keeps
the same expectation. **Propose to the owner:** adding, removing, or moving content; changing
dates, people, or time estimates.

## Fixtures

- A test new hire, tagged TEST, starting on a Monday three weeks out, with every setup field
  filled. Never touch a plan that isn't tagged TEST.
- "See it as it looks on Day N" in the plan banner shows any day without changing the start
  date.
- Reset: untick everything on the test plan, or remove it and set it up again.

## Checks

Program > Run checks renders sample plans and checks names, dates, show and hide rules, and
links. Every check should pass.

---

## Flow: manager setup

**Who and what:** a manager setting up a plan for a new hire for the first time. Judges
whether they can create a correct plan without help.

### Scenarios

1. Set up a plan with every field filled.
2. Set up a plan with the optional fields blank.
3. Edit a plan after it's created.
4. Remove a plan.

### Questions at each scenario

- Is it clear what each field does and what happens if it's left blank?
- Does the new hire's plan show what was entered?
- Can anything be lost by one click?

### Rubric

Score from 1 to 10. Sub-scores: clear next step, field labels, blank-field consequences,
error handling, safety.

### Settled decisions

- The setup form is for managers only; new hires never see it.

### Run log

- **Round 1 (baseline), 6/10.** Clear next step 7, labels 5, blank fields 5, errors 6,
  safety 7. Findings: "one per line with |" boxes were confusing (became rows with Add and
  Remove); blank 1:1 time had no visible effect (the plan now asks the new hire to book it);
  Remove deleted on one click (now needs a second click). Proposed: drop the "principal" role
  from the people section.
- **Round 2, 7/10.** Clear next step 8, labels 7, blank fields 7, errors 6, safety 8.
  Findings: the test-hire option was hidden below the directory search (moved above it);
  setup copied meeting times from the last plan (now copies people only). Not covered:
  claiming a plan from a second account.
