#!/usr/bin/env bash
set -euo pipefail

echo "== NetFabric lab health check =="

command -v docker >/dev/null || { echo "Docker is required"; exit 1; }
docker info >/dev/null || { echo "Docker daemon is not reachable"; exit 1; }

if command -v containerlab >/dev/null; then
  echo "containerlab: $(containerlab version 2>/dev/null | head -n 1)"
else
  echo "containerlab: not installed (required for the virtual topology)"
fi

if command -v python >/dev/null; then
  echo "python: $(python --version)"
fi

if docker network inspect netfabric  >/dev/null 2>&1; then
  echo "docker network netfabric: present"
else
  echo "docker network netfabric: not present"
fi

echo "Health check completed."
