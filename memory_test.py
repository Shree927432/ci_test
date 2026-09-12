# memory_test.py
def test_runner_memory():
    chunks = []
    # Allocate 1 GB raw byte arrays per iteration to bypass swap delay
    while True:
        chunks.append(bytearray(1024 * 1024 * 1024))

