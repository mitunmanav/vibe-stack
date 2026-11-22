# Vibe Stack

Skills that let a person who does not read code build working software by describing it in plain words. A project's own wordbook (`.vibe/WORDS.md`) follows the same idea for that project's words.

## Language

**Playable Step**:
One small slice of the app that the user can open and click as soon as it is built. Inside the skills it is a vertical slice, stored at `.vibe/steps/<feature>/<NN>-<step>.md`.
_Avoid_: ticket, issue, task

**Save Point**:
A snapshot of the project taken before the agent changes anything, so one command can bring the app back. Inside the skills it is a git commit tagged `restore/<feature>-<NN>`, `restore/repair-<time>`, or `restore/tidy-<time>`.
_Avoid_: commit, branch, stash, checkpoint

**Demo Card**:
A page opened in the browser after a step is built: what is new, three things to click, and the results of the automated checks. Stored at `.vibe/previews/demo-<NN>.html`.
_Avoid_: report, summary

**Automated Check**:
A check the agent writes and runs that drives the app the way a person would and says pass or fail. Inside the skills it is a test, written red before green.
_Avoid_: unit test, assertion, mock

**Preview**:
A throwaway clickable page in `.vibe/previews/` that settles one question words cannot: how a screen should look, or how something behaves over time.
_Avoid_: prototype, mockup, wireframe

**One-way door**:
A choice that is hard or impossible to take back: it costs money, exposes private information, connects an outside account, or deletes saved data. The agent explains the real-world result and waits for a yes. Everything else is a two-way door the agent may decide and record.
_Avoid_: irreversible choice, high-impact decision

**Wordbook**:
A project's `.vibe/WORDS.md`: the everyday words for its screens, people, and things, so the user, the screens, and the agent all say the same thing.
_Avoid_: dictionary, vocabulary list

**Decision log**:
A project's `.vibe/DECISIONS.md`: the choices made for the project that the user might want to change, in plain words.
_Avoid_: ADR, changelog

**User command**:
A skill that runs only when the human types `/name`.
_Avoid_: slash skill, workflow

**Background skill**:
A skill the agent reaches for on its own, or a user command calls. It never shows in the human's menu.
_Avoid_: model skill, capability, helper

## Relationships

- A feature plan in `.vibe/specs/` is split into many **Playable Steps**
- Every **Playable Step** is built behind its own **Save Point** and ends in a **Demo Card**
- A **Playable Step** lists the **Automated Checks** that prove it
- A **Preview** settles one choice, which is recorded in the **Decision log**
- A **User command** can call **Background skills**, never another **User command**

## Flagged ambiguities

- "helper" means a separate agent, started in a fresh context window, that does one job and reports back. It is not a **Background skill**, which runs inside the current agent.
- "plan" is the whole feature plan in `.vibe/specs/`; one slice of it is a **Playable Step**, never a "plan step".
