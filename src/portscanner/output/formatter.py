import json
import csv
from io import StringIO
from typing import Dict, Any


def as_table(results: Dict[str, Any]) -> str:
    rows = [(host, port, info.get('state', ''), info.get('meta', {}).get('banner', '') or info.get('meta', {}).get('name', '') or '')
            for host, ports in results.items() for port, info in sorted(ports.items())]
    if not rows:
        return "No results."
    h1, h2, h3, h4 = "Host", "Port", "State", "Info"
    widths = [
        max(len(str(x)) for x in [h1] + [r[0] for r in rows]),
        max(len(str(x)) for x in [h2] + [str(r[1]) for r in rows]),
        max(len(str(x)) for x in [h3] + [r[2] for r in rows]),
        max(len(str(x)) for x in [h4] + [r[3] for r in rows]),
    ]