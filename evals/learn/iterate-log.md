# Iterate log: the learn skill

## Flow: dry run

**Run state:** ended after round 9 (rule 2, budget spent: 2 of 2). Target 9/10 not reached.
The primary's best score since the latest baseline (round 3) and for this run: 8; last round
with progress: 9. Starting version of this run: the trimmed text round 7 scored, saved in the
session scratchpad as `learn-run5-private/start.md`. Fixes: uncommitted in the working tree;
round 9's fixes were applied after its score and are not yet scored. Earlier runs ended
after round 1 (rule 1), round 2 (rule 1), round 6 (rule 4), and round 7 (report only).

- 2026-11-08, round 1 (first baseline), `opus` only, 7/10, progress yes: pacing, check answers, goal shape, too-broad rule, one-off line. Blind comparison: fixed version, strong confidence. Run ended on rule 1.
- **2026-11-08, between runs.** Owner set 8/10 within 5 rounds and accepted the
  recommendations. Accepted and applied: the pacing opt-out and the closing step. Declined
  for now and added to Settled decisions (not a break): the message shape and the routing
  table. Scenarios, questions, rubric, evaluators, and brief are unchanged, so round 2 is
  not a new baseline.
- 2026-11-08, round 2, `opus` only, 8/10, progress yes: goals follow the source, a path for correct answers, the held-back answer given before moving on. Blind comparison: fixed version, strong confidence. Run ended on rule 1.
- **2026-11-08, between runs. Break in comparability.** Owner set 9/10 within 5 rounds and a
  panel of `opus` (primary), `sonnet`, and `haiku` at high effort, in place of `opus` alone.
  With the owner's agreement, scenario 6 gained a part B (a correct answer at the last goal,
  then the learner says they have it) to cover the correct-answer path and the end of a
  lesson, and the brief's "the two replies" became "each reply". Round 3 is a new baseline.
  Declined for now and added to Settled decisions: the numbered goals step.
- **2026-11-08, round 3 (new baseline).** Panel: `opus` (primary), `sonnet`, `haiku`, high
  effort. All eight scenarios covered. **Scores:** `opus` 8 (clarity 8, completeness 8,
  reproducibility 7, scope fit 9, economy 9); `sonnet` 7 (7, 7, 6, 8, 8); `haiku` 6 (6, 5,
  5, 7, 7). The 2-point gap from primary to smallest is moderate; it comes mostly from the
  first message and finding an owner's docs. What holds it back, per the primary: the first
  turn still varies. Checks: pass before the round and after the fixes. Next point, per the
  primary: in the skill (findings 1 to 3). High-impact [direct] fixes applied: 3. Progress:
  yes. No stop rule holds. Cost: about 387k tokens across the three; 7 minutes in parallel.
  `opus` used one Bash command to make its scratch folder and `haiku` used PowerShell; the
  repository is unchanged beyond the run's own files.
  - [direct][high] `opus`: "or ask once" about level gave two moves with no signal. Removed.
    Kept [direct]: the next sentence already gives the no-signal behaviour, so no step goes.
  - [direct][high] `opus` (and `sonnet` low): how much to read before stating goals. Added.
  - [direct][high] `opus` (and `sonnet` low): divisions over five. Now grouped, and said so.
  - [direct][low per `opus`, high per `sonnet`] First-message order. The first bullet now
    gives it: sources, goals, mental model, then goal 1. Dropped the two sentences this
    replaces. A sentence inside the bullets, so the settled decision stands.
  - [direct][low] `opus`: invite questions once near the start; answer before any new
    scenario.
  - [direct][low] `opus`: "if a check went unanswered"; after a second wrong answer, give
    the answer and ask whether to go on.
  - [direct][low] `opus` (and `sonnet` high): likeliest owner first; fall back to the first.
  - [direct][low] `opus`: a sandbox you already have access to.
  - [direct][low] `opus`: the one-off line marks partial reads too.
  - [direct][low] `haiku`: "the `unslop` skill". Smaller-model clarity fix, not contradicted;
    `sonnet` also reported not loading it. Left out the `tstack:` prefix, which is
    platform-specific.
  - Not applied, smaller model only and not clarity problems: `haiku` how to reach an owner's
    docs [high], answering pushback the source doesn't cover [high], search before asking
    [high], a worked example of grouping [low]; `sonnet` version-dependent answers and
    partly settled conflicts [high], the partial-read wording [low], one-off contents [low],
    what's allowed around production [low], the slice criterion [low], neighbouring concepts
    [low].
  - Not applied, conflict: `haiku` "got it" only moves on with no open check. The primary
    keeps the current rule; the owner's text moves on at the learner's word.
  - Verified by checks and by walking the changed text through scenarios 1 to 6 myself.
    Effects on other flows: none new.
  - Not covered: verbatim source wording (all three: WebFetch summaries); a second agent's
    output.
- 2026-11-08, round 4, 8/10 (`sonnet` 7, `haiku` 7), progress yes: opening order for declines and pushback, partly right answers, reference sections.
- 2026-11-08, round 5, 8/10 (`sonnet` 7, `haiku` 6), progress yes: grouping stops at five, background knowledge labelled, versions the learner hasn't given.
  - Open proposals from rounds 4 and 5: the "how does X work" trigger (`opus`); a nearly complete answer gets a one-line note (`haiku`); a source that says it's invented (`haiku`); an optional level question (`sonnet`).
- 2026-11-08, round 6, 8/10 (`sonnet` 7, `haiku` 6), progress yes, run ended on rule 4: the slice's source, reading on after a cut-off. Blind comparison: final version, clear confidence.
  - Open proposals from round 6: more than five supplied goals (`opus`); a term with no owner (`haiku`).
- **2026-11-08, after run 3: trim at the owner's request, not scored.** Cut the skill from
  1172 words without a round. Removed: "merge the earliest qualifying pair" (false
  precision), the "walk me through" parenthetical (now "explicitly asks"), "say if you
  grouped them", where "what to read next" comes from, the method-as-inference line (the
  general inference rule covers it), the one-off's cross-references, repeat disclosure of
  partial reads, and the duplicate conflict placement in the opening order. Step 1's long
  paragraph is split into reading, versions, and conflicts. Kept the behaviours evaluators
  relied on, and the partly-right rule, which is still an open decision. Verified by checks
  and by walking all eight scenarios through the text myself. A fresh scored round hasn't
  run on it.
- **2026-11-08, round 7, report only, on the trimmed text (1020 words).** Panel: `opus`
  (primary), `sonnet`, `haiku`, high effort. All eight scenarios covered. **Scores:** `opus`
  8 (clarity 8, completeness 8, reproducibility 7, scope fit 9, economy 9); `sonnet` 7 (7, 7,
  6, 9, 8); `haiku` 7 (7, 6, 6, 8, 7). No fixes; progress: no (report only). The trim held
  the primary's score, took its economy from 8 back to 9, and took `haiku` from 6 to 7.
  Checks: pass. Next point, per the primary: in the skill. Cost: about 410k tokens.
  A usage limit stopped `opus` and `sonnet` partway; both resumed with one added message
  (retry failed fetches, don't count them against the skill). `haiku` finished before the
  reset, and some of its failed fetches came from that limit.
  Findings, all open for the owner (none applied):
  - [direct][high] `opus` (and `sonnet` high, `haiku` high): reading past a summary or a
    failed fetch. `opus` reports a scenario 2 draft that would have taught an error from a
    summary that dropped a condition, while disclosing the summary. Not independently
    verified. `opus` wording: get the exact text of each passage a goal rests on.
  - [direct][high] `opus`: "name any section you drop" has no depth; top-level sections only.
  - [direct][high per `sonnet`, low per `opus`] The merge rule: which pairs, and whether five
    is a floor or a cap. `haiku` read it as a required merge.
  - [direct][low] `opus`: where the version note goes, or say the sources don't say how
    (`sonnet` also); a dated record settles it but name the code that would confirm it; set
    checks on an invented system; admit owner order is a judgement (`sonnet` also).
  - [direct][low] `sonnet`: conflict placement for goal 1; use the source's own headings; a
    size for one-offs; "My inference:" covers background in the model and sandbox advice.
    `haiku`: don't research before asking.
  - [proposal][low] `opus`: move the too-broad test next to goal-setting. `haiku`: a source
    that says it's invented; a learner who says "I don't know".
  - Not covered: verbatim source wording beyond scenario 2's key passages; a second agent's
    output; a real learner.
- **2026-11-08, between runs.** Owner set 9/10; budget 2 rounds. Round 7's findings applied
  before round 8 (no break): reading past a summary and failed fetches (all three); top-level
  sections only; merge wording, "as few as you can" (`sonnet`, `haiku`); the version note's
  place; naming code that would confirm a dated record; owners most people mean; checks on
  an invented system. Not applied: `opus`'s merge tie-break, which it called arbitrary: the
  owner-requested trim removed the same kind of rule as false precision. Conflict logged.
- **2026-11-08, round 8.** Panel: `opus` (primary), `sonnet`, `haiku`, high effort. All
  eight scenarios covered. **Scores:** `opus` 8 (clarity 8, completeness 8, reproducibility
  7, scope fit 9, economy 8); `sonnet` 8 (8, 8, 7, 9, 9); `haiku` 7 (7, 6, 6, 8, 7). What
  holds it back, per the primary: no path when a tool can't return exact text, and two
  goal-setting sentences that compete. Checks: pass before the round and after the fixes.
  Next point, per the primary: in the skill, with part of the first finding in the test
  (WebFetch capped quotes at 125 characters). High-impact [direct] fixes applied: 2.
  Progress: yes. No stop rule holds. Cost: about 415k tokens.
  - [direct][high] `opus` (and `haiku`, `sonnet`): no fallback when exact text can't be had.
    Folded into the failed-fetch sentence. Dropped "in the opening", since a later goal's
    source is read after the opening.
  - [direct][high] `opus`: the merge and reference clauses competed. What counts as a
    division is now named, and looked-up divisions skip the merge.
  - [direct][low] `opus`: a wrong answer's correction includes the outcome; the second gives
    that scenario's answer.
  - [direct][low] `opus`: the slice is the overview pages the goals need; closing links
    aren't sections to name (`sonnet` also raised the level, high).
  - [direct][low] `opus`: the version rule covers single answers and not knowing whether a
    version matters.
  - [direct][low] `opus`: "that topic's checks" on an invented system.
  - [proposal][low] Open, `haiku`: a table for the check paragraph.
  - Not applied: `sonnet` exactly five goals (conflicts with the owner's two to five), checks
    only on pages read [medium], extracts in the sources line, marking every small claim, a
    bare "got it" counts (covered); `haiku` "got it" before the new scenario (covered),
    "that part" of the production rule.
  - Test note from `sonnet`: scenario 6 part B's "what does the log need to say" quietly needs
    `templates.md`. A fixture problem; fixing it would be a break.
  - Verified by checks and by walking the changed text through scenarios 1, 2, 4, 5, 6, and 7
    myself.
  - Not covered: verbatim source wording; a second agent's output; a real learner.
- **2026-11-08, round 9.** Panel: `opus` (primary), `sonnet`, `haiku`, high effort. All
  eight scenarios covered. **Scores:** `opus` 8 (clarity 8, completeness 8, reproducibility
  7, scope fit 9, economy 8); `sonnet` 7 (8, 7, 6, 9, 8); `haiku` 6 (6, 6, 5, 8, 6). What
  holds it back, per the primary: goal selection and what counts as exact text. Checks: pass
  before the round and after the fixes. Next point, per the primary: in the skill, with part
  of the exact-text finding in this test's tool. High-impact [direct] fixes applied: 3.
  Progress: yes. **Stop: rule 2** (budget spent). Cost: about 445k tokens.
  - [direct][high] `opus`: "the pages your goals need" was circular. The slice is now the
    owner's concept or overview docs in their order, skipping admin and platform sections,
    stopping at what five goals can cover.
  - [direct][high] `opus` (and `sonnet` high): quoted passages count as exact text; paraphrase
    is a summary. `haiku` proposed a "From a summary:" label instead; the primary wins.
  - [direct][high] `opus`: look-up divisions leave the count and fold into the goals.
  - [direct][low] `opus` (and `sonnet` high): what counts as dropped, and when to name it.
  - [direct][low] `opus`: a model counts as a version; missing a detail the check didn't ask
    for isn't partly right.
  - **Not applied, conflict across rounds, kept closest to the owner's intent:** a merge
    tie-break (`opus` and `sonnet`, high) and where "what to read next" comes from (`opus`,
    low). Both were cut in the owner-requested trim; re-adding would flip. Open decisions;
    added to Settled decisions as pending the owner (not a break).
  - [proposal][low] Open, `haiku`: whether production covers shared staging with real data.
  - Not applied, smaller model only and not clarity problems: `haiku` how to tell look-ups
    from decisions (the primary's rewrite covers it), owners a search leads to, a source that
    doesn't answer, a source calling itself a sample, unslop's location; `sonnet` the opening
    may mention a conflict, owner cap and fallback, message length, sandbox exercise design,
    "it depends" one-offs.
  - Open alternatives: a bulleted goals block in the intro (`opus`); a worked merge example
    (`sonnet`, `haiku`); a source ledger (`haiku`).
  - Verified by checks and by walking the changed text through scenarios 1, 2, 4, and 6
    myself.
  - Not covered: verbatim source wording; later goals outside scenario 6; a real learner.
  - **Before and after this run (blind, one fresh `opus`, high; about 65k tokens; prompt also
    weighs length):** the final version preferred with clear confidence, 7 scenarios to 0
    (scenarios 6 and 8 only slightly) with scenario 3 tied. Where it's worse: the goals
    paragraph is a dense run of about ten conditionals; dropped-section bookkeeping can clutter
    openings; document order can beat teaching order on Kubernetes; "quotation marks count as
    exact" is tool-specific and trusts a summarizer; "as best you can judge" buys nothing.
    All open for the owner; none scored.
  - **End-of-run note.** The skill is 1245 words, more than the 1172 before the trim. The
    primary has scored 8 in every round since round 2.
- 2026-11-08, after run 5: the owner kept the final text (1245 words) over the trimmed text.
- 2026-11-08, after run 5: at the owner's request, split the goals paragraph into bullets.
  Layout only, no rule changed; not scored.
