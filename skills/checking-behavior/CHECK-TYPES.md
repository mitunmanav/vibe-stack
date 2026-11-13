# Check Types (`CHECK-TYPES.md`)

Every check recorded in a step file or Demo Card carries one plain line on what it catches and one on what it misses, so the user knows why their own 30-second click-through still matters.

| Check | Catches | Misses (the user's click-through judges this) |
| :--- | :--- | :--- |
| **Click-through check** (headless browser on the real page) | Dead buttons, blank screens, form errors, missing text. | Whether the spacing, colours, and wording feel right. |
| **Save-and-reload check** (save through the app, reload, read it back) | Things not saving, vanishing on reload, or breaking a rule in `.vibe/WORDS.md`. | Whether the form felt long or confusing. |
| **Privacy check** (visit as a stranger or another user) | Private items visible to the wrong person, secret keys shipped to the browser. | Whether the "not allowed" message sounds polite. |
