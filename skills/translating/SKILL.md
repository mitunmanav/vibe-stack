---
name: translating
description: "Sorts each open decision before the user sees it: hidden build choices settled and logged, everyday choices asked plainly, and risky ones asked as one-way doors. Use when any skill is about to ask the user something or decide for them."
user-invocable: false
---

# Translating

Stand between the design tree and the user. Every open decision passes through here before anyone answers it, so each branch still gets settled, by the right person, and leaves a trace in `.vibe/DECISIONS.md`.

## 1. Sort the decision

Read `TRIAGE-RULES.md` and put the decision in exactly one bucket. The tests run in order and the first that fires wins:

1. **Fact**: the project, the running app, docs, or a look online can settle it. Start a helper in a fresh context window and have it look. Not a decision; record it only when a choice rests on it.
2. **One-way door**: any answer could cost money, touch private information, change who can see or do what, put someone at risk, need an outside account, delete or reshape saved data, or be hard to take back once real people use it.
3. **Taste question**: any answer changes what people see, click, type, wait for, receive, or are told, which rules the app keeps, what words it uses, or who it is for.
4. **Build choice**: everything else. It is invisible from outside and a Save Point can undo it.

Done when the decision sits in one bucket and, if it mixes a hidden part with a visible effect, it has been split into two decisions.

## 2. Act on the bucket

- **Build choice**: decide it yourself with the simplest reliable option, and log it (step 3). Add it to the line `Choices I made for you this round:` that closes the round, in everyday words.
- **Taste question**: word it with `QUESTION-GUIDE.md`. Lead with your recommendation so "yes" accepts it, give an example or a short story from the user's world, and invite their own words. When seeing beats reading, call the Skill tool with "showing-options".
- **One-way door**: open with `⚠️ **Why this matters:**` and the real-world result (cost, who sees what, what cannot be undone), then the question, then your recommendation. Only a clear yes to this exact question counts.

When the user is not in the conversation (a helper, a run nobody is watching), write taste questions and one-way doors into `.vibe/LATER.md` and wait. Never answer them on the user's behalf.

Done when every build choice is logged and every other decision is either asked or parked.

## 3. Log it

After each answer, and right away for each build choice, add an entry to `.vibe/DECISIONS.md` in the shape `DECISION-LOG-FORMAT.md` gives. Settled words go to `.vibe/WORDS.md` the moment they settle, in the shape `WORDBOOK-FORMAT.md` gives.

When the user changes an entry, re-sort the change (it may now be a one-way door), mark the old entry `SUPERSEDED BY D-NN`, add the new one, and reopen every entry that lists the old one under `Depends on`. Reopened decisions go back into the next round.

Done when nothing decided in this round is missing from the log.

## When the user is lost

When the user says they don't follow, asks for another way to put it, wants an example, or asks what a choice leads to, read `LOST.md`. Simplify the wording; keep the options and your recommendation the same.
