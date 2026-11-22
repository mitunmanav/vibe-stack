# Feature Plan Template

Write `.vibe/specs/<feature-slug>.md` in the user's words.

<plan-template>

```markdown
# Feature Plan: <plain title>

## What Problem This Solves
<Two or three plain sentences, from the user's side: who this is for and what it lets them do.>

## What People See and Do
1. <One numbered line per thing a person can see or do, in the words from .vibe/WORDS.md.>

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

</plan-template>

"What People See and Do" is a long list: every action and every screen state the conversation settled, including the empty, refused, and error cases. It is the checklist `auditing-work` holds the build against, so a missing line is a missing feature.

Leave out code and file paths: they go stale fast, and the user cannot check them. The one exception is a flow simulator from `showing-options` whose rules settled a decision more precisely than words can: link the preview and name the rule it proved.
