#!/usr/bin/env bash
set -euo pipefail

for router in r1 r2 r3 r4; do
  echo "===== $router ====="
  docker exec clab-netfabric-$router vtysh -c "show ip ospf neighbor"
  docker exec clab-netfabric-$router vtysh -c "show ip route"
  echo
done
