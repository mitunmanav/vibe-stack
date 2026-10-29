# Session Handoff Note Template (`HANDOFF-TEMPLATE.md`)

Write `.vibe/handoff.md` using pointers to existing files (never copy-paste entire spec files into the handoff note, and never include secret keys):

```markdown
# Session Handoff Note (`.vibe/handoff.md`)

* **Saved on:** YYYY-MM-DD HH:MM
* **Where we stopped:** <1 plain sentence>
* **Active plan file:** `.vibe/specs/<slug>.md`
* **Last completed step:** `.vibe/steps/<slug>/<NN>.md` (`DONE`)
* **Next step to build:** `.vibe/steps/<slug>/<NN+1>.md` (`TODO`)
* **Latest working Save Point:** `restore/<slug>-<NN>`
* **Exact command to type in your next chat:** `/build-step <NN+1>`
```
