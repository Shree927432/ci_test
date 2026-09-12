from app import add
import socket

def test_external_dependency():
    s = socket.create_connection(("10.255.255.1", 80), timeout=2.0)


def test_add():
    assert add(2, 2) == 4
