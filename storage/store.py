from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

DB_PATH = Path(__file__).with_name("netfabric.db")
SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def connect(path: Path = DB_PATH) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
    return connection


def record(
    experiment_id: str,
    metric: str,
    value: float,
    unit: str,
    source: str,
    target: str | None = None,
    timestamp: str | None = None,
    path: Path = DB_PATH,
) -> None:
    timestamp = timestamp or datetime.now(timezone.utc).isoformat()
    with connect(path) as db:
        db.execute(
            """INSERT INTO measurements
               (experiment_id,timestamp,metric,value,unit,source,target)
               VALUES (?,?,?,?,?,?,?)""",
            (experiment_id, timestamp, metric, value, unit, source, target),
        )


def recent(
    experiment_id: str | None = None,
    limit: int = 100,
    path: Path = DB_PATH,
) -> list[dict]:
    if limit < 1:
        raise ValueError("limit must be positive")
    with connect(path) as db:
        if experiment_id:
            rows = db.execute(
                """SELECT * FROM measurements
                   WHERE experiment_id=?
                   ORDER BY timestamp DESC LIMIT ?""",
                (experiment_id, limit),
            ).fetchall()
        else:
            rows = db.execute(
                "SELECT * FROM measurements ORDER BY timestamp DESC LIMIT ?",
                (limit,),
            ).fetchall()
    return [dict(row) for row in rows]


def clear(path: Path = DB_PATH) -> None:
    with connect(path) as db:
        db.execute("DELETE FROM measurements")
