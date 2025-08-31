import pytest
from portscanner.core.utils import parse_ports, resolve_targets


def test_parse_ports_single_and_range():
    assert parse_ports("80,443,1000-1002") == [80, 443, 1000, 1001, 1002]


def test_parse_ports_bounds():
    assert parse_ports("0,1,65535,65536") == [1, 65535]


def test_resolve_targets_localhost():
    t = resolve_targets(["127.0.0.1"])
    assert "127.0.0.1" in t
