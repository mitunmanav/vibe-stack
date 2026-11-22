# Flow Simulator

A page where the user drives the rules of a feature by pressing buttons and watching what happens. The moments that matter are "wait, that should not be allowed" and "huh, I assumed it would do X": those are the mistakes in the _idea_, found before any of it is built.

## The rules: a small, liftable script block

Put the rules in one `<script>` block, written so they could move into the real app once agreed. Pick the shape the question needs, not the one easiest to wire to buttons:

- **Plain functions over plain data**, when there is no "current situation", just calculations (prices, splits, dates).
- **A step function** `(situation, action) => new situation`, when things happen one event at a time.
- **A small state machine** (named states, allowed moves), when "what can I even do right now" is part of the question.

The rules never touch the page: no `document`, no button handlers inside them. The page calls the rules; nothing flows back.

## The page, top to bottom

1. **The question** and one plain line on what this page lets you explore.
2. **What is true right now:** the full current situation in labelled, plain words (never raw data), redrawn after every press, with the thing that just changed highlighted.
3. **Free-play buttons:** one per action a person can take ("Send Invite", "Claim Spot", "Skip Ahead 7 Days"), always available, in any order.
4. **Story tabs:** the normal path, an awkward edge case, an attempt at something that should be refused, and any story the interview raised. Each tab tells its story in one plain sentence and lists its steps as buttons to press in order. Opening a tab resets to the same starting point, so a story plays the same way every time.

Use the words from `.vibe/WORDS.md` on every button and label. Keep the look calm: clear text, plenty of space, one accent colour, no animation.

When the user asks for a new action or story, add it: previews grow as the idea does.
