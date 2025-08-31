from typing import Dict, Any, Iterable
from .scanner_base import ScannerBase


class ScapyScanner(ScannerBase):
    def __init__(self, timeout: float = 1.0, retries: int = 0, rate: int = 1000, mode: str = "syn"):
        super().__init__(timeout=timeout, retries=retries)
        self.rate = rate
        self.mode = mode  # 'syn' or 'udp'

    def scan(self, targets: Iterable[str], ports: Iterable[int]) -> Dict[str, Any]:
        from scapy.all import IP, TCP, UDP, sr1, conf
        conf.verb = 0
        results: Dict[str, Any] = {}
        for host in targets:
            results.setdefault(host, {})
            for port in ports:
                try:
                    if self.mode == "udp":
                        pkt = IP(dst=host) / UDP(dport=port)
                    else:
                        pkt = IP(dst=host) / TCP(dport=port, flags="S")
                    ans = sr1(pkt, timeout=self.timeout, retry=self.retries)
                    if ans is None:
                        state = "filtered"