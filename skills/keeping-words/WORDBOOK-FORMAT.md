# Wordbook Format

`.vibe/WORDS.md` holds this project's everyday words, in the user's own language.

<wordbook-template>

```markdown
# <Project name> Wordbook

<One or two plain sentences: what the app is for and who uses it.>

## Words We Use

**Booking**:
One 30-minute grooming slot that an Owner has claimed.
_Avoid_: appointment, reservation

**Owner**:
A person who brings a dog in and makes Bookings.
_Avoid_: customer, client, user

## How They Fit Together

- An **Owner** can hold many **Bookings**
- A **Booking** belongs to exactly one **Groomer**

## Words We Cleared Up

- "customer" was used for both the Owner and the Groomer. Settled: they are **Owner** and **Groomer**.
```

</wordbook-template>

## Rules

- **Be opinionated.** When several words exist for one thing, pick the clearest and list the rest under `_Avoid_`.
- **Keep meanings tight.** One or two plain sentences: what the thing _is_, not how the app handles it.
- **Only this project's words.** Everyday words ("button", "page", "email") stay out, even when the app uses them everywhere.
- **Words only.** Rules ("a slot can be booked once") belong in the plan's "Rules That Always Hold". File and code names belong nowhere in this file.
- **Group under subheadings** once natural clusters appear; a flat list is fine until then.
