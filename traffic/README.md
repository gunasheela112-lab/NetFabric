# Traffic scenarios

## Baseline ping

```bash
./traffic/run_ping.sh
```

## Throughput

```bash
./traffic/run_iperf.sh
```

The iperf3 command returns JSON so the result can be archived and analyzed without scraping terminal formatting.

Traffic endpoints are part of the virtual topology. Measurements therefore exercise the routed path instead of measuring two unrelated host processes.
