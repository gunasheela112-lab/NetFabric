# NetFabric — Network Engineering & Traffic Intelligence Lab

A reproducible network engineering lab for building virtual routed topologies, generating traffic, measuring performance, inspecting routing behaviour, and testing resilience through controlled failures.

**Primary focus:** networking · routing · telemetry · traffic engineering · automation

> NetFabric is built around the network itself. The API and dashboard consume measurements from the lab; they do not simulate network state in the frontend.

## What this demonstrates

- Linux networking and virtual interfaces
- IPv4 subnetting and multi-segment routing
- FRRouting (FRR) and OSPF
- Route inspection and convergence experiments
- Real ICMP and iperf3 traffic through the virtual topology
- Packet capture with tcpdump
- Flow/protocol analytics
- Controlled link-failure testing
- Python automation and REST APIs
- Unit tests and GitHub Actions CI
- Reproducible experiment artifacts

## Architecture

```text
 client + iperf3
  10.10.10.10
       |
     [ R1 ]
     /    \
   [R2]  [R3]
     \    /
     [ R4 ]
       |
 server + iperf3
  10.20.20.20

       | telemetry
       v
 Python collectors
       |
       +--> latency / loss
       +--> throughput
       +--> PCAP / flow analysis
       +--> route observations
       |
     FastAPI
       |
   operator UI
```

The topology has two routed paths between R1 and R4. This creates a controlled environment for observing route selection, failure recovery and convergence.

## Quick start

Prerequisites: Linux, Docker, Containerlab, Python 3.11+ and iperf3.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
chmod +x scripts/*.sh traffic/*.sh simulations/*.sh experiments/*.sh

./scripts/lab_up.sh
```

Inspect routing:

```bash
./scripts/show_routes.sh
```

Generate routed traffic:

```bash
./traffic/run_ping.sh
./traffic/run_iperf.sh
```

Run the resilience experiment:

```bash
./experiments/run_resilience.sh
```

Run tests:

```bash
pytest -q
```

Remove the lab:

```bash
./scripts/lab_down.sh
```

## Signature experiment

NetFabric's main experiment deliberately removes one redundant link while traffic is flowing.

The experiment records:

- route before failure
- failure timestamp
- route after failure
- packet loss during the event
- latency before/after
- restoration timestamp
- final route

The objective is to observe routing convergence and resilience from actual lab behaviour rather than from a precomputed visualization.

## Measurement pipeline

```text
Virtual network
     |
     +-- ping ----------> RTT / packet loss
     |
     +-- iperf3 --------> throughput
     |
     +-- tcpdump --------> PCAP
     |
     +-- FRR ------------> route state
             |
             v
       Python analytics
             |
             v
          FastAPI
```

Raw observations remain distinct from derived metrics so experiments can be audited and repeated.

## Project structure

```text
topology/       Containerlab topology
routing/        FRR configuration
traffic/        Real traffic scenarios
telemetry/      Network measurement collectors
analytics/      Metric and flow calculations
experiments/    Resilience experiments
api/            FastAPI service
simulations/    Manual failure controls
tests/          Automated tests
docs/           Engineering documentation
scripts/        Lab lifecycle helpers
```

## Engineering principles

- Measure the network; don't fabricate telemetry.
- Keep routing behaviour inside the virtual network.
- Preserve raw experiment evidence.
- Make failure scenarios reproducible.
- Clearly distinguish lab measurements from production benchmarks.
- Prefer inspectable engineering over unnecessary abstraction.
- Avoid AI/ML unless a demonstrated networking problem justifies it.

## Current status

**Milestone 2 — measurement layer:** routed traffic, ICMP telemetry, iperf3 throughput collection, PCAP support, flow analytics and controlled resilience experiments.

Next: automated convergence measurement, route/path intelligence, persistent experiment history and the operator dashboard.

## Limitations

This is a virtual lab. Results depend on the host, Docker networking, kernel scheduling and experiment parameters. They should not be interpreted as production-network performance benchmarks.

## License

MIT
