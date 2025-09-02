from typing import Dict, Any, Optional
from jinja2 import Template
from .formatter import as_json, as_csv

HTML_TEMPLATE = Template(
    """<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Port Scan Report</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 2rem; }
    h1 { font-size: 1.5rem; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #ddd; padding: 8px; font-size: 14px; }
    th { background: #f5f5f5; text-align: left; }
    tr:nth-child(even){background-color: #fafafa;}
    code { white-space: pre-wrap; display:block; background:#f8f8f8; padding:1rem; }
  </style>
</head>
<body>
  <h1>Port Scan Report</h1>
  <p><strong>Engine:</strong> {{ engine }} | <strong>Targets:</strong> {{ targets|join(', ') }} | <strong>Ports:</strong> {{ ports|join(', ') }}</p>
  <table>
    <thead>
      <tr><th>Host</th><th>Port</th><th>State</th><th>Info</th></tr>
    </thead>
    <tbody>
      {% for host, ports in results.items() %}
        {% for port, info in ports|dictsort %}
          <tr>
            <td>{{ host }}</td>
            <td>{{ port }}</td>
            <td>{{ info.state }}</td>
            <td>{{ info.meta.banner or info.meta.name or info.meta.engine or '' }}</td>
          </tr>
        {% endfor %}
      {% endfor %}
    </tbody>
  </table>
  <h2>Raw JSON</h2>
  <code>{{ raw_json }}</code>
</body>
</html>"""
)