# Stand-Ins

Replace only what the project does not own. Everything the project owns runs for real.

| Replace with a stand-in | Run for real |
| :--- | :--- |
| Payment providers (always test mode or a fake) | The app's own pages, forms, and rules |
| Email and text-message senders | The app's own saved data (a throwaway copy is fine) |
| The clock and randomness | Any module the project wrote |
| Any outside service that bills or rate-limits | |

## Make the outside services easy to replace

**Pass the service in** rather than creating it deep inside the code, so a check can hand over a stand-in:

```typescript
// Easy to replace
function confirmBooking(booking, payments) {
  return payments.charge(booking.total);
}

// Hard to replace
function confirmBooking(booking) {
  const payments = new StripeClient(process.env.STRIPE_SECRET_KEY);
  return payments.charge(booking.total);
}
```

**One small function per outside action** (`charge`, `refund`, `sendReceipt`), not one general-purpose caller with branches inside. Each stand-in then returns one plain shape, and a reader can see which outside actions a check touches.

Never point a check at a live payment or a real inbox: that is a one-way door.
