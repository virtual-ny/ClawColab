from pathlib import Path
from typing import Union

import pandas as pd

REQUIRED_COLUMNS = ["timestamp", "open", "high", "low", "close"]


def load_ohlcv_csv(path: Union[str, Path]) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    return df.sort_values("timestamp").reset_index(drop=True)


def make_direction_dataset(df: pd.DataFrame, horizon_bars: int = 5) -> pd.DataFrame:
    out = df.copy()
    out["future_close"] = out["close"].shift(-horizon_bars)
    out["target_up"] = (out["future_close"] > out["close"]).astype("Int64")
    out = out.dropna(subset=["future_close"]).reset_index(drop=True)
    return out
