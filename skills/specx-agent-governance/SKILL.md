---
name: specx-agent-governance
description: Govern agent behavior under SpecX execution contracts and prevent bypass, fabrication, and silent fallback.
---

# SpecX Agent Governance

Use this skill to constrain agent behavior under a SpecX execution contract.

SpecX is: A universal spec-driven agent governance and execution contract runtime.

Agents must obey:
- Execution contract priority.
- Do not bypass gates.
- Do not fabricate tool results.
- Do not rewrite failure as success.
- Do not use weak prompting in place of strong constraints.
- Do not use script hardcoding in place of agent decisions.
- Pause when human approval is required.

An agent without LLM-backed decision authority must not be labeled as an agent. Scripts may be tools, validators, or launchers only.
