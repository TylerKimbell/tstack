---
name: postman
description: >
  Create or revise importable Postman requests, workflow folders, or full collections
  from an API task, documentation, or an existing collection. Use when asked for a
  Postman request or collection, or to package API calls for import. Ordinary endpoint/body
  explanations do not require this skill unless an importable artifact is requested.
---

# Postman

Deliver a saved Postman Collection v2.1 JSON file: a single request, additions to an
existing collection, or a full collection. Generating files does not authorize sending
requests, importing into a live workspace, changing permissions, committing, or pushing;
those need separate authorization. Apply `unslop` to descriptions and the handoff.

## Project conventions

Look for the project's own rules first; they override the defaults below.

- The project's agent instructions (`AGENTS.md`, `CLAUDE.md`, or equivalent) and any
  README beside existing `*.postman_collection.json` or `*.postman_environment.json`
  files. These may set save locations, file naming, base URL and token variable names,
  extra API verification checks, and a secret or publish scanner to run.
- Existing collections and environment files: reuse their variable names, auth setup,
  folder style, and labels.

Defaults when the project sets none:

- Save shareable, sanitized files beside existing collections, or else in `postman/`
  at the project root (the working directory outside a project), named
  `<api>-<topic>.postman_collection.json` (`-additions` before the suffix for additions).
- Save anything you write that holds real values (populated environments, copies of
  exports, live IDs) in `postman/local/`, and leave the user's own files where they
  are. In a git repository, confirm with `git check-ignore` that `postman/local/` is
  ignored; if not, tell the user and ask before adding an ignore rule.

## Choose the shape and gather context

- **Single request:** wrap it in a small collection so it imports.
- **Additions to a customized collection:** default to a supplemental collection with
  its own ID, holding one folder the user can move into the original, and reusing
  the original's variables and auth. No export is needed when the additions are
  independent and verified against API sources. When editing a supplied export
  instead, preserve unrelated requests, order, IDs, auth, scripts, examples, variables,
  and the user's naming and capitalization.
- **Full collection:** organize around the user's subjects or workflow. Do not expand a
  bounded task into the whole API or mirror every path segment as a folder.

Know what each input proves. An export establishes saved configuration. A screenshot
establishes visible names, methods, and order only, not bodies, URLs, scripts, auth, or
variable values. A local template may be a subset of the live collection: list unseen
user-added requests without inventing their configuration, and never call the result a
full backup. Before adding a request, check for an existing one by method and path as
well as name.

Ask only for missing information that changes the workflow. Runtime IDs and
credentials can stay as documented variables.

## Verify the API mechanics

From supplied API definitions or official documentation, check method, path,
identifier syntax, query parameters, auth, required permissions, writable body fields,
and useful response expansions. A response example shows value structure, not which
fields are writable. Also run any verification checks the project's conventions add,
then recheck them against the actual operation, since they are not universal rules.

Record the source version or URL, and the operation ID when there is one, in each
request description. Mark unresolved behavior as unresolved instead of presenting the
payload as ready to run.

## Build

- Collection v2.1: `info.name`, `info._postman_id`, the v2.1 schema URL, and `item`.
- Prefer inherited collection auth. Keep services with different credentials separate.
- Use `{{variables}}` for credentials and real environment identifiers. Reuse existing
  variables, add only necessary inputs, and never overwrite a populated environment.
- List operations: small page size and the API's own pagination parameters, with a note
  on where the next page comes from. Add no pagination or expansion parameters an
  operation does not support.
- Keep `url.raw` consistent with the structured host, path, and query entries. Disabled
  parameters stay out of the raw URL.
- JSON bodies: raw mode, `options.raw.language: json`, and a `Content-Type` header.
  Keep numbers and booleans unquoted when substituting variables. Omit the body when the
  endpoint takes none.
- Descriptions state prerequisites, effects, required permissions, sources, and a
  concrete response check. Label mutations with the user's convention, or `[WRITE]`.
- Omit saved responses and scripts unless needed. Add variable capture, assertions, or
  runner sequencing only when requested or the workflow requires them. Never silently
  pick the first returned entity or overwrite the user's context.
- On repeated generation, update the existing file and keep its ID rather than adding
  duplicate folders.

## Check

1. Parse every JSON file and check the v2.1 shape. Use a schema validator if one is
   available; do not call a JSON parse full schema validation.
2. Compare each added or changed method and normalized path with the source operation,
   including declared query parameters, required and writable fields, and body types.
   A matching name or method alone is not enough.
3. Account for every `{{variable}}`: existing environment or collection variables,
   Postman dynamic variables, or a listed new input. Render templated JSON bodies with
   typed sample values and parse them. Check request order and ID handoffs.
4. When editing a supplied export, diff it to confirm unrelated configuration is unchanged.
5. Scan shareable files for credentials and real identifiers, which colleagues may
   receive: run the project's scanner if it names one; otherwise search for tokens,
   keys, passwords, `Authorization` values, emails, private hostnames, and literal IDs
   from this session that are not `{{variables}}` or documented placeholders.
6. Update any README, blank environment template, or walkthrough the project keeps for
   the collection. Keep imported or screenshot-confirmed state distinct from locally
   prepared additions.

These checks establish structure and agreement with the inspected source, not a
successful Postman import or live API behavior. Report exactly what was verified. A
generation-only request needs no live calls.

## Deliver

Give the file path, request names, destination collection and folder, new variables
and where their values come from, and the first request to run. Mention material write
effects and permissions. Keep the handoff short; details belong in request descriptions.
