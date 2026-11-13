---
name: undo
description: "Take the app back to a Save Point when a change went wrong. Your plan and decisions are kept, and the undo itself can be undone."
argument-hint: "[optional: which Save Point, e.g. 'before step 02']"
disable-model-invocation: true
---

# Undo

Bring the app's files back to a Save Point without losing anything for good.

## 1. Pick the Save Point

List the three newest Save Points (`git tag --list 'restore/*' --sort=-creatordate`), each with its date and, in plain words, what came right after it (read from the step file or the commit message). If the user named one after the command, match it. List in plain words every step and repair that going back will remove (`git log --oneline <tag>..HEAD`). Ask:

```markdown
❓ **Q1** - **Go back**: Take the app back to how it was <plain description, e.g. "just before Step 02 was built">? This removes <the steps and repairs listed above>.
➡️ Yes, go back. (Your plan and decisions stay as they are, and you can undo this undo later.)
```

Wait for a yes.

## 2. Go back by moving forward

1. Commit anything not yet saved (`git add -A`, message "Saved before undo"), so nothing is lost.
2. Bring back every file except `.vibe/` as it was at the Save Point: `git restore --source=<tag> --staged --worktree -- . ':!.vibe'`. This also removes files created after it.
3. Set any step built after the Save Point back to `Status: TODO` in its step file.
4. Commit ("Undo: back to <tag>").

History keeps every earlier version, so this undo is a two-way door: the commit before it can always be restored the same way.

Done when `git status` is clean, the app starts, and its files match the Save Point (`git diff <tag> -- . ':!.vibe'` shows nothing).

## 3. Tell the user

Say in one plain sentence how the app is now, and the command to type next (usually `/build-step` to try the step again, or `/ask-me` to rethink it).
