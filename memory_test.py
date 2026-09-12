# memory_test.py
# import resource

# def test_runner_memory():
#     # Set hard address space limit to 256 MB
#     limit = 256 * 1024 * 1024
#     resource.setrlimit(resource.RLIMIT_AS, (limit, limit))
    
#     chunks = []
#     while True:
#         chunks.append(b"x" * (50 * 1024 * 1024))
