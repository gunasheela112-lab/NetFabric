from __future__ import annotations

from statistics import mean, median
from typing import Iterable


def percentile(values: Iterable[float], p: float) -> float:
    data = sorted(float(v) for v in values)
    if not data:
        raise ValueError("values must not be empty")
    if not 0 <= p <= 100:
        raise ValueError("p must be between 0 and 100")
    if len(data) == 1:
        return data[0]

    rank = (len(data) - 1) * p / 100
    lower = int(rank)
    upper = min(lower + 1, len(data) - 1)
    weight = rank - lower
    return data[lower] + (data[upper] - data[lower]) * weight


def summarize_latency(values: Iterable[float]) -> dict[str, float]:
    data = [float(v) for v in values]
    if not data:
        raise ValueError("latency values must not be empty")

    return {
        "mean_ms": mean(data),
        "median_ms": median(data),
        "p95_ms": percentile(data, 95),
        "min_ms": min(data),
        "max_ms": max(data),
    }


def packet_loss(sent: int, received: int) -> float:
    if sent < 0 or received < 0 or received > sent:
        raise ValueError("invalid packet counts")
    if sent == 0:
        return 0.0
    return (sent - received) / sent * 100.0


def throughput_delta(before_mbps: float, after_mbps: float) -> float:
    if before_mbps == 0:
        raise ValueError("before_mbps must not be zero")
    return (after_mbps - before_mbps) / before_mbps * 100.0
