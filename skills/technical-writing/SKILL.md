---
name: technical-writing
description: "Write or review technical docs, READMEs, RFCs, PR descriptions, and commit messages so they read clearly the first time."
disable-model-invocation: true
---

# Technical writing

The goal is writing a tired engineer understands on the first read. Four layers get you there, one question each: what kind of document is this (Diátaxis), how do sentences address the reader (Google developer style), how much does each sentence carry (STE), and can any sentence be read two ways (Global English). Apply all four, then apply the `unslop` skill to the result. Unslop owns the catalog of AI tells: vocabulary, filler, hedging, and formatting.

Three rules sit above the layers:

- **Cut every word that does no work.** If the sentence survives without a word, the word goes. Words that fix how a sentence parses do work (see Global English).
- **Use the short, everyday word.** A long word has to buy its length with precision.
- **When a rule makes a sentence worse, fix the sentence another way or leave it alone.** The rules serve the reader. A sentence that follows every rule and sounds like a machine wrote it has failed.

Name things by their real names. Write the actual symbol, file, flag, or command, not a synonym or a description of it. Every name, path, count, and claim about the change must be true when the text lands. For a count or file tree that will drift, give the command that regenerates it. Don't invent jargon: write "move", "delete", or "a budget that only decreases", not "evacuate", "ratchet", or "endgame". A named pattern is fine when the doc says what it means the first time.

One thought per sentence does not mean one length per sentence. Split the sentence that carries two thoughts, and keep the long one that carries one. Where unslop asks for a position or voice, the mode decides how much: explanation can weigh trade-offs and say what you make of them, while reference stays dry.

PR descriptions and commit messages get every layer except Diátaxis. Keep any headings their template requires. Product UI strings are not documentation. Use the product's copy guidelines for those.

## Pick the mode first (Diátaxis)

One document, one mode. Two questions pick it: does the content inform action (doing) or understanding (thinking), and does it serve learning or work?

- Action + learning: **tutorial**.
- Action + work: **how-to**.
- Understanding + work: **reference**.
- Understanding + learning: **explanation**.

Use this compass on a whole document or on one sentence whenever you are unsure what you are writing. Gut feel is often wrong here.

**Tutorial: learning by doing.** You are the teacher, and the learner's success is your job. Open with what the learner will build, not what they will "learn". Every step produces a visible result, early and often. Tell them what they should see: the expected output, the prompt change, the log line. Cut explanation to one clause and a link. Stay concrete. Write as "we", in commands: "First, do x. Now, do y."

**How-to: steps to a goal.** Solve a problem a person has, not an operation the machine can perform. Assume competence and skip teaching. Action only: no digressions, background, or completeness for its own sake. Link those instead. Allow forks and judgment: "If you want x, do y." Name the guide by the task: "How to calibrate the radar array", not "Radar array calibration".

**Reference: facts for lookup.** Describe, and only describe: no instruction, persuasion, or opinion. Be dry, complete, and sure. State facts, options, limits, and errors with no hedging. Mirror the structure of the thing described, so readers can navigate code and docs together. Generate from code where possible, so it stays true.

**Explanation: understanding and why.** One bounded topic, readable away from the product. Each title should tolerate an implicit "About..." in front. Anchor on a real why question. Give context: design decisions, history, constraints, alternatives. Opinion is allowed here and nowhere else.

Don't mix modes: no reference tables inside a tutorial or how-to, no tutorial hand-holding inside reference, no arguing inside a how-to. Split and link instead.

## Write sentences to the reader (Google developer style)

- Talk to the reader as "you", in the present tense. Use "will" only for things that happen later.
- Say who does what: "the compiler checks", not "is checked". Passive is fine only when the actor is unknown or beside the point.
- Write instructions and procedures as direct commands: "Click Submit." Never narrate them or write "should be done" or "must be installed".
- Put the condition or warning before the step it guards: "To delete the document, click Delete." The reader skips what does not apply and sees the danger before acting.
- Put the common case first and exceptions after.
- Sound like a knowledgeable friend. No buzzwords, no "please" in instructions, and never "simply", "easy", or "quickly" in a procedure. If it were simple, the reader would not be here.
- Don't pre-announce ("we will soon support...") and don't start consecutive sentences with the same phrase.
- Link with words that say where the link goes: the page title or a short description, never "click here". Prefer a sentence of context on the page over a link off it.
- Headings carry the point, not just the topic ("Pick the mode first", not "Modes"). Use sentence case. A task heading is a bare verb phrase ("Create an instance"). A concept heading is a noun phrase. Use one h1 per page and skip no levels.
- Use numbered lists for sequences and bullets for everything else. Introduce a list with a complete sentence. Keep items parallel.
- Put code in code font and UI elements in bold. Use serial commas. Drop "etc." and say up front that a list is partial.

## Make statements load one at a time (STE)

- One instruction per sentence. One thought per sentence everywhere else.
- Split instructions longer than about 20 words and other sentences longer than about 25.
- Give each word one meaning, and each thing or action one word. If "check" means inspect, don't also use it for restrain. Write "start" everywhere, not "initiate" in places. A doc that calls one thing "the gate", "the ratchet", and "the budget check" teaches three things. When you revise, don't reword sentences whose meaning didn't change.
- Avoid "-ing" words where you can. They take too many grammatical jobs and breed misreadings.

## Leave no sentence open to two readings (Global English)

- Keep words like "only" and "not" next to the word they change: "only fails on growth" and "fails only on growth" say different things.
- Break up long noun strings: "the proto import budget check script" becomes "the script that checks the proto-import budget".
- Make every "it", "they", and "this" point at one obvious thing. Repeat the noun when in doubt. Never use "this" or "which" to point at a whole clause.
- Don't drop verbs: "Phase 1 moves the converters and Phase 2 the runtime" leaves Phase 2 without one. Give it one.
- Keep the small words that fix the parse. "Remove backup file" reads two ways, and "Remove the backup file" reads one. "Ensure that the switch is off" keeps "that". Repeat the article when a series names separate things: "the client and the host", not "the client and host".
- Say which parts "and" or "or" joins when a sentence can group two ways. "Both...and", "either...or", and "if...then" are free disambiguators.
- Use periods, not semicolons or em dashes.
- Make text in parentheses a full grammatical unit or its own sentence. Never form plurals with "(s)".
- No slashes: write "a, b, or both" instead of "a/b" or "and/or".
- Skip idioms, colloquialisms, figurative language, and Latin abbreviations. A non-native reader, a translator, and an agent all parse plain constructions best.

## Worked example

Before:

> Configuration of the proto import ratchet budget script parameters is performed via budget.json. Note that it's important to remember that running with --write, which updates the committed budget to reflect the current count, should only be done when lowering it. If exceeded, CI fails.

After:

> `budget.mjs` reads the committed budget from `budget.json` and counts the files that import protos. If the count exceeds the budget, CI fails. Run `budget.mjs --write` only to lower the budget.

The fixes: "configuration is performed" becomes "`budget.mjs` reads", so someone does something (Google). "Ratchet" goes, and the script's real filename does the naming (real names). The five-noun string becomes plain clauses (Global English). The hedge "note that it's important to remember" is deleted (cut words). The failure condition moves ahead of the step (Google). "Should only be done when lowering" becomes a command with "only" next to what it limits (Google, Global English). "If exceeded" gets a subject: the count (Global English).

## Review checklist

Run this on every draft. Skip item 1 for PR descriptions and commit messages.

1. Is each document one Diátaxis mode, with links where modes meet?
2. Is every instruction a command, with its condition or warning in front?
3. Does any sentence carry two instructions or two thoughts? Split it.
4. Can any word be cut without losing meaning? Cut it.
5. Is "only" next to the word it changes? Does every "it" and "this" point at one thing? Does every clause keep its verb?
6. Does each thing have exactly one name throughout?
7. Would a developer say these words out loud? Replace invented metaphors and fancy synonyms with the plain word or the real name.
8. Are all symbols, paths, counts, and claims about the change true when the text lands, with commands that regenerate the counts?

Sources: diataxis.fr, developers.google.com/style, ASD-STE100 Simplified Technical English (Issue 9), and John R. Kohl's *The Global English Style Guide* (SAS Press).

<!-- Adapted from backnotprop/pstack (https://github.com/backnotprop/pstack). MIT License, Copyright (c) 2026 Lauren Tan; see the upstream repository for the full license text. Local changes are ours. -->
