# Use Cases

## Software Engineering

Before:

```text
Refactor this backend.
```

After SpecX:

- Planner and verification agents are explicit.
- Public behavior inventory is required before edits.
- Tests and diff evidence are required before success.
- Missing verification becomes `blocked` or `failed`.

Demo: `examples/demo_software_engineering_contract.json`

## Research Tasks

Before:

```text
Research this market.
```

After SpecX:

- Source quality gates are required.
- Claims require citations.
- Decision packets include risk notes.
- Unsupported claims stay unsupported.

Demo: `examples/demo_research_task_contract.json`

## Multi-Agent Systems

Before:

```text
Agents freestyle.
```

After SpecX:

- Runtime is contract-first.
- Planner, executor, and verifier boundaries are explicit.
- Every decision requires evidence and gate checks.
- Failure state is explicit.

Demo: `examples/demo_multi_agent_system_contract.json`
