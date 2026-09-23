# Experiments

## Baseline

Record OSPF neighbours, selected routes, latency, packet loss and throughput when the traffic generator is available.

## Link failure

Disable one redundant inter-router link and record:

1. failure timestamp
2. route withdrawal
3. alternate route installation
4. traffic recovery

Convergence duration is measured from the failure event to the first stable observation of the alternate path.

## Reporting rules

Every result should identify the topology version, scenario, endpoints, test duration, traffic parameters and host environment.

Lab-generated measurements must not be presented as production-network benchmarks.
