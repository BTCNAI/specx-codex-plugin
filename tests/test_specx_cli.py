import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "specx_cli.py"
VALID = ROOT / "examples" / "generic_research_contract.json"


def run_cli(*args):
    process = subprocess.run(
        [sys.executable, str(CLI), *args],
        cwd=str(ROOT),
        text=True,
        capture_output=True,
        check=False,
    )
    payload = json.loads(process.stdout)
    return process.returncode, payload


class SpecXCliTests(unittest.TestCase):
    def test_validate_valid_contract_returns_ok_true(self):
        code, payload = run_cli("validate", str(VALID))
        self.assertEqual(code, 0)
        self.assertTrue(payload["ok"])

    def test_validate_missing_required_field_returns_ok_false(self):
        contract = json.loads(VALID.read_text(encoding="utf-8"))
        contract.pop("objective")
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump(contract, handle)
            temp_path = handle.name
        code, payload = run_cli("validate", temp_path)
        Path(temp_path).unlink()
        self.assertNotEqual(code, 0)
        self.assertFalse(payload["ok"])

    def test_compile_returns_status_compiled(self):
        code, payload = run_cli("compile", str(VALID))
        self.assertEqual(code, 0)
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["result"]["status"], "compiled")

    def test_verify_detects_missing_gates(self):
        contract = json.loads(VALID.read_text(encoding="utf-8"))
        contract["gates"] = []
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump(contract, handle)
            temp_path = handle.name
        code, payload = run_cli("verify", temp_path)
        Path(temp_path).unlink()
        self.assertNotEqual(code, 0)
        self.assertFalse(payload["ok"])
        self.assertIn("gates missing or empty", payload["details"])

    def test_explain_returns_summary(self):
        code, payload = run_cli("explain", str(VALID))
        self.assertEqual(code, 0)
        self.assertTrue(payload["ok"])
        self.assertIn("summary", payload["result"])


if __name__ == "__main__":
    unittest.main()
