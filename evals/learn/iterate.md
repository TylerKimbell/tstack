# Iterate spec: the learn skill

The spec for improving `skills/learn/SKILL.md` with the iterate skill. Claude never loads
this file as part of the skill; it's here so anyone working on the skill can rerun the same
flow and compare scores. The run log and Run state are in `iterate-log.md` beside it, which
evaluators never read.

## The thing

`skills/learn/SKILL.md` teaches an agent to teach a person a topic, goal by goal, from
verified sources: find the source that defines the topic, set or take the learning goals,
explain from a mental model, check understanding with a scenario after each goal, and move
on when the learner says they have it. It runs for anyone who asks to learn, understand, or
study something, at any level. Evaluators read the skill on disk.

## Guardrails

**In scope:** whether an agent can follow the skill without guessing, whether two agents
would do the same thing, whether it takes the requests it should and turns away the ones it
shouldn't, and its length.

**Out of scope:** the other skills and the plugin manifests, and the README except that its
row must still describe the skill. Whether a given teaching topic is interesting.

**Fix directly:** wording, order, examples, and a missing instruction that serves what the
skill already does.

**Propose to the owner:** changing what the skill is for, adding or removing a step or a
rule, renaming it, or changing which requests trigger it.

## Fixtures

- `fixtures/retrykit/README.md`, `fixtures/retrykit/CHANGELOG.md`, and
  `fixtures/retrykit/defaults.py`: the docs and defaults of an SDK, invented and marked as
  invented, whose sources disagree. For scenario 5.
- `fixtures/mid-session.md`: a learn session at two points, after goal 1 and at the last
  goal, written as a stand-in. For scenario 6.
- `skills/iterate/SKILL.md` in this repository: a real source for scenarios 1 and 6.
- The live web, for official documentation in the scenarios that need it. Scenario 2 needs
  Anthropic's docs.
- A scratch folder for the evaluator's output: a new empty temporary folder each round,
  outside this repository. That's the reset; nothing in the repository changes during a
  round.

Off limits: any real system. Scenario 7 mentions a production database; no evaluator
connects to anything.

## Checks

Run `python evals/learn/check.py` from the repository root before every round. It checks
that the skill's frontmatter has the right name and a description under 1024 characters,
that `agents/openai.yaml` exists and names the skill, that the plugin manifests are valid
JSON, that the README has a row for the skill, that every fixture this spec names exists,
and that the run log lives only in `iterate-log.md`.

---

## Flow: dry run

**Card:** skill dry run.
**Who and what:** an agent that has just loaded learn and has a request from a learner. It
judges whether it can carry out the request from the skill alone.
**Target and budget:** 9/10 within 2 rounds.
**Evaluators:** `opus` (primary), `sonnet`, and `haiku`, all at high effort.
**Publishing:** a draft for the owner: uncommitted changes in the working tree, which
evaluators read on disk.

The evaluator doesn't teach anyone. For each scenario it writes, in the scratch folder, what
it would send by following the skill. Then it reviews the skill.

### Scenarios

Each scenario stands alone, and none of them is in a project that defines its own `learn`
skill.

1. **Direct source, no goals.** "Walk me through how the stop rules work, from
   `skills/iterate/SKILL.md`."
2. **Owner of the topic.** "Learn prompt caching from Anthropic."
3. **Ambiguous topic, no source.** "Teach me about workspaces." A new conversation with no
   project open.
4. **Too broad.** "Teach me Kubernetes." A new conversation with no project open.
5. **Supplied goals, sources that disagree.** "Teach me how retries work in RetryKit, from
   the files in `evals/learn/fixtures/retrykit/`. Module objectives: state the default
   number of attempts; predict which status codes get retried; decide whether to set a
   custom backoff for a rate-limited API."
6. **Mid-session.** Work through `fixtures/mid-session.md`, and answer the two learner
   messages at the end of each part.
7. **Practice on production.** "We run Postgres with Patroni. Teach me how failover works,
   and let's practice by failing over our production primary."
8. **A one-off question.** "What's the default timeout for Node's fetch?" A new conversation
   with no project open.

### Questions at each scenario

- What do I do next, at each step of the skill?
- Where did I have to guess, and what did I guess?
- Would a second agent read the same sources, set comparable goals, and send a comparable
  reply?
- Did the skill handle this request the right way: teach it, ask first, narrow it, refuse
  the unsafe part, or not take it on?
- Does the reply follow the skill: goals stated, sources read, mental model first, the
  source's terms defined, a scenario check after each goal, and what's documented kept apart
  from what's inferred?

### Rubric

Score from 1 to 10, a judgement, not an average of the sub-scores.
Anchors: 10, every request carried out without guessing; 7, all carried out with some
guessing; 4, stuck or wrong in at least one; 1, unusable.
Sub-scores:

- **Clarity:** each instruction says what to do without interpretation.
- **Completeness:** no step leaves the agent stuck or guessing.
- **Reproducibility:** two agents would produce comparable output.
- **Scope fit:** it handles the requests it should and turns away the ones it shouldn't.
- **Economy:** nothing could be cut without losing behaviour.

### Settled decisions

- **Step 2 stays as bullets.** The owner declined replacing them with first-message and
  later-message formats for now: the bullets are working.
- **No routing table at the top.** The owner declined it for now: it would add length for
  cases the skill already handles.
- **No numbered goals step.** The owner declined a separate step between finding the source
  and teaching for now: "after Step 1" covers the ordering.
- **No merge tie-break, pending the owner.** Evaluators keep asking for a rule on which
  adjacent pairs to merge; the owner's trim removed one as false precision.
- **No stated source for "what to read next", pending the owner.** Raised, added, then cut in
  the owner's trim.

### Brief

The runner adds two lines at the top: the repository root and the scratch folder path.

> You are an agent that has just loaded the `learn` skill, working through sample requests.
> Write what you would produce; don't run anything outward-facing.
> Don't change the skill or anything else in the repository. Write only in the scratch
> folder named above. Never connect to any real system; scenario 7 mentions a production
> database, and you only write what you would say.
>
> **What it's for:** the skill teaches a person a topic, goal by goal, from verified
> sources. It finds the source that defines the topic, sets or takes learning goals,
> explains from a mental model, checks understanding with a scenario after each goal, and
> moves on when the learner says they have it. Two agents following it should behave
> comparably.
>
> **Settled decisions:** the spec's Settled decisions for this flow; don't raise or score
> them.
>
> **Read**, with paths relative to the repository root:
> - `skills/learn/SKILL.md`, the version on disk now, and any file it tells you to load.
> - `evals/learn/iterate.md`: the shared part (The thing, Guardrails, Fixtures, Checks) and
>   the "Flow: dry run" section. Don't open `evals/learn/iterate-log.md`; form your own
>   view. Judge only what this flow's Who and what covers.
> - The fixtures in `evals/learn/fixtures/` and the sources a scenario names.
>
> Use only file reading, WebSearch, WebFetch, and writing in the scratch folder. Don't spawn
> subagents or open a browser. Where a tool is missing, say so and carry on.
>
> **For each of the eight scenarios** in the dry-run section, follow the skill as if the
> learner had just sent that request, and write `scenario-N.md` in the scratch folder with:
> 1. What you did before replying: the sources you read, and any you looked for and didn't
>    find.
> 2. The reply you'd send, exactly as you'd send it, however long that turns out to be. For
>    scenario 6, each reply.
> 3. **Guesses:** every place the skill left you guessing, and what you guessed.
>
> **Then report, in about 700 words:**
> 1. Score N/10 as a whole number, one line on what holds it back, and whole-number
>    sub-scores for clarity, completeness, reproducibility, scope fit, and economy.
> 2. How well the skill serves an agent carrying out these requests.
> 3. Findings ranked by impact: the section of `SKILL.md`, what's wrong, the concrete change
>    (replacement wording where you can), and what it replaces. Tag each **[direct]** or
>    **[proposal]** using the spec's guardrails, and **[high]** or **[low]** impact.
> 4. Next point: what would raise the score by one, and whether that lies in the skill or in
>    this test (invented stand-ins, tools that can't reach part of it).
> 5. Alternatives: a different format or structure that would work better, and what it would
>    replace.
> 6. Keep: what works and shouldn't change.
> 7. What you wrote in the scratch folder, and what you couldn't check.
