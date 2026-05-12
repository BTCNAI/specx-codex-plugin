# Comparison

## Without SpecX

- The task starts from vague natural language.
- Agents can act before evidence is available.
- Missing outputs can be hidden behind generic summaries.
- Failed gates can be described as partial success.
- Scripts can be mislabeled as agents.

## With SpecX

- The task starts from a contract.
- Required agents, tools, evidence, gates, artifacts, and failure semantics are explicit.
- Decisions are gate-bound and evidence-bound.
- Missing evidence blocks the workflow.
- Failed verification remains failed.
- Script-only components stay tools.

## Core Claim

Stop agents from pretending success.
Make every task contract-bound, gate-bound, evidence-bound, and failure-explicit.
