from experiments.convergence import RouteObservation, convergence_seconds


def test_convergence_duration():
    before = RouteObservation(100.0, "r1", "10.0.24.0/30", "10.0.12.2")
    after = RouteObservation(100.35, "r1", "10.0.24.0/30", "10.0.13.2")
    assert convergence_seconds(before, after) == 0.35
