---
name: tidy-up
description: "Beta. Keep your app easy to change: tidy the code behind the scenes, change nothing you see, and prove every check still passes."
disable-model-invocation: true
---

# Tidy Up

Each step is reviewed on its own, so mess that builds up across steps goes unseen. This command finds **deepening** opportunities (places where a shallow module could become a **deep module**: a lot of behaviour behind a small interface) and refactors them while every Automated Check stays green. Nothing the user sees changes.

## 1. Start from green

If `.vibe/config.md` is missing, tell the user to type `/start-project`, and stop. If `git status` shows a step left half-built, tell the user to finish it with `/build-step` or drop it with `/undo`, and stop.

Run the check command. If it is red, tell the user to type `/repair` with what failed, and stop: tidying needs a green start to prove it broke nothing.

Tag the current commit `restore/tidy-<YYYYMMDD-HHMM>`.

## 2. Survey where it pays

Tidying pays off by making the next change easier, so weight the parts that keep changing. Read `git log --stat` back across recent Save Points to find the **hot spots**: the files that keep coming up. If the user typed an area after the command, take that instead.

Start a helper in a fresh context window. Give it the hot spots, the app's folders, `.vibe/WORDS.md`, and this brief: read the code (not a diff), hot spots first, and report tidy-up candidates, most valuable first:

- understanding one thing means bouncing between many small files;
- a **shallow module**: its interface is nearly as big as what it hides. Apply the deletion test: would deleting it gather the complexity in one place, or just move it?
- the same logic written out in more than one place;
- one file doing several unrelated jobs;
- behaviour that no check reaches through a seam;
- dead code;
- names in the code that differ from `.vibe/WORDS.md`.

For each: the files involved, and one line on what becomes easier to change.

## 3. Refactor one candidate at a time

Take the candidates in order. For each:

1. If no check covers the behaviour it touches, call the Skill tool with "checking-behavior" and write one first, forcing the red.
2. Change the structure and keep the behaviour identical.
3. Run the check command. Green: commit ("Tidy: <what>"). Red: undo the whole candidate (`git restore`) and move to the next.

Every choice here is a technical two-way door: decide it yourself. A candidate that would change what people see or what is saved is a new idea: leave the code alone and list it for the user to take to `/ask-me`.

Done when every candidate is committed, skipped with a reason, or listed as an idea.

## 4. Review and report

Call the Skill tool with "auditing-work", naming the Save Point from step 1 and every plan in `.vibe/specs/`.

Tell the user in plain words: what is now easier to change, that every check passed before and after, that nothing on screen changed, and that `/undo` takes the tidy-up back.
