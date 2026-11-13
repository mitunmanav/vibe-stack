# Vibe Stack Wordbook

The words Vibe Stack uses with its users, and what each one means inside the skills. A project's own wordbook (`.vibe/WORDS.md`) follows the same idea for that project's words.

## Language

**Playable Step**:
One small slice of the app that the user can open and click as soon as it is built. Every step works on its own before the next one starts. Inside the skills it is a vertical slice, stored at `.vibe/steps/<feature>/<NN>-<step>.md`.
_Avoid_: ticket, issue, task

**Save Point**:
A snapshot of the project taken before the agent edits anything, so one command can bring the app back. Inside the skills it is a git commit tagged `restore/<feature>-<NN>` or `restore/repair-<time>`.
_Avoid_: commit, branch, stash, checkpoint

**Demo Card**:
A page opened in the browser after a step is built: what is new, three things to click, and the results of the automated checks. Stored at `.vibe/previews/demo-<NN>.html`.
_Avoid_: report, summary

**Automated Check**:
A check the agent writes and runs that drives the app the way a person would and says pass or fail. Inside the skills it is a test, written red before green.
_Avoid_: unit test, assertion, mock

**One-way door**:
A choice that is hard or impossible to take back: it costs money, exposes private information, connects an outside account, or deletes saved data. The agent explains the real-world result and waits for a yes. Everything else is a two-way door the agent may decide and record.
_Avoid_: irreversible choice, high-impact decision

**Wordbook**:
A project's `.vibe/WORDS.md`: the everyday words for its screens, people, and things, so the user, the screens, and the agent all say the same thing.
_Avoid_: dictionary, vocabulary list

**Decision log**:
A project's `.vibe/DECISIONS.md`: the choices the agent made on the user's behalf that the user might want to change, in plain words.
_Avoid_: ADR, changelog
