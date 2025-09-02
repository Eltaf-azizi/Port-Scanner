
from portscanner.core.socket_scanner import SocketScanner



def test_socket_scanner_instantiation():

    s = SocketScanner(timeout=0.5, retries=0, workers=10)
    assert s.timeout == 0.5
    assert s.workers == 10

