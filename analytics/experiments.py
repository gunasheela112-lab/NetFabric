from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ResilienceSummary:
    baseline_loss_pct: float
    failure_loss_pct: float
    baseline_latency_ms: float | None
    failure_latency_ms: float | None
    convergence_seconds: float | None


def latency_delta_percent(before: float | None, after: float | None) -> float | None:
    if before is None or after is None:
        return None
    if before == 0:
        raise ValueError("baseline latency must not be zero")
    return (after - before) / before * 100.0
