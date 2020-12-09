import sys

preamble = [None] * 25

def get_sum_pair(num):
    for i, x in enumerate(preamble):
        for y in preamble[i+1:]:
            if x + y == num:
                return x, y

nums = [int(line) for line in sys.stdin]

for i, num in enumerate(nums):
    if i >= len(preamble) and not get_sum_pair(num):
        break

    preamble[i % len(preamble)] = num

print(num)

first = 0
last = 0
total = 0

while total != num:
    while total < num:
        total += nums[last]
        last += 1
    while total > num:
        total -= nums[first]
        first += 1

num_range = nums[first:last]

print(min(num_range) + max(num_range))
