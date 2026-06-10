Validate the drops-course JupyterBook before deploying to GitHub Pages.

Run this before every deployment to catch build errors, broken links, and missing assets.

---

## Steps

### 1. Verify pinned dependencies

Check that `requirements.txt` contains `jupyter-book<2`:
```
grep "jupyter-book" requirements.txt
```
If it says `jupyter-book>=2` or has no upper bound, flag [ERROR] — the build will install JB2 (breaking rewrite) and fail.

### 2. Check that all TOC entries have matching files

Read `book/_toc.yml` and verify every `file:` entry has a corresponding `.ipynb` or `.md` file under `book/`. List any missing files as [ERROR].

### 3. Check that all data/samples references exist

Grep all notebooks for `data/samples/`:
```
grep -r "data/samples/" book/ --include="*.ipynb" -h | grep -oP '"data/samples/[^"]*"' | sort -u
```
For each referenced file, check it exists under `data/samples/`. List missing files as [ERROR].

### 4. Check Colab badge URLs

Grep all notebooks for colab badge URLs:
```
grep -r "colab.research.google.com/github" book/ --include="*.ipynb" -h
```
Each URL should match the pattern:
`https://colab.research.google.com/github/mr-pablinho/drops-course/blob/main/book/<path>.ipynb`

Flag [WARNING] if the URL references the wrong org/repo, a wrong branch (not `main`), or a path that doesn't match the file's actual location.

### 5. Build the JupyterBook

```
HYDRO_ML_CI=1 jupyter-book build book/ 2>&1
```
Capture the output. If the build exits non-zero, report the last 50 lines of output as [ERROR].

### 6. Check for broken internal links (after build)

```
jupyter-book build book/ --builder linkcheck 2>&1 | grep -E "broken|ERROR"
```
Report any broken internal links as [WARNING].

### 7. Final report

```
## Deploy Check: drops-course

Build:          PASS / FAIL
TOC coverage:   X/Y pages found
Sample files:   X missing / all present
Colab badges:   X malformed / all valid
Broken links:   X found / none

Verdict: READY TO DEPLOY / FIX BEFORE DEPLOYING
```

If deploying manually:
```bash
# After all checks pass
git add .
git commit -m "chore: pre-deploy check passed"
git push origin main
# GitHub Actions will build and deploy automatically
```
