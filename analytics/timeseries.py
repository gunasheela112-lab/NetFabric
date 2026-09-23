from __future__ import annotations

from collections import defaultdict
from statistics import mean
from typing import Iterable


def group_metric_series(rows: Iterable[dict], metric: str) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = defaultdict(list)

    for row in rows:
        if row.get("metric") != metric:
            continue
        grouped[row["experiment_id"]].append({
            "timestamp": row["timestamp"],
            "value": row["value"],
            "unit": row["unit"],
        })

    for values in grouped.values():
        values.sort(key=lambda item: item["timestamp"])

    return dict(grouped)


def experiment_summary(rows: Iterable[dict]) -> list[dict]:
    grouped: dict[str, list[float]] = defaultdict(list)

    for row in rows:
        if isinstance(row.get("value"), (int, float)):
            grouped[row["experiment_id"]].append(float(row["value"]))

    return [
        {
            "experiment_id": experiment_id,
            "samples": len(values),
            "mean": mean(values),
            "minimum": min(values),
            "maximum": max(values),
        }
        for experiment_id, values in sorted(grouped.items())
    ]
