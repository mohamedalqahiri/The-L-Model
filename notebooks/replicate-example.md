# Replicate the numerical example (t=5)

This is a small markdown reproducible example that shows how to run the numeric case and where to find expected outputs.

Steps:
1. Create virtualenv and activate it

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # optional
```

2. Run the simulation script

```bash
python src/simulation.py
```

3. Expected intermediate values (from repo documentation):
- f_5 ≈ 0.820
- r_5 ≈ 0.866
- Sync(5) ≈ 1.411
- L_5 ≈ 116.673
- PROSUM.A ≈ 9482.511

If the repo is refactored into a package, replace `python src/simulation.py` with `python -m src.cli` or `python -m the_l_model.cli` as applicable.
