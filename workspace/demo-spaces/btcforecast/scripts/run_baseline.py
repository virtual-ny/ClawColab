#!/usr/bin/env python3
from btcforecast.baseline import momentum_signal


def main():
    sample = [100.0, 100.5, 100.8, 101.2, 101.0]
    pred = momentum_signal(sample)
    label = 'up' if pred == 1 else 'down'
    print(f'baseline prediction: {label}')


if __name__ == '__main__':
    main()
