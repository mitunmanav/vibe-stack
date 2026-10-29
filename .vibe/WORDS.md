# Project Wordbook (`.vibe/WORDS.md`)

**Purpose:** Maps the everyday words you use to what they mean in your project so you and the agent never use different words for the same thing.

## Everyday Words We Use

| Everyday Word | What It Means in Plain Words | Rules It Always Follows | Agent Code Mapping (Agent Only) |
| :--- | :--- | :--- | :--- |
| **Playable Step** | One small slice of your app that you can see and click in your browser as soon as it is built. | Every step must work on its own before the next step starts. | `.vibe/steps/<slug>/<NN>-<step>.md` |
| **Save Point** | A safety snapshot created automatically before the agent edits any code so you can undo mistakes in one step. | Created before every `/build-step` and `/repair` run. | Git tag `restore/<slug>-<NN>` |
| **Demo Card** | A simple page opened in your browser after a step finishes, listing 3 things to click and try yourself. | Must show automated check receipts alongside the human try-it list. | `.vibe/previews/demo-<NN>.html` |
| **One-Way Choice** | A decision that costs money, affects privacy, connects an outside account, or deletes saved information. | Agent must explain the real-world consequence and ask you before acting. | Logged in `.vibe/DECISIONS.md` as `HUMAN APPROVED` |

## Words We Avoid (Retired Synonyms)

* **Ticket / Issue / PR / Pull Request:** Say **Playable Step** or **Launch Check** instead.
* **Commit / Branch / Worktree / Stash:** Say **Save Point** or **Undo** instead.
* **Unit Test / Seam / Mock / Assertion:** Say **Automated Check** instead.
