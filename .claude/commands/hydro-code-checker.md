Audit a notebook's hydrological computations for correctness, unit consistency, and common ML/hydrology mistakes.

The user provides a file path: /hydro-code-checker book/05-time-series-forecasting/03-lstm-pytorch.ipynb

---

## What to check

Read all code cells in the notebook and audit the following:

### 1. Formula implementations

Verify each formula against its correct definition:

| Formula | Correct implementation |
|---------|----------------------|
| NSE | `1 - np.sum((obs - sim)**2) / np.sum((obs - obs.mean())**2)` |
| KGE | `1 - sqrt((r-1)² + (std_sim/std_obs - 1)² + (mean_sim/mean_obs - 1)²)` where r is Pearson correlation |
| PBIAS | `100 * np.sum(obs - sim) / np.sum(obs)` (positive = model underestimates) |
| RMSE | `np.sqrt(np.mean((obs - sim)**2))` |
| SPI | standardized anomaly from gamma-fitted precipitation; must use at least 30 years of data |
| GEV | three-parameter distribution; block maxima approach; verify parameters α, ξ, κ |
| Return period | `T = 1 / (1 - F(x))` where F is the fitted CDF |

Flag [ERROR] if any formula is implemented incorrectly.

### 2. Physical unit consistency

- Is streamflow in consistent units throughout (m³/s or mm/day — not mixed)?
- Are precipitation and evapotranspiration in the same time step units?
- Are area-weighted conversions done correctly (mm to m³/s requires catchment area)?
- Is time in the correct format for the operation (daily timestamps for daily data)?

Flag [WARNING] for inconsistent or undocumented units.

### 3. ML data leakage (the #1 error in hydrology ML)

- **Temporal split leak**: Is `train_test_split` called with `shuffle=True` on a time series? [ERROR]
- **Normalization leak**: Is `StandardScaler` (or equivalent) fitted on the full dataset before splitting? [ERROR]
  - Correct: `scaler.fit(X_train)` then `scaler.transform(X_test)`
  - Wrong: `scaler.fit(X)` then split
- **Look-ahead bias**: Do any features use future information (e.g., next-day precipitation to predict today's discharge)? [ERROR]
- **Target leak**: Is the target variable itself used as a predictor? [ERROR]

### 4. Physical plausibility of outputs

- Does predicted streamflow ever go negative? (impossible)
- Are NSE/KGE values in a plausible range for the model type? (e.g., NSE > 0.95 for a linear regression on daily streamflow would be suspicious)
- Are predicted return periods reasonable for the dataset length? (you can't reliably estimate a 100-year return period from 20 years of data)

### 5. Deep learning specifics (Modules 5+)

- Is the EPOCHS variable read from `os.environ.get("HYDRO_ML_EPOCHS", 30)`?
- Is the sequence length (lookback window) appropriate for daily streamflow? (7–365 days typical)
- Are gradients clipped to prevent exploding gradients? (common in LSTM training)
- Is the model set to `model.eval()` before inference?

---

## Output format

```
## Hydro Code Check: <filename>

### Errors (must fix)
[ERROR] Cell 15: NSE formula missing squared terms.
  Found:  1 - np.sum(obs - sim) / np.sum(obs - obs.mean())
  Correct: 1 - np.sum((obs - sim)**2) / np.sum((obs - obs.mean())**2)

[ERROR] Cell 22: Scaler fitted on full dataset before split (normalization leak).
  Found:  scaler.fit(X)  # line before train_test_split
  Fix:    scaler.fit(X_train)

### Warnings
[WARNING] Cell 8: Streamflow units switch from m³/s (loading) to mm/day (model input) without explicit conversion or documentation.

### Clean
- Temporal split: PASS (split is index-based, no shuffle)
- EPOCHS env var: PASS
- Physical plausibility: PASS (no negative predictions)

### Summary
Errors: 2 | Warnings: 1
DO NOT MERGE until errors are fixed.
```
