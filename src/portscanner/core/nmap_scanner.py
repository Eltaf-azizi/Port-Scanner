from typing import Dict, Any, Iterable
from .scanner_base import ScannerBase
import nmap



class NmapScanner(ScannerBase):

    def __init__(self, timeout: float = 1.0, retries: int = 0, arguments: str = "-sS -T4"):
        super().__init__(timeout=timeout, retries=retries)
        self.arguments = arguments
        self.nm = nmap.PortScanner()


    def scan(self, targets: Iterable[str], ports: Iterable[int]) -> Dict[str, Any]:
        results: Dict[str, Any] = {}
        target_str = " ".join(targets)
        port_str = ",".join(str(p) for p in ports)

        # python-nmap interprets arguments as string. Timeout not directly applied; user can adapt arguments.
        self.nm.scan(hosts=target_str, ports=port_str, arguments=self.arguments)
        for host in self.nm.all_hosts():
            results.setdefault(host, {})
            tcpdata = self.nm[host].get('tcp', {}) or {}
            udpdata = self.nm[host].get('udp', {}) or {}

            # combine
            for p, info in {**tcpdata, **udpdata}.items():
                results[host][int(p)] = {
                    "state": info.get('state', 'unknown'),
                    "meta": {
                        "name": info.get('name'),
                        "product": info.get('product'),
                        "version": info.get('version'),
                        "extrainfo": info.get('extrainfo'),
                        "protocol": 'tcp' if int(p) in tcpdata else 'udp'
                    }
                }
                
        return results
