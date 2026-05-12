#!/usr/bin/env python3
"""SpecX MCP launcher placeholder with fail-closed behavior."""

import sys


TODO = [
    "specx.validate",
    "specx.compile",
    "specx.verify",
    "specx.explain",
]


def main():
    try:
        import mcp  # noqa: F401
    except ImportError:
        print(
            "MCP SDK not installed. Use scripts/specx_cli.py directly or install MCP runtime.",
            file=sys.stderr,
        )
        print("TODO: " + ", ".join(TODO), file=sys.stderr)
        return 2
    print("SpecX MCP runtime integration is TODO: " + ", ".join(TODO), file=sys.stderr)
    return 3


if __name__ == "__main__":
    sys.exit(main())
