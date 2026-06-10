# Hydrology Meets Machine Learning

[![Build and Deploy](https://github.com/mr-pablinho/drops-course/actions/workflows/build-deploy.yml/badge.svg)](https://github.com/mr-pablinho/drops-course/actions/workflows/build-deploy.yml)
[![Test Notebooks](https://github.com/mr-pablinho/drops-course/actions/workflows/test-notebooks.yml/badge.svg)](https://github.com/mr-pablinho/drops-course/actions/workflows/test-notebooks.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/Content-CC%20BY%204.0-lightgrey.svg)](LICENSE-CONTENT)

**A free, interactive online course on machine learning, data science, and AI applied to hydrology.**

Live course: **https://mr-pablinho.github.io/drops-course**

---

## Course overview

9 modules, ~35 lessons, all runnable in Google Colab. No installation required.

| Module | Topic |
|--------|-------|
| 1 | Python for Hydrologists |
| 2 | Hydrological Data Sources (USGS, ERA5, Caravan) |
| 3 | Exploratory Data Analysis |
| 4 | Classical ML (Random Forests, SHAP) |
| 5 | Time Series & LSTM Forecasting |
| 6 | Floods & Extreme Events |
| 7 | Groundwater |
| 8 | Drought & Water Scarcity |
| 9 | Capstone Project |

## Local development

```bash
conda env create -f environment.yml
conda activate drops-course
jupyter-book build book/
```

## Running notebook tests

```bash
HYDRO_ML_CI=1 HYDRO_ML_EPOCHS=1 pytest --nbmake --nbmake-timeout=600 book/**/*.ipynb -v
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Code: [MIT](LICENSE) | Content: [CC BY 4.0](LICENSE-CONTENT)

## Citation

See [CITATION.cff](CITATION.cff) or click "Cite this repository" on GitHub.
