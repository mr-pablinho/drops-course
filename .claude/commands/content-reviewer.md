Review a lesson notebook (or markdown file) in the drops-course project for scientific accuracy, educational clarity, and completeness.

The user provides a file path, e.g.: /content-reviewer book/04-classical-ml/03-random-forests.ipynb

**Audience reminder:** The reader knows hydrology but is new to Python and ML. Explanations should be technically correct and written for a hydrology researcher learning ML — not for an ML practitioner learning hydrology.

---

## Review checklist

Work through each section and flag issues with severity: [ERROR], [WARNING], or [NOTE].

### 1. Scientific accuracy

Check all of the following. For each item, read the relevant cells and verify:

**Hydrology claims:**
- Are all physical units stated and consistent (m³/s, mm/day, etc.)?
- Are all named indices defined correctly?
  - NSE (Nash-Sutcliffe Efficiency): `NSE = 1 - Σ(Qobs - Qsim)² / Σ(Qobs - Q̄obs)²`
  - KGE (Kling-Gupta Efficiency): `KGE = 1 - √((r-1)² + (α-1)² + (β-1)²)`
  - SPI: computed from precipitation fitted to a gamma distribution
  - SPEI: SPI extended with potential evapotranspiration
  - PBIAS: `100 × Σ(Qobs - Qsim) / Σ(Qobs)`
- Are threshold values (e.g., NSE > 0.5 = "satisfactory") cited and defensible?
- Are physical constraints respected (streamflow ≥ 0, probabilities ∈ [0,1], etc.)?

**ML claims:**
- Is the train/test split done correctly for time series? (temporal split, NOT random shuffle)
- Is normalization/scaling fitted only on the training set? (never on the full series)
- Are model evaluation metrics correctly implemented?
- Is the distinction between interpolation and extrapolation addressed where relevant?
- Are overconfident claims about model performance avoided?

### 2. Code correctness

- Do code cells produce the outputs described in surrounding text?
- Are variable names, function calls, and imports consistent throughout?
- Does the CI guard pattern (`HYDRO_ML_CI`) work for both CI and live paths?
- Are any deprecated API calls used (e.g., old `dataretrieval` syntax)?

### 3. Educational clarity

- Does the lesson open with a specific real-world hook (not a generic "hydrology is important")?
- Are there 3 clear learning objectives at the top?
- Is each concept introduced before it's used?
- Are visualizations labeled (axes, units, titles)?
- Is there at least one exercise?

### 4. Quiz questions (if the file contains a quiz)

Auto-generated distractors are especially prone to errors. For each question:
- Is the correct answer actually correct?
- Are distractors plausible but clearly wrong to someone who understands the material?
- Does any distractor accidentally describe a real valid alternative?

---

## Output format

```
## Content Review: <filename>

### Errors (must fix before merging)
[ERROR] Cell 12: NSE formula is missing the squared term in the denominator.
  Code: `nse = 1 - np.sum((obs - sim)) / np.sum((obs - obs.mean()))`
  Fix: `nse = 1 - np.sum((obs - sim)**2) / np.sum((obs - obs.mean())**2)`

### Warnings (should fix)
[WARNING] Cell 8: Train/test split uses random shuffle (`train_test_split(shuffle=True)`).
  For time series, the split must respect temporal order. Use `shuffle=False`.

### Notes (suggestions)
[NOTE] The real-world hook is generic. Consider anchoring to a specific event
  (e.g., "The 2011 Missouri River flood — could a random forest have predicted it?")

### Summary
- Errors: 1
- Warnings: 1
- Notes: 1
- Verdict: DO NOT MERGE until errors are fixed.
```

If the lesson is clean: "No errors found. Ready for merge."
