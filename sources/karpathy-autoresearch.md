---
title: Karpathy, autoresearch (2026)
url: https://github.com/karpathy/autoresearch
kind: code
tracks: [autoresearch]
---

## Why it matters here

The pattern the autoresearch project follows: an agent edits one training file, runs a fixed five-minute experiment, keeps the change if validation loss improves and reverts it otherwise, while a human edits only the instructions in program.md. It optimises a training metric with no adversary; a verification loop also has to keep its negative controls passing.
