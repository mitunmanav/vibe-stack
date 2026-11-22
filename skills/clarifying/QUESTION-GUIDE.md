# Wording Questions for the User

Ask about the world the user already knows: people, screens, buttons, money, and time. Under every technical question sits an everyday one; ask that one.

| The technical question | Ask this instead |
| :--- | :--- |
| How pieces of data relate | A story: "Can one person book for several friends at once, or one spot each?" |
| Where data is kept | "Will this be used on this one computer, or on several phones and computers?" |
| How people sign in | A one-way door: "Start with a simple passcode on this computer (free), or set up Google sign-in now?" |
| Whether to use a paid outside service | A one-way door with the price, recommending a free stand-in first. |

When a technical word slips into a draft question, rewrite the question rather than explaining the word. Keep each question to one decision. Write the recommended answer so the user can reply "yes" and mean it.

## A sheet for someone else

When the answer sits in another person's head (a client, a partner, a friend), interview the user about the **send**, which they can always answer, and leave the subject to the sheet.

1. **Who is it for?** Ask, in one round, who the person is and what they know that the user does not. That sets the sheet's tone and how much context it carries.
2. **What do you need back?** Ask, in one round, the exact choices or facts the user cannot settle alone. Done when you have a concrete list.
3. **Write the sheet** to `.vibe/questions-for-<name>.md`:

<question-sheet-template>

```markdown
# Questions for <name>

**Why I'm asking:** <one plain sentence: the choice riding on your answers>

## A little background
<One short paragraph for someone who was not in this chat.>

## How to answer
Write under each question. "I'm not sure" is a useful answer, so say it rather than skip.

## <Theme>

### <One question, about one thing>
_Why this matters: <only where the question could be misread>_

>

## Anything else?
Is there anything we should have asked?
```

</question-sheet-template>

Put the most important question first: the person may only answer once. Done when every item from step 2 has a question on the sheet. Tell the user where the file is; when the answers come back, they bring them to `/ask-me`.
