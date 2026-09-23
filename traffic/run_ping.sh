#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-10.20.20.20}"
COUNT="${2:-10}"

docker exec clab-netfabric-client ping -c "$COUNT" "$TARGET"
