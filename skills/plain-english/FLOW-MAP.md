# Flow Map and Chat Memory Guide (`FLOW-MAP.md`)

Tell the user where they are on this map in one sentence, and advise whether to **keep going in this chat** or **type `/clear` first** (so the AI stays fast and sharp):

| Where You Are Right Now | Exact Command to Type Next | Should You Type `/clear` First? |
| :--- | :--- | :--- |
| Brand new folder, no `.vibe/` setup yet | `/start-project` | No - run it right here. |
| Have a rough idea or feature in mind | `/ask-me` | Yes, if the current chat is long and cluttered. |
| Finished `/ask-me` and agreed on the idea | `/freeze-plan` | **No - stay in this chat** so `/freeze-plan` can read what you just agreed on! |
| Plan and playable steps are saved in `.vibe/steps/` | `/build-step 01` | **Yes - type `/clear` first** so the builder starts with a clean, fast memory window. |
| A button or screen is acting broken | `/repair` | Yes, if the chat is already long. |
| Want to undo the last change or pause for today | `/undo` | No - run `/undo` first, then `/clear`. |
| All playable steps work and you want to launch | `/launch-check` | Yes - type `/clear` first for a fresh safety scan. |
