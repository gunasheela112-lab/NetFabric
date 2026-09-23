from analytics.experiments import latency_delta_percent


def test_latency_delta():
    assert latency_delta_percent(10.0, 12.0) == 20.0


def test_missing_latency():
    assert latency_delta_percent(None, 12.0) is None
