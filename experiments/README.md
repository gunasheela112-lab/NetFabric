# Experiment runner

The experiment layer turns individual lab commands into reproducible measurements.

The current convergence helper records timestamped route observations. The next runner will combine it with interface failure and traffic probes to calculate an end-to-end convergence interval.

A result should always retain the raw observations alongside the derived duration.
