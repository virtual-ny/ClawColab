from dataclasses import dataclass


@dataclass
class BaselineConfig:
    lookback_bars: int = 5


def momentum_signal(recent_closes):
    """Return 1 for up, 0 for down based on simple recent momentum."""
    if len(recent_closes) < 2:
        raise ValueError("Need at least two close prices")
    return 1 if recent_closes[-1] > recent_closes[0] else 0


def mean_reversion_signal(recent_closes):
    """Return 1 for up, 0 for down by fading recent direction."""
    if len(recent_closes) < 2:
        raise ValueError("Need at least two close prices")
    return 0 if recent_closes[-1] > recent_closes[0] else 1
