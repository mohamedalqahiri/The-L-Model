---
title: Regression test for numeric example
labels: good-first-issue, tests, outreach
assignees: []

---

Description:

Add a pytest-based regression test that runs the numerical example (t=5 case) and checks the PROSUM.A output matches the reference value (~9482.511 within tolerance).

Acceptance criteria:
- tests/test_regression.py with a test that imports the model and asserts numeric equality within 1e-3 relative tolerance
- CI (optional) runs pytest and passes

Suggested bounty: $150
