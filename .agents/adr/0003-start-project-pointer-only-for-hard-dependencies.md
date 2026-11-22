# The `/start-project` pointer appears only where it is load-bearing

Most commands depend on what `/start-project` sets up. Some cannot work without it: they need the start command, the check command, or the `.vibe/` folder to write into (`ask-me`, `freeze-plan`, `build-step`, `launch-check`, `tidy-up`, `look-back`). Those open with one line: if `.vibe/config.md` is missing, tell the user to type `/start-project` first, and stop. Without it, their output is wrong, not just less sharp.

Others only read `.vibe/` files to sharpen their words (`plain-english`, `what-next`), or depend on something else entirely (`undo` needs Save Points, `repair` takes its own). They mention `.vibe/` files in passing and still work when those files are missing. Keeping the pointer out of them keeps them short, and stops the pointer being copied into places where it changes nothing.
