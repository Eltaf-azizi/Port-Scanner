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
            for p in range(start, end + 1):
                if 1 <= p <= 65535:
                    result.add(p)
        else:
            p = int(part)
            if 1 <= p <= 65535:
                result.add(p)
    return sorted(result)



def expand_targets(target: str) -> Iterable[str]:
    """Expand a single target which can be host/IP or CIDR."""
    target = target.strip()
    try:
        if '/' in target:
            net = ipaddress.ip_network(target, strict=False)
            for ip in net.hosts():
                yield str(ip)
        else:
            # Validate DNS resolution
            try:
                socket.gethostbyname(target)
                yield target
            except socket.gaierror:
                return
    except ValueError:
        return



def resolve_targets(raw_targets: Iterable[str]) -> List[str]:
    seen: Set[str] = set()
    final: List[str] = []
    for t in raw_targets:
        for ip in expand_targets(t):
            if ip not in seen:
                seen.add(ip)
                final.append(ip)
    return final
 
 