# Experiments

## Controlled resilience experiment

The main experiment combines routing state and traffic observations.

```bash
./experiments/run_resilience.sh
```

Optional parameters:

```bash
ROUTER=r1 INTERFACE=eth1 TARGET=10.20.20.20 PING_COUNT=30 ./experiments/run_resilience.sh
```

The script records route state, traffic behaviour and failure timestamps under `results/`.

### Interpretation

A valid experiment should answer:

- Which route was selected before the failure?
- Did OSPF install an alternate path?
- How much packet loss occurred during convergence?
- How did latency change?
- Was connectivity restored?
- What route was present after recovery?

The project deliberately keeps these observations as artifacts instead of collapsing them into a single health score.
