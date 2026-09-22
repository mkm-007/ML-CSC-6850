from pathlib import Path

from run_eval import DATA, evaluate, load_xy


def test_sample_data_exists():
    assert DATA.exists()


def test_eval_returns_three_models():
    rows = evaluate()
    assert len(rows) == 3
    assert all("rmse" in r and "mae" in r for r in rows)
    assert all(r["rmse"] > 0 for r in rows)


def test_train_test_shapes():
    X_train, X_test, y_train, y_test = load_xy()
    assert len(X_train) > len(X_test) > 50
    assert len(X_train) == len(y_train)
