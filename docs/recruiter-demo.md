# Five-minute recruiter demo

The fastest way to demonstrate NetFabric is to show the engineering loop rather than read the dashboard.

## 1. Show the topology

Explain that four FRR routers provide two paths between the endpoint networks.

## 2. Show routing state

Run:

```bash
docker exec clab-netfabric-r1 vtysh -c "show ip route"
docker exec clab-netfabric-r1 vtysh -c "show ip ospf neighbor"
```

Point out the learned route and next hop.

## 3. Show measured traffic

Run a controlled ICMP or iperf3 test and record the result through the API.

## 4. Break the network

Run:

```bash
./experiments/run_convergence.sh
```

Explain that the failure is intentional and the lab observes how routing reacts.

## 5. Show evidence

Open:

- `results/convergence.json`
- before/after route output
- the dashboard measurement history
- the experiment comparison panel

The key story is:

**engineer a topology → generate traffic → measure it → introduce a failure → observe routing recovery → preserve the evidence.**
