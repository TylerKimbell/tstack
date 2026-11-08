---
name: learn
description: >-
  Teach a topic goal by goal from verified sources. Use when the user asks to learn,
  understand, or study something: "teach me X", "how does X work", "walk me through X",
  "learn X from Y". Y can be a direct source (a URL, file, repo, or doc) or an owner of the
  topic (a company, product, framework, or project) whose own docs define it. Distinct from
  answering a one-off question: learn builds understanding and checks it.
---

# Learn

If the project defines its own `learn` skill, use that one instead.

The user names a topic, and may give learning goals with it, such as a training module's
objectives. Apply the `unslop` skill to everything you send the learner.

Keep supplied goals in their wording and order. Without goals, set two to five after Step 1:

- **Each goal** is something the learner can do and a scenario can test, and builds on the
  last.
- **Divisions:** follow the source's own where it has them. Numbered rules, steps, and
  concepts are divisions.
- **More than five:** merge adjacent ones that rest on the same idea, as few as you can,
  until five remain.
- **Look-up divisions** (settings, pricing, limits): leave them out of the count and fold
  what the learner must decide from them into the goals. If nothing else remains, build
  every goal that way.
- **Dropped sections:** name any top-level section you drop from the pages you teach from
  (not closing links such as "What's next"), unless the request already limits the source.
  A section counts as dropped if no goal uses it. For pages read later, name drops when you
  open that goal.

A single factual question isn't a lesson: answer it from a named source in a few lines,
marking any inference or partial read, with no goals or check.

## Step 1: Find the source

Never teach from memory anything a source can confirm: behavior, limits, defaults,
versions, syntax, or steps. Work out what "from Y" means first:

- **Y is a direct source** (a URL, file, repo, or doc): read it, and treat it as the main
  authority. Code is the primary source for what code does.
- **Y is an owner or context** (a company, product, framework, or project): find Y's
  official documentation on X, and teach X as Y defines it: Y's terms, Y's limits, and
  where Y's version differs from the general concept.
- **No Y given:** infer it from context, such as the current project or the conversation.
  If the topic means different things depending on who owns it, ask once, naming two to
  four likely owners from what you know, the ones most people mean first, as best you can
  judge, and wait. If the reply doesn't pick one, take the first and say so. Otherwise use
  the topic's own official documentation.

Prefer primary sources. Use secondary sources only to fill gaps, and label them. Before
stating goals, read the source's index or outline and whatever the first goal needs. Read
each later goal's source before teaching it. If a tool cuts off a page and the goal could
depend on the rest, read on. If a tool returns a summary, get the exact text of each
passage a goal rests on before teaching from it, since summaries drop conditions. Passages
a tool returns in quotation marks count as exact text; anything it paraphrases is a
summary. If you can't get the exact text, or a page won't load, say so and mark what rests
on it "My inference:". Look for a moved or renamed page before calling something
undocumented.

Use the newest source when recency matters. If the answer depends on a version (of
software, an API, or a model) the learner hasn't given, don't stop to ask: teach the
newest, and say, in the goal it affects or the answer to a single question, what differs
for earlier ones and how to check theirs, or that the sources don't say how. If you can't
tell whether a version matters, name the one you read.

Where sources disagree, say so, and name which one you trust and why. An undated doc
doesn't outrank a dated change record that contradicts it, but name any code that would
confirm it and that you couldn't read. If nothing you can read settles it, say so and name
what would. Raise a conflict in the message teaching the goal it affects, right before that
goal.

## Step 2: Teach it, goal by goal

Pitch it at the user's level. Infer it from how they ask. Without a signal, write for an
experienced practitioner who is new to this topic.

- Open with, in order: anything you're declining or narrowing, the sources you read (and
  whether a tool gave you only part of a page or a summary), the goals, the mental model of
  the whole topic (what it is, what problem it solves, and where it fits), and a line
  inviting questions or pushback. Then teach goal 1. Open each later goal by placing it in
  that model.
- Define the source's own terms on first use.
- Teach one goal per message, in order, unless the learner explicitly asks for it all at
  once; then put the checks at the end. End each goal's message on a concrete check, with
  the answer held back: a scenario to reason about, not a quiz question. For a recall goal,
  use a scenario that needs the fact. Then wait.
- In each goal, teach what its check needs, and call out gotchas, limits, and the
  neighboring concepts people confuse with it.
- Answer any question or pushback before moving on, and before any new scenario.
- Separate what the sources document from anything you inferred, reconstructed, or know
  from background, and mark the latter "My inference:". Name any source you add later when
  you first use it.

Respond to each check answer first: say whether the reasoning holds and correct it from the
source. After a correct answer, ask whether they have it or want more; if more, teach that
point further and end on a new scenario. Treat a partly right answer as wrong on the part
it missed. Missing a detail the check didn't ask for isn't partly right. After a wrong
answer, include the right outcome and give one new scenario on the same point; after a
second, give that scenario's answer and ask whether to go on. Move to the next goal when
the user says they have it, not when you finish writing, first giving any unanswered
check's answer in one line. After the last goal, say what was covered and what to read
next.

## Rules

- One topic per session. A topic is too broad if five goals can't cover it. Narrow first:
  take the owner's concept or overview docs in the order they list them (a getting-started
  path only if there are none), skipping admin and platform-specific sections and stopping
  at what five goals can cover, unless the request points elsewhere. Say what you left out,
  and start without asking.
- Don't experiment on production systems or live data, or coach the learner through it as
  practice. Decline that part first, teach the rest, say the exercise needs a sandbox, and
  offer to use one if they have it. Set that topic's checks on an invented system.
  Explaining what a command does is teaching; steps aimed at their system are not.