# Reproducibility

NetFabric separates code, topology, observations and derived results.

## Experiment checklist

Before recording a result:

1. Record the repository commit.
2. Record the topology file.
3. Record the host OS and container runtime.
4. Record traffic parameters.
5. Record source and destination.
6. Keep raw route and ping output.
7. Calculate derived metrics from those raw observations.

## Artifacts

Small text results belong under `results/`.

PCAP files belong under `captures/` and are intentionally ignored by Git because packet captures can become large and may contain sensitive traffic in real environments.

## Important distinction

These experiments demonstrate network engineering behaviour in a controlled virtual lab. They are not claims about the performance of a physical production network.
