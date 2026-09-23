# Architecture

NetFabric has four operational layers.

## Network lab

Containerlab creates the topology. FRRouting provides OSPF routing. The routers are Linux containers with real interfaces, routing tables and routing processes.

## Traffic and observation

The lab generates traffic and collects observations from the network. The first milestone uses ICMP and FRR route inspection. iperf3 and packet capture are added as dedicated measurement scenarios.

## Analytics

Python converts raw observations into metrics such as p95 latency, packet loss, throughput change and convergence duration.

## API

FastAPI exposes measurements and experiment state to the operator interface.

## Design decision

The topology stays deliberately small. Four routers provide redundant paths without making route inspection unnecessarily difficult. The goal is measurable network behaviour, not topology size.
