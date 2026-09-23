# NetFabric — Network Engineering & Traffic Intelligence Lab

A reproducible network engineering lab for building virtual routed topologies, generating traffic, measuring performance, inspecting routing behaviour, and testing resilience through controlled failures.

**Primary focus:** networking · routing · telemetry · traffic engineering · automation

> NetFabric is built around the network itself. The API and dashboard are consumers of measurements from the lab; they do not simulate a network in the frontend.

## What this demonstrates

- Linux networking and virtual interfaces
- IPv4 subnetting and multi-segment topologies
- FRRouting (FRR)
- OSPF routing and route convergence
- Static-route inspection
- Latency, jitter, throughput and packet-loss measurement
- Packet/flow analysis
- Controlled link-failure experiments
- Network telemetry and analytics
- Python automation and REST APIs
- Tests and GitHub Actions CI
- Reproducible network experiments

## Architecture

```text
                    Traffic / measurement host
                              |
                           +--+--+
                           | R1  |
                           | FRR |
                           +--+--+
                            /    \
                           /      \
                       +--+--+  +--+--+
                       | R2  |--| R3  |
                       | FRR |  | FRR |
                       +--+--+  +--+--+
                           \      /
                            \    /
                           +--+--+
                           | R4  |
                           | FRR |
                           +--+--+
                              |
                       Application host

                 telemetry + measurements
                              |
                       Python analytics
                              |
                         REST API
```

The topology deliberately has two paths between the edge routers. That makes routing decisions, failure recovery and convergence measurable rather than purely theoretical.

## Repository structure

```text
NetFabric/
├── topology/                 # Containerlab topology
├── routing/frr/              # FRR router configuration
├── traffic/                  # Traffic scenarios
├── telemetry/                # Collectors
├── analytics/                # Network metrics
├── api/                      # FastAPI service
├── dashboard/                # Operator UI (next milestone)
├── simulations/              # Failure experiments
├── scripts/                  # Lab lifecycle helpers
├── tests/                    # Automated tests
├── docs/                     # Architecture and experiments
└── .github/workflows/        # CI
```

## Quick start

### Prerequisites

Linux, Docker, Containerlab, Python 3.11+, and iperf3.

Windows users can use WSL2 with Docker integration.

### Start the network lab

```bash
chmod +x scripts/*.sh
./scripts/lab_up.sh
```

Inspect the topology:

```bash
sudo containerlab inspect --topo topology/netfabric.clab.yml
```

Inspect OSPF and routes:

```bash
./scripts/show_routes.sh
```

Run a baseline observation:

```bash
./scripts/run_baseline.sh
```

Remove the lab:

```bash
./scripts/lab_down.sh
```

### Run the Python tests

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Signature experiment — controlled link failure

The main experiment removes one redundant path and observes what the routing system actually does.

1. Establish the baseline route.
2. Generate traffic between endpoints.
3. Disable one inter-router link.
4. Record route changes and packet loss.
5. Measure the convergence interval.
6. Compare latency and throughput before and after failure.
7. Restore the link and verify recovery.

The final project will preserve the raw observations so results can be reproduced and inspected rather than reduced to a dashboard score.

## Measurement model

Raw observations are kept separate from derived analytics.

Typical fields:

```text
timestamp
source
destination
protocol
latency_ms
jitter_ms
packet_loss_pct
throughput_mbps
route
next_hop
interface
scenario
```

Derived metrics include:

- mean and median latency
- p95 latency
- packet-loss rate
- throughput change
- route-change count
- convergence duration
- performance delta before/after failure

## API

Current endpoints:

```text
GET /health
GET /api/v1/metrics
GET /api/v1/metrics/summary
GET /api/v1/experiments
```

Run locally:

```bash
uvicorn api.main:app --reload
```

## Engineering principles

- Measure the network instead of inventing telemetry.
- Keep routing behaviour inside the network lab.
- Make experiments reproducible.
- Record assumptions and limitations.
- Clearly label lab-generated measurements.
- Prefer simple, inspectable engineering over unnecessary abstraction.
- Do not add AI/ML unless it solves a demonstrated networking problem.

## Status

**Milestone 1 — foundation:** topology, FRR/OSPF configuration, lifecycle scripts, metric calculations, API skeleton, tests, CI and engineering documentation.

Upcoming milestones add real traffic collectors, PCAP/flow analysis, automated failure experiments and the operator dashboard.

## Limitations

This is a virtual network lab. Results depend on the host, container runtime, kernel scheduling and experiment parameters. They are not production-network benchmarks.

## License

MIT
