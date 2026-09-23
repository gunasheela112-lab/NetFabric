#!/usr/bin/env bash
set -euo pipefail

echo "===== OSPF neighbours ====="
for router in r1 r2 r3 r4; do
  echo "--- $router ---"
  docker exec clab-netfabric-$router vtysh -c "show ip ospf neighbor"
done

echo
echo "===== Route from R1 toward R4 ====="
docker exec clab-netfabric-r1 vtysh -c "show ip route 10.0.24.0/30"

echo
echo "===== Baseline ICMP ====="
docker exec clab-netfabric-r1 ping -c 5 10.0.24.2
