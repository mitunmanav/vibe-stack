# Vibe Stack

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](./CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

Vibe Stack is a set of skills for AI coding assistants (Claude Code, OpenAI Codex, GitHub Copilot, Cursor, Gemini CLI, and others) that lets people without a programming background build working software by describing it in plain language.

The assistant makes the technical decisions, records them in a readable log, shows visual options in the browser when a choice is easier to see than describe, and builds the project in small steps that can each be tried before moving on. Every change is preceded by a save point, so any step can be undone.

## Why Vibe Stack

General-purpose coding assistants tend to fail non-technical users in four ways:

| Problem | How Vibe Stack addresses it |
| :--- | :--- |
| The assistant starts building before it understands the idea, or asks technical questions the user cannot answer. | Questions are limited to what people will see, click, and pay for. Each one comes with a recommended answer (marked `➡️`), so replying "yes" is always enough. |
| Explanations are full of jargon the user cannot verify. | Technical choices are recorded in plain language in `.vibe/DECISIONS.md` and can be changed at any time by asking in chat. |
| A small change breaks other parts of the app, with no easy way back. | Work is split into Playable Steps. Each step is checked automatically, reviewed, and preceded by a Save Point that `/undo` can return to. |
| Secret keys end up in public files, or paid services are connected too early. | `/launch-check` scans for exposed keys and private data, and flags anything that cannot be reversed before it happens. |

## Installation

Choose one route per assistant. Installing through two routes registers every command twice.

**Claude Code**

```text
/plugin marketplace add mitunmanav/vibe-stack
/plugin install vibe-stack@vibe-stack-catalog
```

**Other assistants** (Codex, Cursor, Copilot, Gemini CLI, OpenCode, and more)

```bash
npx skills@latest add mitunmanav/vibe-stack
```

To update later, run `npx skills@latest update`.

## Quick Start

Open your assistant in an empty folder (or an existing project) and type the following commands in order.

1. **Set up the project** (once per project)

   ```text
   /start-project I want a simple booking page where dog owners can book a 30-minute grooming slot.
   ```

   The assistant summarizes the idea in two sentences and asks for confirmation. It then creates a small app that already starts and checks itself, a `.vibe/` workspace, and the first Save Point.

2. **Shape the idea**

   ```text
   /ask-me
   ```

   The assistant asks short, everyday questions in rounds. When a choice is easier to see than describe, it opens clickable options in the browser.

3. **Lock the plan**

   ```text
   /freeze-plan
   ```

   The conversation becomes a short plan divided into Playable Steps, each ending in something you can open and click. Reply "yes" to confirm, then type `/clear` to start the next part with a fresh chat.

4. **Build one step at a time**

   ```text
   /build-step
   ```

   The assistant takes a Save Point, writes an automated check and confirms it fails, builds the step until the check passes, has two independent helpers review the work, and opens a Demo Card listing three things to try. Repeat `/clear` and `/build-step` for each step.

5. **Check before sharing**

   ```text
   /launch-check
   ```

   The assistant checks for exposed keys and private data, explains anything that cannot be undone, and walks you through connecting any outside service.

## Commands

| Command | Purpose |
| :--- | :--- |
| `/start-project` | Set up the `.vibe/` workspace, a starter app that runs and checks itself, and the first Save Point. |
| `/ask-me` | Shape the idea through everyday questions with recommended answers and clickable previews. |
| `/freeze-plan` | Turn the agreed idea into a plain-language plan and a list of Playable Steps. |
| `/build-step` | Build and check one Playable Step, then open a Demo Card to try it. |
| `/repair` | Reproduce a problem, fix its root cause, and add a check so it stays fixed. Example: `/repair the Save button does nothing`. |
| `/launch-check` | Check for exposed keys, private data, and irreversible actions before sharing the app. |
| `/plain-english` | Say the previous reply again in everyday words and show the next command to type. |
| `/undo` | Return the app to an earlier Save Point. The plan and decisions are kept, and the undo can itself be undone. |
| `/tidy-up` (beta) | Clean up the code behind the scenes without changing what the app does. |
| `/look-back` (beta) | After a step or repair that went badly, suggest checks or rules that would have prevented it. |

Beta commands are new and have seen less real-world use.

**Pausing work:** close the chat at any time. Progress is stored in `.vibe/` and in your Save Points. To resume, open a new chat and type `/plain-english` to see where you left off.

## What to Expect

| Command | Working correctly looks like |
| :--- | :--- |
| `/ask-me` | Every question is about something you can see, click, or pay for, and "yes" accepts the suggestion. |
| `/freeze-plan` | Every step ends in something you can open and click. |
| `/build-step` | A Demo Card appears with three things to try, and all three work. |
| `/repair` | The problem is reproduced before anything is changed. |
| `/undo` | You are told exactly what going back removes before you confirm. |
| `/launch-check` | The result is a report with pass and fail badges, not a wall of text. |
| `/plain-english` | The second explanation is shorter and clearer than the first. |

## Feedback and Contributing

If a command does not behave as described, please [open an issue](https://github.com/mitunmanav/vibe-stack/issues) with what you typed, what happened, and what you expected. Contribution guidelines are in [SCOPE.md](./SCOPE.md) and [AGENTS.md](./AGENTS.md). Release notes are in [CHANGELOG.md](./CHANGELOG.md).

## License

[MIT](./LICENSE)
