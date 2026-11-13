# Decision 0002: Plans, steps, and decisions live as files in `.vibe/`

* **Context:** Engineering skill sets usually publish plans and work items to an issue tracker. The people Vibe Stack serves do not have one and should not need an account to start.
* **Decision:** Every plan, Playable Step, preview, wordbook, and decision log is a plain file inside the project's `.vibe/` folder, tracked by git along with the app.
* **Consequences:** A user can start in an empty folder with nothing but an AI assistant. The step files and git history are the whole record of where a project stands, so no separate handoff note is needed to pick up tomorrow. Undo rewinds app files but leaves `.vibe/` alone, because the plan and the decision log are the user's agreements, not the change being undone.
