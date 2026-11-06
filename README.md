# tstack

Agent skills that work in any project. None of them reads project files to do its job, so you can install them once and use them everywhere. They run as a plugin in claude.ai, Cowork, and Claude Code, and in OpenAI Codex as plain skill folders.

| Skill | What it does | How it runs |
|---|---|---|
| `unslop` | Cuts AI-writing tells (puffery, filler, AI vocabulary, em dashes, chatbot phrases) from prose and adds a human voice. | Automatically when the agent writes prose for a person, or on request |
| `technical-writing` | Writes or reviews docs, READMEs, RFCs, PR descriptions, and commit messages in four layers: Diátaxis, Google developer style, Simplified Technical English, and Global English. Finishes with `unslop`. | Only when you invoke it |
| `bro` | Restates the agent's previous reply in plain words and keeps the numbers, paths, and next steps. Add text to restate only one part. | Only when you invoke it |
| `postman` | Builds importable Postman Collection v2.1 files: one request, additions to an existing collection, or a full workflow. It checks each request against the API source and keeps credentials out of shareable files. | Automatically when you ask for a Postman artifact, or on request |

## Install on claude.ai

Add the plugin to your Claude account once, and you get it in chat, Cowork, and Claude Code:

1. Open [Customize > Plugins](https://claude.ai/customize/plugins) in claude.ai or the Claude desktop app.
2. Select **Add > Add marketplace**, then enter `TylerKimbell/tstack`.
3. On **Discover**, select `tstack`, then select **Add**.

In chat, describe the task and Claude loads the matching skill. To pick a skill yourself, type `/tstack` in the message box and select it from the menu.

Claude Code downloads the plugin the next time you start a session signed in to the same account. In a session that is already open, run `/reload-plugins` to load it.

To get new versions, open the marketplace on the **Plugins** page and select **Check for updates**, or turn on **Sync automatically**.

On Team and Enterprise plans, an Owner controls whether members can add their own marketplaces. If you don't see **Add marketplace**, ask an Owner, or install from the Claude Code command line instead.

## Install from the Claude Code command line

Use this method if you don't use claude.ai, or you want the plugin on one machine only. Plugins you install this way aren't added to your claude.ai account.

Add the marketplace, then install the plugin:

```
/plugin marketplace add TylerKimbell/tstack
/plugin install tstack@tstack
```

Claude Code lists the skills under the plugin name, for example `/tstack:bro` or `/tstack:technical-writing`.

To have a project offer the plugin to everyone who opens it, add this to the project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "tstack": {
      "source": { "source": "github", "repo": "TylerKimbell/tstack" }
    }
  },
  "enabledPlugins": { "tstack@tstack": true }
}
```

To get new versions, run `/plugin marketplace update tstack`.

## Use in Codex

Copy or symlink the folders in `skills/` into your user skills folder, `~/.agents/skills/`, or into a project's `.agents/skills/`. Codex reads each skill's `agents/openai.yaml`. `bro` and `technical-writing` turn off implicit invocation there, so call them with `$bro` and `$technical-writing`.

## Project conventions

The skills follow your project's instructions (`AGENTS.md`, `CLAUDE.md`, or a house style guide) when they conflict with the skills' defaults. `postman` also reads any README beside existing collections for save locations, variable names, extra API checks, and a secret scanner to run. Without one, it saves shareable files in `postman/`, keeps files with real values in `postman/local/`, and runs its own credential scan.

## Changing a skill

Each skill is one `SKILL.md`, plus `agents/openai.yaml` for Codex settings where needed. Bump `version` in `.claude-plugin/plugin.json` when you change behavior, so installed copies pick up the update. Check the manifests with `claude plugin validate .`.

## License

MIT. `unslop`, `technical-writing`, and `bro` are adapted from [backnotprop/pstack](https://github.com/backnotprop/pstack) (MIT, Copyright (c) 2026 Lauren Tan). See [LICENSE](LICENSE).
