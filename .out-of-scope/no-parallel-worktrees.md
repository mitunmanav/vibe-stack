# Out of Scope: Parallel Multi-Branch Building

Vibe Stack builds one playable step at a time via `/build-step`. Running multiple background coders in parallel git worktrees creates merge conflicts on shared files that non-technical users cannot untangle.
