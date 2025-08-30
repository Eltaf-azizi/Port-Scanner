import logging
from typing import Dict, Any

from portscanner.core.socket_scanner import SocketScanner
from portscanner.core.scapy_scanner import ScapyScanner
from portscanner.core.nmap_scanner import NmapScanner
from portscanner.core.utils import parse_ports, resolve_targets
from portscanner.output.formatter import as_table, as_json, as_csv
from portscanner.output.report import save_report


log = logging.getLogger(__name__)
