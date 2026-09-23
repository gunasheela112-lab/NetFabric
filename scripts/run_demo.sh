#!/usr/bin/env bash
set -euo pipefail

echo "NetFabric demonstration workflow"
echo
echo "1. Start the lab using the topology instructions in docs/lab.md"
echo "2. Start the API:"
echo "   uvicorn api.main:app --reload"
echo "3. Serve the dashboard:"
echo "   python -m http.server 8080 --directory dashboard"
echo "4. Inspect routing from the dashboard."
echo "5. Generate ICMP/iperf3 traffic."
echo "6. Run the controlled failure experiment:"
echo "   ./experiments/run_convergence.sh"
echo "7. Review results/convergence.json and the dashboard history."
