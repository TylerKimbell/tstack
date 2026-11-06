# tstack

Agent skills that work in any project without setup. Install them once and use them everywhere. They run as a plugin in claude.ai, Cowork, and Claude Code, and in OpenAI Codex as plain skill folders.

| Skill | What it does | How it runs |
|---|---|---|
| `unslop` | Cuts AI-writing tells (puffery, filler, AI vocabulary, em dashes, chatbot phrases) from prose and adds a human voice. Runs whenever the agent writes prose for a person. | Automatic, or on request |
| `technical-writing` | Writes or reviews docs, READMEs, RFCs, PR descriptions, and commit messages in four layers: Diátaxis, Google developer style, Simplified Technical English, and Global English. Finishes with `unslop`. | On request only |
| `bro` | Restates the agent's previous reply in plain words and keeps the numbers, paths, and next steps. Add text to restate only one part. | On request only |
| `postman` | Builds importable Postman Collection v2.1 files: one request, additions to an existing collection, or a full workflow. It checks each request against the API source and keeps credentials out of shareable files. Runs when you ask for a Postman request or collection. | Automatic, or on request |

## Install on claude.ai

Add the plugin to your Claude account once, and you get it in chat, Cowork, and Claude Code:

1. Open [Customize > Plugins](https://claude.ai/customize/plugins) in claude.ai or the Claude desktop app.
2. Select **Add > Add marketplace**, then enter `TylerKimbell/tstack`.
3. On **Discover**, select `tstack`, then select **Add**.

Claude loads `unslop` and `postman` when the task calls for them. To run `bro` or `technical-writing`, type `/tstack` in the message box and select the skill.

Claude Code downloads the plugin the next time you start a session signed in to the same account. In a session that is already open, run `/reload-plugins` to load it.

To get new versions, open the marketplace on the **Plugins** page and select **Check for updates**, or turn on **Sync automatically**.

On Team and Enterprise plans, an Owner controls whether members can add their own marketplaces. If you don't see **Add marketplace**, ask an Owner, or [install from the Claude Code command line](#install-from-the-claude-code-command-line) instead.

## Install from the Claude Code command line

Use this method if you don't use claude.ai, or you want the plugin on one machine only. Plugins you install this way aren't added to your claude.ai account.

Add the marketplace, then install the plugin:

```text
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

## Install in Codex

1. Clone the repository:

   ```bash
   git clone https://github.com/TylerKimbell/tstack
   ```

2. Copy the skill folders into your user skills folder, `~/.agents/skills/`:

   ```bash
   mkdir -p ~/.agents/skills && cp -r tstack/skills/* ~/.agents/skills/
   ```

   To use the skills in one project only, copy them into that project's `.agents/skills/` instead. To pick up new versions with `git pull`, symlink the folders instead of copying them.

Codex reads each skill's `agents/openai.yaml`. It runs `bro` and `technical-writing` only when you call them with `$bro` or `$technical-writing`.

## Override the defaults with your project's instructions

The skills follow your project's instructions (`AGENTS.md`, `CLAUDE.md`, or a house style guide) when they conflict with the skills' defaults. `postman` also reads any README beside existing collections for save locations, variable names, extra API checks, and a secret scanner to run. Without one, it saves shareable files in `postman/`, keeps files with real values in `postman/local/`, and runs its own credential scan.

## Change a skill

Each skill is one `SKILL.md`, plus `agents/openai.yaml` for Codex settings where needed. Bump `version` in `.claude-plugin/plugin.json` when you change behavior, so installed copies pick up the update. Check the manifests with `claude plugin validate .`.

## License

MIT. `unslop`, `technical-writing`, and `bro` are adapted from [backnotprop/pstack](https://github.com/backnotprop/pstack) (MIT, Copyright (c) 2026 Lauren Tan). See [LICENSE](LICENSE).
