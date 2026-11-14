# Iterate spec: the reflect skill

The spec for improving `skills/reflect/` with the iterate skill. Claude never loads this
file as part of the skill; it's here so anyone working on the skill can rerun the same
flow and compare scores. The run log and Run state are in `iterate-log.md` beside it,
which evaluators never read.

## The thing

`skills/reflect/` turns the work done in a session into a skill: a new one, or an edit to
one that exists. `SKILL.md` has the agent build a digest of the session's transcript with
`scripts/digest.py`, pick the thread, extract the method, separate it from case details,
check existing skills, propose, write, dry-run the result, and hand off. It is for anyone
who wants a session's method made repeatable. Evaluators read the skill on disk and run
the script.

Reflect is only as good as the skills it writes, so this flow judges both: the
instructions, and what an agent following them produces.

## Guardrails

**In scope:** `skills/reflect/SKILL.md` and `skills/reflect/scripts/digest.py`: whether an
agent can follow them without guessing, whether two agents would reach comparable output,
whether reflect takes the requests it should and turns away the ones it shouldn't, its
length, and the quality of the skills and edits it produces.

**Out of scope:** fixing the produced skills themselves (they are throwaway; a flaw in one
is a finding about reflect's instructions). Other skills, the plugin manifests, and the
README except that its row must still describe reflect. Whether the work done in a fixture
session was right.

**Fix directly:** wording, order, examples, a missing instruction that serves what reflect
already does, and digest.py bugs or output changes that keep its purpose.

**Propose to the owner:** changing what reflect is for or which requests trigger it,
adding or removing a step or an approval gate, renaming it, and new scripts.

## Fixtures

The fixture sessions are real transcripts, frozen as copies in `evals/reflect/local/`,
which git ignores. They hold private data and never leave this machine. Someone rerunning
this flow elsewhere supplies their own sessions of the same kinds and lists them in
`local/sessions.md`.

- `local/sessions.md`: which frozen transcript belongs to which scenario, the title the
  user would call each session by, and the held-out material.
- `local/sessions/`: the four fixture transcripts, and helper transcripts for one of them.
- `local/heldout/`: material for testing a produced skill on a target it wasn't built on.
- `local/artifacts/`: files a fixture session wrote to a scratch folder, frozen in case the
  original is cleared.
- For every scenario, reflect is invoked from a session in a project whose `AGENTS.md`
  describes where skills live (core skills in the repo, company skills in a separate data
  folder). The runner brief names the paths.
- A scratch folder per round, outside this repository, holding a `runner/` and an
  `evaluator/` folder. A new empty one each round is the reset.

Off limits: every repository and data folder on disk except this round's scratch folder is
read-only. No agent sends, publishes, commits, pushes, or changes a scheduled task.

## Checks

Run `python3 evals/reflect/check.py` from the repository root before every round. It
checks reflect's frontmatter (name, description under 1024 characters), that
`agents/openai.yaml` names `$reflect`, that the plugin manifests parse, that the README
has a row for reflect, that `digest.py` compiles and digests every fixture transcript into
at least one turn with a files section, that `local/` is ignored and nothing in it is
tracked, and that the run log lives only in `iterate-log.md`. In a clone with no `local/`
folder it skips the fixture checks and says so; supply the fixtures before a round.

---

## Flow: session to skill

**Card:** custom, built on the skill dry run card, with a runner and an evaluator so no
model grades its own work.
**Who and what:** an agent that has just loaded reflect and gets a reflect request about a
past session. It judges whether it can carry out the request from the skill alone, and
whether the skill or edit it ends up with would work on a new target.
**Target and budget:** 9/10 within 2 rounds.
**Evaluators:** one, `opus` at high effort (primary, and the only score). A runner, also
`opus` at high effort, carries out the scenarios first and never scores.
**Publishing:** a draft for the owner: uncommitted changes in this repository's working
tree, which agents read on disk. The installed plugin doesn't change until the owner
pushes.

Each round has two stages. The **runner** follows reflect on every scenario and writes
what it would produce into `runner/`, including the drafted skill or edit where a scenario
gets that far. The **evaluator** starts fresh: it reads reflect, reads the runner's
output, tests each produced skill or edit on its held-out request, and scores reflect.

### Scenarios

Session titles are in `local/sessions.md`. Where the user approves a proposal, the runner
assumes the user said "yes, as proposed" and carries on.

1. **New skill, thread named.** "Reflect on the 'Local setup' session. The part I care
   about is where we audited how many tokens the daily-agenda skill used and worked out
   how to make it cheaper. I want to automate that kind of skill-efficiency work." Runner:
   through the drafted skill (Step 7) and the self-check (Step 8). Evaluator's held-out
   request for the produced skill: "Audit what the scheduled account-brief runs cost, and
   find ways to make them cheaper", using the two runs in `local/heldout/`.
2. **Same session, no thread named.** "Reflect on the 'Local setup' session." Runner:
   through Step 2, and the message it would send.
3. **An existing skill covers the job.** "Reflect on the 'Port the agenda notice'
   session." The session ported a change from a private working copy into a shareable
   repository's core skill, which an installed skill already does. Runner: through the
   proposal, and on to the drafted edit if it proposes one. Evaluator's held-out request
   for a produced edit: "Bring the old working copy's latest change to the email skill
   into the clone's core skill", desk-checked against the repositories on disk.
4. **A company-specific process.** "Reflect on the 'service case' session." The session
   followed a company's internal process. Runner: through the proposal (Step 6).
5. **Nothing reusable.** "Reflect on the 'Performance marketing definition' session." A
   one-off question. Runner: as far as the skill takes it.
6. **Not a skill.** In a fresh session with no work in it: "Reflect: remember that I sign
   intro replies 'Best, TK'." Runner: as far as the skill takes it.

### Questions at each scenario

- What do I do next, at each step of the skill?
- Where did I have to guess, and what did I guess?
- Would a second agent pick the same thread, reach the same new-or-edit-or-nothing call,
  propose the same home, and draft a comparable skill?
- Did reflect handle this request the right way: build a skill, edit one, ask which
  thread, route it to memory, or say nothing here is worth a skill?
- Does the digest give enough to work from, or did I have to open the raw transcript, and
  for what?
- For a produced skill or edit: could an agent run it on the held-out request without
  guessing? Does it capture the method rather than the fixture's case? Does every step
  trace to the session, or say it's inferred? Does it keep the session's gates? Is it in
  the right home, with no private details where it would be shared?

### Rubric

Score from 1 to 10, a judgement, not an average of the sub-scores. The overall score is at
most one point above the Produced skill sub-score: reflect exists to produce skills.
Anchors: 10, every request carried out without guessing, and every produced skill runs on
its held-out request as is; 7, all carried out with some guessing, and produced skills
work after small edits; 4, stuck or wrong in at least one, or a produced skill misses the
method; 1, unusable.
Sub-scores:

- **Clarity:** each instruction says what to do without interpretation.
- **Completeness:** no step leaves the agent stuck or guessing.
- **Reproducibility:** two agents would produce comparable output.
- **Scope fit:** it handles the requests it should and turns away the ones it shouldn't.
- **Economy:** nothing could be cut without losing behaviour.
- **Produced skill:** the skills and edits reflect produced in scenarios 1 and 3, judged
  on their held-out requests. 10, an agent runs them as is and they match what the session
  showed; 7, usable after small edits; 4, they miss the method, invent steps, or sit in
  the wrong home; 1, unusable.

### Settled decisions

None yet.

### Runner brief

The runner adds three lines at the top: the repository root, this round's scratch folder,
and the fixtures folder (`evals/reflect/local/`).

> You are an agent that has just loaded the `reflect` skill, working through sample
> requests. Carry out each one as the skill says, and write what you would produce. You
> do not score anything; a separate evaluator judges your output.
>
> Don't change the skill or anything else on disk. Write only in the `runner/` folder of
> the scratch folder named above. Every repository and data folder is read-only. Never
> send, publish, commit, push, or change a scheduled task.
>
> **Setting:** reflect is invoked from a Claude Code session in `~/dev/ai-workspace`, a
> project whose `AGENTS.md` says where skills live; its data folder is
> `~/dev/ai-workspace-data`. Skills you can check for overlap are in that project's
> `.agents/skills/`, its data folder's `company/skills/`, `~/.claude/skills/`, and
> `~/dev/tystack/skills/` (a plugin repo the user keeps for general skills). The sessions
> the user names are frozen copies listed in `local/sessions.md` in the fixtures folder:
> pass those paths to `digest.py` instead of session ids. A file the digest lists that no
> longer exists may have a frozen copy in `local/artifacts/`.
>
> **Read:** `skills/reflect/SKILL.md` in the repository, the version on disk now, and
> run its script as it says. Read `evals/reflect/iterate.md`, the "Flow: session to
> skill" section, for the six scenarios. Don't open `evals/reflect/iterate-log.md`.
>
> Use file reading, Bash for running `digest.py` and read-only commands, and writing in
> `runner/`. Don't spawn subagents; where the skill asks for a helper agent, follow its
> fallback for when there is none, and say so.
>
> **For each scenario**, write `runner/scenario-N/` with:
> 1. `transcript.md`: what you did, step by step, and every message you would send the
>    user, exactly as you'd send it. Where the scenario says the user approves, write
>    "User: yes, as proposed" and carry on.
> 2. The skill or edit you drafted, if the scenario gets that far: new files at the paths
>    they'd have under `runner/scenario-N/files/`, mirroring their real location (for
>    example `files/home/.claude/skills/<name>/SKILL.md`), and an edit as the full edited
>    file plus a unified diff.
> 3. `guesses.md`: every place the skill left you guessing, what you guessed, and every
>    time you had to open a raw transcript instead of the digest, and why.
>
> Finish with `runner/summary.md`: one line per scenario saying where it ended, and the
> paths of what you produced.

### Evaluator brief

The runner adds three lines at the top: the repository root, this round's scratch folder,
and the fixtures folder (`evals/reflect/local/`).

> You are evaluating the `reflect` skill. Another agent (the runner) has just followed it
> on six sample requests; its output is in the `runner/` folder of the scratch folder named
> above. You judge reflect: its instructions, and the skills and edits an agent following
> them produced. Don't change the skill or anything else on disk. Write only in the
> `evaluator/` folder of the scratch folder. Every repository and data folder is
> read-only. Never send, publish, commit, push, or change a scheduled task.
>
> **What it's for:** reflect turns the work done in a session into a skill, a new one or an
> edit to an existing one, so the next session can repeat the method without the user
> walking it through again. It captures the method, not the case. Two agents following it
> should reach comparable results, and the skills it produces should work on targets they
> weren't built on.
>
> **Settled decisions:** the spec's Settled decisions for this flow; don't raise or score
> them.
>
> **Read**, with paths relative to the repository root:
> - `skills/reflect/SKILL.md` and `skills/reflect/scripts/digest.py`, the versions on disk
>   now.
> - `evals/reflect/iterate.md`: the shared part and the "Flow: session to skill" section.
>   Don't open `evals/reflect/iterate-log.md`; form your own view. Judge only what this
>   flow's Who and what covers.
> - Everything in `runner/`.
> - The fixtures: `local/sessions.md` in the fixtures folder, and the frozen transcripts
>   through `digest.py`, as much as you need to judge whether the runner's output was what
>   reflect should have led to.
>
> Use file reading, Bash for running `digest.py` and read-only commands, and writing in
> `evaluator/`. Don't spawn subagents.
>
> **Test each produced skill or edit** (scenarios 1 and 3, if the runner got that far) on
> its held-out request from the spec. Load it as if it were installed and carry out the
> request as far as you can read-only, then write `evaluator/heldout-N.md`: what you did,
> what you'd send, where the produced skill left you guessing, what it got wrong or
> missed, and whether it captures the method or the fixture's case. If the runner
> produced no skill where it should have, that is a finding.
>
> **Then judge every scenario** against the spec's questions, using the runner's
> `guesses.md` as evidence but checking claims yourself.
>
> **Report, in about 800 words:**
> 1. Score N/10 as a whole number, one line on what holds it back, and whole-number
>    sub-scores for clarity, completeness, reproducibility, scope fit, economy, and
>    produced skill. Apply the rubric's cap.
> 2. How well reflect serves this flow overall.
> 3. Findings ranked by impact: the file and section, what's wrong, the concrete change
>    (replacement wording where you can), and what it replaces. Tag each **[direct]** or
>    **[proposal]** using the spec's guardrails, and **[high]** or **[low]** impact. Trace
>    each produced-skill flaw back to the reflect instruction that allowed it.
> 4. Next point: what would raise the score by one, and whether that lies in reflect or in
>    this test (the fixtures, the runner's limits, tools that can't reach part of it).
> 5. Alternatives: a different format or structure that would work better, and what it
>    would replace.
> 6. Keep: what works and shouldn't change.
> 7. What you wrote in `evaluator/`, and what you couldn't check.
