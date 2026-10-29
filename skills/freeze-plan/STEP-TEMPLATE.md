# Playable Step Template (`STEP-TEMPLATE.md`)

Write each step to `.vibe/steps/<feature-slug>/<NN>-<step-slug>.md` (`01`, `02`, etc.) ordered so Step 01 works on its own before Step 02 begins:

```markdown
# Step <NN>: <Plain-English Title>

* **Status:** TODO
* **Parent Plan:** `.vibe/specs/<feature-slug>.md`
* **Save Point Tag:** `restore/<feature-slug>-<NN>`

## 1. What You Will Be Able to Try After This Step
<1 to 2 plain sentences describing the visible buttons, screen, or action the user can try.>

## 2. Try-It-Yourself Checklist (30 Seconds)
1. Open the app and <action 1> -> you should see <result 1>.
2. Click <action 2> -> you should see <result 2>.

## 3. Automated Self-Checks (Agent Only)
* **Check 1:** <Behavioral check to run red-before-green>
  * *Catches:* <1 line on what broken behavior this catches>
  * *Misses:* <1 line on what visual/human nuance the user still checks>
```
