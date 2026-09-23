# NetFabric operator dashboard

The dashboard is intentionally downstream from the network.

Planned panels:

1. **Topology** — routers, links and link state.
2. **Routing** — selected route, next hop and protocol.
3. **Traffic** — throughput, latency and loss.
4. **Resilience** — failure event and measured convergence.
5. **Evidence** — raw experiment artifacts and timestamps.

The first implementation should consume the FastAPI endpoints rather than maintaining a second source of network state.
