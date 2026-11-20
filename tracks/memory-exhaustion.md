---
title: Memory exhaustion
question: Can a verifier tell that an accelerator's memory is fully occupied by a declared workload, leaving none for an undeclared one?
status: open
---

## Why it matters

If a verifier knows a device's memory size and can check that declared state fills it, it has a bound on what else can run there. That is one building block for checking how compute is used, for example that a cluster serves declared inference and not undeclared training.

## Approaches

| Project | Approach | Status |
|---|---|---|
| [poc-memory-exhaustion](../projects/poc-memory-exhaustion.md) | To be defined by the maintainer: claim, setting, adversary, mechanism | scaffold |

Other approaches to the same question are welcome as separate projects.

## What we know

No findings yet.

## Open questions

- **Compressibility.** A prover can hold the declared state compressed and spend the freed memory elsewhere. How incompressible can the state be made, and at what cost to the declared workload?
- **Locality.** The state must sit next to the compute cores, not in host memory or on another device. Do timed challenges tell the two apart on current hardware, and with what margin?
- **Layering.** Memory is one of three resources a verifier can try to exhaust, with compute and memory bandwidth. Can the challenges run side by side?

## Sources

- [SASH, Exploring Memory Exhaustion as a Verification Approach](../sources/sash-memory-exhaustion-note.md)
- [Dziembowski et al., Proofs of Space](../sources/proofs-of-space.md)
- [Komargodski and Weinstein, Proofs of Useful Work from Arbitrary Matrix Multiplication](../sources/proofs-of-useful-work-matmul.md)
- [Monfared et al., Timing and Memory Telemetry on GPUs for AI Governance](../sources/gpu-timing-memory-telemetry.md)
- [Cankaya, A system overview for near-term, low-trust AI compute verification](../sources/miri-low-trust-compute-verification.md)
- [Kubů, Proof of useful work for verifying AI treaties](../sources/kubu-pouw-ai-treaties.md)
