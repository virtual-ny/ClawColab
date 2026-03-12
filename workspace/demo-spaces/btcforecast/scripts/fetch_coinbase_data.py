#!/usr/bin/env python3
import csv
import json
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path


def main():
    end = datetime.now(timezone.utc).replace(second=0, microsecond=0)
    start = end - timedelta(minutes=300)
    url = (
        'https://api.exchange.coinbase.com/products/BTC-USD/candles'
        f'?granularity=60&start={start.isoformat().replace("+00:00","Z")}'
        f'&end={end.isoformat().replace("+00:00","Z")}'
    )
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    data = sorted(data, key=lambda x: x[0])
    out = Path('data/raw/coinbase/btcusd_1m_coinbase_recent.csv')
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        for row in data:
            ts = datetime.fromtimestamp(row[0], tz=timezone.utc).isoformat().replace('+00:00', 'Z')
            w.writerow([ts, row[3], row[2], row[1], row[4], row[5]])
    print(f'wrote {out} ({len(data)} rows)')


if __name__ == '__main__':
    main()
