from analytics.metrics import packet_loss, percentile, summarize_latency, throughput_delta


def test_percentile_interpolates():
    assert percentile([1, 2, 3, 4, 5], 95) == 4.8


def test_latency_summary():
    result = summarize_latency([1, 2, 3, 4, 5])
    assert result["mean_ms"] == 3
    assert result["median_ms"] == 3
    assert result["p95_ms"] == 4.8


def test_packet_loss():
    assert packet_loss(100, 95) == 5


def test_throughput_delta():
    assert throughput_delta(100, 120) == 20
