# Flow Simulator (`FLOW-SIMULATOR.md`)

A page where the user drives the rules of a feature by pressing buttons and watching what happens. It finds the mistakes in the idea itself ("wait, that should not be allowed") before any of it is built.

1. **Rules in one small script block** written as plain functions over plain data (or a small state machine), with no page code inside them. The page calls the rules; nothing in the rules touches the page. Built this way, the rules can move into the real app once they are agreed.
2. **What is true right now:** a panel showing the full current state in labelled, plain words (never raw data), redrawn after every click, with the thing that just changed highlighted.
3. **Free-play buttons:** one button per action a person can take ("Send Invite", "Claim Spot", "Skip Ahead 7 Days"), always available, in any order.
4. **Story tabs:** two to four scenarios, one per tab: the normal path, an awkward edge case, and an attempt at something that should be refused. Each tab explains the story in one plain sentence and lists its steps as buttons to press in order. Opening a tab resets to the same starting point, so a story plays the same way every time.

Keep the look calm: clear text, plenty of space, one accent colour, no animation.
