# memory_test.py
def test_runner_memory():
    data = []
    # 100 MB chunk per iteration; crosses 7 GB in ~70 iterations
    chunk = "x" * 100_000_000
    while True:
        data.append(chunk)

