#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

command -v containerlab >/dev/null || { echo "containerlab is required"; exit 1; }
command -v docker >/dev/null || { echo "docker is required"; exit 1; }

sudo containerlab deploy --topo topology/netfabric.clab.yml
sudo containerlab inspect --topo topology/netfabric.clab.yml
