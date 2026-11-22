# Playable Step Template

Write one file per step at `.vibe/steps/<feature-slug>/<NN>-<step-slug>.md`, numbered from `01` in build order. One step per file.

<step-template>

```markdown
# Step <NN>: <plain title>

* **Status:** TODO
* **Plan:** `.vibe/specs/<feature-slug>.md`
* **Builds on:** <Step NN, or "Nothing (start here)">

## What You Can Try After This Step
<One or two plain sentences about the screen, button, or action the user can try.>

## Try It Yourself (30 Seconds)
1. Open the app and <action> -> you should see <result>.
2. Click <action> -> you should see <result>.
3. <Reload, or try something that should be refused> -> you should see <result>.

## Automated Checks (agent only)
* **<check in plain words, with its worked example>**
  * *Catches:* <what broken behaviour this catches>
  * *Misses:* <what the user's own click-through still has to judge>
```

</step-template>

Describe what the user can do, never a layer-by-layer build list.
