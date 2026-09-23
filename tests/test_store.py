from pathlib import Path

from storage.store import recent, record


def test_store_round_trip(tmp_path: Path):
    db = tmp_path / "test.db"
    record(
        "baseline",
        "latency",
        2.4,
        "ms",
        "icmp",
        "10.20.20.20",
        path=db,
    )
    rows = recent("baseline", path=db)
    assert len(rows) == 1
    assert rows[0]["metric"] == "latency"
    assert rows[0]["value"] == 2.4
