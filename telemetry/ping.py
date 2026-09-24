"""ICMP ping telemetry helpers for the NetFabric lab."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import re
import subprocess


@dataclass(frozen=True)
class PingResult:
    target: str
    count: int
    received: int
    loss_pct: float
    avg_ms: float | None
    samples_ms: list[float]


def run_ping(target: str, count: int = 5) -> PingResult:
    """Run the system ping command and return normalized telemetry."""
    if not target.strip():
        raise ValueError("target must not be empty")
    if count < 1:
        raise ValueError("count must be at least 1")

    completed = subprocess.run(
        ["ping", "-c", str(count), "-W", "2", target],
        capture_output=True,
        text=True,
        check=False,
    )
    output = f"{completed.stdout}\n{completed.stderr}"
    samples = [float(value) for value in re.findall(r"time[=<]([0-9]+(?:\\.[0-9]+)?)\\s*ms", output)]
    match = re.search(r"(\\d+(?:\\.\\d+)?)% packet loss", output)
    loss_pct = float(match.group(1)) if match else (0.0 if completed.returncode == 0 else 100.0)
    received = max(0, count - round(count * loss_pct / 100.0))
    avg_ms = sum(samples) / len(samples) if samples else None

    return PingResult(
        target=target,
        count=count,
        received=received,
        loss_pct=loss_pct,
        avg_ms=avg_ms,
        samples_ms=samples,
    )


def result_dict(result: PingResult) -> dict:
    """Convert a ping result into a JSON-friendly dictionary."""
    return asdict(result)
