import ipaddress
from typing import Iterable, List, Set
import socket


def parse_ports(spec: str) -> List[int]:
    """Parse port specs like "22,80,443" or "1-1024" or mixed."""
    result: Set[int] = set()
    for part in spec.split(','):
        part = part.strip()
        if not part:
            continue
        if '-' in part:
            a, b = part.split('-', 1)
            start, end = int(a), int(b)
            if start > end:
                start, end = end, start