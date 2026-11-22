# Plans, steps, and decisions live as files in `.vibe/`

Engineering skill sets usually publish plans and work items to an issue tracker. The people Vibe Stack serves have no tracker and should not need an account to start, so every plan, Playable Step, preview, wordbook, and decision log is a plain file in the project's `.vibe/` folder, tracked by git with the app.

A user can start in an empty folder with nothing but an AI assistant. The step files and git history are the whole record of where a project stands, which is also why there is no handoff command: a new chat reads `.vibe/` and `/what-next` says where things are.

`/undo` rewinds the app's files but leaves `.vibe/` alone. The plan and the decision log are the user's agreements, not the change being undone, and the commit guardrail in `.vibe/hooks/` must survive every undo.
