#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path
import json
import pandas as pd

from btcforecast.baseline import momentum_signal, mean_reversion_signal
from btcforecast.data import load_ohlcv_csv, make_direction_dataset
from btcforecast.evaluate import (
    accuracy_score,
    always_up_baseline,
    random_direction_baseline,
    confusion_counts,
    train_test_split_time,
)

DATASET = Path('data/raw/coinbase/btcusd_1m_coinbase_multiwindow.csv')


def rolling_signal_predictions(df, signal_fn, lookback_bars=5):
    preds = []
    closes = df['close'].tolist()
    for i in range(len(df)):
        if i < lookback_bars - 1:
            preds.append(pd.NA)
            continue
        window = closes[i - lookback_bars + 1:i + 1]
        preds.append(signal_fn(window))
    return pd.Series(preds, dtype='Int64')


def score_block(y_true, y_pred):
    return {
        'accuracy': round(accuracy_score(y_true, y_pred), 6),
        'confusion': confusion_counts(y_true, y_pred),
    }


def compute_test_block(test):
    y_test = test['target_up']
    return {
        'samples': int(len(test)),
        'class_balance_up': round(float(y_test.astype('Int64').mean()), 6),
        'baselines': {
            'momentum': score_block(y_test, test['pred_momentum']),
            'mean_reversion': score_block(y_test, test['pred_mean_reversion']),
            'always_up': score_block(y_test, always_up_baseline(len(y_test))),
            'always_down': score_block(y_test, pd.Series([0] * len(y_test), dtype='Int64')),
            'random': score_block(y_test, random_direction_baseline(len(y_test))),
        },
    }


def summarize_batches(scored, batch_count=5):
    batches = []
    n = len(scored)
    batch_size = max(1, n // batch_count)
    for i in range(batch_count):
        start = i * batch_size
        end = n if i == batch_count - 1 else min(n, (i + 1) * batch_size)
        block = scored.iloc[start:end].copy().reset_index(drop=True)
        if len(block) < 10:
            continue
        block['pred_momentum'] = rolling_signal_predictions(block, momentum_signal, lookback_bars=5)
        block['pred_mean_reversion'] = rolling_signal_predictions(block, mean_reversion_signal, lookback_bars=5)
        block = block.dropna(subset=['pred_momentum', 'pred_mean_reversion']).reset_index(drop=True)
        if len(block) < 10:
            continue
        _, test = train_test_split_time(block, train_frac=0.7)
        if len(test) == 0:
            continue
        batches.append({
            'batch_index': i + 1,
            'start_timestamp': str(block.iloc[0]['timestamp']),
            'end_timestamp': str(block.iloc[-1]['timestamp']),
            **compute_test_block(test),
        })
    return batches


def main():
    df = load_ohlcv_csv(DATASET)
    labeled = make_direction_dataset(df, horizon_bars=5)
    labeled['pred_momentum'] = rolling_signal_predictions(labeled, momentum_signal, lookback_bars=5)
    labeled['pred_mean_reversion'] = rolling_signal_predictions(labeled, mean_reversion_signal, lookback_bars=5)
    scored = labeled.dropna(subset=['pred_momentum', 'pred_mean_reversion']).reset_index(drop=True)
    train, test = train_test_split_time(scored, train_frac=0.7)

    metrics = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'dataset': str(DATASET),
        'reference_price_rule': 'current bar close at time t',
        'horizon_bars': 5,
        'total_samples': int(len(scored)),
        'train_samples': int(len(train)),
        'test_samples': int(len(test)),
        'test_class_balance_up': round(float(test['target_up'].astype('Int64').mean()), 6),
        'full_test': compute_test_block(test),
        'batch_summaries': summarize_batches(scored, batch_count=5),
    }

    reports_dir = Path('reports')
    reports_dir.mkdir(parents=True, exist_ok=True)
    json_out = reports_dir / 'latest_metrics.json'
    md_out = reports_dir / 'latest_summary.md'
    json_out.write_text(json.dumps(metrics, indent=2), encoding='utf-8')

    lines = []
    lines.append('# Latest Evaluation Summary')
    lines.append('')
    lines.append(f"- Dataset: `{metrics['dataset']}`")
    lines.append(f"- Total samples: {metrics['total_samples']}")
    lines.append(f"- Train samples: {metrics['train_samples']}")
    lines.append(f"- Test samples: {metrics['test_samples']}")
    lines.append(f"- Test class balance up: {metrics['test_class_balance_up']:.3f}")
    lines.append('')
    lines.append('## Full Test Baselines')
    for name, block in metrics['full_test']['baselines'].items():
        lines.append(f"- {name}: accuracy={block['accuracy']:.3f}, confusion={block['confusion']}")
    lines.append('')
    lines.append('## Batch Summaries')
    for batch in metrics['batch_summaries']:
        lines.append(f"- Batch {batch['batch_index']} ({batch['start_timestamp']} -> {batch['end_timestamp']}), samples={batch['samples']}, class_balance_up={batch['class_balance_up']:.3f}")
        for name, block in batch['baselines'].items():
            lines.append(f"  - {name}: accuracy={block['accuracy']:.3f}")
    md_out.write_text('\n'.join(lines) + '\n', encoding='utf-8')

    print(f"total_samples={metrics['total_samples']}")
    print(f"train_samples={metrics['train_samples']}")
    print(f"test_samples={metrics['test_samples']}")
    print(f"test_class_balance_up={metrics['test_class_balance_up']:.3f}")
    for name, block in metrics['full_test']['baselines'].items():
        print(f"{name}_accuracy={block['accuracy']:.3f}")
    print(f"wrote_report={json_out}")
    print(f"wrote_summary={md_out}")


if __name__ == '__main__':
    main()
