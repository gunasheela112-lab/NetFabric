# NetFabric

## Network Engineering & Traffic Intelligence Lab

NetFabric is a reproducible virtual network lab for studying **routing, traffic behaviour, telemetry and network resilience**.

Instead of simulating a network entirely inside a dashboard, NetFabric runs a small routed topology with FRRouting, generates measurable traffic, collects network evidence and exposes the observations through an API and operations console.

### What it demonstrates

- Linux/container networking
- IPv4 subnetting and routed segments
- FRRouting
- OSPF
- Route and next-hop inspection
- ICMP and iperf3 measurements
- Latency, packet loss and throughput analysis
- PCAP capture and protocol analysis
- Persistent experiment history
- Controlled link-failure testing
- Route convergence observation
- Network operations dashboard
- Python/FastAPI automation
- Automated tests and CI

## Architecture

```text
                    ┌───────────────┐
                    │ Traffic /     │
                    │ Test Endpoints│
                    └───────┬───────┘
                            │
                       ┌────▼────┐
                       │   R1    │
                       │  FRR    │
                       └──┬───┬──┘
                          │   │
                    ┌─────▼┐ ┌▼─────┐
                    │  R2  │ │  R3  │
                    │ FRR  │ │ FRR  │
                    └───┬──┘ └──┬───┘
                        │        │
                        └───┬────┘
                            │
                       ┌────▼────┐
                       │   R4    │
                       │  FRR    │
                       └────┬────┘
                            │
                       ┌────▼────┐
                       │ Endpoint│
                       └─────────┘

          routing / traffic / packet evidence
                         │
                    ┌────▼────┐
                    │Telemetry│
                    └────┬────┘
                         │
                    ┌────▼────┐
                    │Analytics│
                    └────┬────┘
                         │
                    ┌────▼────┐
                    │ FastAPI │
                    └────┬────┘
                         │
                    ┌────▼────┐
                    │ Console │
                    └─────────┘
```

## Signature experiment: controlled link failure

The topology contains redundant paths. A failure experiment deliberately disables a routed interface and observes:

1. failure injection
2. route-state change
3. alternate-path selection
4. traffic recovery
5. convergence time
6. before/after evidence

The result is saved as machine-readable JSON alongside the raw route observations.

## Quick start

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Run the unit tests:

```pytest -q
```

For the full network lab, see **[docs/lab.md](docs/lab.md)**.

Start the API:

```uvicorn api.main:app --reload```

Serve the console:

```python -m http.server 8080 --directory dashboard```

Then open port 8080 locally.

## API surface

| Endpoint | Purpose |
|---|---|
| `GET /health` | service health |
| `POST /api/v1/routes/inspect` | inspect a router's route |
| `POST /api/v1/measurements/ping` | run and persist an ICMP measurement |
| `POST /api/v1/measurements` | record a measurement |
| `GET /api/v1/measurements` | retrieve experiment evidence |
| `GET /api/v1/analytics/series` | time-series data |
| `GET /api/v1/analytics/experiments` | experiment comparison |
| `POST /api/v1/analytics/pcap` | summarize a PCAP |

## Engineering principles

**Network first.** The dashboard is a consumer of network state, not the source of it.

**Evidence over claims.** Measurements are timestamped and associated with an experiment.

**Reproducibility over screenshots.** A useful result should be repeatable from the lab instructions.

**No artificial AI layer.** Machine learning is not added merely as a portfolio keyword. The central problem is network engineering.

## Repository map

```text
topology/       virtual network definition
routing/        FRR routing configuration
telemetry/      network measurements and route inspection
traffic/        traffic-generation scenarios
analytics/      metric, path and PCAP analysis
storage/        persistent experiment history
api/            FastAPI interface
dashboard/      operator console
experiments/    controlled failure experiments
tests/          automated tests
docs/           lab and engineering documentation
scripts/        operational helpers
```

## Limitations

This is a reproducible virtual lab, not a production network. Results depend on the host, container runtime, routing timers and generated traffic profile.

The project does not claim that lab measurements represent carrier, enterprise or maritime production performance.

## Roadmap

See [docs/roadmap.md](docs/roadmap.md).

## License

MIT
