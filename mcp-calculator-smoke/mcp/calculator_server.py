#!/usr/bin/env python3
"""Minimal placeholder MCP server entry point for descriptor packaging tests."""

from __future__ import annotations

import json
import sys


def main() -> int:
    # This file is intentionally tiny: marketplace preflight validates launch
    # metadata statically, while real MCP protocol execution is tested in CLIO.
    if len(sys.argv) > 1 and sys.argv[1] == "serve":
        sys.stderr.write("calculator smoke MCP placeholder is not enabled by default\n")
        return 0
    print(json.dumps({"name": "calculator-smoke", "tools": ["calculator_add"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
