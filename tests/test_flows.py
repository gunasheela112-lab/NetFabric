from analytics.flows import FlowRecord, protocol_distribution, top_talkers


def test_protocol_distribution():
    records = [
        FlowRecord("10.0.0.1", "10.0.0.2", "tcp", 10, 1000),
        FlowRecord("10.0.0.2", "10.0.0.3", "udp", 5, 500),
        FlowRecord("10.0.0.1", "10.0.0.4", "TCP", 4, 400),
    ]
    assert protocol_distribution(records) == {"TCP": 2, "UDP": 1}


def test_top_talkers():
    records = [
        FlowRecord("a", "b", "TCP", 1, 100),
        FlowRecord("a", "c", "TCP", 1, 50),
        FlowRecord("b", "c", "UDP", 1, 200),
    ]
    assert top_talkers(records, 2) == [("b", 200), ("a", 150)]
