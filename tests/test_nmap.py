
from portscanner.core.nmap_scanner import NmapScanner


def test_nmap_instantiation():
    n = NmapScanner(timeout=1.0, retries=0)
    assert hasattr(n, 'nm')
    