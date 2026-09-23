from pathlib import Path

import pytest

from analytics.pcap_reader import summarize_pcap


def test_missing_pcap():
    with pytest.raises((FileNotFoundError, OSError)):
        summarize_pcap(Path("does-not-exist.pcap"))
