from __future__ import annotations

import subprocess
from pathlib import Path


def capture(interface: str, output: str, duration: int = 10) -> Path:
    if duration < 1:
        raise ValueError("duration must be positive")

    destination = Path(output)
    destination.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "timeout",
        str(duration),
        "tcpdump",
        "-i",
        interface,
        "-w",
        str(destination),
        "-n",
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode not in (0, 124):
        raise RuntimeError(completed.stderr.strip() or "tcpdump failed")

    return destination
