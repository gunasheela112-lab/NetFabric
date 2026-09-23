from analytics.timeseries import experiment_summary, group_metric_series


def rows():
    return [
        {"experiment_id": "baseline", "timestamp": "2026-01-01T00:00:01Z",
         "metric": "latency_avg", "value": 2.0, "unit": "ms"},
        {"experiment_id": "baseline", "timestamp": "2026-01-01T00:00:02Z",
         "metric": "latency_avg", "value": 4.0, "unit": "ms"},
        {"experiment_id": "failure", "timestamp": "2026-01-01T00:00:03Z",
         "metric": "latency_avg", "value": 8.0, "unit": "ms"},
    ]


def test_series_grouping():
    result = group_metric_series(rows(), "latency_avg")
    assert len(result["baseline"]) == 2
    assert result["baseline"][0]["value"] == 2.0


def test_experiment_summary():
    result = experiment_summary(rows())
    baseline = next(item for item in result if item["experiment_id"] == "baseline")
    assert baseline["mean"] == 3.0
    assert baseline["minimum"] == 2.0
