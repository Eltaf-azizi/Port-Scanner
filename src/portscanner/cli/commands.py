import logging
from typing import Dict, Any

from portscanner.core.socket_scanner import SocketScanner
from portscanner.core.scapy_scanner import ScapyScanner
from portscanner.core.nmap_scanner import NmapScanner
from portscanner.core.utils import parse_ports, resolve_targets
from portscanner.output.formatter import as_table, as_json, as_csv
from portscanner.output.report import save_report


log = logging.getLogger(__name__)




def run_scan(args, settings: Dict[str, Any]):
    defaults = settings.get('defaults', {})

    engine = args.engine or defaults.get('engine', 'socket')
    port_spec = args.ports or defaults.get('ports', '1-1024')
    timeout = args.timeout if args.timeout is not None else float(defaults.get('timeout', 1.0))
    retries = args.retries if args.retries is not None else int(defaults.get('retries', 0))
    workers = args.workers if args.workers is not None else int(defaults.get('workers', 200))
    rate = args.rate if args.rate is not None else int(defaults.get('rate', 1000))


    # targets
    raw_targets = [t.strip() for t in args.target.split(',') if t.strip()]
    targets = resolve_targets(raw_targets) if (not args.no_resolve and defaults.get('resolve_hosts', True)) else raw_targets


