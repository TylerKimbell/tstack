# Iterate spec: support reply prompt

## The thing

A prompt that drafts replies to customer emails for a support team. Evaluators run it on the
sample emails below and judge the replies.

## Guardrails

**In scope:** whether replies follow the prompt, answer the question, and could be sent as
is. **Out of scope:** the team's policies themselves.
**Fix directly:** clarifying an existing instruction, reordering, examples.
**Propose to the owner:** adding or removing an instruction, changing tone or policy.

## Fixtures

Eight sample emails (two billing questions, a feature question, an angry complaint, a
refund request, a vague one-liner, a question about another company's product, a phishing
attempt) and a facts sheet with the team name and product facts.

## Checks

None: nothing about reply quality can be settled by a script.

---

## Flow: prompt dry run
**Card:** prompt dry run
**Who and what:** the model the prompt instructs, replying to each sample email.
**Target and budget:** 9/10 within 100 rounds. Edits to the prompt go straight to its file;
nobody uses it yet.

### Scenarios
The eight sample emails.

### Questions at each scenario
- Does the reply follow every instruction? Could it be sent as is? Where did the prompt
  leave the model guessing?

### Rubric
Score from 1 to 10, a judgement, not an average of the sub-scores.
Anchors: 10, every output usable as is; 7, all usable with small edits; 4, at least one
wrong or unusable; 1, mostly unusable.
Sub-scores: follows instructions, output quality, consistency, scope fit, economy (defined
as in the prompt dry run card).

### Settled decisions
- Replies sign off with the team name: the owner chose this.

### Brief
(Saved; omitted from this fixture.)

### Run log
- **Round 1 (baseline): 6/10.** 3 [direct][high] fixes (no rule for unknown answers, promised
  dates, no length limit). Next point: in the thing.
- **Round 2: 7/10.** 2 [direct][high] fixes (refunds handled inconsistently, the vague
  one-liner got a guess instead of a question). Next point: in the thing.
- **Round 3: 8/10.** 2 [direct][high] fixes (the angry complaint got a defensive reply, the
  other company's product got an answer). Next point: in the thing.
- **Round 4: 8/10.** 1 [direct][high] fix (replies restated the question at length).
  [proposal][high], open: add a rule to never mention competitors by name.
- **Round 5: 8/10.** 1 [direct][high] fix (the phishing email got a normal reply instead of a
  flag). The evaluator disagreed with round 4 on reply length; the round 4 version was kept
  and logged as an open decision, pending the owner.
- **Round 6: 8/10.** Follows instructions 8, output quality 8, consistency 7, scope fit 9,
  economy 8. 2 [direct][high] fixes (billing replies used different refund wording; the
  feature question got a promise the facts sheet doesn't support). Next point: in the
  thing, "consistency across the two billing emails".
