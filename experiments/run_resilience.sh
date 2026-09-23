#!/usr/bin/env bash
set -euo pipefail

ROUTER="${ROUTER:-r1}"
INTERFACE="${INTERFACE:-eth1}"
TARGET="${TARGET:-10.20.20.20}"
PING_COUNT="${PING_COUNT:-20}"

mkdir -p captures results

timestamp() { date +%s.%N; }

echo "=== NetFabric resilience experiment ==="
echo "Router: $ROUTER"
echo "Interface: $INTERFACE"
echo "Target: $TARGET"
echo

echo "Collecting baseline route..."
docker exec clab-netfabric-r1 vtysh -c "show ip route $TARGET" | tee results/route_before.txt

echo "Starting baseline traffic..."
docker exec clab-netfabric-client ping -c "$PING_COUNT" "$TARGET" | tee results/ping_before.txt

echo "Failure at $(timestamp)" | tee results/timeline.txt
docker exec "clab-netfabric-$ROUTER" ip link set "$INTERFACE" down

echo "Route immediately after failure:"
docker exec clab-netfabric-r1 vtysh -c "show ip route $TARGET" | tee results/route_after_failure.txt

echo "Traffic after failure:"
docker exec clab-netfabric-client ping -c "$PING_COUNT" "$TARGET" | tee results/ping_after.txt

echo "Restoring link at $(timestamp)" | tee -a results/timeline.txt
docker exec "clab-netfabric-$ROUTER" ip link set "$INTERFACE" up

echo "Final route:"
docker exec clab-netfabric-r1 vtysh -c "show ip route $TARGET" | tee results/route_restored.txt

echo "Experiment artifacts written to results/"
