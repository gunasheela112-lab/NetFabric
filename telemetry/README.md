# Telemetry

Telemetry is intentionally collected from the running lab.

## Ping

The Python collector wraps the system `ping` utility and extracts packet loss and RTT statistics.

Example:

```python
from telemetry.ping import run_ping

print(run_ping("10.0.24.2", count=5))
```

## iperf3

The iperf3 collector requests JSON output so throughput measurements can be processed without scraping human-readable terminal output.

The collectors do not invent measurements. If the underlying command fails, the failure is surfaced to the caller.
