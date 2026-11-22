# Workspace Templates

## `.vibe/config.md`

<config-template>

```markdown
# Project Setup

* **What this app is:** <two plain sentences>
* **Start command:** `<one command that runs the app on this computer>`
* **Check command:** `<one command that runs every Automated Check>`
```

</config-template>

The other `.vibe/` files and folders (`WORDS.md`, `DECISIONS.md`, `specs/`, `steps/`, `previews/`) are created lazily by the skills that first write to them.

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

This project is built with someone who does not read code. Talk with them in plain everyday words, using the words in `.vibe/WORDS.md`. The plan and steps are in `.vibe/specs/` and `.vibe/steps/`; choices made on their behalf are in `.vibe/DECISIONS.md`, and they can change any of them by asking. When they seem unsure what to do next, point them to `/what-next`.
```
