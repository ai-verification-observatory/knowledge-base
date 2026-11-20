---
title: Proof of inference
question: What does it cost to prove that a reply is exactly what a committed model computes for a prompt, and what does each proof actually establish?
status: open
---

## Why it matters

Every reply from an AI service arrives on trust. A proof of inference lets anyone check, on an ordinary CPU and without the weights, that the reply came from the committed model. Several open provers now exist, but each reports on its own model, precision, hardware and clock boundaries, so their numbers cannot be read side by side.

## Approaches

| Project | Approach | Status |
|---|---|---|
| [inference-proofs](../projects/inference-proofs.md) | Open benchmark: fixed workload, pinned commits, six correctness gates before any cost is shown, public claim cards | active |

## What we know

No findings recorded here yet. Results live at [inferenceproofs.ai](https://www.inferenceproofs.ai), each with its model, hardware and claim card.

## Open questions

- How to put systems with different trust models (cryptographic proofs, sampling, recomputation, trusted hardware) on one scale.
- Soundness and weight secrecy are taken from each system's documentation. Who tests them adversarially?
- A proof binds a reply to committed weights. It does not show who owns the weights, that the proved reply was the one served, or that the model is safe.

## Sources

- [Inference Proofs RFCs](https://github.com/ai-verification-observatory/inference-proofs/blob/main/rfcs/README.md)
