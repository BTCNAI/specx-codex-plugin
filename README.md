# SpecX Codex Plugin

SpecX turns vague agent tasks into governed execution contracts.
It enforces required agents, tools, evidence, gates, artifacts, and failure semantics.
It prevents fake success, silent fallback, and uncontrolled agent execution.

SpecX is a governance layer for Codex agents.

## Install

Install from the marketplace repository:

```bash
codex plugin marketplace add BTCNAI/specx-codex-marketplace
```

Or pin the stable release:

```bash
codex plugin marketplace add https://github.com/BTCNAI/specx-codex-marketplace.git --ref v0.1.0
```

## What It Provides

- Contract-first workflow definition.
- Required LLM-backed agents with role, execution, and output specs.
- Gate-bound and evidence-bound decisions.
- Artifact contracts and explicit failure states.
- Fail-closed verification for fake success and silent fallback.

## Current Release

Version `v0.1.0` is a skills + CLI release.

Included skills:

- `specx-contract-compiler`
- `specx-runtime`
- `specx-agent-governance`
- `specx-verifier`

Included CLI:

```bash
python3 scripts/specx_cli.py validate examples/demo_software_engineering_contract.json
python3 scripts/specx_cli.py compile examples/demo_software_engineering_contract.json
python3 scripts/specx_cli.py verify examples/demo_software_engineering_contract.json
python3 scripts/specx_cli.py explain examples/demo_software_engineering_contract.json
```

## Contract Shape

Every valid contract must define:

- `required_agents`
- `required_tools`
- `required_evidence`
- `gates`
- `expected_artifacts`
- `failure_semantics`
- `execution_constraints.no_fake_success`
- `execution_constraints.no_silent_fallback`

If required evidence, tools, specs, gates, or artifacts are missing, the workflow must return `blocked`, `failed`, or `unsupported`. It must not claim success.

## Demos

Demo 1: Software engineering

- Before: "Refactor this backend."
- After SpecX: required agents, gates, tests, failure semantics, and artifact contract.
- File: `examples/demo_software_engineering_contract.json`

Demo 2: Research task

- Before: "Research this market."
- After SpecX: evidence requirements, source gates, decision packet, and risk notes.
- File: `examples/demo_research_task_contract.json`

Demo 3: Multi-agent system

- Before: agents freestyle.
- After SpecX: contract-first runtime, verifier, and explicit failure state.
- File: `examples/demo_multi_agent_system_contract.json`

## Docs

- `docs/quickstart.md`
- `docs/contract-format.md`
- `docs/use-cases.md`
- `docs/comparison.md`

## Roadmap

P0:

- Real MCP server.
- Contract schema v0.1.
- `specx.validate`
- `specx.compile`
- `specx.verify`
- `specx.explain`

P1:

- `specx init`
- `specx verify`

The next release target is skills + CLI + MCP tools.

## Repository Structure

```text
specx-codex-plugin/
├── .codex-plugin/plugin.json
├── docs/
├── skills/
├── scripts/
├── schemas/
├── examples/
├── tests/
├── README.md
├── marketplace.json
└── LICENSE
```

## Failure Policy

SpecX must not replace agent decisions with hardcoded fallback logic. Scripts may validate, transform, launch, or verify; they must not impersonate agent reasoning.

No LLM-backed decision authority means no agent label.
