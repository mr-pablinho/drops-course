Run all Jupyter notebooks in the drops-course project and report which pass or fail.

This skill validates that every notebook executes end-to-end in CI mode (no live API calls, minimal epochs for DL notebooks).

Steps:

1. Check that pytest and nbmake are installed:
   ```
   pip show nbmake pytest
   ```
   If missing, install from requirements.txt first.

2. Run the full notebook test suite:
   ```
   HYDRO_ML_CI=1 HYDRO_ML_EPOCHS=1 pytest --nbmake --nbmake-timeout=600 book/**/*.ipynb -v 2>&1
   ```

3. Parse the output and produce a summary table:
   ```
   NOTEBOOK                                    STATUS    TIME
   book/01-python-for-hydrology/01-colab-intro PASS      4.2s
   book/02-hydrological-data/01-usgs-nwis      FAIL      12.1s
   ...
   ```

4. For each FAILED notebook, show:
   - The notebook path
   - The cell number where the error occurred
   - The error type and message (first 20 lines of traceback)
   - A likely cause (API call without CI guard, missing sample file, import error, etc.)

5. After reporting failures, also check for notebooks that are MISSING the CI guard pattern.
   For each .ipynb in book/, check if the file contains the string "HYDRO_ML_CI".
   List any notebooks missing it as a warning:
   ```
   WARNING: These notebooks have no CI guard (HYDRO_ML_CI check) — they will hit live APIs in CI:
   - book/02-hydrological-data/01-usgs-nwis.ipynb
   ```

6. Final summary line:
   ```
   Result: X passed, Y failed, Z warned (missing CI guard)
   ```
   If all pass and no warnings: "All notebooks clean. Ready to merge."
   If any fail: "Fix failures before merging."

Note: DL notebooks (Module 5+) use HYDRO_ML_EPOCHS=1 so the LSTM trains for 1 epoch — fast, but the full pipeline (data → model → eval) still runs and validates correctly.
