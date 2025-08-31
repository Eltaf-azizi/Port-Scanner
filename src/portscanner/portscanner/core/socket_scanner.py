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