import sys

adapters = set(int(line) for line in sys.stdin)

diffs = {}

prev_adapter = 0
for adapter in adapters:
    diff = adapter - prev_adapter
    diffs[diff] = diffs.get(diff, 0) + 1
    prev_adapter = adapter

diffs[3] = diffs.get(3, 0) + 1 # built-in adapter

print(diffs[1] * diffs[3])

memo = {}

def arrangements(adapter):
    if adapter in memo:
        return memo[adapter]

    count = 0
    for connection in range(adapter + 1, adapter + 4):
        if connection in adapters:
            count += arrangements(connection)
    if count == 0:
        count = 1
    memo[adapter] = count
    return count

print(arrangements(0))
