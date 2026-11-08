# Iterate spec: the iterate skill

The spec for improving `skills/iterate/SKILL.md` with the iterate skill itself. Claude never
loads this file as part of the skill; it's here so anyone working on the skill can rerun the
same flows and compare scores. The run log and Run state are in `iterate-log.md` beside it,
which evaluators never read.

## The thing

`skills/iterate/SKILL.md`, with its `templates.md`, teaches an agent to improve something
in repeatable rounds, one testing flow at a time: write a spec, have a fresh subagent run the flow and score it, fix
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
every file this spec names exists, and that the run log lives only in `iterate-log.md`.

---

## Flow: dry run

**Who and what:** an agent that has just loaded iterate and has a request from a user. It
judges whether it can carry out the request from the skill alone.
**Card:** skill dry run.
**Target and budget:** 9/10 within 4 rounds, one evaluator per round.
**Publishing:** a draft for the owner: uncommitted changes in the working tree, which
evaluators read on disk.
**Evaluators:** one, the session's model (`opus` in Claude Code), which is the primary.

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
>   and the "Flow: dry run" section. Don't open `evals/iterate/iterate-log.md`; form your
>   own view.
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
