---
title: Red team
question: Can agents find what breaks a verification design, experiment or prototype before anyone relies on it?
status: open
---

## Why it matters

A verification mechanism is only as good as the best attack anyone has tried on it. Teams test their own mechanisms against the cheating strategies they thought of. Agent-run red teaming can try more of them, on every commit, and record what held as well as what broke.

## Approaches

| Project | Approach | Status |
|---|---|---|
| [redteam](../projects/redteam.md) | Scoped engagements: agents restate the claim and threat model, rank candidate attacks by class, try them, and confirm every break with a reproduction | scaffold |

## What we know

No findings yet.

## Open questions

- Can an agent tell a real break from a plausible-sounding one without a human rerunning it?
- Which attack classes do agents find well (permissive verifiers, measurement confounds) and which do they miss (cryptographic soundness)?
- How to disclose a break in a system outside the organisation, and to whom, without slowing the open work down.

## Sources

None yet.
