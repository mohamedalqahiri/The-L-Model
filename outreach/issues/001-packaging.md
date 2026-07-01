---
title: Packaging and project structure: make the code a package
labels: good-first-issue, help-wanted, outreach
assignees: []

---

Description:

Refactor the `src/` folder to make the model importable as a Python package. Add `src/__init__.py`, consolidate functions into `src/model.py` (or similar), and add a simple CLI entry point `src/cli.py` that calls a `run_simulation()` function.

Acceptance criteria:
- `src/__init__.py` exists and exposes a `run_simulation` function
- `python -m src.cli` runs the example simulation and prints results
- Minimal unit test demonstrating `run_simulation()` returns the example numeric output

Suggested bounty: $300 (suggested; paid only if funding is available)
