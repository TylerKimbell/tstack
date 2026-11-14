# Iterate log: the reflect skill

## Flow: session to skill

**Run state:** ended after round 2 (rule 2, budget spent: 2 of 2). Target 9/10 not
reached. The primary's best score since the latest baseline (round 1) and for this run: 8.
Last round with progress: 2. Round 2's fixes were applied after its score and are not yet
scored. Starting version: the session
scratchpad's `reflect-iterate/start/reflect/` (the skill was never committed before this
run). Fixes: uncommitted in the tystack working tree.

- **2026-11-14, before round 1.** Digest bug fixed before the baseline: a session opened
  by a schedule or another session had zero turns. Fixtures frozen in `local/`.
- **2026-11-14, round 1 (baseline).** Runner `opus` high (no score); evaluator `opus` high,
  primary. All six scenarios covered; held-out tests for scenarios 1 and 3. **Score:** 7
  (clarity 8, completeness 6, reproducibility 7, scope fit 8, economy 7, produced skill 7;
  cap 8). Checks: pass before the round and after the fixes. Scenario outcomes all landed
  where they should (new tystack skill; thread question; edit to the installed sync skill;
  company skill in the data folder; nothing; memory). Held-out: the produced cost skill ran
  steps 1-4 on the account-brief runs as is, and stopped at steps 5-6, which assume helper
  agents those runs don't have; the sync edit reached the right "nothing to port" but
  weakened an existing commit gate. Next point, per the primary: in the thing (findings
  1-3); also in the test (runner has no helper agents; scenario 3's held-out target has
  nothing to port). High-impact [direct] fixes applied: 3. Progress: yes. Cost: runner
  about 260k tokens, 15 min; evaluator about 175k tokens, 4 min. The runner couldn't write
  `summary.md` (harness refused the subagent's Write); the iterate runner saved it from
  its report.
  - [direct][high] digest clipped Bash and Agent inputs even at `--max-text 0` and printed
    connector calls with no input; 3 of 4 sessions needed the raw transcript. Fixed:
    `--max-text 0` lifts input clips, unknown inputs print as compact JSON, a leading
    `cd <folder> &&` is stripped; Step 2 says so.
  - [direct][high] produced steps fit only the one variant the session tried. Added a
    step-shape check to Step 4 and "steps it couldn't exercise" to Step 8.
  - [direct][high] an edit loosened the target skill's commit gate. Step 7 now says never
    loosen an existing gate.
  - [direct][low] memory turn-away and the "nothing" exit lived only in the description.
    Added to the intro and Step 4.
  - [direct][low] fixes found while reading the target skill: Step 5 now says to list them
    separately, marked as yours.
  - [direct][low] which project decides the home vs. files and version bumps: Step 5
    clarified; leave an already bumped unreleased version.
  - [direct][low] interleaved threads (Step 2) and session openers from another session
    (Step 3): clarified.
  - [proposal][low] a method seen once (one case) should say so and offer a lighter home,
    such as a section of an existing skill. **Open**, for the owner.
  - Not applied (runner only, not the evaluator): Bash heredoc file writes don't appear in
    the digest's files list.
- **2026-11-14, round 2.** Runner `opus` high (no score); evaluator `opus` high, primary.
  All six scenarios covered; held-out tests for scenarios 1 and 3. **Score:** 8 (clarity 8,
  completeness 8, reproducibility 7, scope fit 9, economy 8, produced skill 8; cap 9).
  Checks: pass before the round and after the fixes. All six scenarios routed correctly
  again; the runner opened no raw transcript (round 1: three of four sessions). Produced
  cost skill reproduced the session's figures and placed both held-out runs; the sync edit
  reached the right answer in about four commands. Next point, per the primary: partly in
  the thing (findings 1-3), mostly in the test: scenario 1's held-out runs are the same two
  runs the fixture session measured in its last turn, so they aren't held out; scenario 3's
  held-out request has nothing to port, so only the compare step runs. High-impact [direct]
  fixes applied: 1. Progress: yes (score rose 7 to 8). Stop rule 2 holds. Cost: runner
  about 274k tokens, 16 min; evaluator about 164k tokens, 4 min. The runner again couldn't
  write `summary.md`; the iterate runner saved it.
  - [direct][high] Step 3 Artifacts: inline code consolidated into a shipped script left the
    runner guessing. Added: say so, and run it on the session's data to reproduce its
    results.
  - [direct][low] Step 8: a self-check fix contradicted its own section. Added: reread the
    whole skill or edit after fixing.
  - [direct][low] Step 2: thread splitting varied. Added: follow-ups, button answers, and
    checks stay in their thread.
  - [direct][low] Step 6: "yes, as proposed" was ambiguous about separate items. Added a
    closing question naming each item.
  - [direct][low] digest `--turns 9-11,13` crashed. Now accepts comma lists; Step 2's
    example uses it.
  - [direct][low] Step 1: the 120k limit now applies to the first digest; read a longer
    rerun in parts.
  - [direct][low] Step 4 table: product facts go wherever the project keeps them.
  - [direct][low] Step 4: values that change over time are case; the skill says where to
    look them up.
  - [proposal][low] if it's unclear a job will recur, ask in the proposal. **Open**, for the
    owner (joins round 1's one-case proposal).
  - **Test changes for the next run (a break, owner's call):** replace scenario 1's
    held-out runs with ones the fixture session never touched; give scenario 3 a held-out
    request with a real unported change.
- **2026-11-14, before and after.** One fresh `opus` evaluator, starting version and final
  version labelled at random (the final was X). **Verdict: the final version, clear
  confidence;** better in all six scenarios, most in scenarios 5 and 6 and the full-thread
  digest for scenario 1. Worse: about 2.4k characters longer; a full `--max-text 0` rerun
  can pass 120k characters (the skill says to read it in parts); connector inputs put more
  private data in the digest (scratch only, deleted at the end). Two defects it found were
  fixed after the comparison, unscored: stripping a leading `cd <folder> &&` lost where a
  command ran (the digest now prints "Bash (in <folder>)"); the description said reflect
  isn't for saving a preference while the body handles it (description now says it saves
  a memory instead).
