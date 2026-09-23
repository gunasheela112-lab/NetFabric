# Measurement data contract

NetFabric treats measurements as evidence.

## Required fields

Every persisted observation should include:

- timestamp
- experiment ID
- source
- destination or target
- metric name
- value
- unit
- topology identifier

## Derived values

Derived metrics such as p95 latency and convergence duration must reference the observations from which they were calculated.

## Reproducibility

A report should also record the topology version, host environment and experiment parameters.

This prevents a dashboard number from becoming detached from the conditions under which it was measured.
