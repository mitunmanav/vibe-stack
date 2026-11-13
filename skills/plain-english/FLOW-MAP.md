# Flow Map (`FLOW-MAP.md`)

The map of every command. Find the user's row from the state of the project, and give them its command.

| Where you are | Type next | `/clear` first? |
| :--- | :--- | :--- |
| No `.vibe/` folder yet | `/start-project` | No |
| Have an idea for something new or a change | `/ask-me` | Yes, if this chat is long or about something else |
| Closed the chat partway through `/ask-me` | `/ask-me` again. It reads your saved answers and carries on. | No |
| Just finished `/ask-me` and agreed on the idea | `/freeze-plan` | **No.** It reads what you just agreed in this chat. |
| Plan saved, a step is still `TODO` | `/build-step` | **Yes.** The builder works best from a fresh start. |
| A step was left half-built (unsaved changes) | `/build-step` to carry on, or `/undo` to drop it | No |
| Something is broken or acting weird | `/repair <what you saw>` | Yes, if this chat is long |
| You don't like the last change | `/undo` | No |
| Every step is `DONE` and you want to share the app | `/launch-check` | Yes |
| The last message made no sense | `/plain-english` | No |
| A step or repair went badly and you want it not to repeat | `/look-back` (beta) | **No.** It reads what happened in this chat. |
| Several steps are built and you want the app kept easy to change | `/tidy-up` (beta) | Yes |

**Stopping for the day:** just close the chat. Everything that matters is saved in `.vibe/` and the Save Points. Tomorrow, reopen this same chat if your assistant keeps chat history, or start a new one and type `/plain-english` to see where you are.
