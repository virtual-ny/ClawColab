import random
import pandas as pd


def _reset(series: pd.Series) -> pd.Series:
    return series.astype('Int64').reset_index(drop=True)


def accuracy_score(y_true: pd.Series, y_pred: pd.Series) -> float:
    y_true = _reset(y_true)
    y_pred = _reset(y_pred)
    if len(y_true) == 0:
        raise ValueError("Empty evaluation series")
    return float((y_true == y_pred).mean())


def always_up_baseline(n: int) -> pd.Series:
    return pd.Series([1] * n, dtype="Int64")


def random_direction_baseline(n: int, seed: int = 42) -> pd.Series:
    rng = random.Random(seed)
    return pd.Series([rng.randint(0, 1) for _ in range(n)], dtype="Int64")


def confusion_counts(y_true: pd.Series, y_pred: pd.Series) -> dict:
    y_true = _reset(y_true)
    y_pred = _reset(y_pred)
    tp = int(((y_true == 1) & (y_pred == 1)).sum())
    tn = int(((y_true == 0) & (y_pred == 0)).sum())
    fp = int(((y_true == 0) & (y_pred == 1)).sum())
    fn = int(((y_true == 1) & (y_pred == 0)).sum())
    return {'tp': tp, 'tn': tn, 'fp': fp, 'fn': fn}


def train_test_split_time(df: pd.DataFrame, train_frac: float = 0.7):
    split = max(1, int(len(df) * train_frac))
    train = df.iloc[:split].copy().reset_index(drop=True)
    test = df.iloc[split:].copy().reset_index(drop=True)
    return train, test
