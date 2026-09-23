# Validation Checklist

Use this checklist before presenting NetFabric.

## Environment

- [ ] Docker daemon is running
- [ ] Containerlab is installed
- [ ] Python dependencies are installed
- [ ] `./scripts/healthcheck.sh` completes

## Routing

- [ ] Four lab routers are running
- [ ] R1 has OSPF neighbours
- [ ] R4 destination route is present
- [ ] Both intended paths are reachable

## Traffic

- [ ] ICMP measurement succeeds
- [ ] iperf3 traffic succeeds
- [ ] Measurements appear in SQLite history
- [ ] PCAP capture can be opened/analyzed

## Resilience

- [ ] Failure experiment completes
- [ ] Before/after route files are generated
- [ ] Convergence JSON contains a recovery result
- [ ] Failed interface is restored

## API

- [ ] `GET /health` returns OK
- [ ] Route inspection works
- [ ] Measurement endpoints work
- [ ] Analytics endpoints work
- [ ] Missing files return useful HTTP errors

## Presentation

- [ ] README commands were tested
- [ ] Results document contains only measured values
- [ ] Screenshots show the actual dashboard
- [ ] Repository contains no placeholder claims presented as results
