from __future__ import annotations

import subprocess
import time
from dataclasses import dataclass


@dataclass(frozen=True)
class ConvergenceResult:
    started_at: float
    recovered_at: float | None
    elapsed_seconds: float | None
    target: str


def route_contains_target(router: str, target: str) -> bool:
    result = subprocess.run(
        [
            "docker", "exec", f"clab-netfabric-{router}",
            "vtysh", "-c", f"show ip route {target}",
        ],
        capture_output=True, text=True, check=False,
    )
    text = result.stdout + result.stderr
    return target in text and ("via" in text or "is directly connected" in text)


def wait_for_recovery(
    router: str,
    target: str,
    timeout: float = 30.0,
    interval: float = 0.25,
) -> ConvergenceResult:
    started = time.time()
    deadline = started + timeout

    while time.time() < deadline:
        if route_contains_target(router, target):
            recovered = time.time()
            return ConvergenceResult(
                started_at=started,
                recovered_at=recovered,
                elapsed_seconds=recovered - started,
                target=target,
            )
        time.sleep(interval)

    return ConvergenceResult(
        started_at=started,
        recovered_at=None,
        elapsed_seconds=None,
        target=target,
    )
