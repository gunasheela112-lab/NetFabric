#!/usr/bin/env bash
set -euo pipefail

SERVER="${1:-10.20.20.20}"
DURATION="${2:-10}"

echo "Starting iperf3 server..."
docker exec -d clab-netfabric-server iperf3 -s

echo "Running client -> server test for ${DURATION}s"
docker exec clab-netfabric-client iperf3 -c "$SERVER" -t "$DURATION" -J
