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
    line = f"{h1:<{widths[0]}}  {h2:<{widths[1]}}  {h3:<{widths[2]}}  {h4}"
    sep = "-" * (sum(widths) + 6)
    out = [line, sep]
    for host, port, state, info in rows:
        out.append(f"{host:<{widths[0]}}  {port:<{widths[1]}}  {state:<{widths[2]}}  {info}")
    return "\n".join(out)


def as_json(results: Dict[str, Any]) -> str:
    return json.dumps(results, indent=2, sort_keys=True)


def as_csv(results: Dict[str, Any]) -> str:
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["host", "port", "state", "info"])
    for host, ports in results.items():
        for port, info in sorted(ports.items()):
            meta = info.get('meta', {})
            info_str = meta.get('banner') or meta.get('name') or ''
            writer.writerow([host, port, info.get('state', ''), info_str])
    return output.getvalue()