import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, Any, Iterable, Tuple, List
from .scanner_base import ScannerBase



class SocketScanner(ScannerBase):

    def __init__(self, timeout: float = 1.0, retries: int = 0, workers: int = 200):
        super().__init__(timeout=timeout, retries=retries)
        self.workers = workers


    def _check_port(self, host: str, port: int) -> Tuple[int, Dict[str, Any]]:
        for attempt in range(self.retries + 1):
            try:

                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(self.timeout)
                    result = s.connect_ex((host, port))

                    if result == 0:
                        banner = ""

                        try:
                            s.settimeout(0.5)
                            s.sendall(b"\r\n")
                            banner = s.recv(128).decode(errors="ignore")
                        except Exception:
                            banner = ""
                        return port, {"state": "open", "meta": {"banner": banner.strip()}}
            
            except Exception:
                pass
        return port, {"state": "closed", "meta": {}}


