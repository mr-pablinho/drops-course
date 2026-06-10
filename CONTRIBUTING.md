# Contributing

Thank you for wanting to improve this course!

## Types of contributions welcome

- **Bug reports** — broken code, wrong output, dead links → open an Issue
- **Scientific corrections** — wrong formula, misleading explanation → open an Issue or PR with a reference
- **New lessons** — propose in an Issue first so we can agree on scope before you write it
- **Typos / clarity** — PRs welcome without prior discussion

## Before submitting a PR

1. Fork the repo and create a branch from `main`
2. If you're adding a lesson, use the `course-scaffolder` command (`.claude/commands/course-scaffolder.md`) to generate the right template
3. Make sure your notebook passes the CI check locally:
   ```bash
   HYDRO_ML_CI=1 HYDRO_ML_EPOCHS=1 pytest --nbmake --nbmake-timeout=600 your_notebook.ipynb
   ```
4. Every notebook **must** contain the dual-path data-loading pattern (CI vs. live); see any existing lesson for the pattern
5. Open the PR — CI runs automatically

## Scientific accuracy

This course prioritizes correctness. If you're unsure whether a claim is accurate, flag it as a question in the PR description and we'll resolve it together. Auto-generated quiz distractors are especially prone to subtle errors — always review them.

## Code of conduct

Be kind. The audience is researchers learning a new skill. Explanations that respect the reader's intelligence go a long way.
