# Changelog

## Unreleased

* New background skill `translating`. Every open decision is sorted before you see it: the agent settles hidden build choices and logs them, everyday choices are asked plainly, and risky ones are asked as one-way doors with the consequence first.
* Every agent choice now goes in `.vibe/DECISIONS.md` with what you will notice, its risks, and how to change it. Changing an entry reopens the choices that depended on it.
* Saying "I don't understand" or "show me an example" during questions now gets a simpler explanation without changing the options.

## 1.0.0

First public release.

* Eight commands for building an app in plain words: `/start-project`, `/ask-me`, `/freeze-plan`, `/build-step`, `/repair`, `/launch-check`, `/plain-english`, `/undo`.
* Two beta commands: `/tidy-up` (tidies the code while every check stays green) and `/look-back` (offers guardrails after a step or repair that went badly).
* Four background skills: `clarifying`, `showing-options`, `checking-behavior`, `auditing-work`.
* Install from GitHub through the Claude Code plugin catalog or `npx skills@latest add mitunmanav/vibe-stack`.
