---
name: specx-verifier
description: Verify SpecX contracts, execution plans, and execution results for governance compliance.
---

# SpecX Verifier

Use this skill to verify whether a contract, execution plan, or execution result complies with SpecX governance.

SpecX is: A universal spec-driven agent governance and execution contract runtime.

Verifier checks:
- Field completeness.
- Gate execution.
- Evidence satisfaction.
- Artifact production.
- Failure semantics compliance.
- Silent fallback detection.
- Fake success detection.
- Hardcoded fallback detection.
- Unsupported capability wrapped as success detection.

Verification must fail closed. If evidence is missing, report the missing evidence; do not infer success.
