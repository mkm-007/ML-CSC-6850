# Weather Time Series Analysis and Forecasting

Course project (CSC 6850 Machine Learning, GSU) on the Max Planck Institute **Jena** weather station series: analyze and forecast temperature from 10-minute meteorological readings.

**Display title (locked):** Weather Time Series Analysis and Forecasting  
**Team:** Hemanth Kumar Mulluri, Sai Kethan Bharadwaj Kanithi, Vignesh Ajith Nair, Murali Krishna Maddineni

---

## Problem

High-resolution weather series are noisy and seasonal. A next-step temperature forecast needs a fair comparison across tree ensembles and sequence models — not a single unchallenged network.

## Build

- Clean / interpolate missing values, drop unit clutter from column names, MinMax scale  
- Models compared in the enrolled run: **XGBoost**, **MLP**, **LSTM**, **GRU**  
- This repo ships a **lightweight reproducible eval** (`run_eval.py`) on bundled sample windows so strangers can run without downloading the full Jena dump or TensorFlow

```
data/sample_jena_windows.csv   # small reproducible slice
run_eval.py                    # sklearn comparison + printed table
M.L_PROJECT_GROUP8_CODE.ipynb  # full course notebook
```

## Proof — course report (enrolled TensorFlow / XGBoost run)

| Model   | Test RMSE (°C) | Test MAE (°C) | Notes                          |
|---------|----------------|---------------|--------------------------------|
| XGBoost | 1.35           | 1.164         | Highest error among models     |
| MLP     | 0.329          | 0.2445        | Competitive                    |
| LSTM    | 0.341          | 0.290         | Captures trends                |
| **GRU** | **0.171**      | **0.127**     | Best overall on the course set |

Evaluation limitation: the notebook fits MinMaxScaler before the chronological train/test split, then inverse-transforms temperatures for RMSE/MAE. The table preserves historical report results in temperature units; it is not a clean train-only-preprocessing benchmark. The sample evaluator uses different data/models and does not reproduce or validate these figures.

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
python run_eval.py
```

`run_eval.py` prints RMSE/MAE on the bundled sample. Those numbers will **not** match the course table above (different data scale / models); the table is the enrolled proof.

## Honesty

Group coursework. Metrics in the table are from the submitted project report — not invented. Notebook may reference training history; prefer `run_eval.py` for a stranger-runnable path.
