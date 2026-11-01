---
name: postman
description: >
  Create or revise importable Postman requests, workflow folders, or full collections
  from an API task, documentation, or an existing collection. Use for /postman,
  $postman, or requests to package API calls for import. Ordinary endpoint/body
  explanations do not require this skill unless an importable artifact is requested.
---

# Postman

Deliver a saved Postman Collection v2.1 JSON file for a single request, additions to
an existing collection, or a full collection. Generating templates does not authorize
sending requests, changing permissions, or importing into a live workspace. Honor
separate authorization for those actions. Follow `AGENTS.md` and apply `unslop`;
external lookup follows `docs/integrations.md`.

## Select the artifact and recover context

- Package a single request inside a small collection so it is importable.
- For additions to a customized collection, default to a supplemental collection
  containing a folder the user can move into the original. Give it its own collection
  ID, and reuse existing variables and authentication. An export is unnecessary when
  the task only needs independent additions verified against API sources.
- For a new full collection, organize around the user's subjects or workflow. Do not
  expand a bounded task into the entire API or mirror every path segment as a folder.
- When editing a supplied export, preserve unrelated requests, order, IDs, auth,
  scripts, examples, and variables. Preserve user naming, including capitalization.
- Start with `company/postman/README.md` and the relevant collection and environment files.
  For platform background, check `company/knowledge-base/_index.md` for notes on the audited
  API definitions and on running collections.
  For other APIs, use supplied files and official docs. Ask only for missing
  information that changes the requested workflow; runtime IDs and credentials can
  remain documented variables.
- An export establishes saved configuration. A user-supplied screenshot establishes
  visible names, methods, and order, not bodies, URLs, scripts, auth, or variable
  values. A local template may be a subset of the live collection. Record unseen
  user-added requests in the inventory without inventing their configurations or
  calling it a full backup.
- Check for existing calls by method/path as well as name before adding duplicates.
  When no export is available, prepare a supplemental import instead of blocking on
  an unnecessary export.

## Verify the API mechanics

Use supplied API definitions or official documentation to check method, path,
identifier syntax, query parameters, auth, permissions, writable body fields, and
useful response expansions. Record the source version/URL and operation ID when
available in each request description. A response example supplies value structure,
not proof that every returned field is writable.

Then apply the platform's own API verification prompts, under "API verification
prompts" in `company/postman/README.md`, when the pack has them.

Prompts are not universal endpoint rules. Recheck the source for the actual API
operation. Mark specific unresolved behavior rather than presenting
an unverified payload as ready to run.

## Build the collection

- Use Collection v2.1 with `info.name`, a collection ID, schema URL, and request items.
  Follow the user's existing folder and request labels.
- Use inherited collection auth where suitable. For the platform's APIs, verify and reuse
  the base URL and token variable names the existing collections establish. Keep API
  services with different credentials separate.
- Use placeholders for credentials and real environment identifiers. Reuse environment
  variables and add only necessary inputs. Preserve an existing populated environment;
  update the repo's blank environment template instead of requiring replacement.
- For list operations, use a small page size and the API's own pagination parameters.
  Explain where the next page comes from. Do not add pagination or expansion
  parameters to operations that do not support them.
- Keep raw URLs consistent with structured path/query entries. Disabled parameters
  must not appear in the active raw URL.
- For JSON bodies, use raw mode, JSON language metadata, and Content-Type. Preserve
  numeric/boolean types when substituting variables. If an endpoint takes no body,
  omit it instead of inventing a payload.
- Request descriptions should state prerequisites, effects, required permissions,
  sources, and a concrete response check. Identify mutations using the user's
  convention or `[WRITE]`.
- Omit saved live responses and scripts unless needed. Use automatic variable capture,
  assertions, or runner sequencing only when requested or justified by the workflow.
  Never silently select the first returned entity or overwrite the user's context.

## Save and validate

Save reusable, sanitized artifacts under `company/postman/`, normally
`<api>-<topic>-additions.postman_collection.json` for additions. Put populated
environments, source exports, and anything with real environment values under the ignored
`private/postman/`. Do not embed this session's IDs, private URLs, or credentials in
the skill or reusable files. Do not automatically import, send, commit, or push
generated artifacts.

Perform focused local checks before delivery:

1. Parse collection/environment JSON and check the v2.1 shape. Use a local schema
   validator when available; do not describe a JSON parse as full schema validation.
2. Compare each added/changed method and normalized path to the source operation.
   Check declared query parameters, required fields, writable fields, and body types.
   Checking only an operation name or method is insufficient.
3. Account for every variable through existing environment/collection variables,
   supported Postman dynamic variables, or an explicit list of new user inputs.
   Validate templated JSON with representative typed substitutions. Check ordering
   and identifier handoffs between requests.
4. Verify preservation of unrelated exported configuration. Check that credentials or
   real identifiers did not enter reusable files, which colleagues may share: run
   `python3 scripts/publish_guard.py --files <paths>` on every file under `company/postman/`
   you add or change. On repeated generation, update the existing artifact and
   preserve its ID rather than accumulating duplicate folders.
5. Update `company/postman/README.md`, the blank environment template, and any walkthrough
   that uses the collection. Keep imported/screenshot-confirmed state distinct from
   locally prepared additions. Do not claim an incomplete local collection is a full
   live backup.

Local checks establish structure and compatibility with the inspected source.
They do not establish successful Postman import or live API behavior. Report exactly
what was verified; no live API calls are needed to finish a generation-only request.

## Deliver

Return the file link, included request names, destination collection/folder, new
variables and their source, and the first request to run. Mention material write
permissions or effects. Keep the chat handoff short; put details in request descriptions
and `company/postman/README.md`.

## Invocation examples

- `/postman Create an importable request to update one field on a record.`
- `/postman Add a lookup request and a link request to my existing collection.`
- `/postman Create a collection for this workflow using the attached OpenAPI file.`
- `/postman Update the attached collection with these requests, preserving my changes.`

`$postman` works the same way where the agent uses that invocation syntax.
