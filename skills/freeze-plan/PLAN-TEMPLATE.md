# Feature Plan Template (`PLAN-TEMPLATE.md`)

Write `.vibe/specs/<feature-slug>.md` in the user's words. Leave out code and file paths: they go stale, and the user cannot check them.

```markdown
# Feature Plan: <plain title>

## What Problem This Solves
<Two or three plain sentences: who this is for and what it lets them do.>

## What People See and Do
* <One line per thing a person can see or do, using the words from .vibe/WORDS.md. List every one; this is the checklist the build is audited against.>

## Rules That Always Hold
* <One line per rule, e.g. "A guest pass can be claimed only once.">

## How We Check It Works
* <One line per Automated Check, in plain words.>

## Not Part of This Plan
* <Anything discussed and left out, so nobody builds it by accident.>

## Previews and Decisions
* Previews: <links to .vibe/previews/ files, or "None">
* Decisions: <D-NN ids from .vibe/DECISIONS.md>
```
