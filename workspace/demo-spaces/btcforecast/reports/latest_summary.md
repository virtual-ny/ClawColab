# Latest Evaluation Summary

- Dataset: `data/raw/coinbase/btcusd_1m_coinbase_multiwindow.csv`
- Total samples: 2988
- Train samples: 2091
- Test samples: 897
- Test class balance up: 0.511

## Full Test Baselines
- momentum: accuracy=0.477, confusion={'tp': 218, 'tn': 210, 'fp': 229, 'fn': 240}
- mean_reversion: accuracy=0.523, confusion={'tp': 240, 'tn': 229, 'fp': 210, 'fn': 218}
- always_up: accuracy=0.511, confusion={'tp': 458, 'tn': 0, 'fp': 439, 'fn': 0}
- always_down: accuracy=0.489, confusion={'tp': 0, 'tn': 439, 'fp': 0, 'fn': 458}
- random: accuracy=0.516, confusion={'tp': 241, 'tn': 222, 'fp': 217, 'fn': 217}

## Batch Summaries
- Batch 1 (2026-03-10 12:15:00+00:00 -> 2026-03-10 22:07:00+00:00), samples=178, class_balance_up=0.506
  - momentum: accuracy=0.494
  - mean_reversion: accuracy=0.506
  - always_up: accuracy=0.506
  - always_down: accuracy=0.494
  - random: accuracy=0.489
- Batch 2 (2026-03-10 22:12:00+00:00 -> 2026-03-11 08:04:00+00:00), samples=178, class_balance_up=0.416
  - momentum: accuracy=0.584
  - mean_reversion: accuracy=0.416
  - always_up: accuracy=0.416
  - always_down: accuracy=0.584
  - random: accuracy=0.545
- Batch 3 (2026-03-11 08:09:00+00:00 -> 2026-03-11 18:01:00+00:00), samples=178, class_balance_up=0.601
  - momentum: accuracy=0.522
  - mean_reversion: accuracy=0.478
  - always_up: accuracy=0.601
  - always_down: accuracy=0.399
  - random: accuracy=0.438
- Batch 4 (2026-03-11 18:06:00+00:00 -> 2026-03-12 04:02:00+00:00), samples=178, class_balance_up=0.534
  - momentum: accuracy=0.444
  - mean_reversion: accuracy=0.556
  - always_up: accuracy=0.534
  - always_down: accuracy=0.466
  - random: accuracy=0.494
- Batch 5 (2026-03-12 04:07:00+00:00 -> 2026-03-12 14:02:00+00:00), samples=179, class_balance_up=0.492
  - momentum: accuracy=0.525
  - mean_reversion: accuracy=0.475
  - always_up: accuracy=0.492
  - always_down: accuracy=0.508
  - random: accuracy=0.520
