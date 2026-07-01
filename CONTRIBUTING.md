# Contributing to The L-Model

Thank you for your interest in contributing to The L-Model. This document explains how to get started quickly, how to submit changes, and the standards we ask contributors to follow.

This repository contains research documentation and a small Python simulation. The maintainers prefer small, well-scoped contributions that improve reproducibility, tests, packaging, and documentation.

---

## How to start (quick)

1. Fork the repository and clone your fork.
2. Create a branch for your work: `git checkout -b my-feature`.
3. Set up a Python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   pip install -r requirements.txt  # if provided
   ```
4. Run the example simulation (if you only want to test):
   ```bash
   python src/simulation.py
   ```

## Issues and bounties

This repository contains "outreach" issues prepared for new contributors. Each issue file under `outreach/issues/` includes a clear description, acceptance criteria, and a suggested small bounty to compensate contributors. These bounties are suggestions and will be posted if/when funding is available.

## Coding standards

- Prefer clear, small functions that are easy to test.
- Add unit tests for new logic (pytest). Tests go under `tests/`.
- Use the repository's existing naming for variables and functions where possible.

## Submitting a change (Pull Request)

1. Push your branch to your fork.
2. Open a pull request against `main` (or the branch specified in the issue).
3. In the PR description, include which issue you address and the steps to reproduce.
4. The maintainers will review and may request small changes.

## Contact & support

If you'd like to contribute but need help, open a GitHub Discussion or create an issue with the label `help-wanted` and explain your constraints. Maintainers may be able to give small guidance or pairing help.


---

برای فارسی/عربی: اگر تفضل، يمكن ترجمة هذا الملف ومساعدتك محليًا.
