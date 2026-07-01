---
title: Add basic requirements.txt and CI job
labels: good-first-issue, ci, outreach
assignees: []

---

Description:

Add `requirements.txt` with minimal dependencies (numpy, pandas, matplotlib, pytest) and a GitHub Actions workflow `.github/workflows/ci.yml` that installs deps and runs pytest.

Acceptance criteria:
- `requirements.txt` present at repo root
- `.github/workflows/ci.yml` runs on pull_request and passes tests (if tests exist)

Suggested bounty: $200
