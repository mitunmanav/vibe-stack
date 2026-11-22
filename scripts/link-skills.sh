#!/usr/bin/env bash
set -euo pipefail
# Links all Vibe Stack skills into ~/.claude/skills and ~/.agents/skills for local use.
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
for target_root in "$HOME/.claude/skills" "$HOME/.agents/skills"; do
  mkdir -p "$target_root"
  for skill_dir in "$REPO_DIR"/skills/*/; do
    skill_name="$(basename "$skill_dir")"
    ln -sfn "$skill_dir" "$target_root/$skill_name"
  done
done
echo "Linked Vibe Stack skills into ~/.claude/skills and ~/.agents/skills."
