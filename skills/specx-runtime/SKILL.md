---
name: specx-runtime
description: Drive contract-first SpecX workflow execution with gates, evidence, artifacts, and explicit failure states.
---

# SpecX Runtime

Use this skill to drive agent workflow execution from a SpecX contract.

SpecX is: A universal spec-driven agent governance and execution contract runtime.

Runtime principles:
- Contract first.
- Gate-bound execution.
- Evidence-bound decision.
- Artifact-bound output.
- Explicit failure state.
- No silent fallback.
- No fake success.
- No hardcoded fallback.
- No task mutation without approval.

Execution must stop when a required gate fails or required evidence is unavailable. Unsupported capability must be reported as unsupported, not wrapped as success.
