---
name: auditing-work
description: "Two-axis review of everything changed since a Save Point, run by two fresh helpers: Safety & Standards, and Plan. Use when a step is built, a repair is done, or the app is about to launch."
user-invocable: false
---

# Auditing Work

The agent that built a change is the worst judge of it: its window is full of the reasons the code looks right. Review it from two fresh windows, along two axes that stay apart, because a change can follow every standard and still build the wrong thing, or build exactly the right thing badly.

## 1. Pin the fixed point

The caller names the Save Point to review from (a step's `restore/...` tag, a repair's tag, or `restore/project-start` for the whole app). Stage everything so new files are included (`git add -A`), then capture the diff once: `git diff --staged <save-point>`. Done when the tag resolves and the diff is not empty; stop and say so if either fails.

## 2. Run both helpers

Start two helpers together, each in a fresh context window, and wait for both reports.

**Safety & Standards helper.** Give it the diff command, `.vibe/STANDARDS.md` if it exists (report every breach of it), and this brief: report every place the change

- puts a secret key or token in a tracked file or in code sent to the browser, or leaves a `.env` file outside `.gitignore`;
- shows one person's private information to anyone else;
- leaves debug leftovers (`[TRACE-` lines, stray console output, commented-out code);
- carries a check that cannot fail: one that tests a stand-in instead of the app, or recomputes its own expected value;
- has duplicated logic, dead code, a name that hides what it holds, one file doing several unrelated jobs, or machinery for needs the plan does not have.

Quote the lines for each finding and mark it **must fix** (secrets, privacy, a check that cannot fail) or **judgement call** (the rest). Under 400 words.

**Plan helper.** Give it the diff command, the plan in `.vibe/specs/`, the step file if the caller named one, `.vibe/WORDS.md`, and `.vibe/DECISIONS.md`, and this brief: for every item in the step file (if given) and the plan's "What People See and Do", say whether it is built, partly built, or missing; list anything built that the plan did not ask for; list every label, button, or message on screen that uses a different word from `.vibe/WORDS.md`. Quote the plan line for each finding. Under 400 words.

## 3. Act on the reports

Keep the two reports separate; never merge or rerank them across axes.

- Fix every Safety & Standards finding yourself, rerun the checks after each fix, and undo any tidy-up that turns a check red. Tell the user about a finding only when fixing it needs their decision (a one-way door).
- Build anything the Plan helper found missing or partial, and remove anything built that was not asked for. Fix every wording mismatch.

Done when both helpers' must-fix and missing items are resolved and every check is green. Give the caller one plain line per axis: what was found and what was fixed.
