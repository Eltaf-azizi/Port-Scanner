
from portscanner.core.scapy_scanner import ScapyScanner



def test_scapy_instantiation():
    s = ScapyScanner(timeout=0.5, retries=0, rate=500, mode="syn")
    assert s.mode == "syn"
    