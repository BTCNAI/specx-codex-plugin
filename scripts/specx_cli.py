#!/usr/bin/env python3
"""SpecX CLI for contract validation, compilation, verification, and explanation."""

import argparse
import json
import sys
from pathlib import Path


REQUIRED_CONTRACT_FIELDS = [
    "contract_id",
    "version",
    "objective",
    "domain",
    "task_type",
    "required_agents",
    "required_tools",
    "required_evidence",
    "gates",
    "expected_artifacts",
    "failure_semantics",
    "execution_constraints",
]

REQUIRED_GATE_FIELDS = ["gate_id", "condition", "on_failure"]
REQUIRED_CONSTRAINTS = ["no_fake_success", "no_silent_fallback"]


def ok(result):
    return {"ok": True, "result": result}


def fail(error, details=None):
    return {"ok": False, "error": error, "details": details or []}


def load_json(path):
    try:
        with Path(path).open("r", encoding="utf-8") as handle:
            return json.load(handle), None
    except FileNotFoundError:
        return None, fail("Input file not found.", [str(path)])
    except json.JSONDecodeError as exc:
        return None, fail("Input is not valid JSON.", [str(exc)])


def missing_required(contract):
    missing = [field for field in REQUIRED_CONTRACT_FIELDS if field not in contract]
    empty = []
    for field in ("required_agents", "required_evidence", "gates", "expected_artifacts"):
        if field in contract and not contract[field]:
            empty.append(field)
    return missing, empty


def validate_contract(contract):
    if not isinstance(contract, dict):
        return fail("Contract must be a JSON object.")
    missing, empty = missing_required(contract)
    details = []
    if missing:
        details.append({"missing_required_fields": missing})
    if empty:
        details.append({"empty_required_fields": empty})
    if details:
        return fail("Contract validation failed.", details)
    if not isinstance(contract.get("required_tools"), list):
        return fail("required_tools must be an array.", ["required_tools"])
    if not isinstance(contract.get("failure_semantics"), dict):
        return fail("failure_semantics must be an object.", ["failure_semantics"])
    if not isinstance(contract.get("execution_constraints"), dict):
        return fail("execution_constraints must be an object.", ["execution_constraints"])
    return ok({"contract_id": contract["contract_id"], "status": "valid"})


def compile_contract(contract):
    validation = validate_contract(contract)
    if not validation["ok"]:
        return validation
    plan = {
        "plan_id": "plan-" + str(contract["contract_id"]),
        "contract_id": contract["contract_id"],
        "objective": contract["objective"],
        "domain": contract["domain"],
        "task_type": contract["task_type"],
        "agents": contract["required_agents"],
        "tools": contract["required_tools"],
        "evidence_requirements": contract["required_evidence"],
        "gates": contract["gates"],
        "artifact_plan": contract["expected_artifacts"],
        "verification_plan": {
            "required_gate_checks": [gate.get("gate_id") for gate in contract["gates"]],
            "required_evidence": contract["required_evidence"],
            "required_artifacts": contract["expected_artifacts"],
        },
        "failure_semantics": contract["failure_semantics"],
        "execution_constraints": contract["execution_constraints"],
        "status": "compiled",
    }
    return ok(plan)


def verify_contract(contract):
    if not isinstance(contract, dict):
        return fail("Contract must be a JSON object.")
    details = []
    if not contract.get("gates"):
        details.append("gates missing or empty")
    if not contract.get("failure_semantics"):
        details.append("failure_semantics missing or empty")
    if not contract.get("expected_artifacts"):
        details.append("expected_artifacts missing or empty")
    if not contract.get("required_agents"):
        details.append("required_agents missing or empty")
    if "required_tools" not in contract:
        details.append("required_tools field missing")
    for index, gate in enumerate(contract.get("gates") or []):
        missing = [field for field in REQUIRED_GATE_FIELDS if field not in gate]
        if missing:
            details.append({"gate_index": index, "missing": missing})
    constraints = contract.get("execution_constraints") or {}
    for name in REQUIRED_CONSTRAINTS:
        if constraints.get(name) is not True:
            details.append(name + " constraint missing or not true")
    if details:
        return fail("Contract verification failed.", details)
    return ok({"contract_id": contract.get("contract_id"), "status": "verified"})


def explain_contract(contract):
    validation = validate_contract(contract)
    unsupported = contract.get("unsupported_features", []) if isinstance(contract, dict) else []
    risk_notes = []
    if not validation["ok"]:
        risk_notes.append("Contract has validation errors.")
    if isinstance(contract, dict):
        constraints = contract.get("execution_constraints") or {}
        for name in REQUIRED_CONSTRAINTS:
            if constraints.get(name) is not True:
                risk_notes.append(name + " is not enforced.")
    result = {
        "summary": contract.get("objective") if isinstance(contract, dict) else "",
        "domain": contract.get("domain") if isinstance(contract, dict) else None,
        "task_type": contract.get("task_type") if isinstance(contract, dict) else None,
        "agent_count": len(contract.get("required_agents", [])) if isinstance(contract, dict) else 0,
        "tool_count": len(contract.get("required_tools", [])) if isinstance(contract, dict) else 0,
        "gate_count": len(contract.get("gates", [])) if isinstance(contract, dict) else 0,
        "artifact_count": len(contract.get("expected_artifacts", [])) if isinstance(contract, dict) else 0,
        "risk_notes": risk_notes,
        "unsupported_features": unsupported,
    }
    return ok(result)


def run(command, path):
    contract, error = load_json(path)
    if error:
        return error
    if command == "validate":
        return validate_contract(contract)
    if command == "compile":
        return compile_contract(contract)
    if command == "verify":
        return verify_contract(contract)
    if command == "explain":
        return explain_contract(contract)
    return fail("Unsupported command.", [command])


def main(argv=None):
    parser = argparse.ArgumentParser(description="SpecX contract CLI")
    parser.add_argument("command", choices=["validate", "compile", "verify", "explain"])
    parser.add_argument("path")
    args = parser.parse_args(argv)
    response = run(args.command, args.path)
    print(json.dumps(response, indent=2, sort_keys=True))
    return 0 if response.get("ok") else 1


if __name__ == "__main__":
    sys.exit(main())
