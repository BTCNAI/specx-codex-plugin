---
name: specx-contract-compiler
description: Compile natural-language workflow requests into verifiable SpecX execution contracts.
---

# SpecX Contract Compiler

Use this skill to convert a natural-language task into a SpecX execution contract.

SpecX is: A universal spec-driven agent governance and execution contract runtime.

This skill only compiles a contract. It does not execute the task.

Required contract fields:
- `contract_id`
- `version`
- `objective`
- `domain`
- `task_type`
- `required_agents`
- `required_tools`
- `required_evidence`
- `gates`
- `expected_artifacts`
- `failure_semantics`
- `execution_constraints`

Rules:
- The output must be a verifiable contract.
- Missing key fields must fail.
- Empty arrays are invalid for `required_agents`, `required_evidence`, `gates`, and `expected_artifacts`.
- Generic placeholders are invalid.
- Do not claim compile success without running validation.
- Do not execute the requested workflow from this skill.
