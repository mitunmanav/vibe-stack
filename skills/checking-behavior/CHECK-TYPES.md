# Automated Check Types and Blind Spots (`CHECK-TYPES.md`)

For every check recorded in a step file or Demo Card, state in one plain line **what it catches** and **what it misses** so the human knows why their 30-second click test still matters:

| Check Type | What It Catches Automatically | What It Misses (Human Checks in 30s Demo) |
| :--- | :--- | :--- |
| **Browser Click Check** | Broken buttons, blank screens, form errors, and missing text on the page. | Whether the visual spacing, colors, and wording feel pleasant to a real person. |
| **Saved-Data Roundtrip Check** | Items failing to save, disappearing on page reload, or breaking rules in `.vibe/WORDS.md`. | Whether the form felt too long or confusing to fill out. |
| **Safety & Access Check** | Private items leaking to uninvited visitors or secret keys appearing in browser files. | Whether the warning message shown to a blocked visitor sounds polite. |
