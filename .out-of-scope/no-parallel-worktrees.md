# Building several steps at once

Vibe Stack builds one Playable Step at a time. Requests to run several builders in parallel, each in its own branch or worktree, and merge the results are out of scope.

## Why this is out of scope

Parallel builders working on one app edit the same files, and their changes collide. Untangling a merge conflict means reading code, which is the one thing the people Vibe Stack serves cannot do, and `SCOPE.md` rules out ever handing it to them.

One step at a time also keeps the user in the loop where it matters: each step ends in a Demo Card they click through before the next one starts. A fast build of five steps nobody tried is slower than five steps that each work.

`/repair` does copy the app into a scratch folder to compare old Save Points, but it only reads there, and removes the copy before it finishes.

## Prior requests

None yet.
