# Experiment Results

This file is intentionally a template for **measured local results**.

Do not copy benchmark numbers into this document without running the experiment on the current lab and recording the resulting artifacts.

## Baseline

- Date:
- Host:
- Docker version:
- Containerlab version:
- Topology commit:
- Traffic profile:
- Destination:

### Measurements

| Metric | Value | Evidence |
|---|---:|---|
| Mean latency | — | measurement history |
| P95 latency | — | measurement history |
| Packet loss | — | measurement history |
| Throughput | — | iperf3 output |

## Link-failure experiment

- Failed interface:
- Failure timestamp:
- Route-change timestamp:
- Traffic-recovery timestamp:
- Route convergence:
- Traffic recovery:
- Packet loss during event:

### Evidence

- `results/convergence.json`
- `results/convergence_before.txt`
- `results/convergence_after.txt`
- relevant PCAP, if captured

## Interpretation

Record observations, not conclusions that the lab cannot support. For example:

- which route was selected before failure
- which alternate route was selected afterward
- how long recovery took
- whether traffic experienced loss
- whether the route returned to the original path after restoration

## Reproducibility

Run the same experiment again and record a new result set. Local virtual-lab timing is affected by the host and container runtime, so results should be treated as experiment observations rather than production-network benchmarks.
