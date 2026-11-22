# Check Examples

Written in a Playwright-like style; translate to the project's own check runner.

## Good: through the page, an expected value from the plan

```typescript
test("an Owner can book a free slot and sees the price", async ({ page }) => {
  await page.goto("/book");
  await page.getByRole("button", { name: "Tue 3:00 pm" }).click();
  await page.getByRole("button", { name: "Add a second slot" }).click();
  await expect(page.getByText("Total: $30")).toBeVisible();
});
```

What makes it good:

- It does what a person does: open a page, click, read the screen.
- `$30` comes from the plan's worked example (2 slots at $15), not from the code.
- It survives any rewrite of the code behind the page.
- Its name says _what_ a person can do, not _how_ the code does it.

## Good: saved data read back through the app

```typescript
test("a Booking is still there after a reload", async ({ page }) => {
  await page.goto("/book");
  await page.getByRole("button", { name: "Tue 3:00 pm" }).click();
  await page.getByRole("button", { name: "Confirm" }).click();
  await page.reload();
  await expect(page.getByText("Your Booking: Tue 3:00 pm")).toBeVisible();
});
```

## Bad: reads the database behind the app's back

```typescript
test("booking saves a row", async () => {
  await createBooking({ slot: "tue-15" });
  const row = await db.query("SELECT * FROM bookings WHERE slot = ?", ["tue-15"]);
  expect(row).toBeDefined();
});
```

It passes while the page still shows nothing, and breaks when the storage changes but the app still works. Read the Booking back through the page instead.

## Bad: recomputes its own answer

```typescript
test("total adds up", () => {
  const slots = [{ price: 15 }, { price: 15 }];
  const expected = slots.reduce((sum, s) => sum + s.price, 0);
  expect(totalFor(slots)).toBe(expected);
});
```

The expected value is computed the way the code computes it, so it can never disagree. Use the literal: `expect(totalFor(slots)).toBe(30)`.

## Bad: counts calls

```typescript
test("checkout calls the payment helper", async () => {
  const spy = vi.spyOn(payments, "charge");
  await checkout(cart);
  expect(spy).toHaveBeenCalledTimes(1);
});
```

It tests how the code is wired, not what the Owner sees. Check the confirmation on screen, with a stand-in for the payment provider only (see `STAND-INS.md`).
