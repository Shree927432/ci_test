from app import add
import time

def test_flaky_timing():
    # Fails roughly 50% of the time based on epoch second
    assert int(time.time()) % 2 == 0, "Transient network timing blip"



def test_add():
    assert add(2, 2) == 4
