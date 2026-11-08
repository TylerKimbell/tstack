# Mid-session transcript

This session is a stand-in written for the dry run. The source it teaches from,
`skills/iterate/SKILL.md`, is real.

## Part A: after goal 1

**Learner:** Teach me how evaluator panels work in the iterate skill, from
`skills/iterate/SKILL.md`.

**Agent:** I read the "Run a round" and "Fix" steps of `skills/iterate/SKILL.md`. We'll
cover three goals:

1. Whose score counts when a panel disagrees.
2. When a finding from a smaller model gets applied.
3. What a wide gap between scores means.

A panel is up to three fresh evaluators who run the same flow. They exist so a run can see
whether the thing being improved works for more than one strength of reader.

**Goal 1: whose score counts.** The skill names one evaluator the *primary*: the strongest
model on the panel, unless the user names another. The primary's score is the score of
record for the target and the stop rules. The other scores are logged beside it.

*Check:* a panel of `opus`, `sonnet`, and `haiku` scores a page 9, 7, and 5, and the target
is 8. Does the run stop on rule 1? Tell me how you worked it out.

**Learner:** It doesn't stop. The score is 7, the average, so it's under 8. Averaging is
fairer anyway, why would one model get to decide?

*(The evaluator writes the agent's reply to the message above, then the reply to this next
message.)*

**Learner:** ok got it, next

## Part B: the last goal

The same session later on. Goals 1 and 2 are done.

**Agent:** **Goal 3: what a wide gap between scores means.** The primary's score is the
score of record and the others are logged beside it. When the primary gives 9 and the
smallest model gives 5, the skill treats that gap as a finding: the thing works only for a
strong reader.

*Check:* a panel of `opus` (primary), `sonnet`, and `haiku` scores a skill 8, 8, and 4, and
the target is 8. Does the run stop, and what does the log need to say about the 4?

**Learner:** It stops on rule 1, because the primary hit 8. The 4 gets logged as a finding,
since a gap that wide means the skill only works for stronger readers.

*(The evaluator writes the agent's reply to the message above, then the reply to this next
message.)*

**Learner:** yep got it, thanks
