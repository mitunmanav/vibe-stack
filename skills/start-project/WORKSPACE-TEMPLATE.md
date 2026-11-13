# Workspace Templates (`WORKSPACE-TEMPLATE.md`)

## `.vibe/config.md`

```markdown
# Project Setup

* **What this app is:** <two plain sentences>
* **Start command:** `<one command that runs the app on this computer>`
* **Check command:** `<one command that runs every Automated Check>`
```

The other `.vibe/` files and folders (`WORDS.md`, `specs/`, `steps/`, `previews/`) are created by the commands that first write to them.

## `.vibe/DECISIONS.md`

The file explains its own format, so every later command adds entries the same way.

```markdown
# Decision Log

Choices made for this project that you might want to change. To change one, tell the agent in chat, for example "change D-02 so it works on phones too".

<!-- Agents: add each entry at the bottom in the same shape as D-01. Never delete an entry: when a choice changes, mark the old one SUPERSEDED BY D-NN, add the new one with "Decided by: USER", and tell the user in one plain sentence what will change on screen. -->

### D-01 YYYY-MM-DD - <short plain title>
* **Status:** ACTIVE | **Decided by:** AGENT
* **What we chose:** <one plain sentence, e.g. "Runs on your computer as a small website; no accounts or payments needed to try it.">
* **Why:** <one plain sentence: how this keeps the app simple, safe, free, or easy to change>
* **What you will notice:** <the visible effect, or "nothing you can see">
* **Assumes:** <what must stay true for this to hold>
* **Risk if wrong:** <what would go wrong, in plain words>
* **Settled by:** <file, page, or check the agent relied on>
* **Depends on:** nothing
* **To change it:** say "change D-01" and what you want instead.
```

## Commit guardrail

Write `.vibe/hooks/pre-commit`, make it executable, and run `git config core.hooksPath .vibe/hooks`. It lives in `.vibe/`, so `/undo` never removes it.

```sh
#!/bin/sh
# Stops a commit that holds a secret key or a key file.
files=$(git diff --cached --name-only --diff-filter=ACM | grep -E '(^|/)\.env($|\.)' | grep -v '\.example$')
keys=$(git diff --cached -U0 -- . ':!.vibe/hooks' | grep -E '^\+.*(sk_live_|sk_test_|rk_live_|AIza[0-9A-Za-z_-]{20}|ghp_[0-9A-Za-z]{20}|xox[bp]-|BEGIN [A-Z ]*PRIVATE KEY)')
if [ -n "$files$keys" ]; then
  echo "Commit stopped: a secret key or key file was about to be saved into the project history."
  echo "$files"
  exit 1
fi
```

When the hook stops a commit, move the key into a git-ignored `.env` file and commit again. Tell the user only if the key was already shared somewhere.

## Pointer block

Add this block to `CLAUDE.md` if the project has one, else to `AGENTS.md` if it has one. If it has neither, create the file the assistant you are running in reads (Claude Code reads `CLAUDE.md`; most others read `AGENTS.md`). Never create the second file next to an existing one. If the block is already there, update it in place.

```markdown
## Vibe Stack

This project is built with someone who does not read code. Talk with them in plain everyday words, using the words in `.vibe/WORDS.md`. The plan and steps are in `.vibe/specs/` and `.vibe/steps/`; choices made on their behalf are in `.vibe/DECISIONS.md`, and they can change any of them by asking.
```
