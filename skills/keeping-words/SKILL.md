---
name: keeping-words
description: "Build and sharpen a project's shared words and decision log. Use when a word for a screen, person, or thing is unclear or clashes, or when a choice should be recorded or changed."
user-invocable: false
---

# Keeping Words

Actively build the project's shared language while you shape it: challenge words, stress-test them with small stories, and write the wordbook and the decision log down the moment something settles. This is the _active_ discipline. Reading `.vibe/WORDS.md` to borrow its words is a one-line habit any skill has; reach for this skill when the words or the decisions are changing.

Both files live in `.vibe/`. Create each lazily: `.vibe/WORDS.md` when the first word settles, a `.vibe/DECISIONS.md` entry when the first choice qualifies.

## During the conversation

### Challenge against the wordbook

When the user says a word that clashes with `.vibe/WORDS.md`, call it out at once: "Your wordbook says a **Booking** is one 30-minute slot, but you seem to mean a whole day. Which is it?"

### Sharpen fuzzy words

When one word is doing two jobs, or two words name one thing, propose one plain word for each thing: "You've said 'customer' for the dog owner and for the groomer. Can we call them **Owner** and **Groomer**?"

### Stories at the edges

When a rule is being discussed, test it with a small story from the user's own world, picked to land on the boundary: "Sam books the 3pm slot, then Priya tries to book it too. What should Priya see?" Stories surface the rules a description skips.

### Cross-check with the app

When the user says how something works today, check whether the app agrees. Surface any mismatch in plain words: "Right now the app lets anyone cancel a whole day of bookings, but you just said only the groomer can. Which is right?"

### Write words down as they settle

When a word settles, write it into `.vibe/WORDS.md` right then, using `WORDBOOK-FORMAT.md`. Capture each one as it happens. The wordbook holds words and their meanings only: rules go in the plan, and file names stay out entirely.

### Record decisions sparingly

Write every answer the user gives into `.vibe/DECISIONS.md` with `Decided by: USER` after each round, so closing the chat loses nothing.

Record a choice you made yourself (`Decided by: AGENT`) only when both are true:

1. **Surprising later**: the user would look at the app and wonder why it works that way.
2. **Real work to change**: flipping it later costs more than a quick edit (moving saved data, rebuilding a screen).

Read `DECISION-FORMAT.md` before writing any entry. When the user changes an earlier choice, follow its rule for superseding.
