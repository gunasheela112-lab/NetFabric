from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass


@dataclass(frozen=True)
class RoutePath:
    router: str
    destination: str
    protocol: str | None
    next_hops: tuple[str, ...]
    interfaces: tuple[str, ...]
    raw: str


def inspect_route(router: str, destination: str) -> RoutePath:
    completed = subprocess.run(
        [
            "docker", "exec", f"clab-netfabric-{router}",
            "vtysh", "-c", f"show ip route {destination}",
        ],
        capture_output=True, text=True, check=False,
    )
    raw = completed.stdout + completed.stderr
    protocol = None
    protocol_match = re.search(r'^\s*([A-Za-z])(?:[>* ]|$)', raw, re.MULTILINE)
    if protocol_match:
        protocol = protocol_match.group(1).lower()

    hops = tuple(re.findall(r'(\d+\.\d+\.\d+\.\d+),\s+via\b', raw))
    interfaces = tuple(re.findall(r',\s+([A-Za-z0-9_.-]+),', raw))
    return RoutePath(router, destination, protocol, hops, interfaces, raw)
