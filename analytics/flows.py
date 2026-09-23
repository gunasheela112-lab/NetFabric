from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class FlowRecord:
    source: str
    destination: str
    protocol: str
    packets: int
    bytes: int


def protocol_distribution(records: Iterable[FlowRecord]) -> dict[str, int]:
    counts = Counter(record.protocol.upper() for record in records)
    return dict(counts)


def top_talkers(records: Iterable[FlowRecord], limit: int = 5) -> list[tuple[str, int]]:
    if limit < 1:
        raise ValueError("limit must be positive")

    totals = Counter()
    for record in records:
        totals[record.source] += record.bytes
    return totals.most_common(limit)
