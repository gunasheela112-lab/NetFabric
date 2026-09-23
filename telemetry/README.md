# Telemetry

Telemetry is collected from the running lab.

Collectors currently cover:

- ICMP RTT and packet loss
- iperf3 JSON throughput
- tcpdump PCAP capture

The project keeps collection separate from analytics so raw observations can be inspected independently of derived metrics.

## PCAP

A packet capture should be treated as an experiment artifact. Do not commit large captures to Git; store them locally under `captures/`.
