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
