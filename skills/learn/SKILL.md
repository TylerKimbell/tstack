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
objectives. Without goals, set two to five yourself in one line and say what they are, so
there is something concrete to check understanding against. Apply `unslop` to the
explanation.

## Step 1: Find the source

Never teach from memory anything a source can confirm: behavior, limits, defaults,
versions, syntax, or steps. Work out what "from Y" means first:

- **Y is a direct source** (a URL, file, repo, or doc): read it, and treat it as the main
  authority. Code is the primary source for what code does.
- **Y is an owner or context** (a company, product, framework, or project): find Y's
  official documentation on X, and teach X as Y defines it: Y's terms, Y's limits, and
  where Y's version differs from the general concept. For example, "learn X from Y" where
  Y is a vendor means reading Y's docs on X and teaching Y's version of X, not X in
  general.
- **No Y given:** infer it from context, such as the current project or the conversation.
  If the topic means different things depending on who owns it, ask once. Otherwise use
  the topic's own official documentation.

Prefer primary sources, and the newest one when recency matters. Use secondary sources
only to fill gaps, and label them. Look for a moved or renamed page before calling
something undocumented. Where sources disagree, say so, and name which one you trust and
why.

## Step 2: Teach it, goal by goal

Pitch it at the user's level. Infer it from how they ask, or ask once. Without a signal,
write for an experienced practitioner who is new to this topic.

- Lead with the mental model: what the thing is, what problem it solves, and where it fits.
- Define the source's own terms on first use.
- Work through the goals in order, one section each, with a concrete check after each: a
  scenario to reason about, not a quiz question.
- Call out gotchas, limits, and the neighboring concepts people confuse with it.
- Invite questions and pushback, and answer them before moving on.
- Separate what the sources document from what you inferred or reconstructed.

Move to the next goal when the user says they have it, not when you finish writing.

## Rules

- One topic per session. Split a topic that is too broad and say which slice you are
  taking.
- Don't experiment on production systems or live data. Use a sandbox, or tell the user
  the exercise needs one.
