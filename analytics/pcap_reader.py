from __future__ import annotations

from collections import Counter
from pathlib import Path


def read_pcap(path: str | Path) -> list[dict]:
    """Read a PCAP with scapy when available.

    The dependency is optional so the core project remains usable without it.
    Each returned record contains only fields useful to the dashboard.
    """
    try:
        from scapy.all import IP, TCP, UDP, ICMP, rdpcap
    except ImportError as exc:
        raise RuntimeError("Install scapy to parse PCAP files") from exc

    packets = rdpcap(str(path))
    records: list[dict] = []

    for packet in packets:
        record = {
            "length_bytes": len(packet),
            "protocol": "OTHER",
            "source": None,
            "destination": None,
        }

        if IP in packet:
            record["source"] = packet[IP].src
            record["destination"] = packet[IP].dst
            if TCP in packet:
                record["protocol"] = "TCP"
            elif UDP in packet:
                record["protocol"] = "UDP"
            elif ICMP in packet:
                record["protocol"] = "ICMP"

        records.append(record)

    return records


def summarize_pcap(path: str | Path) -> dict:
    records = read_pcap(path)
    protocols = Counter(record["protocol"] for record in records)
    total_bytes = sum(record["length_bytes"] for record in records)

    return {
        "packets": len(records),
        "bytes": total_bytes,
        "protocols": dict(protocols),
    }
