from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PathComparison:
    primary: tuple[str, ...]
    alternate: tuple[str, ...]


def hop_count(path: tuple[str, ...]) -> int:
    return len(path)


def compare_paths(primary: tuple[str, ...], alternate: tuple[str, ...]) -> PathComparison:
    if not primary:
        raise ValueError("primary path must not be empty")
    return PathComparison(primary=primary, alternate=alternate)
