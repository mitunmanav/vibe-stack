# Changelog

## 1.1.0

### Minor Changes

- **`/what-next`** is the new router: where your project stands, and the one command to type next, including whether to type `/clear` first. People coming back after a break had to know that `/plain-english` also did this, and most didn't.
- **`/plain-english`** now only re-explains the last message, so it stays short enough to use in the middle of any other command.
- **`/ask-me`** now runs two background skills: `clarifying` (the interview) and the new **`keeping-words`**, which owns the wordbook and the decision log. The wordbook holds words and meanings only; rules moved to the plan, where the review checks them.
- New background skill **`connecting-services`**: a click-by-click guide through outside-service setup, checked stage by stage. `/build-step` used to reach into `/launch-check`'s folder for it, which breaks once a harness copies skills apart.
- `/repair` shows its ranked theories to you before testing them, handles slow problems by measuring first, and ends on a checklist.
- `auditing-work` carries a plain smell list for the Standards helper, and both helpers run in the foreground with their reports used as returned.
- `checking-behavior` gained worked examples of good and bad checks, and rules for what may be faked.
- `/tidy-up` looks at the parts of the app that keep changing first.
- Every command and background skill has a plain-words docs page in `docs/`.
- Both plugin manifests now list every skill by name. The Codex manifest was missing `/tidy-up` and `/look-back`.

## 1.0.0

First public release.

* Eight commands for building an app in plain words: `/start-project`, `/ask-me`, `/freeze-plan`, `/build-step`, `/repair`, `/launch-check`, `/plain-english`, `/undo`.
* Two beta commands: `/tidy-up` (tidies the code while every check stays green) and `/look-back` (offers guardrails after a step or repair that went badly).
* Four background skills: `clarifying`, `showing-options`, `checking-behavior`, `auditing-work`.
* Install from GitHub through the Claude Code plugin catalog or `npx skills@latest add mitunmanav/vibe-stack`.
