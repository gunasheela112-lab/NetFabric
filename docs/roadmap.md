# Roadmap

## Milestone 1 — foundation
- [x] Four-router reproducible topology
- [x] FRR/OSPF configuration
- [x] Lab lifecycle scripts
- [x] Metric calculations
- [x] FastAPI foundation
- [x] Unit tests and CI

## Milestone 2 — measurements
- [x] ICMP telemetry
- [x] iperf3 throughput collection
- [x] PCAP capture support
- [x] Flow analytics
- [x] Controlled link failure
- [x] Routed traffic endpoints

## Milestone 3 — network intelligence
- [x] Route inspection
- [x] Next-hop extraction
- [x] Path comparison primitives
- [x] Automated convergence experiment
- [ ] Persistent experiment history
- [ ] PCAP protocol parser

## Milestone 4 — operator interface
- [ ] Live topology view
- [ ] Route/next-hop inspection
- [ ] Traffic charts
- [ ] Failure timeline
- [ ] Experiment comparison
- [ ] Evidence browser

The dashboard is intentionally last: the network and measurement pipeline must work before visualization is treated as complete.
