# Engineering Notes

## Why a real lab?

The project is deliberately built around an operating virtual network rather than generated dashboard data. This makes routing decisions, traffic behaviour and failures observable and reproducible.

## Why FRRouting?

FRR exposes conventional routing protocols and operational state through the same command-line interfaces used by network engineers. It keeps the lab focused on routing behaviour rather than application-only simulation.

## Why SQLite?

The first persistence layer is intentionally small. SQLite is enough for local experiment history and keeps the project reproducible without requiring an external database. A time-series database can be introduced later if the experiment volume warrants it.

## Why the dashboard comes last?

Network state should have one authoritative source. The lab and telemetry layer own the state; the API exposes it; the dashboard visualizes it. This prevents the UI from becoming a fake representation of the network.

## Measurement discipline

Every displayed measurement should have:

- a timestamp
- an experiment identifier
- a unit
- a source
- an optional target

Generated or example measurements must remain clearly labelled. The project does not claim that local lab measurements represent production-network performance.

## Failure methodology

The resilience experiment separates:

1. failure injection
2. route observation
3. traffic observation
4. recovery
5. evidence collection

This makes convergence behaviour inspectable rather than reducing resilience to a single health score.
