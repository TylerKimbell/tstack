---
name: unslop
description: "Cut AI-writing tells (puffery, filler, AI vocabulary, em dashes, chatbot phrases) and add human voice. Use when writing or editing prose for a person to read (docs, READMEs, PR descriptions, commit messages, emails, status updates, posts) or when asked to de-slop or humanize text. Not for code, logs, or data."
---

# Unslop

Scan for the patterns below, rewrite in the intended register, add voice, then ask "what still reads as AI-written?" and fix that.

- Keep the meaning, facts, numbers, and caveats the reader needs. Never invent a specific, source, or opinion to replace a vague line. Cut it or flag the gap.
- Leave code, identifiers, names, and quotations unchanged.
- A house style guide or the user's explicit instructions win over these rules.
- Asked to unslop a passage, return the rewrite. Add a line or two after it only for a cut claim or a gap the writer must fill.

## Voice

Text stripped of patterns can still read sterile, which is its own tell. Match the register: a chat reply or marketing copy carries more personality than reference docs or a commit message.

- **Be specific.** Not "schema changes can cause issues" but "a column rename fails the build".
- **Vary rhythm.** Short sentences land a point. Longer ones carry a fact with its condition. One idea per sentence doesn't mean one length.
- **Take a position where the text allows one.** Weigh the trade-off instead of listing pros and cons. "Fast, but the cache goes stale" beats "fast".
- **Use "I" or "we" when it fits.**
- **Don't force symmetry.** Equal-length bullets, same-shaped paragraphs, and a punchline closing every section look machine-made.

## Patterns

### Content

1. **Puffery and promotion.** "pivotal moment", "testament to", "setting the stage for", "nestled", "breathtaking", "groundbreaking", "must-visit". Say plainly what happened or what it is.
2. **Significance tails.** A trailing "-ing" clause that claims meaning: "..., highlighting/ensuring/reflecting/showcasing/fostering ...". Delete it, or make it its own sentence with a concrete claim.
3. **Vague or piled-up attribution.** "Experts believe", "Industry reports suggest", a list of outlets with no context. Name one source and what it said, or cut.
4. **Formulaic framing.** Openers like "In today's fast-paced world", "Despite challenges, X continues to thrive", and closers that recap or cheer ("In summary...", "The future looks bright"). Replace with a specific fact or plan, or end sooner.
5. **Feelings instead of mechanisms.** "SQL you can read" names a feeling. "`.toSQL()` returns the exact string sent to the database" names the mechanism. Cut a sentence you can't restate as a concrete fact, instruction, or number, or that could appear unchanged in another project's docs.

### Language

6. **AI vocabulary and inflated words.** additionally, crucial, delve, enduring, enhance, foster, garner, interplay, intricate, landscape, pivotal, robust, seamless, showcase, tapestry, testament, underscore, vibrant; utilize, leverage, facilitate, numerous. Use the plain word or cut.
7. **Fancy "is".** "serves as", "stands as", "boasts", "features". Write "is" or "has".
8. **Contrast framing.** "Not just X, but Y", "It's not X, it's Y", "more than just X". State the point directly.
9. **Forced threes.** Use the natural number of items.
10. **Synonym cycling.** One thing gets one name. Don't rotate "the tool", "the platform", "the solution".
11. **False ranges.** "From X to Y" where X and Y aren't ends of a real scale. Name the items.
12. **Filler.** "In order to" becomes "to". "Due to the fact that" becomes "because". "It's important/worth noting that" gets deleted.
13. **Hedge stacks.** "could potentially possibly" becomes "may". Hedge once, where the uncertainty is real.
14. **Abstract metaphor nouns.** substrate, wedge, vector, locus, nexus, vantage, bedrock, modality, paradigm, endgame, north star, flywheel; and as metaphors: primitive, harness, surface ("API surface"), scaffolding, gold-plating, ratchet, evacuate (for moving code). Use the concrete word ("base", "add", "way", "move out", "a limit that only tightens") or the thing's real name.
15. **Adverb props.** "runs quickly", "significantly improves". Use a stronger verb, or the measured number if you have it.
16. **Passive voice.** "Queries are validated" becomes "the compiler validates queries". Keep the passive only when the actor is unknown or doesn't matter.
17. **Dense sentences.** If the reader has to backtrack, split the sentence or drop clauses.

### Punctuation and formatting

18. **Dashes.** No em dashes. Don't swap in an en dash, a spaced hyphen, or parentheses as a stand-in. Use a period, a comma, or a new sentence. En dashes in number ranges are fine, and so are short parentheses that hold a unit, abbreviation, default, or example.
19. **Reveal colons.** Colons introduce a list, an example, or a label. Don't use one to stage a reveal ("Here's the thing: ...", "The result: ...", "The fix is simple: ..."). Write the plain sentence.
20. **Inline-header lists.** The tell is a bold label and colon that the line then restates: "**Performance:** Performance improved...". Rewrite as prose or a plain list. A lead-in that names the item and is followed by new detail is fine.
21. **Over-formatting.** Bold scattered across phrases, headers and bullets on a short answer, decorative emojis. Write short answers as prose.
22. **Title case headings.** Use sentence case.
23. **Curly quotes.** Use straight quotes.

### Chatbot artifacts

24. **Chatbot phrases.** "Great question!", "You're absolutely right!", "Certainly!", "Let's dive in", "Found the smoking gun!", "I hope this helps!", "Let me know if you'd like me to...". Start with the answer and stop when it's done. On an email the user is sending, a conventional close ("Let me know if you have questions", "Thanks") is fine.
25. **Knowledge disclaimers.** "While specific details are limited...", "As of my last update...". Find the fact, or state the real gap once, specifically.

<!-- Adapted from backnotprop/pstack (https://github.com/backnotprop/pstack). MIT License, Copyright (c) 2026 Lauren Tan; see the upstream repository for the full license text. Local changes are ours. -->
