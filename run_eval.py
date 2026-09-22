#!/usr/bin/env python3
"""Lightweight reproducible temperature forecast eval on bundled sample data."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "sample_jena_windows.csv"
TARGET = "T"
LAG = 6


def load_xy(path: Path = DATA):
    df = pd.read_csv(path)
    feature_cols = [c for c in df.columns if c != TARGET]
    frames = [df[feature_cols]]
    for lag in range(1, LAG + 1):
        frames.append(df[TARGET].shift(lag).rename(f"T_lag{lag}"))
    X = pd.concat(frames, axis=1).iloc[LAG:]
    y = df[TARGET].iloc[LAG:]
    split = int(len(X) * 0.8)
    return X.iloc[:split], X.iloc[split:], y.iloc[:split], y.iloc[split:]


def rmse(y_true, y_pred) -> float:
    return float(np.sqrt(mean_squared_error(y_true, y_pred)))


def evaluate():
    X_train, X_test, y_train, y_test = load_xy()
    models = {
        "GradientBoosting (XGB-style)": GradientBoostingRegressor(
            random_state=42, max_depth=3, n_estimators=80
        ),
        "MLP": Pipeline(
            [
                ("scale", StandardScaler()),
                (
                    "mlp",
                    MLPRegressor(
                        hidden_layer_sizes=(64, 32),
                        max_iter=200,
                        random_state=42,
                    ),
                ),
            ]
        ),
        "LagLinear (RNN-proxy)": Pipeline(
            [
                ("scale", StandardScaler()),
                (
                    "mlp",
                    MLPRegressor(
                        hidden_layer_sizes=(50,),
                        max_iter=200,
                        random_state=0,
                    ),
                ),
            ]
        ),
    }
    rows = []
    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        rows.append(
            {
                "model": name,
                "rmse": rmse(y_test, pred),
                "mae": float(mean_absolute_error(y_test, pred)),
            }
        )
    return rows


def main():
    rows = evaluate()
    print("Bundled-sample eval (not the enrolled Jena full-run table):")
    print(f"{'model':<32} {'RMSE':>8} {'MAE':>8}")
    for r in rows:
        print(f"{r['model']:<32} {r['rmse']:8.3f} {r['mae']:8.3f}")
    best = min(rows, key=lambda r: r["rmse"])
    print(f"\nBest on sample: {best['model']} (RMSE {best['rmse']:.3f})")
    print(
        "Course-report best was GRU (RMSE 0.171 / MAE 0.127 °C) on the enrolled dataset."
    )


if __name__ == "__main__":
    main()
