#!/usr/bin/env python3
from pathlib import Path

from btcforecast.data import load_ohlcv_csv, make_direction_dataset


def main():
    src = Path('data/raw/sample/btcusd_1m_sample.csv')
    dst = Path('data/processed/btcusd_1m_sample_labeled.csv')
    df = load_ohlcv_csv(src)
    labeled = make_direction_dataset(df, horizon_bars=5)
    dst.parent.mkdir(parents=True, exist_ok=True)
    labeled.to_csv(dst, index=False)
    print(f'wrote {dst} ({len(labeled)} rows)')


if __name__ == '__main__':
    main()
