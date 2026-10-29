# Visual Layout Options Guide (`VISUAL-OPTIONS.md`)

Build a single self-contained HTML file in `.vibe/previews/<slug>-options.html` with zero external build steps required:

1. **Top Switcher Bar:** Render a fixed bar at the top of the page with buttons for **Option A**, **Option B**, and **Option C** (also switchable via `?option=a`, `?option=b`, `?option=c`), plus a 1-sentence label explaining the vibe of each option:
   * **Option A (Calm & Minimal):** High whitespace, focused single-column or airy cards, warm neutral palette.
   * **Option B (Compact & Action-Dense):** High information density, quick-filter bar, side-by-side summary metrics.
   * **Option C (Bold & Expressive):** Strong typography, high-contrast feature cards, guided step callouts.
2. **Real Project Words:** Use the exact everyday nouns from `.vibe/WORDS.md` and realistic sample items (never `Lorem ipsum` or `foo/bar`).
