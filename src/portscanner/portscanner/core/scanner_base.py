from abc import ABC, abstractmethod
from typing import Dict, Any, Iterable

ScanResult = Dict[str, Any]


class ScannerBase(ABC):
    """Abstract base for all scanners."""

    def __init__(self, timeout: float = 1.0, retries: int = 1):
        self.timeout = timeout
        self.retries = retries

    @abstractmethod
    def scan(self, targets: Iterable[str], ports: Iterable[int]) -> ScanResult:
        """Return a mapping { host: {port: {state: 'open'|'closed'|'filtered', meta: {...}}}}"""
        raise NotImplementedError
