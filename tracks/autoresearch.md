---
title: Autoresearch
question: Can coding agents run AI verification experiments in a loop and produce findings that hold up under human review?
status: open
---

## Why it matters

Every team in the organisation is short of time. If an agent can run the routine part of an experiment (try a change, measure it, keep or revert, write it down) and humans only review, each track moves faster and negative results get recorded instead of forgotten.

## Approaches

| Project | Approach | Status |
|---|---|---|
| [autoresearch](../projects/autoresearch.md) | A research loop against one project and one metric, after Karpathy's autoresearch, and a workflow loop that proposes changes to the organisation's own rules | scaffold |

## What we know

No findings yet.

## Open questions

- Which verification metric can a loop optimise without learning to weaken the check behind it?
- How much review does one loop's output cost a human, and does it beat doing the runs by hand?
- Can a workflow loop improve `AGENTS.md`, templates and workflows from review friction without drifting from what the teams want?

## Sources

- [Karpathy, autoresearch](../sources/karpathy-autoresearch.md)
