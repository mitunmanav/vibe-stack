# Sorting Rules (`TRIAGE-RULES.md`)

Run the four tests in order. The first test that fires decides the bucket.

## The tests

1. **Fact test.** Could the project files, the running app, the docs of a tool, or a quick search settle this without anyone's preference? Then go and find out. Examples: "Does the project already save things to a file?", "Does this service have a free tier?".
2. **One-way door test.** Ask of every possible answer, not just your favourite: would it spend or commit money; collect, store, show, or send private information; change who can log in, see, or change what; put a person's safety at risk; need an outside account, key, or signed agreement; delete, overwrite, or reshape data people already saved; or be hard to take back once real people use it? Any yes makes it a one-way door.
3. **Taste test.** Would any answer change what a person sees, clicks, types, waits for, receives, or is told; which rules the app enforces (who wins a clash, what counts as late); the words on screen; who the app is for; or what "finished" means? Any yes makes it a taste question.
4. **Build choice.** Nothing above fired. The choice is about how the app is put together, nobody outside can tell, and going back to a Save Point would undo it.

## When unsure

- Move it up, never down: unsure between build choice and taste question means taste question; unsure between taste question and one-way door means one-way door.
- Split mixed decisions. "Which database?" is a build choice, but "do we keep people's emails?" hiding inside it is a one-way door. Ask the hidden part on its own.
- A build choice the user asks about becomes a taste question at once. Explain it plainly and let them pick.
- A build choice whose effect turns out to be visible later (it made a page slow, it changed a message) is reopened as a taste question.

## Worked examples

| Open decision | Bucket | What happens |
| --- | --- | --- |
| Which test tool to use | Build choice | Pick the one the project already has, log it. |
| Folder layout for the code | Build choice | Follow the project, log it. |
| What a person sees when the slot they want is taken | Taste question | Ask with a two-person story and a recommendation. |
| Whether the list shows newest or oldest first | Taste question | Ask, or show both with "showing-options". |
| Saving sign-up names and phone numbers | One-way door | Say who could see them and for how long, then ask. |
| Sending email reminders through an outside service | One-way door | Say it needs an account and may cost money, then ask. |
| Clearing old entries when the format changes | One-way door | Say what will be lost, then ask. |
