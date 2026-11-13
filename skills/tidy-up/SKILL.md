---
name: tidy-up
description: "Beta. Keep the app easy to change: take a Save Point, tidy the code behind the scenes without changing anything you see, and prove every check still passes."
disable-model-invocation: true
---

# Tidy Up

Each step is reviewed on its own, so mess that builds up across steps goes unseen. This command surveys the whole app and refactors it while every Automated Check stays green. Nothing the user sees changes.

## 1. Start from green

Read `.vibe/config.md`; if it is missing, tell the user to type `/start-project`, and stop. If `git status` shows a step left half-built, tell the user to finish it with `/build-step` or drop it with `/undo`, and stop.

Run the check command. If it is red, tell the user to type `/repair` with what failed, and stop: tidying needs a green start to prove it broke nothing.

Tag the current commit `restore/tidy-<YYYYMMDD-HHMM>`.

## 2. Survey the whole app

Start a helper in a fresh context window. Give it the app's folders, `.vibe/WORDS.md`, and this brief: read the whole app (not a diff) and report tidy-up candidates, most valuable first:

- the same logic written out in more than one place;
- one file doing several unrelated jobs;
- a shallow module, whose interface is as big as what it hides, that could become a deep module behind a small interface;
- behaviour that no check reaches through a seam;
- dead code;
- names in the code that differ from `.vibe/WORDS.md`.

For each: the files involved and one line on what becomes easier to change.

## 3. Refactor one candidate at a time

Take the candidates in order. For each:

1. If no check covers the behaviour it touches, call the Skill tool with "checking-behavior" and write one first, forcing the red.
2. Change the structure and keep the behaviour identical.
3. Run the check command. Green: commit ("Tidy: <what>"). Red: undo the whole candidate (`git restore`) and move to the next.

Every choice here is a technical two-way door: decide it yourself. A candidate that would change what people see or what is saved is a new idea, so leave the code alone and list it for the user to take to `/ask-me`.

Done when every candidate is committed, skipped with a reason, or listed as an idea.

## 4. Review and report

Call the Skill tool with "auditing-work", naming the Save Point from step 1 and every plan in `.vibe/specs/`.

Tell the user in plain words: what is now easier to change, that every check passed before and after, that nothing on screen changed, and that `/undo` takes the tidy-up back.
