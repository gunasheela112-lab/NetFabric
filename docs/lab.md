# NetFabric Lab Guide

## Purpose

NetFabric is a reproducible network-engineering lab. The dashboard is not a simulator of network behaviour; it reads measurements and routing state produced by the lab.

## Prerequisites

- Linux host or Linux VM
- Docker
- Containerlab
- Python 3.11+
- iperf3
- tcpdump (for packet capture)

FRRouting runs inside the lab routers.

## Start the lab

From the repository root:

```bash
containerlab deploy -t topology/lab.clab.yml
```

Confirm the nodes are running:

```containerlab inspect -t topology/lab.clab.yml
```

## Verify routing

Inspect an FRR router:

```docker exec clab-netfabric-r1 vtysh -c "show ip route"
docker exec clab-netfabric-r1 vtysh -c "show ip ospf neighbor"
```

The expected result is an OSPF-learned route between the lab endpoint networks.

## Start the API

```python
uvicorn api.main:app --reload
```

The API exposes health, measurement, route-inspection, time-series, experiment and PCAP-analysis endpoints.

## Start the dashboard

In another terminal:

```python
python -m http.server 8080 --directory dashboard
```

Open the local dashboard at port 8080.

## Generate traffic

Use the endpoint hosts to generate controlled ICMP or iperf3 traffic. Record measurements through the API so they become part of the experiment history.

## Failure experiment

The convergence experiment deliberately brings down a selected router interface, observes route recovery and restores the interface afterward:

```bash
./experiments/run_convergence.sh
```

The experiment writes raw evidence to `results/`. Do not treat those files as universal benchmark numbers; convergence depends on the host, container runtime, topology and routing timers.

## Packet capture

Capture traffic with tcpdump:

```tcpdump -i <interface> -w captures/experiment.pcap
```

Analyze the capture through the PCAP API or the analytics module.

## Shutdown

```containerlab destroy -t topology/lab.clab.yml
```

## Troubleshooting

### No OSPF neighbors

Check interfaces and addressing:

```docker exec clab-netfabric-r1 ip addr
docker exec clab-netfabric-r1 vtysh -c "show ip ospf interface"
```

### Route exists but traffic fails

Check the route on both endpoints, then verify the next hop and interface state.

### Dashboard says API offline

Start the FastAPI service and confirm:

```curl http://localhost:8000/health
```

### Convergence result is null

A null convergence value means the expected route was not observed before the configured timeout. Inspect the saved before/after route output instead of treating it as a zero-second result.
