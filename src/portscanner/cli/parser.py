import argparse


def build_parser():
    p = argparse.ArgumentParser(prog="port-scanner", description="Extensible Port Scanner")
    sub = p.add_subparsers(dest="command", required=True)

    scan = sub.add_parser("scan", help="Run a port scan")
    scan.add_argument("--target", required=True, help="Target host, IP, CIDR or comma-separated list")
    scan.add_argument("--ports", default=None, help="Port spec like 22,80,443 or 1-1024")
    scan.add_argument("--engine", default=None, choices=["socket", "scapy", "nmap"], help="Scan engine")
    scan.add_argument("--mode", default="syn", choices=["syn", "udp"], help="Scapy mode")
    scan.add_argument("--timeout", type=float, default=None, help="Timeout seconds")
    scan.add_argument("--retries", type=int, default=None, help="Retries per port")
    scan.add_argument("--workers", type=int, default=None, help="Socket engine threads")
    scan.add_argument("--rate", type=int, default=None, help="Scapy packets per second hint")
    scan.add_argument("--output", default=None, choices=["table", "json", "csv"], help="Output format to console")
    scan.add_argument("--report", default=None, choices=["html", "json", "csv", "none"], help="Also write a report")
    scan.add_argument("--save", default=None, help="Path to save report (implies --report)")
    scan.add_argument("--no-resolve", action="store_true", help="Do not resolve hostnames")

    return p
