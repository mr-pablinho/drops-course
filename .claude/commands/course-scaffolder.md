Generate a new lesson notebook for the drops-course project (https://github.com/mr-pablinho/drops-course).

The user will provide: module number, lesson number within the module, and lesson title.
Example invocation: /course-scaffolder module=2 lesson=3 title="Caravan Dataset"

Steps:
1. Determine the file path from the module and lesson numbers, e.g.:
   - module=2, lesson=3 → book/02-hydrological-data/03-caravan.ipynb

2. Compute the Google Colab badge URL:
   https://colab.research.google.com/github/mr-pablinho/drops-course/blob/main/book/<module-folder>/<lesson-file>.ipynb

3. Write the notebook as a JSON file (.ipynb) with the following cell structure in order:

   Cell 1 — Markdown (frontmatter + badge):
   ```
   ---
   jupytext:
     text_representation:
       format_name: myst
   kernelspec:
     display_name: Python 3
     language: python
     name: python3
   ---
   # <Lesson Title>

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](<COLAB_URL>)

   **Learning objectives**
   By the end of this lesson you will be able to:
   - [ ] TODO: add objective 1
   - [ ] TODO: add objective 2
   - [ ] TODO: add objective 3
   ```

   Cell 2 — Code (Colab bootstrap — installs missing packages on Colab only):
   ```python
   # Install course dependencies when running on Google Colab
   import sys
   if "google.colab" in sys.modules:
       import subprocess
       subprocess.run([
           sys.executable, "-m", "pip", "install", "-q",
           "-r", "https://raw.githubusercontent.com/mr-pablinho/drops-course/main/requirements-colab.txt"
       ], check=True)
   ```

   Cell 3 — Code (CI / live data switch — REQUIRED in every data-loading lesson):
   ```python
   import os
   import pandas as pd

   CI = os.environ.get("HYDRO_ML_CI", "0") == "1"

   if CI:
       # Load pre-fetched sample for fast CI runs (no live API calls in CI)
       # TODO: replace with the actual sample file for this lesson
       df = pd.read_parquet("../data/samples/PLACEHOLDER.parquet")
   else:
       # TODO: replace with the actual live data loading for this lesson
       pass  # e.g. df = nwis.get_record(...)

   print(f"CI mode: {CI}")
   df.head()
   ```

   Cell 4 — Markdown:
   ```
   ## Introduction

   TODO: 2–3 sentence real-world hook (a specific event or finding that motivates the lesson).
   ```

   Cell 5 — Code (main lesson content stub):
   ```python
   # TODO: main lesson content
   ```

   Cell 6 — Markdown:
   ```
   ## Exercise

   **Try it yourself:** TODO — describe the exercise here.

   *Hint: TODO — provide a hint.*
   ```

   Cell 7 — Code (exercise solution, collapsed by default):
   ```python
   # Solution — try on your own first!
   # TODO: solution code
   ```
   Tag this cell with: `"tags": ["hide-cell"]`

4. After writing the file, print a checklist:
   ```
   Lesson created: book/<path>/<file>.ipynb

   Before this lesson is ready to merge:
   [ ] Fill in the 3 learning objectives
   [ ] Replace the real-world hook in the Introduction
   [ ] Replace PLACEHOLDER.parquet with the actual CI sample file
   [ ] Implement the live data loading (CI=False branch)
   [ ] Write the main lesson content
   [ ] Write the exercise and solution
   [ ] Run /nb-runner to verify the notebook executes clean in CI mode
   [ ] Run /content-reviewer on the finished lesson
   [ ] Run /hydro-code-checker if the lesson includes hydrological computations
   [ ] Add a /quiz-generator pass to draft the quiz questions
   ```
