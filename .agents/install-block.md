# The Install Block

One install story, one wording. `README.md` copies these commands exactly. Change them here first, then copy them across.

Routes marked _not yet run_ follow the tool's documented form but have not been tried against this repo. Remove the mark once someone has run it.

## Claude Code

```text
/plugin marketplace add mitunmanav/vibe-stack
/plugin install vibe-stack@vibe-stack-catalog
```

## Any other assistant (Codex, Cursor, Copilot, Gemini CLI, OpenCode, and more)

```bash
npx skills@latest add mitunmanav/vibe-stack
```

To update later, run `npx skills@latest update`.

## Gemini CLI, without npx (_not yet run_)

```bash
gemini skills install https://github.com/mitunmanav/vibe-stack.git --path skills
```

Pick one route per assistant. Installing two gives you every command twice.
