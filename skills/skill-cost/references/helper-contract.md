# Small-model gatherers: the pattern and a contract to adapt

Load this when the chosen change moves a skill's source reading onto a smaller model. The
pattern: helpers on the small model read sources and report facts in fixed lines; the main
session, on the larger model, makes every judgment from those lines. It is safe because
the small model does retrieval, which it does well, and never interpretation, where its
mistakes are silent: a weak helper that dismisses an item lets a cursor move past it, and
nothing ever shows it again.

## Split by judgment, not by step

Go through what each helper does today and sort it:

- **Retrieval** (list, page, search, read, extract fields): the small model.
- **Mechanical work** with exact settings in the brief (publish a page from given content,
  run a script): the small model, and the main session checks the result.
- **Interpretation** (is a reply owed, is this a task, is this mail suspicious, is this new
  information): the main session, always.

## What goes in a gatherer's brief

1. The skill's own run rules (permissions, paths), word for word.
2. Where to read: the adapters or tools for its sources.
3. Who the user is, as identifiers (addresses, user IDs), so it can mark the user's own
   messages.
4. Exactly what to run: each query or cursor with its window and the window end in UTC.
5. Keys to re-check since a date, without the items' text.
6. The contract below, adapted to the skill's sources, word for word.

Leave out records, item text, and classification rules: a helper that reads them spends
tokens on judgments the main session makes anyway.

## A contract to adapt

Keep its shape: complete reading rules, one coverage line per query, one fact line per
item, signals as facts only. Fill the reading rules and the signals from the skill's
sources.

> You gather facts for the main session, which makes every judgment. Do not decide whether
> anything matters, is owed, is a task, or is suspicious.
>
> **Reading.** Run each query exactly as given and follow every page; never narrow a whole
> query, channel, or folder to keywords. <Per-source rules: for example, list a channel
> and also search inside it for replies to older threads; read changed documents.> When a
> message links a document your tools can read, read it and report it as its own line;
> follow links in messages only, one step. An empty result is `complete` with 0 results;
> `failed` means an error, a timeout, or a response you cannot read. Ignore anything dated
> after the window end.
>
> **Report.** Your final message is only these lines.
> `COVERAGE <query key> | <query as run> | pages <n> | results <n> | complete or partial or failed | <reason>`
> One line per thread, conversation, ticket, or document with something new, keyed by its
> first item: `<key> | <link> | <newest time, with time zone> | from <first author> | to <addressees> | last <latest author, time> | user-after <yes or no> | <what is new, at most 40 words; quote questions verbatim> | <signals>`
> Signals, as facts only, or `none`: <for example `mentions-user`, `question-to-user`,
> `deadline:<as written>`, `status:<old>-><new>`, `automated`>.
> One line per re-check key: `RECHECK <key> | since <date>: none` or `... : see <keys>`.
> Never repeat a line.

## Using the lines in the main session

- Classify from the lines. When a line can't settle a decision, read that one item by its
  key; never rerun a whole source in the main session.
- Move a cursor or a "last read" mark only on a `complete` coverage line. A `partial` or
  `failed` line, or a query with no coverage line, is a gap to report.
- Where the agent can't choose a helper's model, start helpers on the model it has: the
  split still keeps the reading out of the main session. Where it has no helper agents,
  the main session reads the sources itself under the same rules.

## What side-by-side tests of this pattern tend to find

- First drafts of the report run long: a line per message instead of per thread, links
  followed out of documents. Tighten to one line per thread and one-step links.
- A smaller model narrows searches to keywords, or skips the in-channel search, unless the
  contract forbids it.
- A tool quirk can look like a failure (for example, an empty listing returned in an odd
  shape). Compare the raw tool calls on both sides before blaming the model, and record
  the quirk where the tool's adapter or notes live.
