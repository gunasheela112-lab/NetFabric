from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import Iterable


def protocol_counts(protocols: Iterable[str]) -> dict[str, int]:
    return dict(Counter(p.upper() for p in protocols))


def summarize_packet_lengths(lengths: Iterable[int]) -> dict[str, float]:
    values = list(lengths)
    if not values:
        return {"count": 0, "mean_bytes": 0.0, "max_bytes": 0.0}
    return {
        "count": len(values),
        "mean_bytes": sum(values) / len(values),
        "max_bytes": float(max(values)),
    }


def pcap_size(path: str | Path) -> int:
    return Path(path).stat().st_size
