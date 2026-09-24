#!/usr/bin/env bash
set -euo pipefail

ROUTER="${ROUTER:-r1}"
FAIL_INTERFACE="${FAIL_INTERFACE:-eth1}"
TARGET="${TARGET:-10.20.20.20}"
TIMEOUT="${TIMEOUT:-30}"

mkdir -p results

echo "=== NetFabric convergence experiment ==="
echo "Router=$ROUTER interface=$FAIL_INTERFACE target=$TARGET"

echo "Baseline route:"
docker exec "clab-netfabric-$ROUTER" vtysh -c "show ip route $TARGET" | tee results/convergence_before.txt

echo "Starting continuous probe..."
docker exec -d clab-netfabric-client sh -c "ping $TARGET > /tmp/netfabric-ping.log 2>&1"

START_NS=$(date +%s%N)
docker exec "clab-netfabric-$ROUTER" ip link set "$FAIL_INTERFACE" down
echo "Failure injected at $START_NS"

deadline=$((SECONDS + TIMEOUT))
recovered=0

while (( SECONDS < deadline )); do
  if docker exec clab-netfabric-r1 vtysh -c "show ip route $TARGET" | grep -q "via"; then
    recovered=1
    break
  fi
  sleep 0.25
done

END_NS=$(date +%s%N)

echo "Route after convergence:"
docker exec "clab-netfabric-$ROUTER" vtysh -c "show ip route $TARGET" | tee results/convergence_after.txt

python3 - "$START_NS" "$END_NS" "$recovered" <<'PY'
import json
import sys

start_ns, end_ns, recovered = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
result = {
    "failure_timestamp_ns": start_ns,
    "observation_timestamp_ns": end_ns,
    "convergence_seconds": (end_ns - start_ns) / 1_000_000_000 if recovered else None,
    "recovered": bool(recovered),
}
print(json.dumps(result, indent=2))
with open("results/convergence.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)
PY

docker exec "clab-netfabric-$ROUTER" ip link set "$FAIL_INTERFACE" up
docker exec clab-netfabric-client sh -c "pkill ping || true"

echo "Result written to results/convergence.json"
