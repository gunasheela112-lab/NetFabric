from __future__ import annotations

import re
import subprocess
import time
from dataclasses import dataclass


@dataclass(frozen=True)
class RouteObservation:
    timestamp: float
    router: str
    route: str
    next_hop: str | None


def route_observation(router: str, route: str) -> RouteObservation:
    completed = subprocess.run(
        [
            "docker",
            "exec",
            f"clab-netfabric-{router}",
            "vtysh",
            "-c",
            f"show ip route {route}",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    output = completed.stdout + completed.stderr
    match = re.search(r"via\s+(\d+\.\d+\.\d+\.\d+)", output)
    return RouteObservation(
        timestamp=time.time(),
        router=router,
        route=route,
        next_hop=match.group(1) if match else None,
    )


def convergence_seconds(before: RouteObservation, after: RouteObservation) -> float:
    if after.timestamp < before.timestamp:
        raise ValueError("after observation must be later than before observation")
    return after.timestamp - before.timestamp
