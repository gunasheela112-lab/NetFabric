from analytics.path import compare_paths, hop_count


def test_hop_count():
    assert hop_count(("10.0.12.2", "10.0.24.1")) == 2


def test_compare_paths():
    result = compare_paths(("r1", "r2", "r4"), ("r1", "r3", "r4"))
    assert result.primary != result.alternate
