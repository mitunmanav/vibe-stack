---
name: clarifying
description: "Plain-language interview loop that investigates project facts silently, sorts questions into three buckets, logs technical choices to .vibe/DECISIONS.md, and updates .vibe/WORDS.md. Use when shaping ideas, resolving ambiguity, or planning features before coding."
user-invocable: false
---

# Clarifying

Walk every unresolved branch of the user's idea until you share the exact same mental picture. **Never ask the human a programmer question, and never start writing application code during this loop.**

## 1. Silent fact-finding

1. Read `.vibe/config.md`, `.vibe/WORDS.md`, and `.vibe/DECISIONS.md` if they exist.
2. Spawn a fresh background helper to inspect existing project files or official documentation before asking anything. Investigating facts is your responsibility, never the human's.

## 2. Three-bucket question filter

Before showing any question to the user, sort every open question into one of three buckets:

* **Bucket 1 - Agent Decides (Silent technical choices):** If a question is about code tools, file structure, database tables, or testing mechanics and can be changed later without losing user data or costing money, decide it yourself using the simplest reliable option and log it in `.vibe/DECISIONS.md`. Read `DECISION-LOG-FORMAT.md` when recording a silent or approved decision.
* **Bucket 2 - Ask the Human in Plain Words (Screen behavior and feel):** If a question changes what people see, click, type, or experience, ask the user in everyday words (max 3 questions per turn). Read `BUCKET-RULES.md` when phrasing Bucket 2 or Bucket 3 questions.
* **Bucket 3 - Ask the Human with Consequences (Money, privacy, outside accounts, or deleting data):** If a choice costs money, exposes private data, requires an outside login, or erases existing data, add a `⚠️ **Why this matters:**` warning line above the question and wait for explicit approval.
* **Visual ambiguity:** If a screen layout or multi-step flow is easier to see than describe in text, run the `showing-options` skill to open clickable options in the browser.

## 3. Question format and wordbook sync

Format every Bucket 2 or Bucket 3 question so replying `"yes"` accepts your recommended default:

```markdown
❓ **Q1** - **<short everyday title>**: <plain question phrased so "yes" accepts the default>
➡️ <recommended default and one short reason why>
---
```

* **Wordbook update:** Once everyday terms for screens, people, or items settle (never on turn 1), update `.vibe/WORDS.md`. Read `WORDBOOK-FORMAT.md` when adding or retiring project words.
* **Gate:** Stop after each question round (1 to 3 questions) and wait for the user's reply. Repeat until no open branches remain, then summarize the agreed idea in 3 plain bullets and tell the user to run `/freeze-plan`.

## Red flags (never rationalize these)

| Tempting Shortcut | Required Action Instead |
| :--- | :--- |
| "I'll ask whether they want SQLite, Postgres, or localStorage." | Decide Bucket 1 silently (unless multi-device access is needed) and log it in `.vibe/DECISIONS.md`. |
| "I'll ask 8 questions at once to save turns." | Ask at most 3 questions on the current open frontier per turn. |
| "The idea seems clear enough, I'll start coding now." | Stop at the gate, confirm shared agreement, and tell the user to run `/freeze-plan`. |
